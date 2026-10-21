import requests

def fetch_all_tasks (user_id):
    # Lists tasks belonging to a specific user
    url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            tasks = response.json()
            print(f'\n{len(tasks)} tasks fo user {user_id}:')
            for task in tasks:
                state = '✅' if task['completed'] else '🔲'
                print(f"{state} {task['title']}")
        else:
            print("❌ Failed to retrieve tasks")
    except Exception as error:
        print(f"🚨 Error: {error}" )
        

fetch_all_tasks(1)
