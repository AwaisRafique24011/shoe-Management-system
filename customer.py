# customer_module.py

from shoe_classes import Shoes
from shoe_data import pre_existing_shoes

class ShoeInventory:
    def __init__(self):
        self.shoes = []

    def view_inventory(self):
        if not self.shoes:
            print("No shoes in the store.")
        else:
            for i, shoe in enumerate(self.shoes, 1):
                print(f"{i}. {shoe}")
    def search_shoe(self, brand):
        found_shoes = [shoe for shoe in self.shoes if shoe.brand.lower() == brand.lower()]
        if found_shoes:
            for i, shoe in enumerate(found_shoes):
                print(f"{shoe}")
        else:
            print("No shoes available for the given brand.")

    def search_size(self, size):
        found_shoes = [shoe for shoe in self.shoes if shoe.size == int(size)]
        if found_shoes:
            for i, shoe in enumerate(found_shoes):
                print(f"{shoe}")
        else:
            print("No shoes available for the given size.")

    def search_price(self, price):
        found_shoes = [shoe for shoe in self.shoes if shoe.price == float(price)]
        if found_shoes:
            for i, shoe in enumerate(found_shoes):
                print(f"{shoe}")
        else:
            print("No shoes available for the given price.")

    def search_color(self, color):
        found_shoes = [shoe for shoe in self.shoes if shoe.color.lower() == color.lower()]
        if found_shoes:
            for i, shoe in enumerate(found_shoes):
                print(f"{shoe}")
        else:
            print("No shoes available for the given color.")
    def intro(self , name , balance) :
        print(f"Welcome '{name}' to Shopping Centre \n Your Balance is '{balance}'.")

class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.cart = []
    
        
    def add_to_cart(self, shoe):
        self.cart.append(shoe)
        print(f"{shoe.brand} added to cart.")

    def view_cart(self):
        if not self.cart:
            print("Cart is empty.")
        else:
            print("Your cart contains:")
            for i, shoe in enumerate(self.cart, 1):
                print(f"{i}. {shoe}")

    def remove_from_cart(self, index):
        if 0 <= index < len(self.cart):
            removed_shoe = self.cart.pop(index)
            print(f"{removed_shoe.brand} removed from cart.")
        else:
            print("Invalid index. No shoe at that index.")

    def checkBill(self):
        total_price = sum(shoe.price for shoe in self.cart)
        print(f"Total price: {total_price}")
        print(f"Your current balance: {self.balance}")
    def checkout(self):
            total_price = sum(shoe.price for shoe in self.cart)
            if self.balance >= total_price:
                self.balance -= total_price
                print(f"Payment successful. Remaining balance: {self.balance}")
                self.cart = []
            else:
                print("Insufficient balance. Please add more funds or remove items from the cart.")

def customer_interface():
    inventory = ShoeInventory()
    inventory.shoes.extend(pre_existing_shoes)

    customer = Customer("John Doe", 500)  # Example customer with initial balance

    while True:
        print("\t\t\t\tWelcome to Shopping Store\t\t\t\t")
        print("0. Customer Detail ")
        print("1. View Inventory")
        print("2. Search show by Brand \t\t\t 3.Search show by Size")
        print("4. Search show by Color \t\t\t 5.Search show by Price")
        print("6. Add Item to Cart \t\t\t\t 7. View Cart")
        print("8. Remove Item from Cart")
        print("9. CheckBill \t\t\t\t\t 10.Checkout")
        print("11. Exit")
        choice = int(input("Enter the option (0--11): "))
        if choice == 0:
            name = input("Enter Your Name Please = ")
            balance = input("Enter Your Balance of ATM Card = ")
            inventory.intro(name ,balance)
        elif choice == 1:
            inventory.view_inventory()
        elif choice == 2:
            
            brand = input("Enter the brand you search for = ")
            inventory.search_shoe(brand)
        elif choice == 3:
            
            size = input("Enter the size you search for = ")
            inventory.search_size(size)
        elif choice == 4:
            
            color = input("Enter the color you search for = ")
            inventory.search_color(color)
        elif choice == 5:
            
            price = input("Enter the price you search for = ")
            inventory.search_price(price)
        elif choice == 6:
            index = int(input("Enter the index of the shoe to add to cart: ")) - 1
            if 0 <= index < len(inventory.shoes):
                customer.add_to_cart(inventory.shoes[index])
            else:
                print("Invalid index.")
        elif choice == 7:
            customer.view_cart()
        elif choice == 8:
            customer.view_cart()
            index = int(input("Enter the index of the item to remove from cart: ")) - 1
            customer.remove_from_cart(index)
        elif choice == 9:
            customer.checkBill()
        elif choice == 10:
            customer.checkout()
        elif choice == 11:
            print("Thank you  for your shopping at our store ")
            break
        else:
            print("Invalid choice. Please try again.")


customer_interface()
