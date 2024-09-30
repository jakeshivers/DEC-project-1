import pandas as pd
from datetime import datetime, timezone
from datetime import datetime, timezone, timedelta
from etl_project.connectors.postgresql import PostgreSqlClient
from etl_project.connectors.petroleum import EiaApiClient
from sqlalchemy import Table, MetaData


def extract(
    eai_api_client: EiaApiClient
):
    response_data = []
    
    #todo what is meta?    
    df = pd.json_normalize(data=response_data, meta=["something?"])
    return df
   



def transform(df: pd.DataFrame, df_petroleum: pd.DataFrame) -> pd.DataFrame:
    # rename columns to more meaningful names
    df_quotes_renamed = df.rename(
        columns={

        }
    )


def load(
    df_petroleum: pd.DataFrame, postgresql_client: PostgreSqlClient, table, metadata
):
    postgresql_client.write_to_table(
        data=df_petroleum.to_dict(orient="records"), table=table, metadata=metadata
    )
