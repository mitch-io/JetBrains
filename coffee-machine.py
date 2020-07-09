# The coffee machine has:
water = 400
milk = 540
beans = 120
cups = 9
money = 550
coffee = 0

def buy(coffee):
    global water, milk, beans, money, cups
    if coffee == str(1) and water >= 250 and beans >= 16 and cups >= 1:
        water = water - 250
        beans = beans - 16
        money = money + 4
        cups = cups - 1
        print('I have enough resources, making you a coffee!\n')
    elif coffee == str(2) and water >= 350 and milk >=75 and beans >= 20 and cups >= 1:
        water = water - 350
        milk = milk - 75
        beans = beans - 20
        money = money + 7
        cups = cups - 1
        print('I have enough resources, making you a coffee!\n')
    elif coffee == str(3) and water >= 200 and milk >=100 and beans >= 12 and cups >= 1:
        water = water - 200
        milk = milk - 100
        beans = beans - 12
        money = money + 6
        cups = cups - 1
        print('I have enough resources, making you a coffee!\n')
    else:
        print('Not enough stuff!\n')

def fill():
    global water, milk, beans, money, cups
    print('How many ml of water do you want to add:')
    water = water + int(input())
    print('How many ml of milk do you want to add:')
    milk = milk + int(input())
    print('How many grams of coffee beans do you want to add:')
    beans = beans + int(input())
    print('How many disposable cups of coffee do you want to add:')
    cups = cups + int(input())

print('(buy, fill, take, remaining, exit): ')

selection = input()

while selection != 'exit':

    if selection == 'buy':
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: \n')
        coffee = input()
        buy(coffee)
        print('(buy, fill, take, remaining, exit): \n')
        selection = input()

    elif selection == 'fill':
        fill()
        print('(buy, fill, take, remaining, exit): \n')
        selection = input()
    elif selection == 'take':
        print('I gave you $' + str(money))
        money = 0
        print('(buy, fill, take, remaining, exit): \n')
        selection = input()
    elif selection == 'remaining':
        print('\n')
        print('The coffee machine has:')
        print(str(water) + ' of water')
        print(str(milk) + ' of milk')
        print(str(beans) + ' of beans')
        print(str(cups) + ' of cups')
        print(str(money) + ' of money\n')
        print('(buy, fill, take, remaining, exit): \n')
        selection = input()