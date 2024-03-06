# class Passport:
#     pages = 20

#     def add_visa(self, visa_name):
#         # hassattr - проверяет наличие атрибута у объекта
#         if not hasattr(self, 'visas'):
#             self.visas = [visa_name]  # Атрибут экземпляра для хранения списка названий виз
#         else:
#             self.visas.append(visa_name)  # Добавление нового названия визы к существующему списку виз

#     def print_all_visas(self):
#         if not hasattr(self, 'visas'):
#             print('Нет виз')
#         else:
#             print(f'Список всех виз: {", ".join(self.visas)}')

# passport_1 = Passport()
# passport_2 = Passport()

# passport_1.name = 'Oleg'
# passport_2.name = 'Kate'

# passport_1.visas = ['visa_1', 'visa_2']
# passport_1.print_all_visas()
# passport_1.add_visa('visa_3')
# passport_1.print_all_visas()

# passport_2.print_all_visas()


class Passport:
    """Класс Паспорт
       
    Описание:
    Этот класс представляет собой модель паспорта с основной информацией о человеке и его визами.
    
    Атрибуты:
    - pages (int): количество страниц в паспорте (по умолчанию 20).
    
    Методы:
    1. __init__(first_name, last_name, date_of_birth)
       Описание: Конструктор класса, создает новый паспорт с указанными данными.
       Аргументы:
       - first_name (str): имя владельца паспорта.
       - last_name (str): фамилия владельца паспорта.
       - date_of_birth (str): дата рождения владельца паспорта в формате "дд.мм.гггг".
       
    2. add_visa(visa_name)
       Описание: Добавляет новую визу в паспорт.
       Аргументы:
       - visa_name (str): название визы.
       
    3. print_all_visas()
       Описание: Выводит список всех виз в паспорте.
       
    4. show_info()
       Описание: Выводит основную информацию о владельце паспорта, включая имя, фамилию и дату рождения.
    """
    pages = 20

    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        print('Добавлен новый паспорт')

    def add_visa(self, visa_name):
        if not hasattr(self, 'visas'):
            self.visas = [visa_name]
        else:
            self.visas.append(visa_name)

    def print_all_visas(self):
        if not hasattr(self, 'visas'):
            print('Нет виз')
        else:
            print(f'Список всех виз: {", ".join(self.visas)}')

    def show_info(self):
        print(f'Имя: {self.first_name}, Фамилия: {self.last_name}, Дата рождения: {self.date_of_birth}')


passport_1 = Passport('Dmitriy', 'Morozov', '10.03.1991')
passport_1.add_visa('MIR_0845')
passport_1.print_all_visas()

passport_1.show_info()