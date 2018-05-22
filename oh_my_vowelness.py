#made it into two functions one to get the vowel count 
#and one to get the color code
#after if goes through the rest of the phrase it combines everything together
def vowel_count(phrase):
    words = phrase.lower().split(" ")
    result_words = []
    for word in words:
    # Calculate vowelness score
        vowel_count = 0
        consonant_count = 0
        for letter in word:
#removed lower case method moved it to word split sentence.
            if letter in "aeiou":
                vowel_count += 1
#removed elif statement with consonants and replaced with a else statement.            
            else:
                consonant_count += 1
        scores = vowel_count - consonant_count
#adding call to function for color code.
        scores = color_count(scores)
#moved the appending and join methods up to the first function.    
        result_words.append("\033[%dm%s\033[0m" % (scores,word))
    result = " ".join(result_words)
    return (result)
    # Select color code
def color_count(scores):
    for score in [scores]:
        if score >= 2:
            color_code = 35
        elif score >= 1:
            color_code = 34
        elif score >= 0:
            color_code = 36
        elif score >= -1:
            color_code = 32
        elif score >= -2:
            color_code = 33
        else:
            color_code = 31
    return (color_code)
#inputs a phrase
phrase = input("Enter a sentence: ")
#starts the function and prints the results
print(vowel_count(phrase))