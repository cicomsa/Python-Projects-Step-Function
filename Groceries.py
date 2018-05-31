import json 

product = input("Product name or write 'finished: ")
groceries = {}


def shopping():
    if quantity > 0:
        groceries.update({product : quantity})  
        if "finished" in groceries:
            del groceries["finished"] 
        return groceries
    
def checkError():
    try:  
        if quantity != int:
            raise TypeError(quantity)
    except TypeError:
        return print("The quantity value must be an integer. Converting now!")

def product_alpha():
    try:
        while product.isalpha() != True:
            raise TypeError(product)   
    except TypeError:
        return print("The product name must contain only letters.")
def quantity_digit():
    try:
        while quantity.isdigit() != True:
            raise TypeError(product)   
    except TypeError:
        return print("The quantity value must contain only digits.")
    
while product != "finished":
    while product.isalpha() != True:
        product_alpha()
        product = input("Product name or write 'finished: ") 
    while product.isalpha() == True:
        quantity = input("Product quantity, digit please: ")
        while quantity.isdigit() == False:
            quantity_digit()
            quantity = input("Product quantity, digit please: ")
        checkError()    
        quantity = int(quantity) 
        shopping()
        
        product = input("Product name or write 'finished: ") 
        shopping()
        if product == "finished":
            shopping()
            for i in groceries:
                if i == "finished":
                    groceries.pop({"finished"})
            break

with open('groceries.json', 'w') as file:
    json.dump(groceries, file)
    
with open('groceries.json') as file:
    groceries = json.load(file)
    print(groceries)