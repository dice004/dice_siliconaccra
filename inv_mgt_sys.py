#Create a program to manage an inventory of products, 
#including adding, 
#updating 
#displaying items.
print("\n") 
inv_dict = {"Tables" :19,
            "iMacs" :19,
            "Chairs" :19, 
            "Keyboards" :19, 
            "Mice" :19,
            "UPS" :19,
            "Preomethean" :1,
            "Whiteboard" :1}
print("Current Inventory is: ", inv_dict)

print("\n")
x = int(input("How many new items do you want to add?: "))

print("\n")
for i in range(x):
    name = input("what is the new item to add to inventory?: ")
    quantity = int(input("What is the quantity of the new inventory item?: "))
    inv_dict[name] = quantity
    print("\n")
print("New inventory is:", inv_dict)






























#yek = 
#lue = 
def update_inv(yek, lue):
    update = {**inv_dict, **{yek:lue}}
    print(update)
    return update


