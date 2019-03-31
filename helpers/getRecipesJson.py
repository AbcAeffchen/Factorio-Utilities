import re
import requests
import time
import json


FACTORIO_WIKI_LINK = 'https://wiki.factorio.com/'


def extractBasic(htmlCode):
    data = re.findall(r'<div class="infobox">[\s\S]*?<img[\s\S]*?src="/images/([^"]+)[\s\S]*?<td class="infobox-header-text">[\s\S]*?<span>([^<]+)', htmlCode)

    return {'name': data[0][1], 'basic': True, 'icon': data[0][0]}


def extractIngredients(htmlCode):
    data = re.findall(r'<div class="factorio-icon"[\s\S]*?href="/([^"]+)[\s\S]*?title="([^"]+)[\s\S]*?<img[\s\S]*?src="/images/([^"]+)[\s\S]*?class="factorio-icon-text">(\d+(\.\d+)?)', htmlCode)

    items = {}
    duration = 0
    for i in data[:-1]:
        if i[0] == 'Time':
            duration = i[3]
            continue

        items[i[0]] = float(i[3])

    return {'name': data[-1][1], 'basic': False, 'icon': data[-1][2], 'amount': float(data[-1][3]), 'time': float(duration), 'recipe': items}


def extractBarrelRecipes():
    barrelPage = requests.get(FACTORIO_WIKI_LINK + 'Barrel').text

    # get empty barrel recipe
    barrels = {}
    barrels['Empty_barrel'] = extractIngredients(re.findall(r'id="Empty_barrels"[\s\S]*?Recipe:([\s\S]*?)</tr>', barrelPage)[0])

    # find recipes for filled barrels
    for barrel in re.findall(r'<tr>[\s]*<td>[\s\S]*?</td>[\s]*<td>[\s\S]*?class="factorio-icon-text"[\s\S]*?href="/([^"]+)[\s\S]*?class="factorio-icon-text">(\d+)[\s\S]*?class="factorio-icon-text">(\d+(\.\d+)?)[\s\S]*?<td>[\s\S]*?<td>[\s\S]*?"([^/]+)\.png"[\s\S]*?/([^/]+)\.png', re.findall(r'<h2><span class="mw-headline" id="Fill_barrels">Fill barrels<[\s\S]*?<table class="wikitable">([\s\S]*?)</table>', barrelPage)[0]):
        barrels[barrel[5]] = {'name': barrel[4], 'basic': False, 'icon': barrel[5] + '.png', 'amount': 1, 'time': float(barrel[2]), 'recipe': {'Empty_barrel': 1, barrel[0]: float(barrel[1])}}

    return barrels


items = {'normal': extractBarrelRecipes(), 'expensive': extractBarrelRecipes()}

time.sleep(.1)

itemPage = requests.get(FACTORIO_WIKI_LINK + 'Items')
itemList = re.findall(r'<div class="factorio-icon"><a href="/([^"]+)', itemPage.text)

for itemCode in itemList:
    if itemCode in ['Crude_oil_barrel', 'Heavy_oil_barrel', 'Light_oil_barrel', 'Lubricant_barrel',
                    'Petroleum_gas_barrel', 'Sulfuric_acid_barrel', 'Water_barrel', 'Empty_barrel']:
        continue

    print(itemCode, '... ', end='')
    time.sleep(.1)
    itemWiki = requests.get(FACTORIO_WIKI_LINK + itemCode)
    ingredients = re.findall(r'Recipe[\s\S]*?<td class="infobox-vrow-value"[^>]+>([\s\S]*?)</td>', itemWiki.text)
    if len(ingredients) == 0:
        items['normal'][itemCode] = extractBasic(itemWiki.text)
        items['expensive'][itemCode] = extractBasic(itemWiki.text)
    else:
        items['normal'][itemCode] = extractIngredients(ingredients[0])
        items['expensive'][itemCode] = extractIngredients(ingredients[len(ingredients) > 1])

    print('check')


with open('factorio-recipes.json', 'w') as fp:
    json.dump(items, fp)
