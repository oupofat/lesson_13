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
#added a function to the dictrionary to get the houses and the dead count.
def house_and_dead_count(harry_potter):
    dead_per_house = {}
    for student in harry_potter:
        if student.house not in dead_per_house:
            dead_per_house[student.house] = 0
        if student.dead:
            dead_per_house[student.house] += 1
    print (dead_per_house)  
    return(dead_per_house)
#added another function to get the houses and dead count
#this code goes through the houses and the count making a total of the highest one
def highest_dead_count(harry_potter):
#calls 
    houses = house_and_dead_count(harry_potter)
    house_with_most_dead = None
    highest_dead_count = 0
    for house, dead_count in houses.items():
        if house_with_most_dead == None or dead_count > highest_dead_count:
            house_with_most_dead = house
            highest_dead_count = dead_count
    return(house_with_most_dead, highest_dead_count)
#this calls the function to and renames the called function
house_of_the_dead=highest_dead_count(harry_potter)
#prints the function highest dead count with a Iterating Dictionary
print("%s had the most dead people with %d." % (house_of_the_dead[0], house_of_the_dead[1]))