my_menu = {}
my_menu["breakfast"] = "Corn flakes"
my_menu["lunch"] = "Falukorv och potatis"
my_menu["dinner"] = "Hamburgare"
print(my_menu)
print(f'Till middag äter jag nästan alltid {my_menu["dinner"]}')
#{'breakfast': 'Corn flakes', 'lunch': 'Falukorv och potatis', 'dinner': 'Hamburgare'}
#Till middag äter jag nästan alltid Hamburgare

my_menu["snacks"] = "Chips"
print(my_menu)
# {'breakfast': 'Corn flakes', 'lunch': 'Falukorv och potatis', 'dinner': 'Hamburgare', 'snacks': 'Chips'}
my_menu["dinner"] = "Köttfärssås och spagetti"
# {'breakfast': 'Corn flakes', 'lunch': 'Falukorv och potatis', 'dinner': 'Köttfärssås och spagetti', 'snacks': 'Chips'}
del my_menu["snacks"]
print(my_menu)
# {'breakfast': 'Corn flakes', 'lunch': 'Falukorv och potatis', 'dinner': 'Köttfärssås och spagetti'}

my_menu_keys = my_menu.keys()
print(my_menu_keys)
#dict_keys(['breakfast', 'lunch', 'dinner'])

my_menu_values = my_menu.values()
print(my_menu_values)
#dict_values(['Corn flakes', 'Falukorv och potatis', 'Köttfärssås och spagetti'])

for key, value in my_menu.items():
    print(f'{key}:{value}')

favorit_språk = {
    "Thomas" : ["Javascript", "C#", "HTML", "CSS"],
    "Hans-Jones" : ["Python", "Java"],
    "Hans-Edy" : ["C#", "Java", "ADA"]
}
for name, languages in favorit_språk.items():
    print(f'{name.title()} favoritspråk är:')
    for lang in languages:
        print("\t" + lang)

users = {
    "tbn": {
        "firstname" : "Thomas",
        "surname" : "Brunström",
        "city" : "Borlänge"
    },
    "Hans": {
        "firstname" : "Hans",
        "surname" : "Jones",
        "city" : "Borlänge"
    }
}
for username, userinfo in users.items():
    print(f'Username: {username}')
    full_name = userinfo["firstname"] + " " + userinfo["surname"]
    city = userinfo["city"]
    print(f'Full name: {full_name} and location: {city}')


username = input("Ange ditt användarnamn")
password = input("Ange ditt lösenord")
print(f'Ditt användarnamn är: {username} och lösenord är: {password}')

age = input("Hur gammal är du? ")
nummer_age = int(age)
print(f'Ålder: {nummer_age} {nummer_age + 10}')

start = 0
while start <= 5:
    print(f'Nuvarande nummer: {start}')
    start += 1

print("Skriv något och programmet kommer repetera det du skrev.")
print("Skriv exit för att avsluta.")
message = ""
while message != "exit":
    message = input()
    if message == "hejsan":
        break
    else :
        print(message)


from Dog import Dog
hund1 = Dog('Skrutten', 3)
print(hund1)

# Komma åt attribut
print(hund1.age)
print(hund1.name.title())

# Anropa metoder
hund1.sit()
hund1.roll_over()

# Skapa flera instanser
hund2 = Dog('Fido', 5)
hund3 = Dog('Aina', 6)


# en bilklass
from Car import Car, ElectricCar
my_car = Car('audi', 'A4', 2018)
print(my_car.get_descriptive_name())
my_car.read_odometer()

my_car.odometer_reading = 42
my_car.read_odometer()
my_car.update_odometer(55)
my_car.read_odometer()

my_tesla = ElectricCar('tesla', 'S', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()