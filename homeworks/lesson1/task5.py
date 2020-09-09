revenue = input("Введите значение выручки фирмы:")

error_message = ""

if not revenue.isdigit():
    error_message = "Введенное значение выручки не является целым неотрицательным числом"
else:
    revenue = int(revenue)
    if revenue < 0:
        error_message = "Введенное значение выручки не является целым неотрицательным числом"

is_profit = False
is_loss = False
income = 0

if not error_message:
    costs = input("Введите значение издержок фирмы:")

    if not costs.isdigit():
        error_message = "Введенное значение издержок не является целым неотрицательным числом"
    else:
        costs = int(costs)
        if costs < 0:
            error_message = "Введенное значение издержок не является целым неотрицательным числом"



if not error_message:
    income = revenue - costs
    if income > 0:
       is_profit = True
       is_loss = False
    elif income < 0:
       is_profit = False
       is_loss = True

    fin_result_str = "баланс"
    if is_profit:
        fin_result_str = "прибыль"
    elif is_loss:
        fin_result_str = "убыток"
    else:
        fin_result_str = "баланс"
    print("Финансовый результат работы фирмы: %s (%d)" % (fin_result_str, income))

    if is_profit and revenue == 0:
        print("Рентабельность невозможно вычислить ввиду того, что значение выручки равно 0")
    elif is_profit:
        profit_margin = income / revenue
        print("Рентабельность выручки равна %f" % profit_margin)

#Расчет прибыли фирмы в расчете на одного сотрудника производится в том случае, если выручка превышает издержки, то есть есть прибыль
if not error_message and is_profit:

    number_of_employees = input("Введите число сотрудников фирмы:")

    if not number_of_employees.isdigit():
        error_message = "Введеное значение численности сотрудников не является целым положительным числом"
    else:
        number_of_employees = int(number_of_employees)
        if number_of_employees < 1:
            error_message = "Введеное значение численности сотрудников не является целым положительным числом"

    if not error_message:
        income_per_employee = income / number_of_employees
        print("Прибыль фирмы в расчете на одного сотрудника %f" % income_per_employee)

if error_message:
    print("Внимание! %s" % error_message)
