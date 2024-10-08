import requests
from datetime import datetime


class EiaApiClient:
    def __init__(self, api_key: str):
        self.base_url = "https://api.eia.gov/v2/petroleum/pri/spt/data/?data[0]=value&sort[0][direction]=desc"
        if api_key is None:
            raise Exception("API key cannot be set to None.")
        self.api_key = api_key

    def get_petroleum_prices(self, start: str, end: str) -> list[dict]:
        """
        Get the data for various petorleum products.

        Args:
            frequency: monthly
            start: start month
            end: end month

        Returns:
            A list of petorleum price between the start and end month

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
