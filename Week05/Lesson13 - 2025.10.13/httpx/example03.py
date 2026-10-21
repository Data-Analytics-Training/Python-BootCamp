import httpx

# Define the URL for the GitHub API endpoint.
url = 'https://api.github.com'

# Send a GET request to the URL.
response = httpx.get(url)

print('Response Code: ', response.status_code)
# Response Code:  200

if response.status_code == 200:
    print('Request was successful')
else:
    print('Request failed with status code: ', response.status_code)
    

# Print the content of the response.
data = response.json()
for key, value in data.items():
    print(key, ':', value)
