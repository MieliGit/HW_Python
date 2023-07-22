
def get_data():
    with open('b:\Work\HW_Python\HW_F\ynotes.txt', 'r', encoding='utf-8') as book:
        print(book.read())


def add_contact(record):
    with open('b:\Work\HW_Python\HW_F\ynotes.txt', "r", encoding="utf-8") as book:
        book.read()
    with open('b:\Work\HW_Python\HW_F\ynotes.txt', "a", encoding="utf-8") as book:
        book.writelines(f"{record}\n")


def del_contact(id_record):
    with open('b:\Work\HW_Python\HW_F\ynotes.txt', 'r', encoding='utf-8') as book:
        book_2 = book.readlines()

    book_2[id_record - 1] = ''

    with open('b:\Work\HW_Python\HW_F\ynotes.txt', "w", encoding="utf-8") as book:
        book.writelines(book_2)


def change_contact(id_record, record):

    with open('b:\Work\HW_Python\HW_F\ynotes.txt', 'r', encoding='utf-8') as book:
        book_2 = book.readlines()

    book_2[id_record - 1] = f"{record}\n"

    with open('b:\Work\HW_Python\HW_F\ynotes.txt', "w", encoding="utf-8") as book:
        book.writelines(book_2)


# def search_contact_read(search_info):
#     with open('b:\Work\HW_Python\HW_F\ynotes.txt', 'r', encoding='utf-8') as book:
#         data = book.read().split('\n')
#         info = []
#         for (res) in data:
#             if search_info in res:
#                 info.append(res)
#         return info


# def shearch_contact(book, res):
#     return list(filter(lambda contact: res.lower() in contact.lower(), book))
