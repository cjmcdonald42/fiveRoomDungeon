"""
    package: fiveRoomDungeon.py
     author: Charles J McDonald «cmcdonald@woonsocketschools.com»
       date: 11/13/2024
    version: 0.1 indev
"""

from random import random
from colorama.ansi import clear_screen

# Player character sheet
playerName = ""
playerAncestry = ""
playerAncestryAdj = ""
playerBackground = ""
playerClass = ""
playerClassName = ""
playerStrength = 0
playerDexterity = 0
playerConstitution = 0
playerIntelligence = 0
playerWisdom = 0
playerCharisma = 0
playerHealth = 0
playerSpeed = 0
playerInititive = 0
playerAttack = 0
hasTorches = False
hasPotion = False

# Introduction to the Game
print('''
Traveling merchants often describe seeing caves in the cliffs south of town as they ride up from the village of
Honeywood. The pass along the shore is the fastest route but those caves are the reason they want to reach the town
gates before dark. The caves exude a dark, foreboding feeling that sends a shiver up one’s spine just thinking about
the dangers that lurk there and one can’t help but notice a stench that makes their pack mules uneasy.
''')
playerName = input("Tell me, brave adventurer, by what name are you known in these lands? : ")

# Character Creation
playerAncestry = input("Will you be a [H]uman, a [D]warf or an [E]lf? : ")

# Create a human character
if playerAncestry == "H":
    print('''
As a human, you get two free Boosts
You can boost your [S]trength, [D]exterity, [C]onstitution, [I]ntelligence, [W]isdom or [Ch]arisma
''')
    playerAncestryAdj = "Human"
    playerSpeed = 25
    playerHealth = 8
    isChoosing = True
    while isChoosing is True:
        playerBoost1 = input("Your first boost is to : ")
        playerBoost2 = input("Your second boost is to : ")
        if playerBoost1 == playerBoost2:
            print("You can't boost the same ability twice")
        else:
            if playerBoost1 == "S" or playerBoost2 == "S":
                playerStrength += 1
            elif playerBoost1 == "D" or playerBoost2 == "D":
                playerDexterity += 1
            elif playerBoost1 == "C" or playerBoost2 == "C":
                playerConstitution += 1
            elif playerBoost1 == "I" or playerBoost2 == "I":
                playerIntelligence += 1
            elif playerBoost1 == "W" or playerBoost2 == "W":
                playerWisdom += 1
            elif playerBoost1 == "Ch" or playerBoost2 == "Ch":
                playerCharisma += 1
            isChoosing = False

# Create a dwarven character
elif playerAncestry == "D":
    playerAncestryAdj = "Dwarven"
    print('''
As a dwarf, you take a penalty to Charisma.
You can boost your Constitution or your Strength and you get one free boost.
[S]trength, [D]exterity, [C]onstitution, [I]ntelligence, [W]isdom or [Ch]arisma

Your Speed is 20 feet per round and you start with 10 Health.
    ''')
    playerBoost1 = input("Would you like to boost your [C]onstitution or your [S]trength? : ")
    playerBoost2 = input("And you get to boost one more attribute: ")
    playerCharisma += -1    # Penalty = -1
    if playerBoost1 == "S" or playerBoost2 == "S":
        playerStrength += 1
    elif playerBoost2 == "D":
        playerDexterity += 1
    elif playerBoost1 == "C" or playerBoost2 == "C":
        playerConstitution += 1
    elif playerBoost2 == "I":
        playerIntelligence += 1
    elif playerBoost2 == "W":
        playerWisdom += 1
    elif playerBoost2 == "Ch":
        playerCharisma += 1
    playerSpeed = 20
    playerHealth = 10

# Create an elven character
elif playerAncestry == "E":
    playerAncestryAdj = "Elven"
    print('''
As an elf, you take a penalty to Strength.
You can boost your Dexterity or your Intelligence and you get one free boost.
[S]trength, [D]exterity, [C]onstitution, [I]ntelligence, [W]isdom or [Ch]arisma

Your Speed is 30 feet per round and you start with 6 Health.
    ''')
    playerBoost1 = input("Would you like to boost your [D]exterity or your [I]ntelligence? : ")
    playerBoost2 = input("And you get to boost one more attribute: ")
    playerStrength += -1  # Penalty = -1
    if playerBoost2 == "S":
        playerStrength += 1
    elif playerBoost1 == "D" or playerBoost2 == "D":
        playerDexterity += 1
    elif playerBoost2 == "C":
        playerConstitution += 1
    elif playerBoost1 == "I" or playerBoost2 == "I":
        playerIntelligence += 1
    elif playerBoost2 == "W":
        playerWisdom += 1
    elif playerBoost2 == "Ch":
        playerCharisma += 1
    playerSpeed = 20
    playerHealth = 10

