import requests

import requests
BASE = "http://127.0.0.1:5000/"

data = [{"name":"Jac","surname":"Moyo","age":30,"gender": "male"},
        {"name":"Sandy","surname":"Grills","age":42,"gender": "female"},
        {"name":"Jonh","surname":"Doe","age":25,"gender": "female"}]

for i in range(len(data)):
    response = requests.put(BASE + "student/" +str(i), data[i])
    print(response.json())

response = requests.patch(BASE + "student/1", {"name":"Jac","surname":"Moyo","age":30,"gender": "male"})
print(response.json())

input()

response = requests.get(BASE + "student/2")
print(response.json())

input()

response = requests.delete(BASE + "student/0")
print(response.json())