from smartphone import Smartphone

catalog = [
    Smartphone ("POCO", "X7", "8-987-987-87-76"),
    Smartphone ("POCO", "X6", "8-987-987-87-75"),
    Smartphone ("POCO", "X5", "8-987-987-87-74"),
    Smartphone ("POCO", "X4", "8-987-987-87-73"),
    Smartphone ("POCO", "X3", "8-987-987-87-71")
]

for smartphone in catalog:
    print (f"{smartphone.brand_phone} - {smartphone.model_phone} - {smartphone.number_phone}")