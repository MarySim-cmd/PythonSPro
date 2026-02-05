from Address import Address
from Mailing import Mailing

mailing = Mailing(
    to_address=Address("123456", "Тюмень", "Республики", "180", "115"),
    from_address=Address("101000", "Москва", "Тверская", "15", "25"),
    cost=350,
    track="TR123456789RU"
)
print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")