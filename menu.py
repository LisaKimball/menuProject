## Setup

# Variable setup
three = 3
two = 2
one = 1
half = 0.50

# Function definition
def order():
    cost = 0
    i = int(input("How many different menu items are you wanting to order? "))
    for x in range(i):
        item = input("What menu item do you want to order? Please enter the menu item spelled correctly: ")
        count = int(input("How many do you want? "))
        if item == "Pasta":
            item = three
        elif item == "Pancake":
            item = two
        elif item == "Sausage" or item == "Hashbrown" or item == "Orange" or item == "Apple slices" or item == "Carrot sticks" or item == "Nacho cheese" or item == "Tortilla chips" or item == "Salsa" or item == "Salad" or item == "Potato" or item == "Rootbeer":
            item = one
        else:
            item = half

        cost += item * count
    return cost

## Menu startup
meal = input("Are you ordering 'breakfast', 'lunch', 'dinner', or just a 'snack'? ")

# Breakfast menu
if meal == "breakfast":
    print()
    print("Here is our breakfast menu:")
    print()
    print("$2.00 - Pancake - A soft, warm pancake the perfect diameter")
    print("$0.50 - Maple syrup - Delicious, cold maple syrup")
    print("$1.00 - Sausage - A warm, freshly fried smoked sausage")
    print("$1.00 - Hashbrown - A crispy warm hashbrown, with a packet of maple syrup for the syrup lovers out there")
    print("$0.50 - Yogurt - Cold, sweet yogurt locally made")
    print("$0.50 - Granola - Crunchy, nutty, sweet granola that's sure to make you think of your grandma")
    print("$1.00 - Orange - Cold, sweet and perfectly ripe")
    print("$0.50 - Milk - Cold, sweet, creamy whole milk that's sure to delight")
    print()
    total = order()

# Lunch menu
elif meal == "lunch":
    print()
    print("Here is our lunch menu:")
    print()
    print("$1.00 - Apple slices - Crispy, ripe apple slices")
    print("$1.00 - Carrot sticks - Cold, sweet carrots")
    print("$1.00 - Nacho cheese - Warm, creamy nacho cheese")
    print("$1.00 - Tortilla chips - Crunchy, salty chips you won't want to stop eating")
    print("$1.00 - Salsa - Cold, fresh salsa that's just the right amount salty")
    print()
    total = order()

# Dinner menu
elif meal == "dinner":
    print()
    print("Here is our dinner menu:")
    print()
    print("$3.00 - Pasta - A delicious pasta dish that's sure to make you think of your gramdma's lasagana")
    print("$1.00 - Salad - Cold, fresh greens locally grown")
    print("$0.50 - Ranch - Cold, creamy ranch")
    print("$1.00 - Potato - A warm baked potato garanteed to be soft and creamy")
    print("$1.00 - Chili - Warm, spicy chili")
    print("$0.50 - Sour Cream - Cold, creamy sour cream")
    print("$1.00 - Rootbeer - The best cold rootbeer you've ever tasted")
    print()
    total = order()

# Snack menu
else:
    print()
    print("Here is our snack menu:")
    print()
    print("$1.00 - Cookie - A sweet, warm chocolate chip cookie better than your grandma's")
    print("$1.00 - Chips - A small bag of chips")
    print("0.50 - Jellybeans - A small box of jellybeans of good and bad flavors")
    print()
    total = order()

## Conclusion
print()
print("Your total is $" + str(total))
number = int(input("Please enter your credit card number: "))
print()
print("Thank you for doing buisness with us.")
