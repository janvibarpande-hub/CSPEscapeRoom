import random
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
wrong_guesses = 0
print(letters)

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
'''  -----------|                                 
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
'''  +----------|                                 
     |          |                                 
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
    `-'   ------|                                                               
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
        
    guess = input("Guess the letter: ")

    if guess.upper() in answer.upper():
        current_display = letter_placer(guess, letters, template)
        print(current_display)
        print("Great job player!")
        continue
    else:
        wrong_guesses += 1
        print(current_display)        
        print(hangmans[wrong_guesses])
        print(f"lives remaining: {len(hangmans) - 1 - wrong_guesses}")
        continue

    if "____" not in template:
        print(f"Winner! The word was {answer}")
    break
else:
    ("-- GAME OVER --")







