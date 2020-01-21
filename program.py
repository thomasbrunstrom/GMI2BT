my_menu = {}
my_menu["breakfast"] = "Corn flakes"
my_menu["lunch"] = "Falukorv och potatis"
my_menu["dinner"] = "Hamburgare"
print(my_menu)
print("Till middag äter jag nästan alltid %s"  %my_menu["dinner"])
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
    print(key + ":" + value)

favorit_språk = {
    "Thomas" : ["Javascript", "C#", "HTML", "CSS"],
    "Hans-Jones" : ["Python", "Java"],
    "Hans-Edy" : ["C#", "Java", "ADA"]
}
for name, languages in favorit_språk.items():
    print("\n" + name.title() + "' favoritspråk är:")
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
    print("\nUsername: " + username)
    full_name = userinfo["firstname"] + " " + userinfo["surname"]
    city = userinfo["city"]
    print("Full name: %s and location: %s" %(full_name, city))


username = input("Ange ditt användarnamn")
password = input("Ange ditt lösenord")
print("Ditt användarnamn är: %s och lösenord är: %s" %(username, password))

age = input("Hur gammal är du? ")
nummer_age = int(age)
print("Ålder: %d %d" %(nummer_age, nummer_age + 10))

start = 0
while start <= 5:
    print("Nuvarande nummer: %s" %start)
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