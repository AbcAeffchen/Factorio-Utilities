import json

with open('factorio-recipes.json') as factorioRecipesFile:
    factorioRecipes = json.load(factorioRecipesFile)['normal']

basicIngredients = ['Iron_plate', 'Copper_plate', 'Steel_plate']


def calculateFactories(item, ratio):

    itemsPerSecond = factorioRecipes[item]['amount'] / factorioRecipes[item]['time']

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
if item not in factorioRecipes:
    print('Item not found...')
    exit()

ratio = float(input('Item/s: '))


printFactories(calculateFactories(item, ratio))
