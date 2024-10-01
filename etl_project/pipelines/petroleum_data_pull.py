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
from etl_project.assets.pipeline_logging import PipelineLogging
from etl_project.assets.metadata_logging import MetaDataLogging, MetaDataLoggingStatus


if __name__ == "__main__":
    #Create some logging (example can be found at 05-ins-logging)
    pipeline_logging = PipelineLogging(pipeline_name="petroleum", log_folder_path="etl_project/logs")
    load_dotenv()

    LOGGING_SERVER_NAME = os.environ.get("LOGGING_SERVER_NAME")
    LOGGING_DATABASE_NAME = os.environ.get("LOGGING_DATABASE_NAME")
    LOGGING_USERNAME = os.environ.get("LOGGING_USERNAME")
    LOGGING_PASSWORD = os.environ.get("LOGGING_PASSWORD")
    LOGGING_PORT = os.environ.get("LOGGING_PORT")

    postgresql_logging_client = PostgreSqlClient(
        server_name=LOGGING_SERVER_NAME,
        database_name=LOGGING_DATABASE_NAME,
        username=LOGGING_USERNAME,
        password=LOGGING_PASSWORD,
        port=LOGGING_PORT,
    )

    metadata_logger = MetaDataLogging(
        pipeline_name="petroleum",
        postgresql_client=postgresql_logging_client,
        config="log_folder_path: /etl_project/logs",
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

    try:
        #This will get you started on the logging
        metadata_logger.log() #log start

        pipeline_logging.logger.info("Starting pipeline run!")
        pipeline_logging.logger.info("Getting pipeline environment variables")
        pipeline_logging.logger.info("Is this getting written to database?")

        API_KEY = os.environ.get("API_KEY")
        DB_USERNAME = os.environ.get("DB_USERNAME")
        DB_PASSWORD = os.environ.get("DB_PASSWORD")
        SERVER_NAME = os.environ.get("SERVER_NAME")
        DATABASE_NAME = os.environ.get("DATABASE_NAME")
        PORT = os.environ.get("PORT")

        pipeline_logging.logger.info("Creating Petroleum API")
        params = {
            "frequency": "monthly",
            "start": "2024-01",
            "end": "2024-02",
            "sort[0][column]": "period",
            "offset": "0",
            "length": "5000",
            "api_key": API_KEY
        } 

        # Set the URL                   
        url = f"https://api.eia.gov/v2/petroleum/pri/spt/data/?data[0]=value&sort[0][direction]=desc"
        

        month = ['01', '02','03','04','05','06','07', '08','09','10','11','12']
        i=0
        while True:
            response = requests.get(
                url=url, params=params
            ) 
            start = '2024-' + month[i]
            end = '2024-' + month[i+1]

            params["start"] = start
            params["end"] = end

            i = i +1
            if i == 11:
                break

            response_data = response.json()
            df_petroleum = pd.json_normalize(data=response_data)
            df_petroleum =pd.DataFrame(df_petroleum["response.data"][0])

            #Extract
            extract(
                eai_api_client=EiaApiClient,
            )

            #Transform
            # TODO Add a Transform here.

            
            #Load
            metadata_logger.log(status="getting data", logs=f"Loading data for dates between {params['start']} and {params['end']}") #log start
            pipeline_logging.logger.info(f"Loading data to postgres database {params['start']}, {params['end']} ")
            postgresql_client = PostgreSqlClient(
                server_name=SERVER_NAME,
                database_name=DATABASE_NAME,
                username=DB_USERNAME,
                password=DB_PASSWORD,
                port=PORT,
            )

            load(
                df_petroleum=df_petroleum,
                postgresql_client=postgresql_client,
                table=table,
                metadata=metadata,
            )
            pipeline_logging.logger.info("Pipeline run successful!")
            metadata_logger.log(
                status=MetaDataLoggingStatus.RUN_SUCCESS, logs=pipeline_logging.get_logs()
            )  # log end

    except BaseException as e: #log error
        pipeline_logging.logger.error(f"Pipeline failed. See detailed logs: {e}")
        metadata_logger.log(status=MetaDataLoggingStatus.RUN_FAILURE, logs=pipeline_logging.get_logs())