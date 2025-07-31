class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def info(self):
        print(f"{self.name} — narxi: {self.price}")

products = [
    Product("iPhone", 999.99, "elektronika"),
    Product("MacBook", 1299.99, "elektronika"),
    Product("AirPods", 199.99, "aksessuar"),
    Product("TV", 799.99, "maishiy"),
    Product("Speaker", 149.99, "aksessuar"),
    Product("iPad", 599.99, "elektronika")
]

most_expensive = max(products, key=lambda p: p.price)
most_expensive.info()
