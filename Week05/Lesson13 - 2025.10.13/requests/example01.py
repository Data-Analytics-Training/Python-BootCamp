"""
API (Application Programming Interface)

An APIis a tool allows different software systems to communicate with each other.

Simple Analogy:
You can think of an API as a waiter in a restaurant.
You (the client) place an order (a request) for the dish (data) you want from the kitchen (the server) through the waiter (the API).
The waiter delivers your order to the kitchen and then bring back the meal (the response) to you.

Real-life example:
Restaurant menu -> Place order (request) -> Kitchen prepares -> Food is served (response)

Why is it used?

Data Exchange:
Allow one program to securely and reliably access data from another application.
(Example: accessing Twitter data, weather information or exchange rates)

Functionality Share:
Enables your application to use the features of another services.
(Example: Integrating payment systems or map services)

REST API: A REST API is an API structure that works over the HTTP protocol and return data in JSON or XML format.

HTTP methods: GET (Retrieve data), POST (Send (create) data), PUT (Update existing data), DELETE (Delete data).
"""

import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/2")

print(response)
# <Response [200]>
print("Response Code: ", response.status_code)
# Response Code:  200

"""
Status codes:
200: OK
201: Created
202: Accepted
404: Not Found
403: Forbidden
405: Method Not Allowed
406: Not Acceptable
408: Request Timeout
409: Conflict
410: Gone
500: Internal Server Error
"""

# To receive the response in text form
print(response.text)
# {
#   "userId": 1,
#   "id": 2,
#   "title": "qui est esse",
#   "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
# }
print(type(response.text))
# <class 'str'>


# To receive the response in JSON form
print(response.json())
# {'userId': 1, 'id': 2, 'title': 'qui est esse', 'body': 'est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla'}

print(type(response.json()))
# <class 'dict'>


data_json = response.json()
print(type(data_json))
# <class 'dict'>
print(len(data_json))


# Another example: Fetching all posts and printing each post's details.
response = requests.get("https://jsonplaceholder.typicode.com/posts")
data_json = response.json()
for data in data_json:
  for knowledge in data:
    print(f"{knowledge} : {data[knowledge]}")
