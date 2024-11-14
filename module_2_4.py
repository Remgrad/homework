# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primes = [] #Используя этот список составьте второй список primes содержащий только простые числа.
# not_primes = [] #А так же третий список not_primes, содержащий все не простые числа.
# Выведите списки primes и not_primes на экран(в консоль).
# is_prime = [2, 3, 5, 7, 11, 13] # Отметить простоту числа можно переменной is_prime, записав в неё занчение True перед проверкой.
# for i in (numbers):
#     if i > 1:
#         for j in is_prime:
#             if (i % j) == 0:
#                 not_primes.append(i)
#             #break
#             else:
#                 primes.append(i)
# print(primes)
# print(not_primes)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for number in numbers:
    if number == 1:
        continue
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)
print(primes)
print(not_primes)