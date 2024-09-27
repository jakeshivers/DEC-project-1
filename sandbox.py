import requests

response = requests.get("http://api.open-notify.org/astros")
print(response.status_code)


response = requests.get("https://api.eia.gov/v2/petroleum/pri/spt/data/\n"
                        "?frequency=weekly\n"
                        "&data[0]=value\n"
                        "&sort[0][column]=period\n"
                        "&sort[0][direction]=desc\n"
                        "&offset=0&length=5000\n"
                        "&api_key=ANf55hWD1ayUpkkQolvUADtq2sMhU83p2VZZlTql")
print(response.status_code)
