
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


def change_contact():
    return None


def search_contact():
    return None
