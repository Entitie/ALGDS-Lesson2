# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
numbers = tuple(map(str, input('Введите через пробел несколько натуральных чисел, '
                               'а я определю наибольшее по сумме цифр: ').split()))

biggest_number = 0
sum_of_digits = 0

for el in numbers:
    temp_sum = 0
    for elem in el:
        temp_sum += int(elem)
    if temp_sum >= sum_of_digits:
        biggest_number = el
        sum_of_digits = temp_sum

print(f'Наибольше число по сумме цифр - это {biggest_number}, сумма его цифр равна {sum_of_digits}')
