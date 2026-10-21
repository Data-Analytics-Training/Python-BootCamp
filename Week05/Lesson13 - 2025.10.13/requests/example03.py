import requests

# Define the URL for the GitHub API endpoint.
url = "https://api.github.com"

# Send a GET request to the GitHub API.
response = requests.get(url)

print("Response Code: ", {response.status_code})
# Response Code:  {200}

if response.status_code == 200:
  print("Request was successful!")
else:
  print("Request failed with status code:", response.status_code)

# Request was successful!

# Print the content of the response.
print(response.json())
# {'current_user_url': 'https://api.github.com/user', 'current_user_authorizations_html_url': 'https://github)

data = response.json()
for key, value in data.items():
  print(key, ":", value)
