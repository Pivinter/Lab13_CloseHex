class Note:
    def __init__(self, surname, name, phone_number, birthdate):
        self.surname = surname
        self.name = name
        self.phone_number = phone_number
        self.birthdate = birthdate


class ClosedHashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, note):
        index = self.hash_function(note.phone_number)
        for i in range(self.size):
            new_index = (index + i) % self.size
            if self.table[new_index] is None:
                self.table[new_index] = note
                return
        raise Exception("Хеш-таблиця повна")
    
    def display(self):
        for index, note in enumerate(self.table):
            if note is not None:
                print(f'[{index}] {note.surname} {note.name}, {note.phone_number}, {".".join(note.birthdate)}')
            else:
                print(f'[{index}] Empty')

    def delete(self, phone_number):
        index = self.hash_function(phone_number)
        for i in range(self.size):
            new_index = (index + i) % self.size
            if self.table[new_index] is not None and self.table[new_index].phone_number == phone_number:
                self.table[new_index] = None
                return True
        return False
    
    def delete_by_name(self, name):
        for i in range(self.size):
            if self.table[i] is not None and self.table[i].name == name:
                self.table[i] = None
                return True
        return False

    def delete_by_birthdate(self, birthdate):
        for i in range(self.size):
            if self.table[i] is not None and self.table[i].birthdate == birthdate:
                self.table[i] = None
                return True
        return False

    def search(self, phone_number):
        index = self.hash_function(phone_number)
        for i in range(self.size):
            new_index = (index + i) % self.size
            if self.table[new_index] is not None and self.table[new_index].phone_number == phone_number:
                return self.table[new_index]
        return None
    
    def search_by_name(self, name):
        result = []
        for note in self.table:
            if note is not None and note.name == name:
                result.append(note)
        return result

    def search_by_birthdate(self, birthdate):
        result = []
        for note in self.table:
            if note is not None and note.birthdate == birthdate:
                result.append(note)
        return result
    
    def save_to_file(self, file_name):
        data = []
        for note in self.table:
            if note is not None:
                data.append(f"{note.surname};{note.name};{note.phone_number};{'.'.join(note.birthdate)}")

        with open(file_name, "w") as file:
            file.writelines('\n'.join(data))

    def load_from_file(self, file_name):
        try:
            with open(file_name, "r") as file:
                data = file.readlines()
        except FileNotFoundError:
            raise Exception(f"Файл {file_name} не знайдено")

        for note_data in data:
            surname, name, phone_number, birthdate = note_data.strip().split(";")
            birthdate = birthdate.split(".")
            note = Note(surname, name, phone_number, birthdate)
            self.insert(note)

hash_table = ClosedHashTable()
while True:
        print("1. Додати запис")
        print("2. Видалити запис")
        print("3. Знайти запис")
        print("4. Зберегти в файл")
        print("5. Завантажити з файлу")
        print("6. Відобразити таблицю")
        print("0. Вихід")

        choice = input("Введіть ваш вибір: ")

        if choice == "1":
            surname = input("Введіть прізвище: ")
            name = input("Введіть ім'я: ")
            phone_number = input("Введіть номер телефону: ")
            birthdate = input("Введіть день народження у форматі ДД.ММ.РРРР: ").split(".")
            note = Note(surname, name, phone_number, birthdate)
            hash_table.insert(note)
            print("Запис додано.")

        elif choice == "2":
            print("Виберіть параметр для видалення:")
            print("1. Номер телефону")
            print("2. Ім'я")
            print("3. Дата народження")
            delete_choice = input("Введіть ваш вибір: ")

            if delete_choice == "1":
                phone_number = input("Введіть номер телефону для видалення: ")
                if hash_table.delete(phone_number):
                    print("Запис видалено.")
                else:
                    print("Запис не знайдено.")
            elif delete_choice == "2":
                name = input("Введіть ім'я для видалення: ")
                if hash_table.delete_by_name(name):
                    print("Запис видалено.")
                else:
                    print("Запис не знайдено.")
            elif delete_choice == "3":
                birthdate = input("Введіть день народження у форматі ДД.ММ.РРРР: ").split(".")
                if hash_table.delete_by_birthdate(birthdate):
                    print("Запис видалено.")
                else:
                    print("Запис не знайдено.")
            else:
                print("Неправильний вибір. Спробуйте ще раз.")

        elif choice == "3":
            print("Виберіть параметр для пошуку:")
            print("1. Номер телефону")
            print("2. Ім'я")
            print("3. Дата народження")
            search_choice = input("Введіть ваш вибір: ")

            if search_choice == "1":
                phone_number = input("Введіть номер телефону для пошуку: ")
                found_note = hash_table.search(phone_number)
                if found_note is not None:
                    print(f"Прізвище: {found_note.surname}")
                    print(f"Ім'я: {found_note.name}")
                    print(f"Номер телефону: {found_note.phone_number}")
                    print(f"День народження: {'.'.join(found_note.birthdate)}")
                else:
                    print("Запис не знайдено.")
            elif search_choice == "2":
                name = input("Введіть ім'я для пошуку: ")
                found_notes = hash_table.search_by_name(name)
                if found_notes:
                    for note in found_notes:
                        print(f"Прізвище: {note.surname}")
                        print(f"Ім'я: {note.name}")
                        print(f"Номер телефону: {note.phone_number}")
                        print(f"День народження: {'.'.join(note.birthdate)}")
                        print("----------")
                else:
                    print("Записи не знайдено.")
            elif search_choice == "3":
                birthdate = input("Введіть день народження у форматі ДД.ММ.РРРР: ").split(".")
                found_notes = hash_table.search_by_birthdate(birthdate)
                if found_notes:
                    for note in found_notes:
                        print(f"Прізвище: {note.surname}")
                        print(f"Ім'я: {note.name}")
                        print(f"Номер телефону: {note.phone_number}")
                        print(f"День народження: {'.'.join(note.birthdate)}")
                        print("----------")
                else:
                    print("Записи не знайдено.")
            else:
                print("Неправильний вибір. Спробуйте ще раз.")
        elif choice == "4":
            file_name = input("Введіть ім'я файлу для збереження: ")
            try:
                hash_table.save_to_file(file_name)
                print("Записи збережено в файл.")
            except Exception as e:
                print(f"Помилка збереження в файл: {str(e)}")

        elif choice == "5":
            file_name = input("Введіть ім'я файлу для завантаження: ")
            try:
                hash_table.load_from_file(file_name)
                print("Записи завантажено з файлу.")
            except Exception as e:
                print(f"Помилка завантаження з файлу: {str(e)}")
        elif choice == "6":
            print("Закрита хеш-таблиця:")
            hash_table.display()
        elif choice == "0":
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")