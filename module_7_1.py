from unittest.mock import right


class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        prod_str = file.read()
        file.close()
        return prod_str

    def add(self, *products):
        current_prod = self.get_products()
        file = open(self.__file_name, 'a')
        for product in products:
            if str(product) not in current_prod:
                file.write(str(product) + '\n')
                current_prod += str(product) + '\n'
            else:
                print('Продукт уже есть в магазине')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

