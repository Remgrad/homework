first = input('Введите первое число: ')
first = int(first)
second = input('Введите второе число: ')
second = int(second)
third = input('Введите третье число: ')
third = int(third)
if first == second and first == third:
    print(3)
elif first == second or first == third:
    print(2)
else:
    print(0)