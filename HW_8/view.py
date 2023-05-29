
import model


def hiuser():
    return None


def menu():

    print(' 1 - Показать список всех контактов \n',
          '2 - Поиск контакта по запросу \n',
          '3 - Добавить контакт \n',
          '4 - Изменить контакт \n',
          '5 - Удалить контакт \n',
          '6 - Выход \n')


def contacts_list(data):
    return data


def add_contact(fio, phone_number):
    print(f"Добавлена запись : {fio} {phone_number}\n")


def output_contact(contact):

    return None


def success():
    print("Действие произведено успешно")
    return None


def fail():
    print("Действие не увенчалось успехом")
    return None


def error():
    print("Ошибка, введены неверные данные")


if __name__ == '__main__':
    menu()
