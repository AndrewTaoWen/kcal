foods = {"bread" : 32, 
"bagel" : 245, 
"egg" : 78, 
"bacon" : 43, 
"yogurt" : 100, 
"cereal" : 379, 
"oats" : 307, 
"pizza" : 285, 
"pasta" : 288, 
"sandwich" : 250, 
"burger" : 354, 
"beef" : 71, 
"chicken" : 68, 
"pork" : 69, 
"rice" : 206, 
"potato" : 163}

def calculataIntake(food, amount):
    food.lower().strip()
    total = 0

    if food == 'other':
        total += amount
    else:
        total += (amount * foods[food])

    return total