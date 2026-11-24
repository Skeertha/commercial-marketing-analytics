from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from functools import partial
from pathlib import Path
from urllib.parse import urlparse, parse_qs
import json
import sqlite3


ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "outputs" / "commercial_analytics.sqlite"


class SalesAPIHandler(BaseHTTPRequestHandler):

    def __init__(self, *args, db_path=DB_PATH, **kwargs):
        self.db_path = db_path
        super().__init__(*args, **kwargs)

    def send_json(self, status, data):
        body = json.dumps(data, default=str).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)

        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row

                if parsed.path == "/health":
                    conn.execute("SELECT 1")
                    return self.send_json(200, {
                        "status": "ok",
                        "database": "connected"
                    })

                if parsed.path == "/kpis":
                    row = conn.execute("""
                        SELECT
                            COUNT(DISTINCT order_id) AS total_orders,
                            COUNT(DISTINCT customer_id) AS unique_customers,
                            ROUND(SUM(revenue), 2) AS total_revenue,
                            ROUND(SUM(gross_profit), 2) AS gross_profit
                        FROM sales_campaigns
                    """).fetchone()

                    return self.send_json(200, dict(row))

                if parsed.path == "/campaigns":
                    rows = conn.execute("""
                        SELECT
                            campaign,
                            COUNT(DISTINCT order_id) AS orders,
                            ROUND(SUM(revenue), 2) AS revenue,
                            ROUND(SUM(gross_profit), 2) AS gross_profit
                        FROM sales_campaigns
                        GROUP BY campaign
                        ORDER BY revenue DESC
                    """).fetchall()

                    return self.send_json(200, {
                        "count": len(rows),
                        "data": [dict(row) for row in rows]
                    })

                if parsed.path == "/monthly":
                    rows = conn.execute("""
                        SELECT
                            month,
                            ROUND(SUM(revenue), 2) AS revenue,
                            ROUND(SUM(gross_profit), 2) AS gross_profit,
                            COUNT(DISTINCT order_id) AS orders
                        FROM sales_campaigns
                        GROUP BY month
                        ORDER BY month
                    """).fetchall()

                    return self.send_json(200, {
                        "count": len(rows),
                        "data": [dict(row) for row in rows]
                    })

                if parsed.path == "/sales":
                    limit = int(params.get("limit", ["100"])[0])
                    offset = int(params.get("offset", ["0"])[0])

                    if limit < 1 or limit > 500 or offset < 0:
                        return self.send_json(400, {
                            "error": "limit must be 1-500 and offset must be non-negative"
                        })

                    query = "SELECT * FROM sales_campaigns WHERE 1=1"
                    values = []

                    for field in ["campaign", "category"]:
                        if field in params:
                            query += f" AND LOWER({field}) = LOWER(?)"
                            values.append(params[field][0])

                    query += " ORDER BY order_id LIMIT ? OFFSET ?"
                    values.extend([limit, offset])

                    rows = conn.execute(query, values).fetchall()

                    return self.send_json(200, {
                        "count": len(rows),
                        "limit": limit,
                        "offset": offset,
                        "data": [dict(row) for row in rows]
                    })

                return self.send_json(404, {
                    "error": "Endpoint not found"
                })

        except ValueError:
            return self.send_json(400, {
                "error": "Invalid numeric parameter"
            })
        except sqlite3.Error:
            return self.send_json(500, {
                "error": "Database operation failed"
            })

    def log_message(self, format, *args):
        pass


def create_server(host="127.0.0.1", port=8000, db_path=DB_PATH):
    handler = partial(SalesAPIHandler, db_path=db_path)
    return ThreadingHTTPServer((host, port), handler)


if __name__ == "__main__":
    server = create_server()
    print("Sales API running at http://127.0.0.1:8000")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nAPI server stopped.")
    finally:
        server.server_close()
