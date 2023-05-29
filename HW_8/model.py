
def get_data():
    with open('b:\Work\HW_Python\HW_8\contact.txt', 'r', encoding='utf-8') as book:
        print(book.read())


def add_contact(fio, phone_number):
    with open('b:\Work\HW_Python\HW_8\contact.txt', "r", encoding="utf-8") as book:
        book.read()
    with open('b:\Work\HW_Python\HW_8\contact.txt', "a", encoding="utf-8") as book:
        book.write(f"{fio} {phone_number}\n")


def del_contact():
    return None


def change_contact(id_contact, fio, phone_number):

    with open('b:\Work\HW_Python\HW_8\contact.txt', 'r', encoding='utf-8') as book:
        book_2 = book.readlines()

    book_2[id_contact - 1] = f"{fio} {phone_number}\n"

    with open('b:\Work\HW_Python\HW_8\contact.txt', "w", encoding="utf-8") as book:
        book.writelines(book_2)


def search_contact():
    return None
