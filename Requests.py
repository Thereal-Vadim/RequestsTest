import requests

print("=== Задание 1 ===")
response = requests.get('https://api.github.com/search/repositories',
                       params={'q': 'language:html'})

print(f"Статус код: {response.status_code}")
print("Ответ от API:")
print(response.json())


print("\n=== Задание 2 ===")
response = requests.get('https://jsonplaceholder.typicode.com/posts',
                       params={'userId': 1})
print("Записи для пользователя с ID 1:")
print(response.json())


print("\n=== Задание 3 ===")
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
response = requests.post('https://jsonplaceholder.typicode.com/posts',
                        json=data)
print(f"Статус код: {response.status_code}")
print("Ответ сервера:")
print(response.json())