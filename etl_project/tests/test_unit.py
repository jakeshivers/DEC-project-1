import pytest
from unittest.mock import patch, Mock
import pandas as pd
from etl_project.connectors.petroleum import EiaApiClient
from etl_project.connectors.postgresql import PostgreSqlClient
from etl_project.assets.petroleum import extract, load
from sqlalchemy import MetaData, Table, Column, Integer, String, Float

# Mock environment variables
@pytest.fixture
def mock_env_vars(monkeypatch):
    monkeypatch.setenv("API_KEY", "test_api_key")
    monkeypatch.setenv("DB_USERNAME", "test_username")
    monkeypatch.setenv("DB_PASSWORD", "test_password")
    monkeypatch.setenv("SERVER_NAME", "test_server")
    monkeypatch.setenv("DATABASE_NAME", "test_db")
    monkeypatch.setenv("PORT", "5432")

# Mock API response data
@pytest.fixture
def mock_api_response():
    return {
        "response": {
            "data": [
                {
                    "period": "2024-01",
                    "duoarea": "USA",
                    "area-name": "United States",
                    "product": "petroleum",
                    "product-name": "Petroleum",
                    "process": "spot",
                    "process-name": "Spot Price",
                    "series": "pet",
                    "series-description": "Petroleum Spot Prices",
                    "value": 80.5,
                    "units": "USD"
                }
            ]
        }
    }


# Test load function
def test_load(mock_env_vars):
    # Mock PostgreSQL client
    mock_pg_client = Mock(spec=PostgreSqlClient)
    
    # Define a test table schema
    metadata = MetaData()
    table = Table(
        "petroleum_prices",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("period", String),
        Column("duoarea", String),
        Column("area-name", String),
        Column("product", String),
        Column("product-name", String),
        Column("process", String),
        Column("process-name", String),
        Column("series", String),
        Column("series-description", String),
        Column("value", Float),
        Column("units", String),
    )

    # Create a sample DataFrame to load
    df_petroleum = pd.DataFrame({
        "period": ["2024-01"],
        "duoarea": ["USA"],
        "area-name": ["United States"],
        "product": ["petroleum"],
        "product-name": ["Petroleum"],
        "process": ["spot"],
        "process-name": ["Spot Price"],
        "series": ["pet"],
        "series-description": ["Petroleum Spot Prices"],
        "value": [80.5],
        "units": ["USD"]
    })

    # Call the load function
    load(df_petroleum=df_petroleum, postgresql_client=mock_pg_client, table=table, metadata=metadata)

