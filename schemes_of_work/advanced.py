import sys
import os

world = {
    'Garage': ( 
        "A dank and dingy grotto of a garage. You can smell creosote and petrol. It feels oppressive in here. Perhaps it's the smell?",
        {
            "west": "Dining Room",
            "north": "Kitchen", 
        }
    ),
    'Dining Room': (
        "An opulent table is set for 23, but nobody seems to be here... disturbingly, the seats are still warm...",
         {
            "east": "Garage",
            "up": "Landing"
         }
    ),
    'Kitchen': (
        "Still boiling, are thirty steel pans filled with whole cabbages? what are they cooking in here? On second thought, that might not be cabbage...",
         {
            "south": "Garage"  ,
            "down": "Cellar",
            "out": "Garden" 
         }
    ),
    "Landing": (
        "Dirty washing is strewn wantonly all over the top of the stairs, but your attention is caught by a thin film of blood over the handrail...",
        {
            "down": "Dining Room",
            "west": "Bedroom",
        }
    ),
    "Bedroom": (
        "Congratulations, you've found the treasure! You haz l33t skillz.",
        {
        }
    ),
    
    "Cellar": (
        "What are those over there in the corner?",
        {
            "up": "Kitchen",
            "east": "Library"
        }
    ),
    "Garden": (
        "A quagmire of tar bubbles around your feet. DEATH surrounds you. The birds are singing.",
        {
            "in": "Kitchen"
        }
    ),
    "Library": (
        "The walls are replete with books arranged from floor to ceiling on solid oak book shelves. There's even a ladder. And a comfy chair and pipe. An old pair of slippers lie beside the armchair. Apart from all of the zombies the place is perfectly restful.",
        { 
            "west": "Cellar"
        }
        )
}

current_room = 'Garage'

while True:
    os.system('clear')
    room = world[current_room]
    print("You are in the %s\n%s\n" % (current_room, room[0]))
    directions = room[1].keys()
    if not directions:
        sys.exit(0)
    direction = None
    while direction not in directions:
       direction = raw_input("Where to next guv'nor %s? " % directions).lower().strip()
       if direction in directions:
            current_room = room[1][direction]
            break
       else:
            print "I can't go that way guv'nor... try again"
			
