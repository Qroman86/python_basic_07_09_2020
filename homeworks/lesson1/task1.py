print("Ввод информации о книге")

warning_message = ""
comment_message = ""

book_authors = input("Введите ФИО автора(-ов):")
if not book_authors:
    warning_message = warning_message + "- ФИО автора(-ов) обязательны к заполнению.\n"

book_title = input("Название книги:")
if not book_title:
    warning_message = warning_message + "- название книги обязательно к заполнению.\n"

book_place_of_publication = input("Место издания:")
book_page_counts = input("Количество страниц:")
if not book_page_counts.isdigit():
    warning_message = warning_message + "- введеное значение для количества страниц не является целым положительным числом\n"
else:
    book_page_counts = int(book_page_counts)
    if book_page_counts <= 0:
        warning_message = warning_message + "- введеное значение для количества страниц не является целым положительным числом\n"

book_year_of_publication = input("Год издания:")
if not book_year_of_publication.isdigit():
    warning_message = warning_message + "- введеное значение для года издания не является целым числом\n"
else:
    book_year_of_publication = int(book_year_of_publication)
    if book_year_of_publication <= 0:
        warning_message = warning_message + "- введеное значение для года издания не является  положительным числом\n"
    if book_year_of_publication < 1920:
        comment_message = comment_message + "данная книга антиквариат!"
    if book_year_of_publication >= 2019:
        comment_message = comment_message + "это книжная новинка!"
    if book_year_of_publication > 2020:
        warning_message = warning_message + "- книга не может быть издана в будущем"

if warning_message:
    print("\nВнимание! Часть данных обязательных к заполнению не введена и/или часть данных введена некорректно.")
    print(warning_message)
else:
    print("Данные введены корректно")
    print("\nВведены данные следующей книги:")
    print("Автор(ы):", book_authors)
    print("Название книги:", book_title)
    print("Место издания:", book_place_of_publication)
    print("Год издания:", book_year_of_publication)
    print("Количество страниц:", book_page_counts)

if not warning_message and comment_message:
    print("\nКомментарий:", comment_message)



