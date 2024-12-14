class Shop_main:

    def __init__(self, name=None, type=None, price=None, total=None):
        self.name = name
        self.price = price
        self.type = type
        self.total = total

    def display_info(self):
        return f"Name : {self.name}\nType : {self.type}\nPrice : {self.price}\nTotal : {self.total}"


class Manage_products:
    def __init__(self):
        self.stock = {}

    def add(self, shop: Shop_main):
        self.stock[shop.name] = {
            "type": shop.type,
            "price": shop.price,
            "total": shop.total,
        }

    def delet(self, name):
        self.stock = {
            name: value for name, value in self.stock.items() if name not in self.stock
        }
        return self.stock

    def search(self, name):
        verify = {
            name: value for name, value in self.stock.items() if name in self.stock
        }
        show_search = ""
        for ke, va in verify.items():
            show_search += f"Name : {ke}\nType : {va['type']}\nPrice : {va['price']}\nTotal : {va['total']}\n"
        return show_search

    def display_info(self):
        result = ""
        for name, detail in self.stock.items():
            result += f"Name : {name}\nType : {detail['type']}\nPrice : {detail['price']}\nTotal : {detail['total']}"
        return result


shop = Shop_main("Sumsung", "Phon", 16000)
# print(shop.display_info())
manage = Manage_products()
manage.add(shop)
print(manage.search("Sumsung"))
