import requests
repos = requests.post("http://localhost:5001/add",json={"id": "3","first":"34","second":"56"})

print(repos.json())