import random
phrase_list = ["grandmother what big eyes you have",
               "all the better to see you with my dear",
               "grandmother what big ears you have",
               "all the better to hear you with my dear",
               "grandmother what big teeth you have"
               "all the better to eat you with",
               "i am going to visit my grandmother",
               "she lives just beyond those trees"
               "little red riding hood"]
phrase = random.choice(phrase_list)
string_list = list(phrase)
random.shuffle(string_list)
new_phrase = "".join(string_list)

guess = 5
input("You have arrived at Granny's house but she has a lock on her door.")
input("To unlock the door you need to unscramble the phrase in 5 or less guesses")
input("The phrase is: ")
input(new_phrase)
unscrambled = input("Please enter the uncrambled phrase: ")
if uncrambled == phrase:
    print("That is correct")
else:
    guesses -= 1
    print(f"That is incorrect, you have {guesses} left")