# Choose a Background
print('''
Who were you before you took up the life or an adventurer?
    [D]eckhand          [S]cholar
    [F]armhand          [W]arrior
    [G]ambler
''')
playerBackground = input("Before this life, I was a: ")
playerBoost2 = input("And you get to choose a free boost: ")
if playerBackground == "D" or playerBoost2 == "D":
    playerDexterity += 1
elif playerBackground == "F" or playerBoost2 == "C":
    playerConstitution += 1
elif playerBackground == "G":
    playerCharisma += 1
elif playerBackground == "S":
    playerCharisma += 1
elif playerBackground == "W" or playerBoost2 == "S":
    playerStrength += 1
elif playerBoost2 == "I":
    playerIntelligence += 1
elif playerBoost2 == "W":
    playerWisdom += 1
elif playerBoost2 == "Ch":
    playerCharisma += 1

# Choose a class
print('''
Your class describes your training and the skills you use to solve problems.
Were you trained as a:
    [F]ighter       [C]leric
    [W]izard        [R]ogue

You also get four free boosts.
''')
playerClass = input("Choose a class: ")
playerBoost1 = input("Choose your first free boost: ")
playerBoost2 = input("Choose your second free boost: ")
playerBoost3 = input("Choose your third free boost: ")
playerBoost4 = input("Choose your fourth free boost: ")

# Four free ability boosts
if playerBoost1 == "S" or playerBoost2 == "S" or playerBoost3 == "S" or playerBoost4 == "S":
    playerStrength += 1
if playerBoost1 == "C" or playerBoost2 == "C" or playerBoost3 == "C" or playerBoost4 == "C":
    playerConstitution += 1
if playerBoost1 == "D" or playerBoost2 == "D" or playerBoost3 == "D" or playerBoost4 == "D":
    playerDexterity += 1
if playerBoost1 == "I" or playerBoost2 == "I" or playerBoost3 == "I" or playerBoost4 == "I":
    playerIntelligence += 1
if playerBoost1 == "W" or playerBoost2 == "W" or playerBoost3 == "W" or playerBoost4 == "W":
    playerWisdom += 1
if playerBoost1 == "Ch" or playerBoost2 == "Ch" or playerBoost3 == "Ch" or playerBoost4 == "Ch":
    playerCharisma += 1

# Each class boosts a key ability score
if playerClass == "F":
    playerClassName = "Fighter"
    playerStrength += 1
    playerAttack = playerStrength
elif playerClass == "W":
    playerClassName = "Wizard"
    playerIntelligence += 1
    playerAttack = playerIntelligence
elif playerClass == "C":
    playerClassName = "Cleric"
    playerWisdom += 1
    playerAttack = playerWisdom
elif playerClass == "R":
    playerClassName = "Rogue"
    playerDexterity += 1
    playerAttack = playerDexterity

# Your initiative is your Wisdom bonus
playerInititive = playerWisdom

def displayCharacterSheet():
    clear_screen()
    print(f'''
== Character Sheet for {playerName} ==
    Level 1 {playerAncestryAdj} {playerClassName}
    Strength: {playerStrength}   Constitution: {playerConstitution}   Dexterity: {playerDexterity}
    Wisdom: {playerWisdom}   Intelligence: {playerIntelligence}   Charisma: {playerCharisma}
    
    Speed: {playerSpeed}    Health: {playerHealth}
    -----
    ''')

displayCharacterSheet()
iAmReadyToBegin = input("Press Enter when you are ready to begin... > ")

