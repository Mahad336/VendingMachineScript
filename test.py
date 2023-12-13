# Vending Machine Program

# Function to display items
def display_items(items):
    print("\nAvailable items:")
    for code, item in items.items():
        if item['stock'] > 0:
            print(f"{code}: {item['name']} - ${item['price']}")

# Function to categorize items
def categorize_items(items):
    categories = {}
    for code, item in items.items():
        category = item['category']
        if category not in categories:
            categories[category] = []
        categories[category].append((code, item))
    return categories

# Function to suggest items based on purchase
def suggest_item(purchase, items):
    suggestions = {
        'Hot Drinks': ['Biscuits', 'Chocolate Bar'],
        'Cold Drinks': ['Chips', 'Gum'],
        'Snacks': ['Juice', 'Water'],
        'Candies': ['Coffee', 'Tea'],
        'Food': ['Soda', 'Hot Chocolate']
    }
    category = items[purchase]['category']
    suggestion_category = suggestions.get(category)
    if suggestion_category:
        print("You might also like:")
        for suggested_item in suggestion_category:
            for item in items.values():
                if item['name'] == suggested_item and item['stock'] > 0:
                    print(f"Would you like to try a {item['name']}?")
                    break

# Function to process purchase with quantity
def purchase_item(code, items, money, quantity):
    item = items[code]
    total_cost = item['price'] * quantity
    if money >= total_cost and item['stock'] >= quantity:
        item['stock'] -= quantity
        return total_cost, item['name']
    elif item['stock'] < quantity:
        return 0, "not enough stock"
    else:
        return 0, None


# Function to manage stock
def check_stock(items, code):
    if items[code]['stock'] > 0:
        return True
    else:
        print("Sorry, this item is out of stock.")
        return False

# Initial stock of items
items = {
    'A1': {'name': 'Coffee', 'price': 1.5, 'stock': 10, 'category': 'Hot Drinks'},
    'A2': {'name': 'Tea', 'price': 1.0, 'stock': 10, 'category': 'Hot Drinks'},
    'A3': {'name': 'Hot Chocolate', 'price': 1.7, 'stock': 8, 'category': 'Hot Drinks'},
    'B1': {'name': 'Soda', 'price': 1.2, 'stock': 15, 'category': 'Cold Drinks'},
    'B2': {'name': 'Water', 'price': 1.0, 'stock': 20, 'category': 'Cold Drinks'},
    'B3': {'name': 'Juice', 'price': 1.5, 'stock': 10, 'category': 'Cold Drinks'},
    'C1': {'name': 'Chips', 'price': 0.8, 'stock': 10, 'category': 'Snacks'},
    'C2': {'name': 'Biscuits', 'price': 0.5, 'stock': 15, 'category': 'Snacks'},
    'C3': {'name': 'Chocolate Bar', 'price': 1.0, 'stock': 12, 'category': 'Snacks'},
    'D1': {'name': 'Gum', 'price': 0.5, 'stock': 20, 'category': 'Candies'},
    'D2': {'name': 'Mints', 'price': 0.6, 'stock': 15, 'category': 'Candies'},
    'D3': {'name': 'Lollipop', 'price': 0.4, 'stock': 25, 'category': 'Candies'},
    'E1': {'name': 'Sandwich', 'price': 2.5, 'stock': 5, 'category': 'Food'},
    'E2': {'name': 'Salad', 'price': 3.0, 'stock': 5, 'category': 'Food'},
    'E3': {'name': 'Fruit Cup', 'price': 2.0, 'stock': 6, 'category': 'Food'}
}

# Start of program
print("Welcome to the Vending Machine!")
selected_items = []
total_cost = 0

while True:
    display_items(items)
    user_code = input("Please enter the code of the item you want to buy: ").upper()

    if user_code in items and check_stock(items, user_code):
        quantity = int(input(f"How many of {items[user_code]['name']} would you like? "))
        if items[user_code]['stock'] >= quantity:
            cost, item_name_or_error = purchase_item(user_code, items, items[user_code]['price'] * quantity, quantity)
            if item_name_or_error == "not enough stock":
                print("Sorry, not enough stock for the requested quantity.")
            elif item_name_or_error:
                selected_items.append((item_name_or_error, quantity, cost))
                total_cost += cost
                print(f"Added {quantity} x {item_name_or_error} to your cart.")
                suggest_item(user_code, items)  # Suggestion based on current selection
            else:
                print("Insufficient funds. Please try again.")
        else:
            print("Not enough stock available for the requested quantity.")
    else:
        print("Invalid code. Please try again.")

    additional_purchase = input("Would you like to add another item? (yes/no): ").lower()
    if additional_purchase != 'yes':
        break

# Process final transaction
if selected_items:
    money_inserted = float(input(f"Your total is ${total_cost:.2f}. Please insert money: "))
    if money_inserted >= total_cost:
        print("Items dispensed:")
        for item, quantity, cost in selected_items:
            print(f"- {quantity} x {item}")
        print(f"Change returned: ${money_inserted - total_cost:.2f}")
    else:
        print("Insufficient funds. Transaction cancelled.")
else:
    print("No items selected.")

print("Thank you for using the Vending Machine!")
