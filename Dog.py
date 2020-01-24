class Dog():
    """En klass för att efterlikna en hund"""
    def __init__(self, name, age = None):
        if age == None:
            self.age = 0
        else:
            self.age = age

        self.name = name

    def sit(self):
        print(f'{self.name.title()} sitter ner!')

    def roll_over(self):
        print(f'{self.name.title()} rullade runt!')