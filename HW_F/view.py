
def hiuser():
    print("Здравствуйте, это блокнот с заметкамми, что бы вы хотели сделать?\n")


def menu():
    print('Выберите интересующий пункт')
    print(' 1 - Показать список всех заметок \n',
          '2 - Добавить заметку \n',
          '3 - Изменить заметку \n',
          '4 - Удалить заметку \n',
          '5 - Выход \n')


def contacts_list(data):
    return data


def add_contact(record):
    print(f"Добавлена запись : {record}\n")


def output_contact(res):
    print(res)


def del_c():
    print("Заметка успешно удалена")


def error():
    print("Ошибка, введены неверные данные")


if __name__ == '__main__':
    menu()
