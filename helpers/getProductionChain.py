import json

with open('data/factorio-recipes.json') as factorioRecipesFile:
    factorioRecipes = json.load(factorioRecipesFile)['normal']

basicIngredients = ['Iron_plate', 'Copper_plate', 'Steel_plate', 'Lubricant', 'Uranium-235', 'Uranium-238']


def calculateFactories(item, ratio):

    itemsPerSecond = 1 if factorioRecipes[item]['basic'] else (factorioRecipes[item]['amount'] / factorioRecipes[item]['time'])

    factories = {item: ratio / itemsPerSecond}

    if factorioRecipes[item]['basic'] or item in basicIngredients:
        return factories

    for i, n in factorioRecipes[item]['recipe'].items():
        for j, m in calculateFactories(i, ratio * n).items():
            if j in factories:
                factories[j] += m
            else:
                factories[j] = m

    return factories


def printFactories(factories):
    # print factories
    for i, n in factories.items():
        if factorioRecipes[i]['basic'] or i in basicIngredients:
            continue

        print(factorioRecipes[i]['name'] + ': ' + str(n) + ' Factories')

    # print Ingredients
    for i, n in factories.items():
        if not factorioRecipes[i]['basic'] and i not in basicIngredients:
            continue

        print(factorioRecipes[i]['name'] + ': ' + str(n) + '/s')


item = input('Build: ')
if item not in factorioRecipes and item != 'full':
    print('Item not found...')
    exit()

ratio = float(input('Items/s: '))

if item == 'full':
    for i, d in factorioRecipes.items():
        if i in basicIngredients or d['basic']:
            continue

        printFactories(calculateFactories(i, ratio))
        print()
else:
    printFactories(calculateFactories(item, ratio))
