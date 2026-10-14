import random

def purchase_item(itemPrice, startingMoney, quantityToPurchase=1):
    # figure out how many we can afford
    num = startingMoney // itemPrice
    if num > quantityToPurchase:
        num = quantityToPurchase
    money = startingMoney - num * itemPrice
    return num, money

def new_random_monster():
    r = random.randint(1, 3)
    if r == 1:
        name = "A goblin"
        description = """This is a lone goblin. When it notices you,
        it rushes at you quickly with a sharp dagger drawn."""
        health = random.randint(8, 20)
        power = random.randint(4, 9)
        money = random.randint(5, 40)
    elif r == 2:
        name = "Vulture"
        description = """You discover a vulture eating the remains of
two orcs that appear to have killed each other. They were carrying a
chest that contains a small treasure horde. You will need to scare off
the vulture before you can take the treasure."""
        health = random.randint(1, 5)
        power = random.randint(1, 4)
        money = random.randint(500, 1500)
    else:
        name = "Troll"
        description = "A big troll blocks the bridge ahead and swings a club at you."
        health = random.randint(40, 80)
        power = random.randint(12, 22)
        money = random.randint(50, 250)
    monster = {}
    monster['name'] = name
    monster['description'] = description
    monster['health'] = health
    monster['power'] = power
    monster['money'] = money
    return monster

# test the functions
print(purchase_item(5, 23, 3))
print(purchase_item(5, 12, 5))
print(purchase_item(5, 12))
m = new_random_monster()
print(m['name'])
print(m['description'])
print(m['health'])
print(m['power'])
print(m['money'])
