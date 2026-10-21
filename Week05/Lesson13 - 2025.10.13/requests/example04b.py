import datetime
import json

import requests

# Define the URL for the API endpoint you want to interact with.
try:
  url = "https://jsonplaceholder.typicode.com/users/1"

  start = datetime.datetime.now()
  response = requests.get(url, timeout=0.1)
  finish = datetime.datetime.now()

  print(f"Time to fetch data from the API: {(finish - start).total_seconds():.3f} seconds\n")

  # Check if the request was successful (HTTP status code 200)
  if response.status_code == 200:
    # to convert the JSON data into a Python dictionary
    user_data = response.json()

    # Accessing specific information from the dictionary
    print(f"User Name: {user_data['name']}")  # User Name: Leanne Graham
    print(f"Email: {user_data['email']}")  # Email: Sincere@april.biz

    # Accessing nested data (e.g., city in address)
    print(f"Street: {user_data['address']['street']}")  # Street: Kulas Light
    print(f"City: {user_data['address']['city']}")  # City: Gwenborough

  else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
except requests.exceptions.HTTPError as error_HTTP:
  print(f"An error occurred: {error_HTTP}")
except requests.exceptions.ConnectionError as error_conn:
  print(f"An error occurred: {error_conn}")
except requests.exceptions.Timeout as error_timeout:
  print(f"An error occurred: {error_timeout}")
except requests.exceptions.RequestException as error:
  print(f"An error occurred: {error}")
except json.JSONDecodeError:
  print("Failed to decode JSON data.")
finally:
  print("Operation completed.")
