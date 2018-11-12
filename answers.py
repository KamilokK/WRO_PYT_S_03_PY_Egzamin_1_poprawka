ZADANIE 2:

def name_sorter():

    for key in names:
        print(key, names)
        ladies.append(female)

        mens.apppend(male)


print(name_sorter(names))

    {'female': ['Alicja', 'Barbara'], 'male': ['Andrzej', 'Cezary', 'Henryk']}
    names = ["Andrzej", "Henryk", "Alicja", "Cezary", "Barbara"]

ZADANIE 3:

def validate_password(password):

valid_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-_=+[{]}\|;:?/>.<,

    if len(password)<9:
        return False
    else:
        for character in password:
            if character not in validate_characters:
            return False
        return True

print(validate_password("mamamamaaa"))

ZADANIE 4:

def div(a,b):
    a=int(a)
    b=int(b)
    if  a%b == 0:
        return True
    else:
        return False

print(div(4,2))

ZADANIE 5:

def find_longest_word(tekst):
    lista = tekst.split(" ")
    posortowane = lista.sort(key=len)
    longer = posortowane[0]
    return longer


print(find_longest_word("MAM adwie kury i czy kozssy"))

ZADANIE 6:

from random import random
from answers import _card_values
from answers import _card_colors

def poker_hand():

cards = [v + ' of ' + c for v in _card_values for c in _card_colors]

print poker_hand















_card_values = ['A', 'K', 'Q', 'J',
                '10', '9', '8', '7', '6', '5', '4', '3', '2']
_card_colors = ['hearts', 'diamonds', 'spades', 'clubs']

# do rozwiązania zadania z kartami pokerowymi użyj tej listy:
cards = [v + ' of ' + c for v in _card_values for c in _card_colors]
