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
            contact = input("Введите данные котакта через пробед: ")
            result_search = model.search_contact(contact)
            view.output_contact(result_search)

        elif ans == '3':
            contact = input("Введите данные котакта через пробед: ")
            add_result = model.add_contact(contact)
            if add_result:
                view.success(add_result)
            else:
                view.fail(add_result)

        elif ans == '4':
            break

        else:
            view.error()
