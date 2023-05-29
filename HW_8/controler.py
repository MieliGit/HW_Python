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
            contact = input("Введите данные котакта через пробел: ")
            result_search = model.search_contact(contact)
            view.output_contact(result_search)

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
            contact = input("Введите данные котакта через пробел: ")
            del_result = model.del_contact(contact)
            if del_result:
                view.success(del_result)
            else:
                view.fail(del_result)

        elif ans == '6':
            break

        else:
            view.error()
