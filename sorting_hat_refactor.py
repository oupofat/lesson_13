class Record(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)

    def __repr__(self):
        return "Record%r" % self.__dict__

harry_potter = [
    Record(name = "Harry Potter", house = "Gryffindor", book_intro = 1),
    Record(name = "Hermione Granger", house = "Gryffindor", book_intro = 1),
    Record(name = "Ron Weasley", house = "Gryffindor", book_intro = 1),
    Record(name = "Draco Malfoy", house = "Slytherin", book_intro = 1),
    Record(name = "Luna Lovegood", house = "Ravenclaw", book_intro = 5),
    Record(name = "Cedric Diggory", house = "Hufflepuff", book_intro = 3),
    Record(name = "Severius Snape", house = "Slytherin", book_intro = 1),
    Record(name = "Lord Voldemort", house = "Slytherin", book_intro = 1),
    Record(name = "Cho Chang", house = "Ravenclaw", book_intro = 4),
    Record(name = "Moaning Myrtle", house = "Ravenclaw", book_intro = 3)
]

houses = {}
key_value = houses
for character in harry_potter:
    if character.house not in key_value:
        key_value[character.house] = []
    key_value[character.house].append(character)
def in_my_house(rolling_it):
    print("Gryffndor student list:")
    for student in key_value["Gryffindor"]:
        print(student.name)
in_my_house(houses)
    
