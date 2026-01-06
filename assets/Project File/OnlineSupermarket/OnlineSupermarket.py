import sys

store_menu = {
    'CD10': {
        'category_name': 'DRINKS',
        'items': {
            'N32': ("Neo's Green Tea", 3.00),
            'M13': ('Melo Chocolate Melt Drink', 2.85),
            'V76': ('Very-Fair Full Cream Milk', 3.50),
            'N14': ('Nirirgold UHT Milk', 4.15)
        }
    },
    'CB20': {
        'category_name': 'BEER',
        'items': {
            'L11': ('Lion (24 x 320ml)', 52.00),
            'P21': ('Panda (24 x 320ml)', 78.00),
            'A54': ('Axe (24 x 320ml)', 58.00),
            'H91': ('Henekan (24 x 320ml)', 68.00)
        }
    },
    'CF30': {
        'category_name': 'FROZEN',
        'items': {
            'E11': ('Edker Ristorante Pizza 335g', 6.95),
            'F43': ('Fazzler Frozen Soup 500g', 5.15),
            'CP31': ('CP Frozen Ready Meal 250g', 4.12),
            'D72': ('Duitoni Cheese 270g', 5.60)
        }
    },
    'CH40': {
        'category_name': 'HOUSEHOLD',
        'items': {
            'FP76': ('FP Facial Tissues', 9.50),
            'FP32': ('FP Premium Kitchen Towel', 5.85),
            'K22': ('Klines Toilet Tissue Rolls', 7.50),
            'D14': ('Danny Softener', 9.85)
        }
    },
    'CS50': {
        'category_name': 'SNACKS',
        'items': {
            'SS93': ('Singshort Seaweed', 3.10),
            'MC14': ('Mei Crab Cracker', 2.05),
            'R35': ('Reo Pokemon Cookie', 4.80),
            'HS11': ('Huat Seng Crackers', 3.55)
        }
    }
}

# Headers for the table
headers = ["Category", "Item", "Code", "Price"]

# List to hold all rows
rows = []

# Generate rows for each item in each category
for category_code, category_data in store_menu.items():
    category_name = category_data["category_name"]
    items = category_data["items"]

    first_item = True
    for item_code, (item_name, item_price) in items.items():
        row = [
            category_name if first_item else "",
            item_name,
            item_code,
            f"${item_price:.2f}"
        ]
        rows.append(row)
        first_item = False

    # Add an empty row after each category
    rows.append([""] * len(headers))

# Function to print the table with center alignment
def print_table(headers, rows):
    # Calculate column widths
    col_widths = [max(len(str(cell)) for cell in col) for col in zip(headers, *rows)]

    # Print the headers
    header_row = " | ".join(f"{header:^{col_widths[i]}}" for i, header in enumerate(headers))
    print(header_row)
    print("-" * len(header_row))

    # Print each row
    for row in rows:
        print(" | ".join(f"{str(cell):^{col_widths[i]}}" for i, cell in enumerate(row)))

# Print the table
print_table(headers, rows)

def display_items(category_index):
    category_codes = list(store_menu.keys())
    category_code = category_codes[category_index - 1]
    print()
    print(store_menu[category_code]['category_name'])
    print('-' * 40)
    items = store_menu[category_code]['items']
    item_codes = list(items.keys())
    for index, item_code in enumerate(item_codes, start=1):
        item_name = items[item_code][0]
        item_price = items[item_code][1]
        print(f"{index}. {item_code}: {item_name} [${item_price:.2f}]")

    while True:
        try:
            print()
            item_index = int(input("Please add desired item to cart (eg:1): "))
            if 1 <= item_index <= len(item_codes):
                item_code = item_codes[item_index - 1]
                break
            else:
                print()
                print('Invalid entry, please try again.')
        except ValueError:
            print()
            print('Invalid entry, please enter a valid number.')

    while True:
        try:
            print()
            quantity = int(input('Please add the desired quantity to cart (eg: 1): '))
            if quantity <= 0:
                print()
                print("Invalid quantity, please enter a valid positive number.")
            else:
                break
        except ValueError:
            print()
            print('Invalid quantity, please enter a valid number.')

    item_name = items[item_code][0]
    item_price = items[item_code][1]
    add_item(item_code, item_name, quantity, item_price)
    print('\n')
    display_cart()

