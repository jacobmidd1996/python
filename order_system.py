def place_order(menu):
    
    
    order = []
    menu_items = get_menu_items_dict(menu)

    print("Welcome to the Generic Take Out Restaurant.")
    print_menu_heading()

    
    menu_number = 1
    for food_category, options in menu.items():
        for meal, price in options.items():
            print_menu_line(menu_number, food_category, meal, price)
            menu_number += 1

    place_order = True
    while place_order:
        try:
            
            menu_selection = input("Type menu number: ")

            
            order = update_order(order, menu_selection, menu_items)

            
            keep_ordering = input("Would you like to keep ordering? (Type 'N' to quit): ")
            if keep_ordering.lower() == 'n':
                print("Thank you for your order.")
                
                prices_list = [item["Price"] * item["Quantity"] for item in order]
                order_total = round(sum(prices_list), 2)
                place_order = False
        except Exception as e:
            print(f"Error: {e}. Please try again.")

    
    return order, order_total


def update_order(order, menu_selection, menu_items):
    
    
    if not menu_selection.isdigit():
        print("Invalid input. Please enter a valid menu number.")
        return order

    menu_selection = int(menu_selection)

    
    if menu_selection not in menu_items:
        print("Invalid menu number. Please try again.")
        return order

    
    item_name = menu_items[menu_selection]["Item name"]
    item_price = menu_items[menu_selection]["Price"]

    
    quantity = input(f"How many of {item_name} would you like? ")
    if not quantity.isdigit():
        print("Invalid quantity. Defaulting to 1.")
        quantity = 1
    else:
        quantity = int(quantity)

    
    order.append({"Item name": item_name, "Price": item_price, "Quantity": quantity})
    print(f"Added {quantity} x {item_name} to your order.")

    return order


def print_itemized_receipt(receipt):
   
    for item in receipt:
        item_name = item["Item name"]
        price = item["Price"]
        quantity = item["Quantity"]
        print_receipt_line(item_name, price, quantity)



if __name__ == "__main__":
    
    
    meals = get_menu_dictionary()

    
    receipt, total_price = place_order(meals)

    
    print("\nThis is what we are preparing for you:\n")

    
    print_receipt_heading()

    
    print_itemized_receipt(receipt)

    
    print_receipt_footer(total_price)


##################################################
#  STARTER CODE
#  Do not modify any of the code below this line:
##################################################


def print_receipt_line(item_name, price, quantity):
    """
    Prints a line of the receipt.

    Parameters:
    item_name (str): The name of the meal item.
    price (float): The price of the meal item.
    quantity (int): The quantity of the meal item.
    """
    # Calculate the number of spaces for formatted printing
    num_item_spaces = 32 - len(item_name)
    num_price_spaces = 6 - len(str(price))

    # Create space strings
    item_spaces = " " * num_item_spaces
    price_spaces = " " * num_price_spaces

    # Print the item name, price, and quantity
    print(f"{item_name}{item_spaces}| ${price}{price_spaces}| {quantity}")


def print_receipt_heading():
    """
    Prints the receipt heading.
    """
    print("----------------------------------------------------")
    print("Item name                       | Price  | Quantity")
    print("--------------------------------|--------|----------")


def print_receipt_footer(total_price):
    """
    Prints the receipt footer with the total price of the order.

    Parameters:
    total_price (float): The total price of the order.
    """
    print("----------------------------------------------------")
    print(f"Total price: ${total_price:.2f}")
    print("----------------------------------------------------")


def print_menu_heading():
    """
    Prints the menu heading.
    """
    print("--------------------------------------------------")
    print("Item # | Item name                        | Price")
    print("-------|----------------------------------|-------")


def print_menu_line(index, food_category, meal, price):
    """
    Prints a line of the menu.

    Parameters:
    index (int): The menu item number.
    food_category (str): The category of the food item.
    meal (str): The name of the meal item.
    price (float): The price of the meal item.
    """
    # Print the menu item number, food category, meal, and price
    num_item_spaces = 32 - len(food_category + meal) - 3
    item_spaces = " " * num_item_spaces
    if index < 10:
        i_spaces = " " * 6
    else:
        i_spaces = " " * 5
    print(f"{index}{i_spaces}| {food_category} - {meal}{item_spaces} | ${price}")


def get_menu_items_dict(menu):
    """
    Creates a dictionary of menu items and their prices mapped to their menu 
    number.

    Parameters:
    menu (dictionary): A nested dictionary containing the menu items and their
                        prices.

    Returns:
    menu_items (dictionary): A dictionary containing the menu items and their
                            prices.
    """
    # Create an empty dictionary to store the menu items
    menu_items = {}

    # Create a variable for the menu item number
    i = 1

    # Loop through the menu dictionary
    for food_category, options in menu.items():
        # Loop through the options for each food category
        for meal, price in options.items():
            # Store the menu item number, item name and price in the menu_items
            menu_items[i] = {
                "Item name": food_category + " - " + meal,
                "Price": price
            }
            i += 1

    return menu_items


def get_menu_dictionary():
    """
    Returns a dictionary of menu items and their prices.

    Returns:
    meals (dictionary): A nested dictionary containing the menu items and their
                        prices in the following format:
                        {
                            "Food category": {
                                "Meal": price
                            }
                        }
    """
    # Create a meal menu dictionary
    #"""
    meals = {
        "Burrito": {
            "Chicken": 4.49,
            "Beef": 5.49,
            "Vegetarian": 3.99
        },
        "Rice Bowl": {
            "Teriyaki Chicken": 9.99,
            "Sweet and Sour Pork": 8.99
        },
        "Sushi": {
            "California Roll": 7.49,
            "Spicy Tuna Roll": 8.49
        },
        "Noodles": {
            "Pad Thai": 6.99,
            "Lo Mein": 7.99,
            "Mee Goreng": 8.99
        },
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    }
    """
    # This menu is just for testing purposes
    meals = {
        "Cake": {
            "Kuih Lapis": 3.49,
            "Strawberry Cheesecake": 6.49,
            "Chocolate Crepe Cake": 6.99
        },
        "Pie": {
            "Apple": 4.99,
            "Lemon Meringue": 5.49
        },
        "Ice-cream": {
            "2-Scoop Vanilla Cone": 3.49,
            "Banana Split": 8.49,
            "Chocolate Sundae": 6.99
        }
    }
    """
    return meals


# Run the program
if __name__ == "__main__":
    # Get the menu dictionary
    meals = get_menu_dictionary()

    receipt, total_price = place_order(meals)

    # Print out the customer's order
    print("This is what we are preparing for you.\n")

    # Print the receipt heading
    print_receipt_heading()

    # Print the customer's itemized receipt
    print_itemized_receipt(receipt)

    # Print the receipt footer with the total price
    print_receipt_footer(total_price)

