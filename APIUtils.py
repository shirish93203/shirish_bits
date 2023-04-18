import requests

response = requests.get('https://api.example.com/data')

print(response.text)

data = {
    'name': 'John Doe',
    'email': 'johndoe@example.com'
}

response = requests.post('https://api.example.com/data', json=data)
print(response.text)


data = {
    'name': 'Jane Doe'
}

response = requests.put('https://api.example.com/data/123', json=data)
print(response.text)


response = requests.delete('https://api.example.com/data/123')
print(response.text)


data = {
    'name': 'Bob Smith'
}

response = requests.patch('https://api.example.com/data/123', json=data)
print(response.text)