# Let's begin our Story
nowInRoom = 1
foe2IsVanquished = False
foe2Health = 6
exploringTheDungeon = True
while exploringTheDungeon is True:
    if nowInRoom == 1:                                          # Enter Room 1
        # Describe the room
        print('''
The cave entrance looms before you, a dark maw set into the rugged hillside. Vines and moss cling to the
rocky edges, and a faint, cool breeze carries the scent of damp earth from within. The shadows inside seem
to shift and beckon, hinting at the mysteries and dangers that lie ahead. You notice a pile of rags in one
corner and the cave continues east into the darkness.
        ''')

        # Offer some options
        print('''
You can [L]eave the dungeon, [S]earch the rags, [E]xamine the vines, or [G]o deeper into the caves.
Type [C] to view your character sheet.
        ''')
        playerAction = input("What would you like to do? : ")
        if playerAction == "L":                                 # Run away!!!
            print('''
The darkening cave light and the wafting stench from ahead paints a grim image of your future.
With a load and stoic "NOPE" you turn and leave the cave.

Perhaps you'll reconsider? 
            ''')
        elif playerAction == "S":                               # Search the rags
            print('''
Searching the rags reveals some torches that can be used to light your way.
You also find a vial of red liquid that seems to glow with an inner holiness.
Drinking this will restore some health!
            ''')
            hasTorches = True
            hasPotion = True

        elif playerAction == "E":                               # Examine the room
            print('''
Cutting back the vines reveals some runic writing painted on the wall along with images
of a large, feathered beast with terrible claws.
            ''')
        elif playerAction == "G":
            nowInRoom = 2
        elif playerAction == "C": displayCharacterSheet()       # Show the character sheet
        else:
            print("That's not a valid option.")

    elif nowInRoom == 2:                                        # Moving into room 2
        # Describe the room
        print("As you cautiously make your way down the narrow east passageway, the air grows colder and the light dims.")
        if foe2IsVanquished is False:
            print('''
Suddenly, you hear the scurrying of tiny feet and the glint of eyes reflecting in the darkness. Before you can react,
a pack of giant rats emerges from the shadows, their teeth bared and eyes gleaming with hunger.
            ''')

        # Offer some options
        print("You can: Use your [T]orch to attempt to ward off the rats", end="")
        if foe2IsVanquished == False:
            print("or [A]ttack the rats.")
        print('''Go back to the [W]est, Travel [E]ast or [S]outh
Type [C] to view your character sheet.
        ''')
        playerAction = input("What would you like to do? : ")

        if playerAction == "T":                                 # brandish your torch
            diceRoll = random.randint(1, 20) + playerStrength   # Roll a d20 and add STR, DC = 15
            print("You brandish your torch, waving the flame in front of the rats to ward them off.")
            if diceRoll >= 12:
                print("The rats are frightened by your intimidating presence, and of course the fire, and scurry away.")
                foeIsVanquished = True
            else:
                print("The rats remain unimpressed by your ineffectual display!")
        elif playerAction == "A":                               # Attack the rats
            diceRoll = random.randint(1, 20) + playerAttack
            if diceRoll >= 12:
                if playerClass == "F":
                    playerDamage = random.randint(1, 8) + 2
                    print(f"You swing your sword and strike the rats, doing {playerDamage}.")
                elif playerClass == "W":
                    playerDamage = random.randint(1, 8) + 2
                    print(f"You cast a magic spell and strike the rats, doing {playerDamage}.")
                elif playerClass == "R":
                    playerDamage = random.randint(1, 4) + random.randint(1, 4)+ 2
                    print(f"You sneak up on the rats and strike, doing {playerDamage}.")
                elif playerClass == "C":
                    playerDamage = random.randint(1, 8) + 2
                    print(f"You call upon your divine will to strike the rats, doing {playerDamage}.")
                foe2Health -= playerDamage
                if foe2Health <= 0:
                    print("The rat swarm is vanquished!")
                    foe2IsVanquished = True
                else:
                    playerHealth -= 2
                    if playerHealth <= 0:
                        print(f"The rats swarm you and do 2 points of damage. You fall down and the world goes dark.")
                    else:
                        print(f"The rats swarm you and do 2 points of damage. You have {playerHealth} left.")
        elif playerAction == "W":                               # describe moving to Room 1
            if foe2IsVanquished is False:
                print("You cannot retreat while in combat with the rats.")
            else:
                nowInRoom = 1
                print("You return from whence you cam heading out of the dungeon")
        elif playerAction == "E":                               # describe moving to Room 3
            if foe2IsVanquished is False:
                print("You cannot retreat while in combat with the rats.")
            else:
                nowInRoom = 3
        elif playerAction == "S":                               # describe moving to Room 4
            if foe2IsVanquished is False:
                print("You cannot retreat while in combat with the rats.")
            else:
                nowInRoom = 4
        elif playerAction == "C": displayCharacterSheet()
        else:
            print("That's not a valid option.")

    elif nowInRoom == 3:                                        # Moving into room 3
        # Describe the room
        print("""Venturing deeper into the cave, you find yourself in a small, unexpected garden oasis.
        The air is filled with the sweet scent of blooming flowers, and a gentle stream trickles nearby.
        Light shines in through a hole in the cave roof. Amidst the lush greenery, a lone skeleton sits propped
        against a stone, its bony fingers tightly clutching an ancient coffer. The scene is eerily serene, yet the
        presence of the skeleton hints at untold stories and hidden dangers.
        """)
        # Offer some options
        print("""You can s[M]ell the flowers, [D]rink from the stream, [E]xamine the skeleton.
        Travel [W]est or [S]outh. [I]nspect the coffer or Type [C] to view your character sheet.
        """)
        playerAction = input("What would you like to do? : ")
        if playerAction == "C": displayCharacterSheet()
        elif playerAction == "S":
            nowInRoom = 5
        elif playerAction == "W":
            nowInRoom = 2
        elif playerAction == "M":
            print("You plant your nose in the flowers and take in a deep breath. Ahhhhh, you exclaim.")
        elif playerAction == "D":
            print("""You bend down and lap some fresh water from the babbling stream.
            Absolutely nothing untoward happens... that you know of...""")
        elif playerAction == "E":
            diceRoll = random.randint(1, 20) + playerWisdom
            if diceRoll >= 8:
                print(f"""You roll {diceRoll} perception.
                Inspecting the skeleton, can tell that this once-adventurer fell to some beast, long forgotten.
                Their body shows signs of quite a struggle that ultimately ended with some very sharp claws.
                """)
            else:
                print("This skeleton has been here for quite some time. I wonder what killed them?")
        elif playerAction == "I":
            print("The coffer is held tightly in the skeleton's grasp... perhaps you could pry it loose?")
            playerAction = input("Sure, let's try to pry it [L]oose: ")
            if playerAction == "L":
                diceRoll = random.randint(1, 20) + playerStrength
                if diceRoll >= 12:
                    print(f"""You roll a {diceRoll}!
With your brutish strength, you pry the coffer from the skeleton's bony hands and easily open it.
The coffer contains 50 pieces of the kings gold coin - more than enough to make this trip a
financial success!""")
                else:
                    print(f"""You roll a {diceRoll}.
Try as you might, you just can't wrest the coffer from the skeleton's grasp.""")

    elif nowInRoom == 4:                                        # Move to Room 4
        # Describe the room
        print(f"""
    Carefully making your way into this next room, you find yourself standing on a precarious, slippery ledge.
    Below, a vast chasm stretches out, its depths shrouded in darkness. The sound of distant water echoes up from
    the abyss, and the ledge beneath your feet feels unstable, threatening to give way at any moment.
        """)
        diceRoll = random.randint(1,20)                         # Make a reflex save or slip over the edge
        if hasTorches == False: diceRoll += -2
        diceRoll = diceRoll + playerDexterity
        if diceRoll >= 12:
            print(f"""You roll a {diceRoll} and make a reflex save!
Although quite perilous, you are sure-footed and make it across the chasm into the next room.
            """)
            nowInRoom = 5                                       # Succeed, move to Room 5
        else:
            print(f"""You roll a {diceRoll} and fail a reflex save.
The precarious ledge is quite slippery and you lose your footing! You slide over the edge and down into
the chasm taking 4 damage""", end = "")
            nowInRoom = 2                                       # Fail, move back to room 2
            playerHealth += -4                                  # And take damage ;)
            if playerHealth <= 0:
                print("and here your adventure ends. Perhaps another, luckier soul will find your loot!")
                exploringTheDungeon = False
            else:
                print(""". At the bottom, you brush yourself off and find a path back up.""")
    elif nowInRoom == 5:                                        # On to the final room!  Woot!!!
        # Describe the room
        print("""As you step into the final room of the dungeon, a foul stench assaults your senses. In the dim light,
    you spot a large, menacing creature lurking in the shadows. Its body is a grotesque fusion of a wolf and a chicken,
    with sharp claws, a beak, and glowing eyes that track your every move. The wolf-chicken lets out a low growl, its
    feathers bristling as it prepares to attack.
        """)
        # Offer some options
        # Show the character sheet
        # Examine the Room
        # Do some stuff

# Epilog