def display_menu():
    print()
    print("CATEGORIES")
    print('-' * 40)
    category_codes = list(store_menu.keys())
    for index, category_code in enumerate(category_codes, start=1):
        print(f'{index}. {store_menu[category_code]["category_name"]}')

    while True:
        try:
            print("")
            select_category = int(input("Please enter desired category number (eg: 1): "))
            if 1 <= select_category <= len(category_codes):
                display_items(select_category)
                break
            else:
                print()
                print('Invalid entry, please try again.')
        except ValueError:
            print()
            print('Invalid entry, please enter a valid number.')


shopping_cart = {}

def add_item(item_code, item_name, quantity, item_price):
    """
    Adds a certain quantity of items to the shopping cart
    Assumption: All variables are valid
    :param item_code: code of the item to add
    :param item_name: name of the item to add
    :param quantity: quantity of the item to add
    :param item_price: price of the item to add
    :return: None, perform operation in place (shopping_cart)
    """
    if item_code in shopping_cart:
        shopping_cart[item_code][1] += quantity
    else:
        shopping_cart[item_code] = [item_name, quantity, item_price]

def remove_item(item_code, remove_quantity):
    if item_code in shopping_cart:
        shopping_cart[item_code][1] -= remove_quantity
        if shopping_cart[item_code][1] <= 0:
            del shopping_cart[item_code]
    else:
        print("Item is not in shopping cart")

def display_cart():
    print(f'\n{"SHOPPING CART":^75}')
    print('-' * 80)
    print(f'{"ITEM CODE":<10} | {"ITEM NAME":<40} | {"QUANTITY":<10} | {"TOTAL PRICE":<10}')
    for item_code, info_list in shopping_cart.items():
        item_name = info_list[0]
        item_quantity = info_list[1]
        item_price = info_list[2]
        print(f"{item_code:<10}   {item_name:<40}   {item_quantity:<10}   ${item_quantity * item_price:<10.2f}")
    print("\n")
    while True:
        choice = input('Press "E" to EDIT items in cart \nPress "C" to CHECKOUT \nPress "M" to return to shop MENU\nPress "S" to SEARCH for an item\n(E / C / M / S): ').upper()
        if choice not in ["E", "M", "C", "S"]:
            print()
            print("Invalid Entry")
        else:
            break

    if choice == "E":
        while True:
            print('\n')
            choose_item = input("Which item would you like to edit? (eg: N32): ").upper()
            if choose_item in shopping_cart:
                break
            else:
                print()
                print("Invalid entry, please try again")
        item_name = shopping_cart[choose_item][0]
        item_price = shopping_cart[choose_item][2]
        while True:
            print('\n')
            edit_choice = input("Would you like to ADD or REMOVE items? (A / R): ").upper()
            if edit_choice in ["A", "R"]:
                break
            else:
                print()
                print("Invalid Entry")
        if edit_choice == "A":
            while True:
                try:
                    print('\n')
                    add_quantity = int(input("Please enter the amount you would like to add: "))
                    if add_quantity >= 0:
                        add_item(choose_item, item_name, add_quantity, item_price)
                        display_cart()
                        break
                    else:
                        print()
                        print('Invalid Entry')
                except ValueError:
                    print()
                    print("Invalid Entry")

        elif edit_choice == "R":
            while True:
                try:
                    print('\n')
                    remove_quantity = int(input("Please enter the amount you would like to remove: "))
                    if remove_quantity > 0 and remove_quantity <= shopping_cart[choose_item][1]:
                        remove_item(choose_item, remove_quantity)
                        display_cart()
                        break
                    elif remove_quantity > shopping_cart[choose_item][1]:
                        print("You have removed more than you have")
                    else:
                        print()
                        print("Invalid Entry")
                except ValueError:
                    print()
                    print("Invalid Entry")
    elif choice == "C":
        checkout()
    elif choice == "M":
        print('\n')
        print_table(headers, rows)
        display_menu()
    elif choice == "S":
        search_item()
        display_cart()

