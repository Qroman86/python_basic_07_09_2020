"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

def ask_parameter(input_str, user_parameters):
    while True:
        input_parameter = input(input_str+":\n")
        try:
            input_parameter = user_parameters.get(input_str)(input_parameter)
        except ValueError as error:
            print(f"{error}\nНеверное значение данных.")
            continue
        return input_parameter


def print_user_data(name, surname, year_birth, city_of_residence, email, phone):
    print_info = f"Имя: {name} "
    print_info += f"Фамилия: {surname} "
    print_info += f"Год рождения: {year_birth} "
    print_info += f"Город проживания: {city_of_residence} "
    print_info += f"Email: {email} "
    print_info += f"Телефон: {phone}"
    print(print_info)

user_parameters = {"Имя": str, "Фамилия": str, "Год рождения": int, "Город проживания": str, "Email": str, "Телефон": str}

name = ask_parameter("Имя", user_parameters)
surname = ask_parameter("Фамилия", user_parameters)
year_birth = ask_parameter("Год рождения", user_parameters)
city_of_residence = ask_parameter("Город проживания", user_parameters)
email = ask_parameter("Email", user_parameters)
phone = ask_parameter("Телефон", user_parameters)


print_user_data(year_birth=year_birth, name=name, surname=surname, email=email, city_of_residence=city_of_residence,  phone=phone)