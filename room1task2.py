while True:
    import random
    import time
    flower_list = [
        "Sunflower", "Daffodil", "Marigold", "Petunia", "Begonia", 
        "Geranium", "Hydrangea", "Snapdragon", "Lavender", "Jasmine", 
        "Gardenia", "Hyacinth", "Magnolia", "Hibiscus", "Wisteria", 
        "Honeysuckle", "Bluebell", "Buttercup", "Foxglove", "Primrose", 
        "Dandelion", "Carnation", "Chrysanthemum", "Amaranth", "Columbine", 
        "Clematis", "Cyclamen", "Foxglove", "Gardenia", "Gladiolus", 
        "Heather", "Lobelia", "Morning Glory", "Oleander", "Petunia", 
        "Trillium", "Verbena", "Wallflower", "Anemone", "Camellia"]
    answer = random.choice(flower_list).upper()
    letters = list(answer)
    template = ["____"] * len(letters)
    current_display = template
    wrong_guesses = 0
    other_letters = []
    print(letters)
    game_won = False

    hangmans = [' --------------------',
    ''' 
                    |                                 
                    |                                 
                    |                                 
                    |                                 
                    |                                 
                    |                                 
                    |                                 
                    |                                 
                    |                                 
                    |                                 
                    |
    ----------------+---''',
    '''  -----------+                                 
                    |                                 
                    |                                 
                    |                                 
                    |                                 
                    |                                 
                    |                                 
                    |                                 
                    |                                 
                    |                                 
                    |
    ----------------+---''',
    '''                                                                                
         +----------+                                                               
        ,|.         |                                                               
       (   )        |                                                               
        `-'         |                                                               
                    |                                                               
                    |                                                               
                    |                                                               
                    |                                                               
                    |                                                               
                    |                                                               
     ---------------+---''',
    '''                                                                                
         +----------+                                                               
        ,|.         |                                                               
       (   )        |                                                               
        `-'         |                                                               
         |          |                                                               
         |          |                                                               
         |          |                                                               
         |          |                                                               
                    |                                                               
                    |                                                               
     ---------------+---''',
    '''                                                                                
         +----------+                                                               
        ,|.         |                                                               
       (   )        |                                                               
        `-'         |                                                               
      \  |          |                                                               
       `.|          |                                                               
         |          |                                                               
         |          |                                                               
                    |                                                               
                    |                                                               
     ---------------+---''',
    '''                                                                                
         +----------+                                                               
        ,|.         |                                                               
       (   )        |                                                               
        `-'         |                                                               
      \  |  /       |                                                               
       `.|.'        |                                                               
         |          |                                                               
         |          |                                                               
                    |                                                               
                    |                                                               
     ---------------+---''',
    '''                                                                                
         +----------+                                                               
        ,|.         |                                                               
       (   )        |                                                               
        `-'         |                                                               
      \  |  /       |                                                               
       `.|.'        |                                                               
         |          |                                                               
         x          |                                                               
        /           |                                                               
       /            |                                                               
     ---------------+---''',
    '''                                                                                
         +----------+                                                               
        ,|.         |                                                               
       (   )        |                                                               
        `-'         |                                                               
      \  |  /       |                                                               
       `.|.'        |                                                               
         |          |                                                               
         x          |                                                               
        / \         |                                                               
       /   \        |                                                               
     ---------------+---''',
    '''                                                                                
         +----------+                                                               
        ,|.         |                                                               
       (   )        |                                                               
        `-'      ---|                                                               
      \  |  /       |                                                               
       `.|.'        |                                                               
         |          |                                                               
         x          |                                                               
        / \         |                                                               
       /   \        |                                                               
     ---------------+---''',
    '''                                                                                
         +----------+                                                               
        ,|.         |                                                               
       (   )        |                                                               
        `-'---------|                                                               
      \  |  /       |                                                               
       `.|.'        |                                                               
         |          |
         x          |                                                               
        / \         |                                                               
       /   \        |                                                               
     ---------------+---''',
    '''---GAME OVER---''']

    def letter_placer(guess, letters, template):
        for i in range(len(letters)):
            if letters[i] == guess.upper():
                template[i] = letters[i]
        return template
    print("\n" + " ".join(template))
    while wrong_guesses < (len(hangmans) - 1):
        guess = input("Guess the letter: ").upper() 
        time.sleep(1.0)
        if guess in current_display or guess in other_letters:
            print("Already guessed!")
            time.sleep(1.0)
            continue

        if guess.upper() in answer.upper():
            current_display = letter_placer(guess, letters, template)
            print("\n" + " ".join(current_display))
            time.sleep(1.0)
            print("Great job player!")
            time.sleep(1.0)

            
            if "____" not in current_display:
                print(f"Winner! The word was {answer}")
                time.sleep(1.0)
                game_won == True
        else:
            wrong_guesses += 1
            other_letters.append(guess)
            print("Wrong guess")
            time.sleep(1.0)
            print("\n" + " ".join(current_display))
            time.sleep(1.0)
            print(hangmans[wrong_guesses])
            time.sleep(1.0)
    else:
        ("-- GAME OVER --")







