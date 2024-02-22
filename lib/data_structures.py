spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

print("")

def get_names(spicy_foods):
    name_list = []
    for spicy_food in spicy_foods:
        name_list.append(spicy_food["name"])
    print(name_list)
    return name_list
get_names(spicy_foods)

print("")

def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for spicy_food in spicy_foods:
        if spicy_food["heat_level"] > 5:
            spiciest_foods.append(spicy_food)
    print(spiciest_foods)
    return spiciest_foods
get_spiciest_foods(spicy_foods)

print("")

def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        pepper = "🌶" * spicy_food["heat_level"]
        print(f'{spicy_food["name"]} ({spicy_food["cuisine"]}) | Heat Level: {pepper}')
print_spicy_foods(spicy_foods)

print("")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy_food in spicy_foods:
        if spicy_food["cuisine"] == cuisine:
            print(spicy_food)
            return spicy_food
get_spicy_food_by_cuisine(spicy_foods, "Thai")

print("")

def print_spiciest_foods(spicy_foods):
    for spicy_food in spicy_foods:
        if spicy_food["heat_level"] > 5:
            pepper = "🌶" * spicy_food["heat_level"]
            print(f'{spicy_food["name"]} ({spicy_food["cuisine"]}) | Heat Level: {pepper}')
print_spiciest_foods(spicy_foods)

print("")

def get_average_heat_level(spicy_foods):
    average_heat_level = 0
    for spicy_food in spicy_foods:
        average_heat_level += spicy_food["heat_level"]
    average_heat_level = average_heat_level / (len(spicy_foods))
    return int(average_heat_level)
get_average_heat_level(spicy_foods)

print("")

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    print(spicy_foods)
    return(spicy_foods)
create_spicy_food(spicy_foods, {"name": "Wasabi",
                                "cuisine": "Japanese",
                                "heat_level": 7,})
