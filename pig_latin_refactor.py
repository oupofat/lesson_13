phrase = input("Enter a phrase: ")

words = phrase.split(" ")
result_words = []
for word in words:
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
#possiable new function?
    if first_consonants == "":
        pigword += "y"
    pigword += "ay"
    result_words.append(pigword)
result = " ".join(result_words)

print(result)

#added a function to the pig latin problem
def pig_latin(phrase):
    words = phrase.split(" ")
    result_words = []
    for word in words:
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
        if first_consonants == "":
            pigword += "y"
        pigword += "ay"
        result_words.append(pigword)
        
    result = " ".join(result_words)
    return result
phrase = input("Enter a phrase")

result = pig_latin(phrase)
print (result)



