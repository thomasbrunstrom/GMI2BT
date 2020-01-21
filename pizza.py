print("Det här är pizzamodulen")
def MakePizzaModule(size, *topping):
    print(f'Vi bakar en {size}cm stor pizza med följande pålägg:')
    for top in topping:
        print(top)