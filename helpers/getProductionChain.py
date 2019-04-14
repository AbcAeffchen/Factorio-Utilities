import json

SECOUND = 1
MINUTE = 60
TWO_MINUTES = 120
FIFE_MINUTES = 300

with open('data/factorio-recipes.json') as factorioRecipesFile:
    factorioRecipes = json.load(factorioRecipesFile)['normal']

basicIngredients = ['Iron_plate', 'Copper_plate', 'Steel_plate', 'Lubricant', 'Uranium-235', 'Uranium-238']

defaultAmountPerSecond = {'Steel_chest': 1 / 10,
                          'Storage_tank': 1 / 10,
                          'Transport_belt': 1,
                          'Fast_transport_belt': 1,
                          'Express_transport_belt': 1 / 5,
                          'Underground_belt': 1,
                          'Fast_underground_belt': 1,
                          'Express_underground_belt': 1 / 5,
                          'Splitter': 1 / 10,
                          'Fast_splitter': 1 / 10,
                          'Express_splitter': 1 / MINUTE,
                          'Inserter': 1 / 2,
                          'Long_handed_inserter': 1 / 5,
                          'Fast_inserter': 1 / 5,
                          'Filter_inserter': 1 / 5,
                          'Stack_inserter': 1 / 5,
                          'Stack_filter_inserter': 1 / 30,
                          'Small_electric_pole': 1 / 5,
                          'Medium_electric_pole': 1 / 5,
                          'Big_electric_pole': 1 / 10,
                          'Substation': 1,
                          'Pipe': 1,
                          'Pipe_to_ground': 1,
                          'Pump': 1 / MINUTE,
                          'Rail': 1,
                          'Train_stop': 1 / MINUTE,
                          'Rail_signal': 1 / MINUTE,
                          'Rail_chain_signal': 1 / MINUTE,
                          'Locomotive': 1 / FIFE_MINUTES,
                          'Cargo_wagon': 1 / FIFE_MINUTES,
                          'Fluid_wagon': 1 / FIFE_MINUTES,
                          'Artillery_wagon': 1 / FIFE_MINUTES,
                          'Car': 1. / FIFE_MINUTES,
                          'Tank': 1. / FIFE_MINUTES,
                          'Logistic_robot': 1 / 10,
                          'Construction_robot': 1 / 10,
                          'Active_provider_chest': 1 / 10,
                          'Passive_provider_chest': 1 / 10,
                          'Storage_chest': 1 / 10,
                          'Buffer_chest': 1 / 10,
                          'Requester_chest': 1 / 10,
                          'Roboport': 1 / TWO_MINUTES,
                          'Lamp': 1 / 30,
                          'Red_wire': 1,
                          'Green_wire': 1,
                          'Arithmetic_combinator': 1,
                          'Decider_combinator': 1 / MINUTE,
                          'Constant_combinator': 1 / MINUTE,
                          'Programmable_speaker': 1 / MINUTE,
                          'Concrete': 5,
                          'Hazard_concrete': 5,
                          'Refined_concrete': 5,
                          'Refined_hazard_concrete': 5,
                          'Landfill': 2,
                          'Cliff_explosives': 1 / 10,
                          'Repair_pack': 1 / 5,
                          'Boiler': 1,
                          'Steam_engine': 1 / 30,
                          'Steam_turbine': 1 / 30,
                          'Solar_panel': 1 / 10,
                          'Accumulator': 1 / 10,
                          'Nuclear_reactor': 1 / FIFE_MINUTES,
                          'Heat_exchanger': 1 / MINUTE,
                          'Heat_pipe': 1 / 30,
                          'Electric_mining_drill': 1 / 20,
                          'Pumpjack': 1 / TWO_MINUTES,
                          'Steel_furnace': 1 / 30,
                          'Electric_furnace': 1 / 30,
                          'Assembling_machine_1': 1 / 30,
                          'Assembling_machine_2': 1 / 30,
                          'Assembling_machine_3': 1 / 30,
                          'Oil_refinery': 1 / FIFE_MINUTES,
                          'Chemical_plant': 1 / FIFE_MINUTES,
                          'Speed_module': 1 / 10,
                          'Speed_module_2': 1 / 30,
                          'Speed_module_3': 1 / MINUTE,
                          'Efficiency_module': 1 / 10,
                          'Efficiency_module_2': 1 / 30,
                          'Efficiency_module_3': 1 / MINUTE,
                          'Productivity_module': 1 / 10,
                          'Productivity_module_2': 1 / 30,
                          'Productivity_module_3': 1 / MINUTE,
                          'Beacon': 1 / MINUTE,
                          'Sulfuric_acid': 50,
                          'Battery': 1,
                          'Explosives': 1,
                          'Electronic_circuit': 1,
                          'Advanced_circuit': 1,
                          'Processing_unit': 1,
                          'Engine_unit': 1 / 5,
                          'Electric_engine_unit': 1 / 10,
                          'Flying_robot_frame': 1 / 5,
                          'Satellite': 1 / FIFE_MINUTES,
                          'Rocket_part': 1 / 10,
                          'Rocket_control_unit': 1 / 10,
                          'Low_density_structure': 1 / 10,
                          'Rocket_fuel': 1 / 5,
                          'Nuclear_fuel': 1 / 10,
                          'Uranium_fuel_cell': 1,
                          'Automation_science_pack': 1 / 2,
                          'Logistic_science_pack': 1 / 2,
                          'Military_science_pack': 1 / 2,
                          'Chemical_science_pack': 1 / 2,
                          'Production_science_pack': 1 / 2,
                          'Utility_science_pack': 1 / 2,
                          'Land_mine': 1 / 30,
                          'Firearm_magazine': 1 / 5,
                          'Piercing_rounds_magazine': 1 / 5,
                          'Uranium_rounds_magazine': 1 / 5,
                          'Shotgun_shells': 1 / 5,
                          'Piercing_shotgun_shells': 1 / 5,
                          'Cannon_shell': 1 / 10,
                          'Explosive_cannon_shell': 1 / 10,
                          'Uranium_cannon_shell': 1 / 10,
                          'Explosive_uranium_cannon_shell': 1 / 10,
                          'Artillery_shell': 1 / 20,
                          'Rocket': 1 / 30,
                          'Explosive_rocket': 1 / 30,
                          'Atomic_bomb': 1 / MINUTE,
                          'Flamethrower_ammo': 1,
                          'Grenade': 1 / factorioRecipes['Grenade']['time'],
                          'Cluster_grenade': 1 / factorioRecipes['Cluster_grenade']['time'],
                          'Poison_capsule': 1 / factorioRecipes['Poison_capsule']['time'],
                          'Slowdown_capsule': 1 / factorioRecipes['Slowdown_capsule']['time'],
                          'Defender_capsule': 1 / factorioRecipes['Defender_capsule']['time'],
                          'Distractor_capsule': 1 / factorioRecipes['Distractor_capsule']['time'],
                          'Destroyer_capsule': 1 / factorioRecipes['Destroyer_capsule']['time'],
                          'Wall': 1,
                          'Gate': 1 / 5,
                          'Gun_turret': 1 / factorioRecipes['Gun_turret']['time'],
                          'Laser_turret': 1 / factorioRecipes['Laser_turret']['time'],
                          'Flamethrower_turret': 1 / factorioRecipes['Flamethrower_turret']['time'],
                          'Artillery_turret': 1 / factorioRecipes['Artillery_turret']['time'],
                          'Radar': 1 / factorioRecipes['Radar']['time']}


