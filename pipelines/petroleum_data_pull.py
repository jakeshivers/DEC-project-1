from urllib.request import urlopen
import os
from dotenv import load_dotenv
import json
import pandas as pd
import requests

if __name__ == "__main__":
    load_dotenv()
    api_key = os.environ.get("api_key")
    #API_KEY_ID = 'ANf55hWD1ayUpkkQolvUADtq2sMhU83p2VZZlTql'
    params = {
        "frequency": "monthly",
        "start": "2024-01",
        "sort[0][column]": "period",
        "offset": "0",
        "length": "5000",
        "api_key": api_key
    } 

    # Set the URL
                   
    url = f"https://api.eia.gov/v2/petroleum/pri/spt/data/?data[0]=value&sort[0][direction]=desc"

    response = requests.get(
        url=url, params=params
    )
    
    response_data = response.json()

    df_petrolium = pd.json_normalize(data=response_data)
    df_petrolium =df_petrolium["response.data"]

    print(df_petrolium)