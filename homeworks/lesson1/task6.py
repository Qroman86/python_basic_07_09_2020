current_day_distance = input("Введите дистанцию, преодоленную в первый день, в километрах (целое число):")

error_message = ""

if not current_day_distance.isdigit():
    error_message = "Введенное значение дистанции, преодоленной в первый день, не является целым неотрицательным числом"
else:
    current_day_distance = int(current_day_distance)
    if current_day_distance < 0:
        error_message = "Введенное значение дистанции, преодоленной в первый день, не является целым неотрицательным числом"

goal_distance = ""

if not error_message:
    goal_distance = input("Введите целевую дистанцию в километрах (целое число):")
    if not goal_distance.isdigit():
        error_message = "Введенное значение целевой дистанции не является целым неотрицательным числом"
    else:
        goal_distance = int(goal_distance)
        if goal_distance < 0:
            error_message = "Введенное значение целевой дистанции не является целым неотрицательным числом"

if not error_message:
    day_count = 1
    while current_day_distance < goal_distance:
        day_count += 1
        current_day_distance = current_day_distance * 1.1
    print("\nНомер дня, на который общий результат спортсмена составил не менее %d км: %d" % ( goal_distance, day_count))


if error_message:
    print("\nВнимание! %s" % error_message)