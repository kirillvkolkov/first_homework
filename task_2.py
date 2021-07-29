# Дано положительное трехзначное число. Найдите сумму его цифр.


input_number = int(input('Введите положительное трехзначное число n: '))

first_number = input_number // 100
second_number = (input_number // 10) % 10
third_number = input_number % 10

print(first_number + second_number + third_number)