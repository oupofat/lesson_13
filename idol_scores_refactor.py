from functools import reduce

class Record(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)

    def __repr__(self):
        return "Record%r" % self.__dict__

contestant = Record(
        name = "Jelly Blockton",
        judge_scores = [9, 4, 7, 8, 10, 5],
        popular_score = 10)

# The final score is the average of the judge's scores combined
# with the popular_score. But the judge's scores has a 70% weight
# while the popular score only has a 30% weight.
def final_score(contestant):
    result = reduce(lambda a, b: a + b, contestant.judge_scores, 0) / len(contestant.judge_scores) * 0.7 + contestant.popular_score * 0.3
    return result

print("%s's final score is %.2f." % (contestant.name, final_score(contestant)))

#This is the refactored from the above code.

def final_score(contestant):
#this line breaks down how many judges and the popular vote there is.
    number_of_judges = len(contestant.judge_scores)+1
#this live breaks down the total average for judges.
    total_of_the_judges_scores = (sum(contestant.judge_scores)*0.7)
#this line breaks down the average of the popular vote.
    total_of_the_popular_score = contestant.popular_score * 0.3
#this returns the value of the code.
    return (total_of_the_judges_scores + total_of_the_popular_score / number_of_judges)
#and finally the print statement for all of it put together.
print("%s's final score is %.2f."%(contestant.name, final_score(contestant)))
#calls the function.
final_score(contestant)