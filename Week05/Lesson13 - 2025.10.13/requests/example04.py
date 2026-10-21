import requests

# Define the URL for the API endpoint you want to interact with.
try:
  url = "https://jsonplaceholder.typicode.com/users/1"

  response = requests.get(url)

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
except requests.exceptions.RequestException as error:
  print(f"An error occurred: {error}")
