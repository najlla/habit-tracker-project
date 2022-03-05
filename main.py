import requests
from datetime import datetime

USER_NAME = "najlla"
TOKEN = "1qaz2wsx3edc4rfv5tgb"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": USER_NAME,
    "username": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixela_endpoint_creation = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/"

today = datetime.now()

pixela_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
    "agreeTermsOfService": "yes",
}

# response = requests.post(url=pixela_endpoint, json=pixela_data, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

pixela_update = {
    "quantity": "4.5"
}

# response = requests.put(url=pixela_endpoint, json=pixela_update, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=pixela_endpoint, headers=headers)
print(response.text)