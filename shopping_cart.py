
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] 

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" 

#print(products)

selected_products=[]
total_price=0
while True:

    #ask for user input
    product_id=input("Please input a product identifier: ")
    #print(product_id) #>9
    #print(type(product_id))
    #type of input(product_id) 9 is a string 
    
    if product_id=="DONE":
        break
    else:
        selected_products.append(product_id)

    #look up corresponding product, store the loop output
    ###for i in products:
    ###    if str(i["id"]) == str(product_id):
    ###        selected_products.append(i["name"])
    ###        selected_products.append(i["price"])

    
#print the product that has an id attribute to 9
    #matching_products=[]
    ##for x in products:
    ##    if str(x["id"]) == str(product_id):
    ##        matching_products.append(x)   #X is a dict
    #print(matching_products)
    #print(type(matching_products)) #it is a list
    #print(len(matching_products))
    # print the name of the matching product
    #Make matching_products from list to dict



import os
#from dotenv import load_dotenv
#load_dotenv() 
#TAX_RATE=os.getenv("TAX_RATE")
TAX_RATE=0.0875



print ("---------------------------------")
print ("GREEN FOODS GROCERY")
print ("WWW.GREEN-FOODS-GROCERY.COM")
print ("---------------------------------")
from datetime import datetime 
print("CHECK OUT AT: ", datetime.now())
print ("---------------------------------")
print ("SELECTED PRODUCTS: ")

matching_products=[]
for product_id in selected_products:
    matching_products = [x for x in products if str(x["id"]) == str(product_id)]
    matching_product = matching_products[0]
    total_price=total_price+matching_product["price"]
    print("... ", matching_product["name"], "(", to_usd(matching_product["price"]), ") ")
print ("---------------------------------")

print ("SUBTOTAL: ", to_usd(total_price))
print ("TAX: ", to_usd(total_price*TAX_RATE))
print ("TOTAL: ", to_usd(total_price*(1+TAX_RATE)))
print ("---------------------------------")
print ("THANKS, SEE YOU AGAIN SOON!")
print ("---------------------------------")
