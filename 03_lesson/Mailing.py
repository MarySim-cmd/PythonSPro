from Address import Address

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

to_addr = Address("123456", "Тюмень", "Республики", "180", "115")
from_addr = Address("101000", "Москва", "Тверская", "15", "25")
mail = Mailing(to_addr, from_addr, 350, "TR123456789RU")

print("Трек-номер:", mail.track)
print("Стоимость:", mail.cost)
print("\nАдрес отправителя:")
print("  Город:", mail.from_address.city)
print("  Улица:", mail.from_address.street)
print("  Дом:", mail.from_address.house)
print("  Квартира:", mail.from_address.apartment)


print("\nАдрес получателя:")
print("  Город:", mail.to_address.city)
print("  Улица:", mail.to_address.street)
print("  Дом:", mail.to_address.house)
print("  Квартира:", mail.to_address.apartment)