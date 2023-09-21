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

def get_names(spicy_foods):
    new_list = [n["name"] for n in spicy_foods]
    return new_list

def get_spiciest_foods(spicy_foods):
    new_list = [n for n in spicy_foods if n["heat_level"] > 5]
    return new_list

def print_spicy_foods(spicy_foods):
    for n in spicy_foods:
        print(f"{n['name']} ({n['cuisine']}) | Heat Level: {'🌶' * n['heat_level']}")
        

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    my_dict = dict()
    for n in spicy_foods:
        if n['cuisine'] == cuisine:
            my_dict.update(n)
    return my_dict

def print_spiciest_foods(spicy_foods):
    for n in spicy_foods:
        if n['heat_level'] > 5:
            print(f"{n['name']} ({n['cuisine']}) | Heat Level: {'🌶' * n['heat_level']}")
        

def get_average_heat_level(spicy_foods):
    total = 0
    length = len(spicy_foods)
    for n in spicy_foods:
        total += n['heat_level']
    average =int(total/length)
    return average
    
    

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
