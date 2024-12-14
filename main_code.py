class Shop:
    def __init__(self):
        self.all_products = []

    def add(self, name, type, price, total):
        add_product = {name: {"type": type, "price": price, "total": total}}
        for verify in self.all_products:
            if name not in verify:
                self.all_products.append(add_product)
                return "\nAdded successfully"
            else:
                return "Same name, please rename."

    def delete(self, name):
        original_length = len(self.all_products)
        self.all_products = [
            delete_product
            for delete_product in self.all_products
            if name not in delete_product
        ]
        if len(self.all_products) < original_length:
            return "Removed successfully"
        else:
            return "No Data"

    def show(self):
        if not self.all_products:
            return "\nNo Data\n"
        details = ""
        for show_product in self.all_products:
            for name, detail in show_product.items():
                details += f"\nName : {name}\n    Type  : {detail['type']}\n    Price : {detail['price']}\n    Total : {detail['total']}"
        return details

    def search(self, name):
        found = False
        result = ""
        for search_product in self.all_products:
            if name in search_product:
                found = True
                for name2, detail in search_product.items():
                    result += f"\nName : {name2}\n    Type  : {detail['type']}\n    Price : {detail['price']}\n    Total : {detail['total']}"
                break
        if found:
            return result
        else:
            return "No Data"


def Enter_Number(message):
    while True:
        try:
            num = int(input(message))
            if num < 0:
                print("Number must be positive. Pleas try again.")
            return num
        except ValueError:
            print("Please Enter Number")


def stock():
    data = Shop()
    running = True
    while running:
        print("\n-----This is your Stocks-----\n")
        print("1.Add\n2.Delete\n3.show\n4.search\n5.Exit\n")
        menu = Enter_Number("Enter Number :")
        if menu == 1:
            print("add")
            name = input("Enter name :")
            type_pro = input("Enter type :")
            price = Enter_Number("Enter price :")
            total = Enter_Number("Enter total :")
            print(data.add(name, type_pro, price, total))
        elif menu == 2:
            print("del")
            Del = input("Enter name :")
            print(data.delete(Del))
        elif menu == 3:
            print("show")
            print(data.show())
        elif menu == 4:
            print("search")
            search = input("Enter name :")
            print(data.search(search))
        elif menu == 5:
            print("Exiting...")
            break
        else:
            print("please try again.")


stock()
