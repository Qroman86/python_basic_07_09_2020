error_message = ""
total_time_in_seconds = input("Введите общее время в секундах:")

if not total_time_in_seconds.isdigit():
    error_message = "введное значение не является целым положительным числом"
else:
    total_time_in_seconds = int(total_time_in_seconds)
    if total_time_in_seconds >= 86400:
        error_message = "время указывается в пределах одних суток. Максимальное допустимое значение - 86399"
    if total_time_in_seconds < 0:
        error_message = "время не должно быть отрицательным"

if error_message:
    print("Внимание! Данные введены некорректно: ", error_message)
else:
    hour_count = total_time_in_seconds // 3600
    minute_count = total_time_in_seconds % 3600
    seconds_count = minute_count % 60
    minute_count = minute_count // 60

    hour_count_str = str(hour_count)
    if hour_count < 10:
        hour_count_str = "0" + hour_count_str

    minute_count_str = str(minute_count)
    if minute_count < 10:
        minute_count_str = "0" + minute_count_str

    seconds_count_str = str(seconds_count)
    if seconds_count < 10:
        seconds_count_str = "0" + seconds_count_str

    print("%s:%s:%s" % (hour_count_str, minute_count_str, seconds_count_str))