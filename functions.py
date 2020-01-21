def WriteMessage():
    """ Den här funktionen skriver bara ut ett meddelande """
    print("Den här funktionen skriver bara ut den här texten.")

WriteMessage()

def WriteMessage(message):
    """ Den här funktionen skriver ut meddelandet vi skickar in """
    print(message)

WriteMessage("Det här är vårt meddelande.")


def PositionArguments(pet_type, pet_name):
    print(f'Du har en {pet_type} och den heter {pet_name}')

PositionArguments(pet_name = 'Harry', pet_type = 'Papegoja')

PositionArguments('hund', 'Caro')

PositionArguments('Hulken', 'katt')

def CalculateValues(value1, value2):
    msg = f'{value1} + {value2} = {value1 + value2}, {value1} - {value2} = {value1 - value2}'
    return msg

print(CalculateValues(20, 10))

def GetCircleArea(radius, pi = 3):
    return radius * radius * pi

print(f'Arean för en cirkel som har radien 3 är: {GetCircleArea(3)}')
print(f'Arean för en cirkel som har radien 3 är: {GetCircleArea(3, 3.14159)}')

def GetCirleAreaDictionary(radius, pi = 3):
    return { "radius": radius, "pi": pi, "area": radius * radius * pi }

info = GetCirleAreaDictionary(3, 3.14159)
print(info)

def GreetPersons(names):
    for person in names:
        print(f'Hej på dig {person}')

GreetPersons(['Thomas', 'Johanna', 'Hans', 'Kristina'])

def printDesigns(unprintedDesigns, completedDesigns):
    while unprintedDesigns:
        currentDesign = unprintedDesigns.pop()
        print(f'Printing model: {currentDesign}')
        completedDesigns.append(currentDesign)

def showPrintedDesigns(completedDesigns):
    for design in completedDesigns:
        print(design)

unprintedDesigns = ['Star destroyer', 'Millenium falcon', 'X-wing', 'B-wing', 'A-Wing']
printedDesigns = []
print('\nUnprinted designs')
printDesigns(unprintedDesigns, printedDesigns)
print('\nPrinted designs')
showPrintedDesigns(printedDesigns)

def MakePizza(*topping):
    print(topping)

MakePizza('Skinka')
MakePizza('Skinka', 'Ost', 'Lök', 'Svamp')

import pizza
pizza.MakePizzaModule(30, 'Kebab', 'Lök', 'Pommes')

from pizza import MakePizzaModule as mp
mp(20, 'Oxfilé', 'Bea', 'Färsta tomater')
