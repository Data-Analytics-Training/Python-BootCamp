import httpx

url = "https://jsonplaceholder.typicode.com/posts/1"
response = httpx.get(url, timeout=0.2)

print(response.json())
# {'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
print(type(response.json()))
# <class 'dict'>

data_json = response.json()

for data in data_json:
  print(f"{data}: \t{data_json[data]}")

# userId: 	1
# id: 	1
# title: 	sunt aut facere repellat provident occaecati excepturi optio reprehenderit
# body: 	quia et suscipit
# suscipit recusandae consequuntur expedita et cum
# reprehenderit molestiae ut ut quas totam
# nostrum rerum est autem sunt rem eveniet architecto
