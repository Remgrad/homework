immutable_var = [1, 2], '3', 'дом', True
print(immutable_var)
#print(type(immutable_var))
# immutable_var[1][1] = 200
# print(immutable_var) # TypeError: 'str' object does not support item assignment - кортеж не поддерживает обращение по элементам
immutable_var[0][0] = 2
print(immutable_var) # Допустимо изменение кортежа внутри которого есть список
mutable_list = [1, 2, '3', 'дом', True]
print(mutable_list)
mutable_list[3] = 'здание'
print(mutable_list)