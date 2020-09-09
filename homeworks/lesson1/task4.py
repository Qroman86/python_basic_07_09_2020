number_n = input("Введите целое положительное число n:")

error_message = ""

if not number_n.isdigit():
    error_message = "Введенное значение не является целым положительным числом"
else:
    number_n = int(number_n)

if not error_message and number_n < 1:
    error_message = "Введенное значение не является целым положительным числом"

if not error_message:
    max_digit = 0
    while number_n:
        digit = number_n % 10
        if max_digit < digit:
            max_digit = digit
        number_n = number_n // 10
    print("Максимальная цифра для указанного числа: %d" % max_digit)
else:
    print("Внимание! %s" % error_message)