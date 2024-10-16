import requests

# Выполнение GET-запроса
response = requests.get('https://jsonplaceholder.typicode.com/posts')

# Проверка статус-кода ответа
if response.status_code == 200:
	# Получение данных в формате JSON
	data = response.json()

	# Вывод заголовков постов
	for post in data[:3]:  # Выводим только первые 5 постов
		print(f"ID: {post['id']}, Title: {post['title']}")
else:
	print(f"Ошибка: {response.status_code}")

