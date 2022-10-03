# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11





user_num = int(input("Введите число - "))



def Making_Sum(num):

    sum = 0
    new_num = str(num)

    for i in new_num:

        if i != str("."):
            sum = sum + int(i)

    return sum


print (Making_Sum(user_num))





