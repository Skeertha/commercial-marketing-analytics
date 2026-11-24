from pathlib import Path
import sqlite3

import numpy as np
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
SOURCE_FILE = ROOT / "data" / "sales_campaigns.csv"
DATABASE_FILE = ROOT / "outputs" / "commercial_analytics.sqlite"


@pytest.fixture
def source_and_target():
    source = pd.read_csv(SOURCE_FILE)

    source["order_date"] = pd.to_datetime(
        source["order_date"], format="%d-%m-%Y"
    )
    source["campaign"] = (
        source["campaign"]
        .fillna("No Campaign")
        .replace("None", "No Campaign")
    )
    source["month"] = source["order_date"].dt.to_period("M").astype(str)

    with sqlite3.connect(DATABASE_FILE) as conn:
        target = pd.read_sql_query(
            "SELECT * FROM sales_campaigns", conn
        )

    target["order_date"] = pd.to_datetime(target["order_date"])

    source = source.sort_values("order_id").reset_index(drop=True)
    target = target.sort_values("order_id").reset_index(drop=True)

    return source, target


def test_source_and_target_row_counts_match(source_and_target):
    source, target = source_and_target
    assert len(source) == len(target)


def test_unique_order_ids_match(source_and_target):
    source, target = source_and_target
    assert source["order_id"].nunique() == target["order_id"].nunique()
    assert source["order_id"].equals(target["order_id"])


def test_financial_totals_reconcile(source_and_target):
    source, target = source_and_target

    for column in ["revenue", "gross_profit", "estimated_cost"]:
        assert source[column].sum() == pytest.approx(
            target[column].sum(), abs=0.01
        )


def test_all_source_columns_match_target(source_and_target):
    source, target = source_and_target

    for column in source.columns:
        if column in [
            "revenue", "gross_profit", "estimated_cost",
            "unit_price", "discount_pct"
        ]:
            np.testing.assert_allclose(
                source[column].astype(float),
                target[column].astype(float),
                rtol=1e-9,
                atol=1e-8,
            )
        else:
            assert source[column].fillna("").astype(str).equals(
                target[column].fillna("").astype(str)
            ), f"Mismatch found in column: {column}"


def test_no_duplicate_order_ids(source_and_target):
    source, target = source_and_target
    assert source["order_id"].duplicated().sum() == 0
    assert target["order_id"].duplicated().sum() == 0
