import random
import time
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

guess = 8
print("You have arrived at Granny's house but she has a lock on her door.")
time.sleep(4)
print("To unlock the door you need to unscramble the phrase in 6 or less guesses")
time.sleep(4)
print("The phrase is: ")
time.sleep(4)
print(new_phrase)
time.sleep(4)
while guess > 0:
    unscrambled = input("Please enter the uncrambled phrase: ")
    if unscrambled == phrase:
        print("That is correct")
        break
    else:
        guess -= 1
        print(f"That is incorrect, you have {guess} left")
