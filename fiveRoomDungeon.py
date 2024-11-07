#    package: fiveRoomDungeon.py
#     author: Charles J McDonald «cmcdonald@woonsocketschools.com»
#       date: 11/07/2024
#    version: 0.1 indev
from colorama.ansi import clear_screen

# Player character sheet
playerName = ""
playerAncestry = ""
playerAncestryAdj = ""
playerBackground = ""
playerClass = ""
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
print("You awaken in a strange land. So far away and yet so long ago...")
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
    playerStrength += 1
    playerAttack = playerStrength
elif playerClass == "W":
    playerIntelligence += 1
    playerAttack = playerIntelligence
elif playerClass == "C":
    playerWisdom += 1
    playerAttack = playerWisdom
elif playerClass == "R":
    playerDexterity += 1
    playerAttack = playerDexterity

# Your initiative is your Wisdom bonus
playerInititive = playerWisdom

def displayCharacterSheet():
    os.system(clear_screen())
    print(f'''
    == Character Sheet for {playerName} ==
        Level 1 {playerAncestryAdj} {playerClass}
        Strength: {playerStrength}   Constitution: {playerConstitution}   Dexterity: {playerDexterity}
        Wisdom: {playerWisdom}   Intelligence: {playerIntelligence}   Charisma: {playerCharisma}
        
        Speed: {playerSpeed}    Health: {playerHealth}
    ----- \n    
    ''')


# Let's begin our Story
print('''                # TODO Write some stuff here...

''')

nowInRoom = 1
exploringTheDungeon = True
while exploringTheDungeon is True:
    if nowInRoom == 1:
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
            print('''
            Go east to room 2
            ''')
            nowInRoom = 2
        elif playerAction == "C": displayCharacterSheet()       # Show the character sheet
        else:
            print("That's not a valid option.")


            # Examine the Room
            # Do some shit
    elif nowInRoom == 2:
        # Describe the room
        # Offer some options
        # Show the character sheet
        # Examine the Room
        # Do some shit
    elif nowInRoom == 3:
        # Describe the room
        # Offer some options
        # Show the character sheet
        # Examine the Room
        # Do some shit
    elif nowInRoom == 4:
        # Describe the room
        # Offer some options
        # Show the character sheet
        # Examine the Room
        # Do some shit
    elif nowInRoom == 5:
        # Describe the room
        # Offer some options
        # Show the character sheet
        # Examine the Room
        # Do some shit


    # Room 1



# Room 2

# Room 3

# Room 4

# Room 5

# Epilog