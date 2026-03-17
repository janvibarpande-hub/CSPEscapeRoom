import random
import time
phrase_list = [
    ["grandmother", "what", "big", "eyes", "you", "have"],
    ["all", "the", "better", "to", "see", "you", "with", "my", "dear"],
    ["grandmother", "what", "big", "ears", "you", "have"],
    ["all", "the", "better", "to", "hear", "you", "with", "my", "dear"],
    ["grandmother", "what", "big", "teeth", "you", "have"],
    ["all", "the", "better", "to", "eat", "you", "with"],
    ["i", "am", "going", "to", "visit", "my", "grandmother"],
    ["she", "lives", "just", "beyond", "those", "trees"],
    ["little", "red", "riding", "hood"]
    ]


#scramble
phrase = random.choice(phrase_list)
length = len(phrase)
work_phrase = []
for i in range(length):
    word = phrase[i]
    string_list = list(word)
    random.shuffle(string_list)
    new_word = "".join(string_list)
    work_phrase.append(new_word)
    new_phrase = "".join(work_phrase)
#add spaces to the word so it all not clump together

print(new_phrase)

guess = 6
print("You have arrived at Granny's house but she has a lock on her door.")
time.sleep(3)
print("To unlock the door you need to unscramble the phrase in 6 or less guesses")
time.sleep(3)
print("The phrase is: ")
time.sleep(3)
print(new_phrase)
time.sleep(3)
while guess > 0:
    unscrambled = input("Please enter the uncrambled phrase: ")
    if unscrambled == phrase:
        print("That is correct")
        break
    else:
        guess -= 1
        print(f"That is incorrect, you have {guess} left")
