my_string = '0123456789'
# Сгенерировать целые числа (тип int) от 0 до 99 и распечатать их.
# Задание нужно выполнить ТОЛЬКО через цикл в цикле(См. пример выше) и приведение типов.
# Генерирование через range или другие "фишки" я засчитывать не буду ))
for symb in my_string:
    a = int(symb)
    print(symb)
symb_int = int(my_string)
my_string_1 = str(symb_int)
for symb_1 in my_string_1:
    for symb_2 in my_string:
        a = int(symb_1 + symb_2)
        print(a)
