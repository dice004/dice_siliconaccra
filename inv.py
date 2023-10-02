# Setting Initial Inventory Database
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

# Making an update to the already existing inventory
update = int(input("If you wish to make changes with items already existing in catalog, how many will they be?: "))
print("\n")
y = int(input("How many already existing items do you want to add changes to?: "))
print("\n")
if update > 0 :
    for i in range(y):
                al_inv = input("what is the already existing item to make changes to?: ")
                new_val = int(input("What is the quantity already existing item to make changes to?: "))
                updated_inv = inv_dict[al_inv] = new_val 
    else:
        print("Updated Inventory is: ",updated_inv)



# Asking User for New Inventory Information to update database with
print("\n")
x = int(input("How many new items do you want to add?: "))

print("\n")
for i in range(x):
    name = input("what is the new item to add to inventory?: ")
    quantity = int(input("What is the quantity of the new inventory item?: "))
    inv_dict[name] = quantity
    print("\n")
print("New inventory is:", inv_dict)

































