def delete_contact():
    name = input('Введите имя контакта, который нужно удалить: ')
    with open('phonebook.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open('phonebook.txt', 'w', encoding='utf-8') as f:
        deleted = False
        for line in lines:
            if line.startswith(name + ":"):
                deleted = True
            else:
                f.write(line)

    if deleted:
        print(f"Контакт <{name}> удален!")
    else:
        print(f"Контакт <{name}> отсутствует в телефонной книге...")


def edit_contact():
    name = input('Введите имя контакта, который нужно изменить: ')
    with open('phonebook.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open('phonebook.txt', 'w', encoding='utf-8') as f:
        edited = False
        for line in lines:
            if line.startswith(name + ":"):
                new_number = input('Введите новый номер телефона: ')
                new_comment = input('Введите новый комментарий: ')
                f.write(f'{name}:{new_number}:{new_comment}\n')
                edited = True
            else:
                f.write(line)

        if edited:
            print(f"Контакт <{name}> изменен!")
        else:
            print(f"Контакт <{name}> отсутствует в телефонной книге...")


def find_contact():
    search_query = input("Введите запрос для поиска: ")
    with open("phonebook.txt", "r", encoding='utf-8') as f:
        phone_book = {}
        for line in f:
            name, number, comment = line.strip().split(":")
            phone_book[name] = (number, comment)
        results = []
        for key, value in phone_book.items():
            if search_query in key or search_query in value[0] or search_query in value[1]:
                results.append((key, value[0], value[1]))
        if results:
            print("Результаты поиска:")
            for result in results:
                print(f"{result[0]}: {result[1]} ({result[2]})")
        else:
            print(f"По запросу <{search_query}> нет результатов...")


def create_contact():
    name = input('Имя: ')
    phone = input('Телефон: ')
    comment = input('Комментарий: ')
    with open('phonebook.txt', 'a', encoding='utf-8') as f:
        f.write(f'{name}:{phone}:{comment}\n')
    print('Новый контакт добавлен!')


def view_contact():
    with open('phonebook.txt', 'r', encoding='utf-8') as f:
        phone_book = {}
        for line in f:
            name, number, comment = line.strip().split(':')
            phone_book[name] = (number, comment)
        for name, (number, comment) in phone_book.items():
            print(f'{name}: {number} ({comment})')


if __name__ == '__main__':
    main_menu = ("""\nГлавное меню
               1. Просмотреть контакты
               2. Создать контакт
               3. Найти контакт
               4. Изменить контакт
               5. Удалить контакт\n""")
    print(main_menu)

    while True:
        choice = int(input('Выберите действие: '))

        if choice == 1:
            view_contact()
        elif choice == 2:
            create_contact()
        elif choice == 3:
            find_contact()
        elif choice == 4:
            edit_contact()
        elif choice == 5:
            delete_contact()
        elif choice == 6:
            print(main_menu)
        elif choice == 7:
            exit()
        else:
            print('Неизвестная команда')
