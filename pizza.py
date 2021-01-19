print("Det här är pizzamodulen")
def make_pizza_module(size, *topping):
    print(f'Vi bakar en {size}cm stor pizza med följande pålägg:')
    for top in topping:
        print(top)