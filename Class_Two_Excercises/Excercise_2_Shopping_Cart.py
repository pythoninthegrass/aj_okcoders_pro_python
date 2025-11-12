# Creates a simple shopping cart, with the ability to add/remove items, show the total cost of all items and display all items and the total cost at-a-glance

# Create an empty shopping cart first, with a list
cart = []

# Add an item (uses a dictionary)
def add_item(name, price, quantity):
    item = {
        'Name': name,
        'Price': price,
        'Quantity': quantity
    }

    cart.append(item)

# Remove an item (or items) matching the item name that is passed in. Show the user the item that was removed, and its quantity if more than one was found.
def remove_item(name):
    i = 0
    count = 0

    while i < len(cart):
        # Look for the item's name in each dictionary in the list; can be a partial match
        if name in cart[i]['Name']:
            # remove the item since it was found via the name
            del cart[i]
            count += 1
        else:
            # If nothing was deleted, increment i to the next value
            i += 1 

    # A more condensed way of handling and printing info for all three cases, using Python's "<something> if condition else <something_else>" condition - a ternary-equivalent of JS
    descriptor = "item" if count == 1 else "items"

    print(
        f'\nNo matching items for "{name}" were found.'
        if count == 0
        else f'\nRemoved {count} {descriptor} matching "{name}" from the cart.'
    )

def calculate_total():
    total = 0

    # Show the total price of all items in the cart
    for item in cart:
        total += item['Price']

    return total

def display_cart():
    print()
    if len(cart) == 0:
        print('Your shopping cart is empty.')
        return
    
    descriptor = "item" if len(cart) == 1 else "items"
    print(f'Your cart has {len(cart)} {descriptor} shown below:\n')
    for item in cart:
        print(f"Item: {item['Name']} | Price: ${item['Price']:.2f} | Quantity: {item['Quantity']}")

    print(f'Total is: ${calculate_total():.2f}')

# Add some items to the cart
add_item("Amy's Pesto Tortellini", 4.55, 1)
add_item("Swiffer Dusters", 10, 2)
add_item("Bounty Papertowels", 31.99, 1)
add_item("Noosa Cheesecake Bites", 11.50, 4)

# Show the cart items
display_cart()

# Remove an item - in this case, we're removing the Amy's Tortellini dinner from the cart
remove_item("Amy's")

display_cart()
