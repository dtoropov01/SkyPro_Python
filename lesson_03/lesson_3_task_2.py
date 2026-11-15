from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 18", "+79226780971"),
    Smartphone("Samsung", "Galaxy S26", "+79226780972"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79226780973"),
    Smartphone("OnePlus", "OnePlus 16", "+79226780974"),
    Smartphone("Huawei", "P60 Pro", "+79226780975"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")