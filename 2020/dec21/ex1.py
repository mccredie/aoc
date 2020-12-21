
import sys, re
from collections import defaultdict

INGREDIENT_MATCHER = re.compile(r"(?P<ingredients>\w+(?: \w+)*) \(contains (?P<allergens>\w+(?:, \w+)*)\)$")

def read_ingredients(lines):
    for line in lines:
        if m := INGREDIENT_MATCHER.match(line):
            ingredients = set(m.group("ingredients").split(" "))
            allergens = set(m.group("allergens").split(", "))
            yield ingredients, allergens

def main():
    all_recipes = list(read_ingredients(sys.stdin))
    may_contain = defaultdict(set) # map ingredient to allergen
    may_be_contained = defaultdict(set) # map allergen to ingredient
    recipe_map = {}
    allergen_map = {}
    for ingredients, allergens in all_recipes:
        recipe_map[frozenset(ingredients)] = allergens
        allergen_map[frozenset(allergens)] = ingredients
        for ingredient in ingredients:
            may_contain[ingredient] |= allergens
        for allergen in allergens:
            may_be_contained[allergen] |= ingredients
    all_allergens = set(may_be_contained)
    all_ingredients = set(may_contain)

    consistent_allergen_assoc = defaultdict(lambda: set(all_ingredients))
    for allergen in all_allergens:
        for allergens, ingredients in allergen_map.items():
            if allergen in allergens:
                consistent_allergen_assoc[allergen] &= ingredients

    safe_ingredients = set(all_ingredients)
    for ingredients in consistent_allergen_assoc.values():
        safe_ingredients -= ingredients

    total = 0
    for ingredients in recipe_map:
        total += len(safe_ingredients & ingredients)

    print(total)

if __name__ == "__main__":
    main()
