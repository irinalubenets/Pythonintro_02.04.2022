input_case = input("Выбери тип операции:\n 1 +\n 2 -\n 3 *\n 4 /\n")
try:
    print("Примечание - Дробные числа вводяться через точку")
    value_1 = float(input("Введи первое число:"))
    value_2 = float(input("Введи второе число:"))
    if input_case == "1":
        print("Результат = ", value_1 + value_2)
    elif input_case == "2":
        print("Результат = ", value_1 - value_2)
    elif input_case == "3":
        print("Результат = ", value_1 * value_2)
    elif input_case == "4":
        print("Результат = ", value_1 / value_2)
    else:
        print("Неверный тип операции")
except ValueError:
    print("Вы ввели не число")
except ZeroDivisionError:
    print("Делить на ноль нельзя")



