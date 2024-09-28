import requests
from datetime import datetime


class EiaApiClient:
    def __init__(self, api_key: str):
        self.base_url = "https://api.eia.gov/v2/petroleum/pri/spt/data/?data[0]=value&sort[0][direction]=desc"
        if api_key is None:
            raise Exception("API key cannot be set to None.")
        self.api_key = api_key

    def get_petroleum_prices(
        self, start: str, end: str
    ) -> list[dict]:
        """
        Get the data for various petorleum products.

        Args:
            stock_ticker: the ticker for the stock
            start_time: start time in isoformat
            end_time: end time in isoformat

        Returns:
            A list of trades for a given stock ticket between the start and end times

        Raises:
            Exception if response code is not 200.
        """
        url = f"{self.base_url}"
        params = {
            "frequency": "monthly",
            "start": "2024-01",
            "end": "2024-02",
            "sort[0][column]": "period",
            "offset": "0",
            "length": "5000"
    } 
        response = requests.get(url=url, params=params)
        if response.status_code == 200 and response.json() is not None:
            return response.json()
        else:
            raise Exception(
                f"Failed to extract data from eis API. Status Code: {response.status_code}. Response: {response.text}"
            )
