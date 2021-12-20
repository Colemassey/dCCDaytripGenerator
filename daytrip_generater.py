# Lists of destinations(13), transport(11), foods (10), and venues(12) that rng will choose from.
# games: Mario, Halo, GTA San Andreas, Zelda BOTW, Skyrim, RDR2, Spider-man, Ghost of Tsushima, Fable, Kingdom Come Deliverance, Among Us, Witcher 3, Pokemon

cities = ("Battle Creek", "Novigrad", "New York", "Hyrule", "Skyrim", "Saint Denis", "Lavender Town", "Tsushima", "Albion", "Pribyslavitz", "Mushroom Kingdom", "Grove Street, Ganton, Los Santos", "Space")

trans = ("Warthog", "magic portal", "webslinging", "Glider", "dragon", "horseback", "a small pidgey that knows Fly", "Warp Pipe", "a Banshee sports car", "walking very, very slowly", "spaceship")

foods = ("custard pie and coffee at Havadi Goodwan", "Witcher potions", "pizza at Lucali's", "Monster Cake", "cheese wheels", "rice and sake", "delicious Slowpoke tails", "red and green mushrooms", "chicken at Cluckin' Bell", "birthday cake")

venues = ("play Grifball with Master Chief!", "slay monsters with Geralt, The White Wolf!", "keep the neighborhood friendly, with Spiderman!", "doing side quests, instead of beating Gannondorf!", "become a samurai with Jin Sakai!", "slay dragons with the Dragonborn!", "do spread tuberculosis with Arthur Morgan", "find your father's sword, with Henry of Skalitz!", "help a cubone find it's mother!", "become King while ignoring your morality meter!", "save a princess who keeps suspiciously getting kidnapped!", "find the traitor among us...", "skydive with CJ")

# RNG, set to list length

import random

def RNG(list):
    end_point = len(list) - 1
    rng=random.randint(0,end_point)
    return (rng)

# Functions to pick from lists with rng rolls

def destination_picker():
    pick = cities[RNG(cities)]
    return pick

def transport_picker():
    drive = trans[RNG(trans)]
    return drive

def restaurant_picker():
    yummy = foods[RNG(foods)]
    return yummy

def entertainment_picker():
    fun = venues[RNG(venues)]
    return fun

# Variables to hold RNG values

selected_destination = destination_picker()
selected_transportation = transport_picker()
selected_restaurant = restaurant_picker()
selected_entertainment = entertainment_picker()

# Dialogue for changing or confirming trip

def input_helper():
    print("To change your destination enter 1")
    print("To change your transportioan enter 2")
    print("To change your food press 3")
    print("To change your enertainment press 4")
    print("To confirm your trip enter 5")
    user_input = input("Input selection here ")
    return user_input

# While loop for setting up trip until confirmed

def destination_pick(destination, transportation, restaurant, entertainment):
    print(f"You trip is setup!")
    print(f"Your destination will be {destination},")
    print(f"you will get there by {transportation},")
    print(f"You will  eat at {restaurant},")
    print(f"While you {entertainment}.")
    user_input = input_helper()
    user_confirmed = False
    while user_confirmed == False:
        if user_input == "1":
            destination = destination_picker()
            print("You're going to " + destination + "!")
            user_input = input_helper()
        elif user_input == "2":
            transportation = transport_picker()
            print("You'll travel by " + transportation)
            user_input = input_helper()
        elif user_input == "3":
            restaurant = restaurant_picker()
            print("You'll eat " + restaurant)
            user_input = input_helper()
        elif user_input == "4":
            entertainment = entertainment_picker()
            print("You're going to " + entertainment)
            user_input = input_helper()
        elif user_input == "5":
            print(f'Your trip is setup!')
            print(f"Your destination will be {destination},")
            print(f"You will get there by {transportation},")
            print(f"You will eat {restaurant},")
            print(f"You will {entertainment}")
            user_confirmed = True

# Calling function

destination_pick(selected_destination, selected_transportation, selected_restaurant, selected_entertainment)