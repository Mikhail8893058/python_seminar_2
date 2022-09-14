# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 0,56 -> 11

numm = input('Введите число с плавающей точкой: ')
summ = 0
for i in numm:
    if i != ',' and (i != '.'):
        summ += int(i) 
print('Сумма цифр равна:' ,summ)


number = '12.5894'
number = number.replace('.', '').replace(',', '')
list_user = []
for i in number:
    if i != '.':
        list_user.append(int(i))
print(sum(list_user))

# x = 1234

# result = []
# while x > 0:
#     result.append(x % 10)
#     x //= 10
# print(result)

# result.reverse()
# print(result)  # [1, 2, 3, 4]

# num = 0
# for i, v in enumerate(reversed(result)):
#     num += v * 10 ** i
# print(num)  # 1234