import os

def menu():
    print("Нажми 1, если хочешь создать контакт")
    print("Нажми 2, если хочешь просмотреть все контакты")
    print("Нажми 3, если хочешь удалить контакт")
    print("Нажми 4, если хочешь изменить контакт")
    print("Нажми 5, чтобы выйти из программы")

def create_contact(contacts):
    name = input("Введите имя контакта: ")
    phone = input("Введите номер телефона: ")
    address = input("Введите адрес контакта: ")
    contacts[name] = {"Телефон": phone, "Адрес": address}
    save_contacts(contacts)
    print(f"Контакт {name} успешно создан!")

def view_contacts(contacts):
    if contacts:
        print("Список контактов:")
        for name, info in contacts.items():
            print(f"Имя: {name}")
            print(f"Телефон: {info['Телефон']}")
            print(f"Адрес: {info['Адрес']}")
            print("------------")
    else:
        print("Справочник пуст!")

def delete_contact(contacts):
    name = input("Введите имя контакта, которого хотите удалить: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Контакт {name} успешно удален!")
    else:
        print(f"Контакт {name} не найден!")

def edit_contact(contacts):
    name = input("Введите имя контакта, которого хотите изменить: ")
    if name in contacts:
        new_phone = input("Введите новый номер телефона: ")
        new_address = input("Введите новый адрес: ")
        contacts[name] = {"Телефон": new_phone, "Адрес": new_address}
        save_contacts(contacts)
        print(f"Контакт {name} успешно изменен!")
    else:
        print(f"Контакт {name} не найден!")

def load_contacts():
    contacts = {}
    if os.path.exists("contacts.txt"):
        with open("contacts.txt", "r", encoding="utf-8") as file:
            for line in file:
                data = line.strip().split(":")
                name = data[0]
                phone = data[1]
                address = data[2]
                contacts[name] = {"Телефон": phone, "Адрес": address}
    return contacts

def save_contacts(contacts):
    with open("contacts.txt", "w", encoding="utf-8") as file:
        for name, info in contacts.items():
            file.write(f"{name}:{info['Телефон']}:{info['Адрес']}\n")


contacts = load_contacts()
while True:
    menu()
    choice = input("Выберите действие: ")
    if choice == "1":
        create_contact(contacts)
    elif choice == "2":
        view_contacts(contacts)
    elif choice == "3":
        delete_contact(contacts)
    elif choice == "4":
        edit_contact(contacts)
    elif choice == "5":
        break
    else:
        print("Неверный выбор. Попробуйте снова.")
