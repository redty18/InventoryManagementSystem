class Product:
    def __init__(self, product_id, name, price, quantity_available):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity_available = quantity_available
    
    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity_available}"
    
    def calculate_value(self):
        return self.price * self.quantity_available 
    
    def add_product(self, productList, newProduct):
        inList = False
        if newProduct == None:
            print("This Product doesn't exist.")
        else:
            for product in productList:
                if product.product_id == newProduct.product_id:
                    inList = True
                    break
            if inList == False:
                productList.append(newProduct)
            else:
                print("This product is already available, please enter a unique product.")


    def display_product_details(self):
        print("Product ID is:", self.product_id)
        print("Product Name is:", self.name)
        print("Product Price is:", self.price)
        print("Quantity of Product Available:", self.quantity_available)
        print("Total Value of Product:", self.calculate_value())

    def find_product_by_id(self, productList, productID):
        isPresent = False
        for product in productList:
            if product.product_id == productID:
                isPresent = True
                break
        if isPresent == True:
            return product
        else:
            return "The Product was not found."
    
    def calculate_inventory_value(self, productList):
        totalValue = 0
        for product in productList:
            totalValue += self.calculate_value()
        return totalValue
    
product1 = Product(product_id=1, name="Laptop", price=1200, quantity_available=5)
product2 = Product(product_id=2, name="Printer", price=300, quantity_available=8)

inventory_list = [product1, product2]

new_product = Product(product_id=3, name="Mouse", price=20, quantity_available=15)
product1.add_product(inventory_list, new_product)

# product3 = Product(product_id=3, name="MLH", price=100, quantity_available=12)
# product3.add_product(inventory_list, product3)

# product4 = None
# product3.add_product(inventory_list, product4)
# product3.display_product_details()

# found_product = product2.find_product_by_id(inventory_list, 4)
# print(found_product)

# if found_product:
#     print("Found product:")
#     product2.display_product_details()
# else:
#     print("Product not found.")

inventory_value = product2.calculate_inventory_value(inventory_list)
print("Inventory value:", inventory_value)