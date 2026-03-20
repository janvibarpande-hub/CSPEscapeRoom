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
        ["little", "red", "riding", "hood"]
        ]


    #scramble
    phrase = random.choice(phrase_list)
    unscram_phr = " ".join(phrase)
    length = len(phrase)
    work_phrase = []
    for i in range(length):
        word = phrase[i]
        string_list = list(word)
        random.shuffle(string_list)
        new_word = "".join(string_list)
        work_phrase.append(new_word)
        new_phrase = " ".join(work_phrase)
    #add spaces to the word so it all not clump together

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
        unscrambled = input("Please enter the uncrambled phrase: ")
        if unscrambled == unscram_phr:
            print("That is correct!")
            print("You have recieved a key")
            break
        else:
            guess -= 1
            print(f"That is incorrect, you have {guess} left")

room2_task2()
    
