def room2_task2():
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
        ["little", "red", "riding", "hood"],
        ["do", "not", "speak", "to", "any", "strangers", "on", "the", "road"], 
        ["he", "swallowed", "poor", "old", "grandmother"], 
        ["the", "wolf", "had", "a", "very", "good", "appetite"]
        ]


    #scramble
    phrase = random.choice(phrase_list)
    unscram_phr = " ".join(phrase)
    length = len(phrase)
    work_phrase = []
    for i in range(length):
        word = phrase[i]
        #seperate each letter in the word into its own part of the list
        string_list = list(word)
        random.shuffle(string_list)
        #join the scrambled letters back together
        new_word = "".join(string_list)
        #make sure the word is scrambled properly
        if new_word == word:
            string_list = list(word)
            random.shuffle(string_list)
            new_word = "".join(string_list)

        work_phrase.append(new_word)
        #add the words into a list
        new_phrase = " ".join(work_phrase)

    guess = 5
    print("You have arrived at Granny's house but she has a lock on her door.")
    time.sleep(3)
    print("""
                                               
        ══════════════════════════════════     
       ║                                  ║    
       ║  ──────────────────────────────  ║    
       ║ │ EEEE N    N TTTTT EEEE RRRRR │ ║    
       ║∙│ E    NN   N   T   E    R   R │∙║    
       ║ │ E    N N  N   T   E    RRRRR │ ║    
       ║ │ EEEE N  N N   T   EEEE R R   │ ║    
       ║∙│ E    N   NN   T   E    R  R  │∙║    
       ║ │ EEEE N    N   T   EEEE R   R │ ║    
       ║  ──────────────────────────────  ║    
       ║                                  ║    
        ══════════════════════════════════     
                                               
    """)
    time.sleep(3)
    print("To unlock the door you need to unscramble the phrase in 5 or less guesses")
    time.sleep(3)
    print("The phrase is: ")
    time.sleep(3)
    print(new_phrase)
    time.sleep(3)
    while guess > 0:
        unscrambled_up = input("Please enter the uncrambled phrase: ")
        unscrambled = unscrambled_up.lower()
        if unscrambled == unscram_phr:
            print("That is correct!")
            print("You have recieved a key")
            break
        else:
            guess -= 1
            print(f"That is incorrect, you have {guess} left")
        if guess == 0:
            print("You have run out of guesses")
            print("Game Over!")

room2_task2()
    
