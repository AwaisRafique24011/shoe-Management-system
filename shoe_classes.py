class Shoes():
    def __init__(self,brand,size,color,price) :
        self.brand = brand
        self.size = size
        self.color = color 
        self.price = price
    def __str__(self) :
        return f"The brand is : '{self.brand}' The size is : '{self.size}' The color is :'{self.color}' The price is : '{self.price}'"
