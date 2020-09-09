number_n_as_str = input("Введите целое неотрицательное число n:")

if not number_n_as_str.isdigit():
    print("Введенное значение не является целым неотрицательным числом")
else:
    number_n = int(number_n_as_str)
    number_nn_as_str = "{}{}".format(number_n_as_str, number_n_as_str)
    number_nnn_as_str = "{}{}".format(number_nn_as_str,number_n_as_str)

    number_nn = int(number_nn_as_str)
    number_nnn = int(number_nnn_as_str)

    total_sum = number_n + number_nn + number_nnn
    print("n + nn + nnn = %d" % total_sum)

