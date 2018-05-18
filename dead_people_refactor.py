class Record(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)

    def __repr__(self):
        return "Record%r" % self.__dict__

harry_potter = [
    Record(name = "Harry Potter", house = "Gryffindor", dead = False),
    Record(name = "Hermione Granger", house = "Gryffindor", dead = False),
    Record(name = "Ron Weasley", house = "Gryffindor", dead = False),
    Record(name = "Draco Malfoy", house = "Slytherin", dead = False),
    Record(name = "Luna Lovegood", house = "Ravenclaw", dead = False),
    Record(name = "Cedric Diggory", house = "Hufflepuff", dead = True),
    Record(name = "Severius Snape", house = "Slytherin", dead = True),
    Record(name = "Lord Voldemort", house = "Slytherin", dead = True),
    Record(name = "Cho Chang", house = "Ravenclaw", dead = True),
    Record(name = "Moaning Myrtle", house = "Ravenclaw", dead = True)
]

dead_per_house = {}
for student in harry_potter:
    if student.house not in dead_per_house:
        dead_per_house[student.house] = 0
    if student.dead:
        dead_per_house[student.house] += 1

house_with_most_dead = None
highest_dead_count = 0
for house, dead_count in dead_per_house.items():
    if house_with_most_dead == None or dead_count > highest_dead_count:
        house_with_most_dead = house
        highest_dead_count = dead_count

print("%s had the most dead people with %d." % (house_with_most_dead, highest_dead_count))