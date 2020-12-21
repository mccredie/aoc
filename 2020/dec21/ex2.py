
import sys, re
from collections import defaultdict

INGREDIENT_MATCHER = re.compile(r"(?P<ingredients>\w+(?: \w+)*) \(contains (?P<allergens>\w+(?:, \w+)*)\)$")

def read_ingredients(lines):
    for line in lines:
        if m := INGREDIENT_MATCHER.match(line):
            ingredients = set(m.group("ingredients").split(" "))
            allergens = set(m.group("allergens").split(", "))
            yield ingredients, allergens

def get_possibilities(all_ingredients, recipes):
    possibilities = defaultdict(lambda: set(all_ingredients))
    for ingredients, allergens in recipes:
        for allergen in allergens:
            possibilities[allergen] &= ingredients
    return possibilities

def find_singles(possibilities):
    found = {}
    for allergen, ingredients in possibilities.items():
        if len(ingredients) == 1:
            found[allergen] = list(ingredients)[0]
    return found

def remove_found(possibilities, found):
    new_possibilities = dict(possibilities)
    for allergen in found.keys():
        del new_possibilities[allergen]
    remove_ingredients = set(found.values())
    for allergen, ingredients in list(new_possibilities.items()):
        new_possibilities[allergen] = set(ingredients) - remove_ingredients
    return new_possibilities

def main():
    all_recipes = list(read_ingredients(sys.stdin))
    all_ingredients = set()
    for ingredients, _ in all_recipes:
        all_ingredients |= ingredients

    possibilities = get_possibilities(all_ingredients, all_recipes)

    known = {}
    while possibilities:
        found = find_singles(possibilities)
        possibilities = remove_found(possibilities, found)
        known.update(found)

    result = ",".join(known[key] for key in sorted(known))
    print(result)

if __name__ == "__main__":
    main()
