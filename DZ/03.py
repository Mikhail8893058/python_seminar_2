# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.
    
k = int(input('Введите число: '))
summ = 0
for i in range(1, k+1):
    summ += (1+1/i)**i
print(summ) 

