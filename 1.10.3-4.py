class Client:
    def __init__(self, name, lastname, city, account):
        self.name = name
        self.lastname = lastname
        self.city = city
        self.account = account

    def __str__(self):
        return f' {self.name} {self.lastname}. {self.city}. Баланс:{self.account} руб. '

    def get_guest(self):
        return f'{self.name} {self.lastname},г. {self.city}'

client_1 = Client("Иван", "Петров", "Москва", 50)
client_2 = Client("Игорь", "Яковенко", "Москва", 50)
client_3 = Client("Дмитрий", "Миленин", "Москва", 50)

print(client_1)

guest_list = [client_1, client_2, client_3]

for guest in guest_list:
    print(guest.get_guest())