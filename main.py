from pyscript import display
#restaurant order system (python data types)

#string
restaurant_name = "A Votre Santé"
owner_name = "Matt Sturniolo"

#integer
year_since = 2025

#float
tax_rate = 0.08

#boolean
has_delivery = True
is_dine_in = True
is_takeaway = False

#list
product_names = ["Croissant", "Eclair", "Pain au chocolat"]
beverages = ["Hot Chocolate", "Champagne", "Cafe au Lait"]

#tuple
business_hours = ("5:00 AM", "10:00 PM")

#dictionary
menu = {
    "Croissant": 3.99,
    "Eclair": 4.99,
    "Pain au chocolat": 5.99,
    "Hot Chocolate": 9.99,
    "Champagne": 19.99,
    "Cafe au Lait": 14.99
}

#set
common_allergens = {"gluten", "dairy"}

#display restaurant information
display(restaurant_name, target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Since {year_since}", target="since")
display("Menu Pricelist", target="heading1")

#display
display(product_names[0], target="prod1")
display(f"€{menu['Croissant']:.2f}", target="price1")
display(product_names[1], target="prod2")
display(f"€{menu['Eclair']:.2f}", target="price2")
display(product_names[2], target="prod3")
display(f"€{menu['Pain au chocolat']:.2f}", target="price3")

display(beverages[0], target="prod4")
display(f"€{menu['Hot Chocolate']:.2f}", target="price4")
display(beverages[1], target="prod5")
display(f"€{menu['Champagne']:.2f}", target="price5")
display(beverages[2], target="prod6")
display(f"€{menu['Cafe au Lait']:.2f}", target="price6")


#Display additional information
display(f"Open: {business_hours[0]} - {business_hours[1]}", target="openingHours")

#Display order type
if is_dine_in:
    display("Dine-in Available", target="orderType")
elif has_delivery:
    display("Delivery Available", target="orderType")
elif is_takeaway:
    display("Takeout Only", target="orderType")
else:
    display("Closed for Orders", target="orderType")
