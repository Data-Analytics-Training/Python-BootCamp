import httpx

# Define the URL for the API endpoint you want to interact with
try:
    url = "https://jsonplaceholder.typicode.com/users/10"
    
    response = httpx.get(url)
    
    if response.status_code == 200:
        # to convert the JSON data into a Python dictionary
        user_data = response.json()
        
        # Accessing specific information from the dictionary
        print(f"User Name: {user_data['name']}")
        print(f"User Email: {user_data['email']}")
        
        # Accessing nested data (e.g., city in address)
        print(f"Street: {user_data['address']['street']}")
        print(f"City: {user_data['address']['city']}")
    else:
        print(f"Failed to retrieve data. Status Code: ", {response.status_code})
except httpx.RequestError as error:
    print(f"An error occurred: {error}") 
except Exception as error:
    print(f"An error occurred: {error}")
