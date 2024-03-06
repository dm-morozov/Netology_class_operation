import datetime

class Client:
    """
    The Client class represents a client with discount information.

    Attributes:
    - email: str - the email of the client
    - order_num: int - the number of orders made by the client
    - registration_year: int - the year of registration in the loyalty program
    - is_employee: bool - indicates if the client is an employee of the company
    - discount: float - the discount percentage for the client

    Methods:
    - __init__(self, email, registration_year, order_num=0, is_employee=False): constructor that initializes the client attributes
    - make_order(self, price): makes an order and updates the discount
    - update_discount(self): updates the discount based on the client's registration year and order count

    Example usage:
    client = Client("example@example.com", 2018)
    client.make_order(100)
    print(client.discount)
    """

    def __init__(self, email, registration_year, order_num=0, is_employee=False):
        self.email = email
        self.order_num = order_num
        self.registration_year = registration_year
        self.is_employee = is_employee

    def make_order(self, price):
        self.update_discount()
        discounted_price = price * (1 - self.discount)

        # тут должна быть реальная логика заказа, но мы просто выводим стоимость
        print(f"Цена заказа для {self.email} составляет {discounted_price}")
        self.order_num += 1

    def update_discount(self):
        current_year = datetime.datetime.now().year  # определение текущего года
        years_since_registration = current_year - self.registration_year
        discount_increment = years_since_registration // 1  # 1% за каждый год
        discount_increment += self.order_num // 10 * 2  # 2% за каждые 10 заказов
        if self.is_employee:
            discount_increment += 10
        self.discount = min(discount_increment / 100, 0.3 if self.is_employee else 0.2)
        print(f'Текущая скидка для {self.email} составляет {self.discount :.2%}')


client_db = [
    Client("gman@gmail.com", 2019),
    Client("ya@ya.ru", 2012, 23),
    Client("old@mail.ru", 2023),
    Client("employee@example.com", 2020, is_employee=True)
]

client_db[0].make_order(100)
client_db[1].make_order(100)
client_db[2].make_order(100)
client_db[3].make_order(100)