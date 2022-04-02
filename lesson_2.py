input_case = input("Выбери тип операции:\n 1 +\n 2 -\n 3 *\n 4 /\n")
value_1 = int(input("Введи первое число:"))
value_2 = int(input("Введи второе число:"))
if input_case == "1":
    print(value_1 + value_2)
elif input_case == "2":
    print(value_1 - value_2)
elif input_case == "3":
    print(value_1 * value_2)
elif input_case == "4":
    print(value_1 / value_2)
else:
    print("Ошибка введенных данных")



