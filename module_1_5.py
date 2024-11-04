# Задайте переменные разных типов данных:
#   - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
#   - Выполните операции вывода кортежа immutable_var на экран.
immutable_var = [1, 2], '3', 'дом', True
print(immutable_var)
#print(type(immutable_var))
# Изменение значений переменных:
# Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.
# immutable_var[1][1] = 200
# print(immutable_var) # TypeError: 'str' object does not support item assignment - кортеж не поддерживает обращение по элементам
immutable_var[0][0] = 2
print(immutable_var) # Допустимо изменение кортежа внутри которого есть список
mutable_list = [1, 2, '3', 'дом', True]
print(mutable_list)