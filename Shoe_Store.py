from shoe_classes import Shoes
class shoeinventory():
    def __init__(self) :
        self.shoes = []
        
    def add_shoes(self , shoe , notify = True):
        self.shoes.append(shoe)
        if notify:
          print(f"The {shoe.brand} is add in the inventory of the store.")
    def view_inventory(self):
        if not self.shoes:
            print("No show is in Store .")
        else:
            for i ,shoe in enumerate(self.shoes, 1):
                print(f"{i} , {shoe}")
    def total_item(self):
        print(len(self.shoes))
    def remove_shoe(self,index):
        if 0 <= index < len(self.shoes):
            removed_shoe = self.shoes.pop(index)
            print(f"{removed_shoe.brand} from inventory")
        else:
            print("Invalid Index . No show on that index")
    
from shoe_data import pre_existing_shoes
def main():
    inventory = shoeinventory()
    
    for shoe in pre_existing_shoes:
        inventory.add_shoes(shoe , notify=False)
    
    while True:
        print("\t\t\t\t\tWelcome to Shoe Management System\t\t\t\t\t")
        print("1. Add Shoes")
        print("2. Show inventory")
        print("3. Reomve Shoes")
        print("4. Total inventory item")
        print("5. Exit")
        choice = int(input("Enter the Option in the Above Give (1--9)"))
        if choice == 1 :
            brand = input("Enter the Brand of Shoes = ")
            size = input("Enter the Size of Shoes = ")
            color = input("Enter the Color of Shoes = ")
            price = input("Enter the Price of Shoes = ")
            shoe = Shoes(brand,size,color,price)
            inventory.add_shoes(shoe) 
        elif choice == 2 :
            inventory.view_inventory()
        elif choice == 3 :
            inventory.view_inventory()
            index = int(input("Enter the index of shoes that you want to remove = "))
            inventory.remove_shoe(index)
        elif choice == 4:
            inventory.total_item()
        elif choice == 5:
            print("You are exit the System")
            break    
main()



    