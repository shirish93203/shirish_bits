import requests

response = requests.get('https://rahulshettyacademy.com/')

print(response.text)

data = {
    'name': 'John Doe',
    'email': 'johndoe@example.com'
}

response = requests.post('https://rahulshettyacademy.com/', json=data)
print(response.text)


data = {
    'name': 'Jane Doe'
}

response = requests.put('https://rahulshettyacademy.com//123', json=data)
print(response.text)


response = requests.delete('https://rahulshettyacademy.com//123')
print(response.text)


data = {
    'name': 'Bob Smith'
}

response = requests.patch('https://rahulshettyacademy.com//123', json=data)
print(response.text)
