import view
import model


def start():
    view.hiuser()

    while True:

        view.menu()
        ans = input('Введите действие, которое хотели бы выполнить: ')
        if ans == '1':
            data = model.get_data()
            view.contacts_list(data)

        elif ans == '2':
            record = input("Введите текст, что хотите добавить: ")
            model.add_contact(record)
            view.add_contact(record)

        elif ans == '3':
            data = model.get_data()
            view.contacts_list(data)
            id_record = int(
                input("Введите строку, которую хотите изменить: "))

            if id_record < 1:
                view.error()
            else:
                record = input("Введите новую заметку: ")
                model.change_contact(id_record, record)
                view.add_contact(record)

        elif ans == '4':
            data = model.get_data()
            id_record = int(
                input("Введите строку, которую хотите удалить: "))
            if id_record < 1:
                view.error()
            else:
                model.del_contact(id_record)
                view.del_c()

        elif ans == '5':
            print("Всего доброго!")
            break

        else:
            view.error()
