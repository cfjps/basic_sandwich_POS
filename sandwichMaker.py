import pyinputplus as pyip

# Bread Prices
wheat = 4
white = 3
sourdough = 6

# Protein Prices
chicken = 9
turkey = 12
ham = 7
tofu = 15

# Cheese Prices
cheddar = 2
swiss = 4
mozzarella = 3

# EExtra prices
addons = 7

# Total amount
total = 0

bread = pyip.inputMenu(['wheat', 'white', 'sourdough'])
if bread == 'wheat':
    total = total + wheat
elif bread == 'white':
    total = total + white
elif bread == 'sourdough':
    total = total + sourdough
else:
    total = total + 0

protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
if protein == 'chicken':
    total = total + chicken
elif protein == 'turkey':
    total = total + turkey
elif protein == 'ham':
    total = total + ham
elif protein == 'tofu':
    total = total + tofu
else:
    total = total + 0

cheese = pyip.inputYesNo(prompt='Do you want cheese? (Yes or No): ')

if cheese == 'yes':
    typeOfCheese = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'])
    if typeOfCheese == 'cheddar':
        total = total + cheddar
    elif typeOfCheese == 'swiss':
        total = total + swiss
    elif typeOfCheese == 'mozzarella':
        total = total + mozzarella
    else:
        total = total + 0

extras = pyip.inputYesNo(prompt = 'Do you want mayo, mustard, lettuce or tomato: ')
if extras == 'yes':
    total = total + addons

sandwiches = pyip.inputInt(prompt='How many sandwiches to you want? ', min=1)
if sandwiches > 0:
    total = total * sandwiches

print('Thank you for your order...')
print('''Your order is as follows:

Your bread choice: %s
Your protein choice: %s
Extra cheese: %s
Extra add-ons ordered: % s
Number of sandwiches: %s

Total amount: R %s
''' % (bread, protein, cheese, extras, sandwiches, total))
