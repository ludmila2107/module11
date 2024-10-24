def introspection_info(obj):
	"""Функция для получения информации об объекте."""

	# Словарь для хранения информации об объекте
	info = {}

	# Получаем тип объекта
	info['type'] = str(type(obj))

	# Получаем атрибуты объекта
	attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
	info['attributes'] = attributes

	# Получаем методы объекта
	methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
	info['methods'] = methods

	# Получаем модуль, к которому принадлежит объект
	info['module'] = getattr(obj, '__module__', 'Неизвестно')

	# Другие интересные свойства
	info['docstring'] = getattr(obj, '__doc__', 'Нет документации')

	# Если это класс, добавляем информацию о наследовании
	if isinstance(obj, type):
		info['bases'] = [base.__name__ for base in obj.__bases__]

	return info


# Пример использования функции
if __name__ == "__main__":
	class Sample:
		"""Пример класса с атрибутами и методами."""

		def method1(self):
			pass

		def method2(self):
			pass


	instance = Sample()

	# Получаем информацию о классе
	class_info = introspection_info(Sample)
	print("Информация о классе:")
	for key, value in class_info.items():
		print(f"{key}: {value}")

	# Получаем информацию о экземпляре класса
	instance_info = introspection_info(instance)
	print("\nИнформация об экземпляре:")
	for key, value in instance_info.items():
		print(f"{key}: {value}")