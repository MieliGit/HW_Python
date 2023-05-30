
def get_data():
    with open('b:\Work\HW_Python\HW_8\contact.txt', 'r', encoding='utf-8') as book:
        print(book.read())


def add_contact(fio, phone_number):
    with open('b:\Work\HW_Python\HW_8\contact.txt', "r", encoding="utf-8") as book:
        book.read()
    with open('b:\Work\HW_Python\HW_8\contact.txt', "a", encoding="utf-8") as book:
        book.write(f"{fio} {phone_number}\n")


def del_contact(id_contact):
    with open('b:\Work\HW_Python\HW_8\contact.txt', 'r', encoding='utf-8') as book:
        book_2 = book.readlines()

    book_2[id_contact - 1] = ''

    with open('b:\Work\HW_Python\HW_8\contact.txt', "w", encoding="utf-8") as book:
        book.writelines(book_2)


def change_contact(id_contact, fio, phone_number):

    with open('b:\Work\HW_Python\HW_8\contact.txt', 'r', encoding='utf-8') as book:
        book_2 = book.readlines()

    book_2[id_contact - 1] = f"{fio} {phone_number}\n"

    with open('b:\Work\HW_Python\HW_8\contact.txt', "w", encoding="utf-8") as book:
        book.writelines(book_2)


def search_contact_read(search_info):
    with open('b:\Work\HW_Python\HW_8\contact.txt', 'r', encoding='utf-8') as book:
        data = book.read().split('\n')
        info = []
        for (res) in data:
            if search_info in res:
                info = res
                # Можно написать здесь print(info), тогда при запуске выведутся все контакты по запросу.
                # Пытался придумать, как это сделать, чтобы вывод был чисто черзе файл view, но в таком
                # случае, получается только вывод одного
        return info


def shearch_contact(book, res):
    return list(filter(lambda contact: res.lower() in contact.lower(), book))
