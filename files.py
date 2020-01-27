import json
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

def WriteToFilePi(filename, path = './', data = ''):
    filelocation = path + filename
    with open(filelocation, 'w') as file_obj:
        file_obj.write(data)


def WriteToFilPiJson(data):
    filename = './data_file/pi.json'
    with open(filename, 'w') as file_obj:
        json.dump(data, file_obj)  

def ReadToFilePiFromJson():
    filename = './data_file/pi.json'
    with open(filename, 'r') as file_obj:
        list = json.load(file_obj)

    for i in range(0, 19):
        print(list[i])         

def ToDick():
    filename = './data_file/pi.txt'
    with open(filename, 'r') as file_obj:
        content = file_obj.read()
        l = content.split('.')
        dick = { 'heltal' : l[0] + '.', 'decimaler' : l[1] }
        with open('./data_file/ksksks.json', 'w') as ff_p:
            json.dump(dick, ff_p)
def SplitPi(): 
    pi = ReadFile('pi.txt', 'data_file/')
    i = 0
    list = []
    numbers = ''
    for c in pi:
        i += 1
        numbers += str(c)
        if i == 20:
            list.append(numbers)
            i = 0
            numbers = ''
    
    WriteToFilePi(filename = 'pidivided.txt', data = '-'.join(list), path = './data_file/')
    WriteToFilPiJson(list)

# ReadFile('data.txt')
# ReadFile('data.txt', 'data_file/')

# list = ReadEachLine('data.txt', 'data_file/')
# #Skriver ut dubbla newlines eftersom filen innehåller det och print skriver ut ett också.
# for line in list: 
#     print(line)

# #Vi plockar bort newline från varje rad och skriver ut.
# for line in list:
#     print(line.rstrip("\n"))

# list2 = ReadEachLineWithReadLines('data.txt', 'data_file/')
# for line in list2:
#     print(line)

#FindBirthdayInPi()
#SplitPi()
#ReadToFilePiFromJson()
ToDick()
# WriteToFile('writetofile.txt', 'data_file/')