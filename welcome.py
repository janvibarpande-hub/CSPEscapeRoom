import time
# welcome message by narrator
narrator = ["""Oh, look who’s decided to take the scenic route. How... brave of you.
Welcome, dear traveler, to the woods. It’s a lovely day for a walk to Granny’s house, isn't it?
Just you, your little red hood, and a forest full of things that haven't had breakfast yet.
""",
"""Be warned: this path is not for the faint of heart.
To survive the journey, you must prove your worth through a series of trials.
In each stage of your trek, you will face two distinct challenges.
Only by successfully completing these tasks will you earn the keys necessary to unlock the way forward
""",
"""But do not grow complacent. The forest is unforgiving;
a single lapse in judgment or a failed task will strip you of your progress, forcing you to return to the start of the room to try again.
Precision is your only friend here, as you must collect every key to truly escape the narrative.
""",
"""The stage is set. The wolf has already tucked his napkin into his collar.
The only question left is: are you the master of this story, or just the main course?
Do try to keep your wits about you.
It would be such a shame to have to start all the way back at the beginning... again.
"""]
#for how many different phrases there are
para_count = len(narrator)
#print with time lag btwn
for s in range(para_count):
    print(narrator[s])
    time.sleep(10.0)
