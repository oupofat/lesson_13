#collects the consonants and then returns the pigword
def pig_collect_consonants(word):    
    pigword = ""
    state = "collect-consonants"
    first_consonants = ""
    for letter in word:
        if state == "collect-consonants":
            if not letter in "aeiou":
                first_consonants += letter
            else:
                state = "collect-rest"
                pigword += letter
        elif state == "collect-rest":
            pigword += letter
    pigword += first_consonants
    return(pigword)
    
#takes the word from above and adds the "y" and "ay".
#then returns the new word to below to be appended.
def change_to_pig_latin(word):
    new_word = pig_collect_consonants(word)
    if new_word == "":
        new_word+="y"
    new_word += "ay"
    return (new_word)
#splits the word.
#This function breaks down and rejoins the phrase.   
#returns the final phrase to be printed out
def pig_latin_phrase(phrase):
    words = phrase.split(" ")
    result_words = []
    for word in words:
        final_word = change_to_pig_latin(word)
        result_words.append(final_word)
    final_phrase = " ".join(result_words)
    return (final_phrase)
        
phrase = input("input your words here!")
#prints out the pig latin phrase.
print ("What does this even mean:",pig_latin_phrase(phrase))