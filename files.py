
def ReadFile(filename, path = './'):
    filelocation = path + filename
    try:
        with open(filelocation) as file_obj:
            content = file_obj.read()
            return content
    except FileNotFoundError as ferr:
        print(ferr)
    return None

def ReadEachLine(filename, path = './'):
    filelocation = path + filename
    lines = []
    try:
        with open(filelocation) as file_obj:
            for line in file_obj:
                lines.append(line)
            return lines
    except FileNotFoundError as ferr:
        print(ferr)

def ReadEachLineWithReadLines(filename, path = './'):
    filelocation = path + filename
    lines = []
    try:
        with open(filelocation) as file_obj:
            lines = file_obj.readlines()
            return lines
    except FileNotFoundError as ferr:
        print(ferr)

def FindBirthdayInPi():
    pi = ReadFile('pi.txt', 'data_file/')
    birthday = input('Skriv in ditt födelsenummer, ÅÅMMDD: ')
    position = pi.find(birthday)
    if position > -1:
        print(f'Din födelsedag finns i de första miljonen decimaler av pi, plats {position}')
    else:
        print('Din födelsedag finns inte i de första miljonen decimaler av pi.')

def WriteToFile(filname, path = './'):
    filelocation = path + filename
    with open(filelocation, 'w') as file_obj:
        file_obj.write('Här skriver vi en rad')
        file_obj.write('Här skriver vi en till rad')


ReadFile('data.txt')
ReadFile('data.txt', 'data_file/')

list = ReadEachLine('data.txt', 'data_file/')
# #Skriver ut dubbla newlines eftersom filen innehåller det och print skriver ut ett också.
# for line in list: 
#     print(line)

# #Vi plockar bort newline från varje rad och skriver ut.
# for line in list:
#     print(line.rstrip("\n"))

# list2 = ReadEachLineWithReadLines('data.txt', 'data_file/')
# for line in list2:
#     print(line)

# FindBirthdayInPi()

WriteToFile('writetofile.txt', 'data_file/')