def checkout():
    print('\n')
    print("DISCOUNT PRIVILEGES")
    print('-' * 40)
    while True:
        try:
            discount_code = int(input(f"1. Seniors (10%) \n2. Members (8%) \n3. NS Men (5%) \n4. No \n\nAre you eligible for any of these discount privileges? (eg: 1): "))
            if 1 <= discount_code <= 4:
                break
            else:
                print()
                print('Invalid Entry, please try again.')
        except ValueError:
            print()
            print('Invalid Entry, please enter a number.')
    if discount_code == 1:
        calculate_cost(0.1)
    elif discount_code == 2:
        calculate_cost(0.08)
    elif discount_code == 3:
        calculate_cost(0.05)
    else:
        calculate_cost(0)

def calculate_cost(discount_rate):
    cost = 0
    for item_code, info_list in shopping_cart.items():
        item_quantity = info_list[1]
        item_price = info_list[2]
        cost += item_quantity * item_price
    gst = cost * 0.09
    discount_amt = cost * discount_rate
    final_cost = cost + gst - discount_amt

    print('\n')
    receipt()
    print()
    print(f"Total before GST: ${cost:.2f}")
    print(f"Discount: ${discount_amt:.2f}")
    print(f"GST: ${gst:.2f}")
    print(f"Final Price: ${final_cost:.2f}")

    # Prompt user to continue shopping or end the program
    while True:
        print()
        continue_shopping = input("Would you like to continue shopping? (Y/N): ").upper()
        if continue_shopping == "Y":
            shopping_cart.clear()  # Clear the existing cart for a new session
            print("Starting a new shopping session.")
            print_table(headers, rows)
            display_menu()  # Display the main menu to start shopping again
            break
        elif continue_shopping == "N":
            print("Thank you for shopping with us! Goodbye!")
            sys.exit()
            #break
        else:
            print()
            print("Invalid input. Please enter 'Y' for yes or 'N' for no.")
def receipt():
    print(f'{"RECEIPT":^75}')
    print('-' * 80)
    print(f'{"ITEM CODE":<10} | {"ITEM NAME":<40} | {"QUANTITY":<10} | {"TOTAL PRICE":<10}')
    for item_code, info_list in shopping_cart.items():
        item_name = info_list[0]
        item_quantity = info_list[1]
        item_price = info_list[2]
        print(f"{item_code:<10}   {item_name:<40}   {item_quantity:<10}   ${item_quantity * item_price:<10.2f}")


def search_item():
    while True:  # Encapsulate the search code in a loop to keep prompting until a valid item is found or until the user wishes to exit
        print()
        search_code = input("Enter item code to search (eg: N32) or type 'exit' to return: ").upper()
        if search_code == 'EXIT':
            break
        item_found = False

        for category_data in store_menu.values():
            if search_code in category_data['items']:
                item_found = True
                item_name = category_data['items'][search_code][0]
                item_price = category_data['items'][search_code][1]
                print(f"\nFound: {item_name} - ${item_price:.2f}\n")

                while True:
                    add_to_cart = input("Would you like to add this item to the cart? (Y/N): ").upper()
                    if add_to_cart == "Y":
                        while True:
                            try:
                                quantity = int(input("Enter the quantity to add to the cart: "))
                                if quantity > 0:
                                    add_item(search_code, item_name, quantity, item_price)
                                    print(f"Added {quantity} of {item_name} to the cart.")
                                    return  # Exit after adding item
                                else:
                                    print()
                                    print("Please enter a positive quantity.")
                            except ValueError:
                                print()
                                print("Invalid quantity. Please enter a number.")
                        break  # Break the inner loop after processing the valid input
                    elif add_to_cart == "N":
                        return  # Exit without adding if the user chooses not to add the item
                    else:
                        print()
                        print("Invalid entry, please enter 'Y' for yes or 'N' for no.")

        if not item_found:
            print("Item not found. Please try again.")


# Start the shopping process
print("\nWelcome to our Store!")
while True:
    print("\n")
    choice = input('Press "S" to SEARCH for an item \nPress "M" to display the MENU\n(S / M): ').upper()
    if choice == "S":
        search_item()
    elif choice == "M":
        print('\n')
        print_table(headers, rows)
        display_menu()
    else:
        print()
        print("Invalid Entry")