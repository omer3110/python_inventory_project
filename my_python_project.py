# my app

def is_category_number(x):#validate that the input is the category number
    return x == 1 or  x == 2 or  x == 3 or  x == 4

def category_name (x):#validate the category name
    if x == 1:
        category = 'Food'
    elif x == 2:
        category = 'Pants'
    elif x == 3:
        category = 'Shirts'
    elif x == 4:
        category = 'Toys'
    else:
        category = 'None'
    return category

def is_action_number(x):#validate the action number
    return x == 1 or  x == 2 

def is_positive_integer(x):
    return x > 0

def is_yes_or_no(x):#validate reapet input yes or no
    lower_input = x.lower()
    return x == 'yes' or x == 'no'

dict_items = {'Food' : 8, 'Pants' :  14, 'Shirts': 8, 'Toys' : 26 }
repeat_input = 'yes'
while repeat_input == 'yes':
    category_input = int(input(""" Please input a number for the desired item to update:
    # 1. Food
    # 2. Pants
    # 3. Shirts
    # 4. Toys
    """))
    while is_category_number(category_input) == False:
        print("Insert number from the suggested categories only!")
        category_input = int(input(""" Please input a number for the desired item to update:
    # 1. Food
    # 2. Pants
    # 3. Shirts
    # 4. Toys
    """))
    category = category_name(category_input)
    
    action_input = 0
    while is_action_number(action_input) == False:
        print(f"{category}: Insert number from the suggested actions only!")
        action_input = int(input(""" Please input the number for action:
        # 1. Add
        # 2. Remove
        """))
    
    if action_input == 1:
        action = 'Add'
    else:
        action = 'Remove'
    number_of_items_input = int(input(f"{category}: Please input the number of items to {action}: current amount is {dict_items[category]} "))
    while is_positive_integer(number_of_items_input) == False:
        print("Insert a positive number only!")
        number_of_items_input = int(input(f"{category}: Please input the number of items to {action}: current amount is {dict_items[category]} "))

    while action == "Remove" and dict_items[category] - number_of_items_input < 0:
        print(f"{category}:The amount of items can not be less then 0, please insert valid number to remove")
        number_of_items_input = int(input(f"{category}: Please input the number of items to {action}: current amount is {dict_items[category]} "))
        
    if action == 'Remove':
        dict_items[category] = dict_items[category] - number_of_items_input
    else:
        dict_items[category] = dict_items[category] + number_of_items_input
        
    print (f"The updated inventory is: {dict_items}")

    repeat_input = input("Do you want to modify another item? (yes/no): ")
    while is_yes_or_no(repeat_input) == False :
        print("Insert only yes/no ")
        repeat_input = input("Do you want to modify another item? (yes/no): ")
