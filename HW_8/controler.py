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
            data = input("Введите данные котакта, которые вам известно: ")
            res = model.search_contact_read(data)
            view.output_contact(res)

        elif ans == '3':
            fio = input("Введите ФИО через пробел: ")
            phone_number = input("Введите номер телефона: ")
            model.add_contact(fio, phone_number)
            view.add_contact(fio, phone_number)

        elif ans == '4':
            data = model.get_data()
            view.contacts_list(data)
            id_contact = int(
                input("Введите строку, которую хотите изменить: "))

            if id_contact < 1:
                view.error()
            else:
                fio = input("Введите новое ФИО через пробел: ")
                phone_number = input("Введите новый номер телефона: ")
                model.change_contact(id_contact, fio, phone_number)
                view.add_contact(fio, phone_number)

        elif ans == '5':
            data = model.get_data()
            id_contact = int(
                input("Введите строку, которую хотите удалить: "))
            if id_contact < 1:
                view.error()
            else:
                model.del_contact(id_contact)
                view.del_c()

        elif ans == '6':
            print("Всего доброго!")
            break

        else:
            view.error()
