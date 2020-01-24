def ZeroDivision():
    try:
        print(5/0)
    except ZeroDivisionError:
        print('Det går inte att dela med 0!!!')


def InputError():
    print('Skriv in två nummer, och jag kommer dividera dem.')
    print('Skriv q för att avsluta')
    while True:
        first_number = input('\nFörsta nummret: ')
        if first_number == 'q':
            break
        second_number = input('\nAndra nummret: ')
        if second_number == 'q':
            break
        try:
            answer = int(first_number) / int(second_number)
            print(answer)
        except ZeroDivisionError as diverr:
            print('Det går inte att dela med 0')
            print(diverr)
        except ValueError as verr:
            print('Det går inte att omvandla strängen till ett tal')
            print(verr)

    print('Tack för att du spelade...')

def FileErrorExample():
    filename = 'myname.txt'
    
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError as ferr: #Anropas om vi får ett FileNotFoundError
        msg = f'Tyvärr, {filename} verkar inte finnas.'
        print(msg)
    finally: #körs alltid, oavsett fel eller inte.
        print('Något gick fel när vi skulle läsa filen')


ZeroDivision()
InputError()
FileErrorExample()