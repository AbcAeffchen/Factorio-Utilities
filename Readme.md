# Factorio Utilities

## Helpers

### getRecipesJson.py

This script generates a JSON file with all the item recipes from wiki.factorio.com/Items.
The result can be found in data/factorio-recipes.json

#### Known Issues
The whole nuclear stuff is kind of broken since there are recipes that have an other name than the result and/or multiple resulting items.

### getProductionChain.py

Tells you how many of the same factories one need to produce a specific item with a given frequency. 
Also tells you the number of basic items one need.