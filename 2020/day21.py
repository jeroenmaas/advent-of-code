import json
import math
from collections import defaultdict, OrderedDict

import numpy as np

with open('day21.txt') as f:
    inputs = f.read().strip().split('\n')

ingedients_list = []
all_allergens = set()
all_ingredients = set()
for i in inputs:
    ingredients = i.split(' (')[0].split(' ')
    allergens = i.replace(')', '').split('(contains ')[1].split(', ')
    ingedients_list.append({'ingredients': ingredients, 'allergens': allergens})
    all_allergens.update(allergens)
    all_ingredients.update(ingredients)

known_ingredients = {}

# Contains lists of ingredients of which one should be the allergien. By check if only a single ingredient is in all lists we can determen we are right.
possible_ingredients_for_allergien = {}
for item in ingedients_list:
    for all in item['allergens']:
        if all not in possible_ingredients_for_allergien:
            possible_ingredients_for_allergien[all] = []
        possible_ingredients_for_allergien[all].append(item['ingredients'])

found_allergien = True
while(found_allergien):
    found_allergien = False

    for all, ingredient_lists in possible_ingredients_for_allergien.items():
        counts = defaultdict(lambda: 0)
        for ingredients in ingredient_lists:
            for ingredient in ingredients:
                if ingredient not in known_ingredients:
                    counts[ingredient] += 1

        ingredients_in_all_list = []
        for ingredient, count in counts.items():
            if count == len(ingredient_lists):
                ingredients_in_all_list.append(ingredient)

        if len(ingredients_in_all_list) == 1:
            ing = ingredients_in_all_list[0]
            known_ingredients[ing] = all
            found_allergien = True

    for all in known_ingredients:
        if all in possible_ingredients_for_allergien:
            del possible_ingredients_for_allergien[all]

unknown_ingredients = []
for ing in all_ingredients:
    if ing not in known_ingredients:
        unknown_ingredients.append(ing)

occurances_unknown_ingredient = 0
for item in ingedients_list:
    for ing in item['ingredients']:
        if ing in unknown_ingredients:
            occurances_unknown_ingredient += 1

print('part1: ', occurances_unknown_ingredient)


sorted_dict = OrderedDict(sorted(known_ingredients.items(), key=lambda t: t[1]))
print('part2: ', ','.join(sorted_dict))