def isBasic(item):
    return factorioRecipes[item]['basic'] or item in basicIngredients


def calculateFactories(item, itemsPerSecond):

    numFactories = 1 if isBasic(item) else (itemsPerSecond / factorioRecipes[item]['amount'] * factorioRecipes[item]['time'])

    factories = {item: numFactories}

    if isBasic(item):
        return factories

    for i, n in factorioRecipes[item]['recipe'].items():
        for j, m in calculateFactories(i, n * itemsPerSecond / factorioRecipes[item]['amount']).items():
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

        print(factorioRecipes[i]['name'] + ': ' + '{:0.2f}'.format(n) + ' Factories')

    # print Ingredients
    for i, n in factories.items():
        if not factorioRecipes[i]['basic'] and i not in basicIngredients:
            continue

        print(factorioRecipes[i]['name'] + ': ' + '{:0.2f}'.format(n) + '/s')


# for key, i in factorioRecipes.items():
#     print('\'' + key + '\': 1,')
#
# exit()

item = input('Build: ')
if item not in factorioRecipes and item != 'full':
    print('Item not found...')
    exit()

ratio = float(input('Items/s: '))

if item == 'full':

    if ratio == 0:
        for i, r in defaultAmountPerSecond.items():
            printFactories(calculateFactories(i, r))
            print()
    else:
        for i, d in factorioRecipes.items():
            if d['basic'] or i in basicIngredients or i == 'Kovarex_enrichment_process':
                continue

            printFactories(calculateFactories(i, ratio))
            print()
else:
    printFactories(calculateFactories(item, ratio))
