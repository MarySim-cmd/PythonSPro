class Smartphone:
    def __init__(self, brand, model, phone_number):
        self.brand = brand
        self.model = model
        self.phone_number = phone_number

my_Smartphone = Smartphone(
    brand="Oneplus",
    model="Snapdragon® 8 Gen 5", 
    phone_number="+79120110100"
)
print(my_Smartphone.brand)
print(my_Smartphone.model)
print(my_Smartphone.phone_number)