import json
import threading
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import urlencode

import pytest

from api.app import create_server


@pytest.fixture(scope="module")
def api_url():
    server = create_server(port=0)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    host, port = server.server_address

    yield f"http://{host}:{port}"

    server.shutdown()
    thread.join()
    server.server_close()


def get_json(url):
    try:
        with urlopen(url, timeout=5) as response:
            return response.status, json.loads(response.read())
    except HTTPError as error:
        return error.code, json.loads(error.read())


def test_health_endpoint(api_url):
    status, body = get_json(f"{api_url}/health")

    assert status == 200
    assert body["status"] == "ok"
    assert body["database"] == "connected"


def test_kpis_endpoint(api_url):
    status, body = get_json(f"{api_url}/kpis")

    assert status == 200
    assert body["total_orders"] == 1800
    assert body["unique_customers"] == 250
    assert body["total_revenue"] == pytest.approx(958498.30)
    assert body["gross_profit"] == pytest.approx(291887.70)


def test_campaigns_endpoint(api_url):
    status, body = get_json(f"{api_url}/campaigns")

    assert status == 200
    assert body["count"] == 5
    assert len(body["data"]) == 5
    assert all("campaign" in row for row in body["data"])


def test_monthly_endpoint(api_url):
    status, body = get_json(f"{api_url}/monthly")

    assert status == 200
    assert body["count"] > 0
    assert all("month" in row and "revenue" in row for row in body["data"])


def test_sales_default_pagination(api_url):
    status, body = get_json(f"{api_url}/sales")

    assert status == 200
    assert body["count"] == 100
    assert body["limit"] == 100
    assert body["offset"] == 0


def test_sales_category_filter(api_url):
    query = urlencode({"category": "Food", "limit": 500})
    status, body = get_json(f"{api_url}/sales?{query}")

    assert status == 200
    assert body["count"] > 0
    assert all(row["category"].lower() == "food" for row in body["data"])


def test_sales_campaign_filter(api_url):
    query = urlencode({"campaign": "Festive Offer", "limit": 500})
    status, body = get_json(f"{api_url}/sales?{query}")

    assert status == 200
    assert body["count"] > 0
    assert all(row["campaign"] == "Festive Offer" for row in body["data"])


def test_sales_pagination_offset(api_url):
    first_status, first = get_json(f"{api_url}/sales?limit=5&offset=0")
    next_status, next_page = get_json(f"{api_url}/sales?limit=5&offset=5")

    assert first_status == 200
    assert next_status == 200
    assert first["count"] == 5
    assert next_page["count"] == 5

    first_ids = {row["order_id"] for row in first["data"]}
    next_ids = {row["order_id"] for row in next_page["data"]}

    assert first_ids.isdisjoint(next_ids)


@pytest.mark.parametrize(
    "query",
    [
        "limit=0",
        "limit=501",
        "offset=-1",
        "limit=abc",
    ],
)
def test_invalid_pagination_returns_400(api_url, query):
    status, body = get_json(f"{api_url}/sales?{query}")

    assert status == 400
    assert "error" in body


def test_unknown_endpoint_returns_404(api_url):
    status, body = get_json(f"{api_url}/unknown")

    assert status == 404
    assert body["error"] == "Endpoint not found"
