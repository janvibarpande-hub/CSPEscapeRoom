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
rand_index = random.randint(0, 39)
answer = flower_list[rand_index]
letters = list(answer)
template = len(letters) * "____  "
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
----------------+---''']

def letter_placer():








