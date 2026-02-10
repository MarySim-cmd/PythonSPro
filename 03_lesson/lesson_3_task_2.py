from smartphone import Smartphone

catalog = [
    Smartphone("OnePlus", "Snapdragon® 8 Gen 5", "+79120110100"),
    Smartphone("Samsung", "Galaxy S23", "+79120110101"),
    Smartphone("iPhone", "18 Pro Max", "+79120110102"),
    Smartphone("Xiaomi", "13T Pro", "+79120110103"),
    Smartphone("Google", "Pixel 8", "+79120110104")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.phone_number}")