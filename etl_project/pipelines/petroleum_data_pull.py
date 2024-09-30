from urllib.request import urlopen
import os
from dotenv import load_dotenv
from IPython.display import display
import json
import pandas as pd
import requests
from etl_project.connectors.petroleum import EiaApiClient
from etl_project.connectors.postgresql import PostgreSqlClient
from sqlalchemy import Table, Column, Integer, String, MetaData, Float
from etl_project.assets.petroleum import (
    extract,
    transform,
    load,
)

if __name__ == "__main__":
    #TODO Create some logging (example can be found at 05-ins-logging)
    load_dotenv()
    #TODO This will get you started on the logging
    # pipeline_logging.logger.info("Starting pipeline run")
    #pipeline_logging.logger.info("Getting pipeline environment variables")    

    API_KEY = os.environ.get("API_KEY")
    DB_USERNAME = os.environ.get("DB_USERNAME")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
    SERVER_NAME = os.environ.get("SERVER_NAME")
    DATABASE_NAME = os.environ.get("DATABASE_NAME")
    PORT = os.environ.get("PORT")
    
    params = {
        "frequency": "monthly",
        "start": "2024-01",
        "sort[0][column]": "period",
        "offset": "0",
        "length": "5000",
        "api_key": API_KEY
    } 

    # Set the URL
                   
    url = f"https://api.eia.gov/v2/petroleum/pri/spt/data/?data[0]=value&sort[0][direction]=desc"

    response = requests.get(
        url=url, params=params
    )
    

    print(response.status_code)
    response_data = response.json()
    df_petroleum = pd.json_normalize(data=response_data)
    df_petroleum =pd.DataFrame(df_petroleum["response.data"][0])
  
    ## 
    postgresql_client = PostgreSqlClient(
        server_name=SERVER_NAME,
        database_name=DATABASE_NAME,
        username=DB_USERNAME,
        password=DB_PASSWORD,
        port=PORT,
    )

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

    extract(
        eai_api_client=EiaApiClient,
    )
    
    # TODO Add a Transform here.

    
    print("loading data")
    load(
        df_petroleum=df_petroleum,
        postgresql_client=postgresql_client,
        table=table,
        metadata=metadata,
    )
