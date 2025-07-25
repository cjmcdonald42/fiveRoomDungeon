'''
      package:  fiveRoomDungeon.py
       author:  Charles J McDonald «github.com/cjmcdonald42»
         date:  2024.12.01
      version:  1.0 β
     maturity:  Beta, ready for public testing
'''

import random
from colorama.ansi import clear_screen, Fore, Style

# Player character sheet
playerName = ''
playerAncestry = ''
playerAncestryAdj = ''
playerBackground = ''
playerBackgroundName = ''
playerClass = ''
playerClassName = ''
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

def displayCharacterSheet():
    '''
    Display the character sheet
    '''

    clear_screen()
    print(f'''
{Fore.GREEN} == {Style.RESET_ALL}Character Sheet for {playerName} {Fore.GREEN} == {Style.RESET_ALL}
    Level 1 {playerAncestryAdj} {playerClassName}
    Background: {Fore.GREEN}{playerBackgroundName}{Style.RESET_ALL}
    Strength: {Fore.GREEN}{playerStrength}{Style.RESET_ALL}   Constitution: {Fore.GREEN}{playerConstitution}{Style.RESET_ALL}   Dexterity: {Fore.GREEN}{playerDexterity}{Style.RESET_ALL}
    Wisdom: {Fore.GREEN}{playerWisdom}{Style.RESET_ALL}     Intelligence: {Fore.GREEN}{playerIntelligence}{Style.RESET_ALL}   Charisma: {Fore.GREEN}{playerCharisma}{Style.RESET_ALL}

    Initiative: {Fore.GREEN}{playerInititive}{Style.RESET_ALL}   Speed: {Fore.GREEN}{playerSpeed}{Style.RESET_ALL}    Health: {Fore.GREEN}{playerHealth}{Style.RESET_ALL}
    -----''')

# Introduction to the Game
print(f''' {Style.RESET_ALL}
=== Welcome to the Foulfest Caves! ===
Traveling merchants often describe seeing caves in the cliffs south of town as they ride up from the village of
Honeywood. The pass along the shore is the fastest route but those caves are the reason they want to reach the town
gates before dark. The caves exude a dark, foreboding feeling that sends a shiver up one’s spine just thinking about
the dangers that lurk there and one can’t help but notice a stench that makes their pack mules uneasy.
''')
playerName = input("Tell me, brave adventurer, by what name are'st thou known in these lands? : ")

# Character Creation
playerAncestry = input(f"Be ye [{Fore.YELLOW}H{Style.RESET_ALL}{Style.RESET_ALL}]uman, a [{Fore.YELLOW}D{Style.RESET_ALL}{Style.RESET_ALL}]warf or an [{Fore.YELLOW}E{Style.RESET_ALL}{Style.RESET_ALL}]lf? : ").lower()

# Create a human character
if playerAncestry == "h":
    print(f'''
As a human, ye get two free Boosts
You can boost your [{Fore.YELLOW}S{Style.RESET_ALL}]trength, [{Fore.YELLOW}D{Style.RESET_ALL}]exterity, [{Fore.YELLOW}C{Style.RESET_ALL}]onstitution, [{Fore.YELLOW}I{Style.RESET_ALL}]ntelligence, [{Fore.YELLOW}W{Style.RESET_ALL}]isdom or [{Fore.YELLOW}Ch{Style.RESET_ALL}]arisma''')
    playerAncestryAdj = "Human"
    playerSpeed = 25
    playerHealth = 8
    isChoosing = True
    while isChoosing is True:
        playerBoost1 = input("Your first boost is to : ").lower()
        playerBoost2 = input("Your second boost is to : ").lower()
        if playerBoost1 == playerBoost2:
            print("You can't boost the same ability twice")
        else:
            if playerBoost1 == "s" or playerBoost2 == "s": playerStrength += 1
            if playerBoost1 == "d" or playerBoost2 == "d": playerDexterity += 1
            if playerBoost1 == "c" or playerBoost2 == "c": playerConstitution += 1
            if playerBoost1 == "i" or playerBoost2 == "i": playerIntelligence += 1
            if playerBoost1 == "w" or playerBoost2 == "w": playerWisdom += 1
            if playerBoost1 == "ch" or playerBoost2 == "ch": playerCharisma += 1
            isChoosing = False

# Create a dwarven character
elif playerAncestry == "d":
    playerAncestryAdj = "Dwarven"
    print(f'''
As a dwarf, you take a penalty to Charisma.
You can boost your Constitution or your Strength and you get one free boost.
[{Fore.YELLOW}S{Style.RESET_ALL}]trength, [{Fore.YELLOW}D{Style.RESET_ALL}]exterity, [{Fore.YELLOW}C{Style.RESET_ALL}]onstitution, [{Fore.YELLOW}I{Style.RESET_ALL}]ntelligence, [{Fore.YELLOW}W{Style.RESET_ALL}]isdom or [{Fore.YELLOW}Ch{Style.RESET_ALL}]arisma

Your Speed is 20 feet per round and you start with 10 Health.''')
    playerBoost1 = input(f"Would you like to boost your [{Fore.YELLOW}C{Style.RESET_ALL}]onstitution or your [{Fore.YELLOW}S{Style.RESET_ALL}]trength? : ").lower()
    playerBoost2 = input("And ye get to boost one more attributes: ").lower()
    playerCharisma += -1    # Penalty = -1
    if playerBoost1 == "s" or playerBoost2 == "s": playerStrength += 1
    if playerBoost2 == "d": playerDexterity += 1
    if playerBoost1 == "c" or playerBoost2 == "c": playerConstitution += 1
    if playerBoost2 == "i": playerIntelligence += 1
    if playerBoost2 == "w": playerWisdom += 1
    if playerBoost2 == "ch": playerCharisma += 1
    playerSpeed = 20
    playerHealth = 10

# Create an elven character
elif playerAncestry == "e":
    playerAncestryAdj = "Elven"
    print(f'''
As an elf, you take a penalty to Strength.
You can boost your Dexterity or your Intelligence and you get one free boost.
[{Fore.YELLOW}S{Style.RESET_ALL}]trength, [{Fore.YELLOW}D{Style.RESET_ALL}]exterity, [{Fore.YELLOW}C{Style.RESET_ALL}]onstitution, [{Fore.YELLOW}I{Style.RESET_ALL}]ntelligence, [{Fore.YELLOW}W{Style.RESET_ALL}]isdom or [{Fore.YELLOW}Ch{Style.RESET_ALL}]arisma

Your Speed is 30 feet per round and you start with 6 Health.''')
    playerBoost1 = input(f"Would you like to boost your [{Fore.YELLOW}D{Style.RESET_ALL}]exterity or your [{Fore.YELLOW}I{Style.RESET_ALL}]ntelligence? : ").lower()
    playerBoost2 = input("And you get to boost one more attribute: ").lower()
    playerStrength += -1  # Penalty = -1
    if playerBoost2 == "s": playerStrength += 1
    if playerBoost1 == "d" or playerBoost2 == "d": playerDexterity += 1
    if playerBoost2 == "c": playerConstitution += 1
    if playerBoost1 == "i" or playerBoost2 == "i": playerIntelligence += 1
    if playerBoost2 == "w": playerWisdom += 1
    if playerBoost2 == "ch": playerCharisma += 1
    playerSpeed = 20
    playerHealth = 10

# Choose a Background
print(f'''
Who were ye before ye took up the life or an adventurer?
    [{Fore.YELLOW}D{Style.RESET_ALL}]eckhand          [{Fore.YELLOW}S{Style.RESET_ALL}]cholar
    [{Fore.YELLOW}F{Style.RESET_ALL}]armhand          [{Fore.YELLOW}W{Style.RESET_ALL}]arrior
    [{Fore.YELLOW}G{Style.RESET_ALL}]ambler''')
playerBackground = input("Before this life, I was a: ").lower()
if playerBackground == "d": playerBackgroundName = "Deckhand"       # Full name of background for character sheet
elif playerBackground == "f": playerBackgroundName = "Farmhand"
elif playerBackground == "g": playerBackgroundName = "Gambler"
elif playerBackground == "s": playerBackgroundName = "Scholar"
elif playerBackground == "w": playerBackgroundName = "Warrior"

playerBoost2 = input("And you get to choose a free boost: ").lower()
if playerBackground == "d" or playerBoost2 == "d": playerDexterity += 1
if playerBackground == "f" or playerBoost2 == "c": playerConstitution += 1
if playerBackground == "g": playerCharisma += 1
if playerBackground == "s": playerCharisma += 1
if playerBackground == "w" or playerBoost2 == "s": playerStrength += 1
if playerBoost2 == "i": playerIntelligence += 1
if playerBoost2 == "w": playerWisdom += 1
if playerBoost2 == "ch": playerCharisma += 1

# Choose a class
print(f'''
Your class describes your training and the skills you use to solve problems.
Were ye trained as a:
    [{Fore.YELLOW}F{Style.RESET_ALL}]ighter       [{Fore.YELLOW}C{Style.RESET_ALL}]leric
    [{Fore.YELLOW}W{Style.RESET_ALL}]izard        [{Fore.YELLOW}R{Style.RESET_ALL}]ogue

You also get four free boosts.''')
playerClass = input("Choose a class: ").lower()
playerBoost1 = input("Choose your first free boost: ").lower()
playerBoost2 = input("Choose your second free boost: ").lower()
playerBoost3 = input("Choose your third free boost: ").lower()
playerBoost4 = input("Choose your fourth free boost: ").lower()

# Four free ability boosts
if playerBoost1 == "s" or playerBoost2 == "s" or playerBoost3 == "s" or playerBoost4 == "s": playerStrength += 1
if playerBoost1 == "c" or playerBoost2 == "c" or playerBoost3 == "c" or playerBoost4 == "c": playerConstitution += 1
if playerBoost1 == "d" or playerBoost2 == "d" or playerBoost3 == "d" or playerBoost4 == "d": playerDexterity += 1
if playerBoost1 == "i" or playerBoost2 == "i" or playerBoost3 == "i" or playerBoost4 == "i": playerIntelligence += 1
if playerBoost1 == "w" or playerBoost2 == "w" or playerBoost3 == "w" or playerBoost4 == "w": playerWisdom += 1
if playerBoost1 == "ch" or playerBoost2 == "ch" or playerBoost3 == "ch" or playerBoost4 == "ch": playerCharisma += 1

# Each class boosts a key ability score
if playerClass == "f":
    playerClassName = "Fighter"
    playerStrength += 1
    playerAttack = playerStrength
elif playerClass == "w":
    playerClassName = "Wizard"
    playerIntelligence += 1
    playerAttack = playerIntelligence
elif playerClass == "c":
    playerClassName = "Cleric"
    playerWisdom += 1
    playerAttack = playerWisdom
elif playerClass == "r":
    playerClassName = "Rogue"
    playerDexterity += 1
    playerAttack = playerDexterity

# Your initiative is your Wisdom bonus
playerInititive = playerWisdom

clear_screen()
print("So, let's now look at your character sheet.")
displayCharacterSheet()
iAmReadyToBegin = input("Press Enter when you are ready to begin... > ")    # This is a throw-away variable
clear_screen()

# Let's begin our Story
nowInRoom = 1
foe2IsVanquished = False                                        # Set up for foe health tracking
foe2Health = 6
foe5IsVanquished = False
foe5Health = 12
exploringTheDungeon = True
triedThisAlready = False                                        # Room 2, use torches
while exploringTheDungeon is True:
    if nowInRoom == 1:                                          # Enter Room 1
        clear_screen()
        # Describe the room
        print('''
=== Welcome to the Foulfest Caves ===
The cave entrance looms before you, a dark maw set into the rugged hillside. Vines and moss cling to the
rocky edges, and a faint, cool breeze carries the scent of damp earth from within. The shadows inside seem
to shift and beckon, hinting at the mysteries and dangers that lie ahead. You notice a pile of rags in one
corner and the cave continues east into the darkness.''')

        # Offer some options
        print(f'''
You can [{Fore.YELLOW}L{Style.RESET_ALL}]eave the dungeon, [{Fore.YELLOW}S{Style.RESET_ALL}]earch the rags, [{Fore.YELLOW}E{Style.RESET_ALL}]xamine the vines, or [{Fore.YELLOW}G{Style.RESET_ALL}]o deeper into the caves.
Type [{Fore.YELLOW}C{Style.RESET_ALL}] to view your character sheet.''')
        playerAction = input("What would you like to do? : ").lower()
        if playerAction == "l":                                 # Run away!!!
            print('''
The darkening cave light and the wafting stench from ahead paints a grim image of your future.
With a load and stoic "NOPE" you turn and leave the cave.

Perhaps you'll reconsider?''')
        elif playerAction == "s":                               # Search the rags
            print('''
Searching the rags reveals some torches that can be used to light your way.
You also find a vial of red liquid that seems to glow with an inner holiness.
Drinking this will restore some health!''')
            hasTorches = True
            hasPotion = True

        elif playerAction == "e":                               # Examine the room
            print('''
Cutting back the vines reveals some runic writing painted on the wall along with images
of a large, feathered beast with terrible claws.''')

        elif playerAction == "g": nowInRoom = 2
        elif playerAction == "c": displayCharacterSheet()       # Show the character sheet
        else: print("That's not a valid option.")

    elif nowInRoom == 2:                                        # Moving into room 2
        clear_screen()
        # Describe the room
        print("As you cautiously make your way down the narrow east passageway, the air grows colder and the light dims.")
        if hasTorches is True:
            print("The light from your torch illuminates the small chamber ahead.")
        if foe2IsVanquished is False:
            print('''
Suddenly, you hear the scurrying of tiny feet and the glint of eyes reflecting in the darkness. Before you can react,
a pack of giant rats emerges from the shadows, their teeth bared and eyes gleaming with hunger.''')

        # Offer some options
        print("\nYou can: ", end='')
        if foe2IsVanquished is False:
            if triedThisAlready is False:
                print(f"Use your [{Fore.YELLOW}T{Style.RESET_ALL}]orch to attempt to ward off the rats or", end=' ')
            print(f"[{Fore.YELLOW}A{Style.RESET_ALL}]ttack the rats.")
        print(f'''Go back to the [{Fore.YELLOW}W{Style.RESET_ALL}]est, Travel [{Fore.YELLOW}E{Style.RESET_ALL}]ast or [{Fore.YELLOW}S{Style.RESET_ALL}]outh.
Type [{Fore.YELLOW}C{Style.RESET_ALL}] to view your character sheet.''')
        playerAction = input("What would you like to do? : ").lower()

        if playerAction == "t":                                 # brandish your torch
            if hasTorches is True:                              # Did you pick up the torches in room 1?
                if triedThisAlready is False:
                    diceRoll = random.randint(1, 20) + playerStrength   # Roll a d20 and add STR, DC = 15
                    print("You brandish your torch, waving the flame in front of the rats to ward them off.")
                    if diceRoll >= 12:
                        print(f"You roll a {diceRoll} and frighten the rats with your intimidating presence, and of course the fire. They scurry away.")
                        foe2IsVanquished = True
                    else:
                        print("The rats remain unimpressed by your ineffectual display!")
                    triedThisAlready = True                         # Can only try this once
                else:
                    print("You've already tried to scare the rats away with your torch.")
            else:
                print("If only you had some torches...")

        elif playerAction == "a":                                   # Attack the rats
            playerDiceRoll = random.randint(1, 20) + playerInititive      # roll initiative
            if hasTorches is False: playerDiceRoll -= 2             # Penalty for no torches
            creatureDiceRoll = random.randint(1, 20)
            if playerDiceRoll >= creatureDiceRoll:                  # Player attacks first
                print("You have the initiative and attack the rats first.")
                diceRoll = random.randint(1, 20) + playerAttack
                if diceRoll >= 12:
                    if playerClass == "f":
                        playerDamage = random.randint(1, 8) + 2
                        print(f"You swing your sword and strike the rats, doing {playerDamage}.")
                    elif playerClass == "w":
                        playerDamage = random.randint(1, 8) + 2
                        print(f"You cast a magic spell and strike the rats, doing {playerDamage}.")
                    elif playerClass == "r":
                        playerDamage = random.randint(1, 4) + random.randint(1, 4) + 2
                        print(f"You sneak up on the rats and strike, doing {playerDamage}.")
                    elif playerClass == "c":
                        playerDamage = random.randint(1, 8) + 2
                        print(f"You call upon your divine will to strike the rats, doing {playerDamage}.")
                    foe2Health -= playerDamage
                else:
                    print("Your attack misses. The rats go into a fighting frenzy!")
                if foe2Health <= 0:
                    print("The rat swarm is vanquished!")
                    foe2IsVanquished = True
                else:
                    playerHealth -= 2
                    if playerHealth <= 0:
                        print("The rats swarm you and do 2 points of damage. You fall down and the world goes dark.")
                        exploringTheDungeon = False
                    else:
                        print(f"The rats swarm you and do 2 points of damage. You have {playerHealth} left.")
            else:                                                   # Rats attack first
                print("The rats have the initiative and they attack.")
                playerHealth -= 2
                if playerHealth <= 0:
                    print("The rats swarm you and do 2 points of damage. You fall down and the world goes dark.")
                    exploringTheDungeon = False
                else:
                    print(f"The rats swarm you and do 2 points of damage. You have {playerHealth} left.")
                    diceRoll = random.randint(1, 20) + playerAttack
                    if hasTorches is False: diceRoll += -2    # Penalty for no torches
                    if diceRoll >= 12:
                        if playerClass == "f":
                            playerDamage = random.randint(1, 8) + 2
                            print(f"You swing your sword and strike the rats, doing {playerDamage}.")
                        elif playerClass == "w":
                            playerDamage = random.randint(1, 8) + 2
                            print(f"You cast a magic spell and strike the rats, doing {playerDamage}.")
                        elif playerClass == "r":
                            playerDamage = random.randint(1, 4) + random.randint(1, 4) + 2
                            print(f"You sneak up on the rats and strike, doing {playerDamage}.")
                        elif playerClass == "c":
                            playerDamage = random.randint(1, 8) + 2
                            print(f"You call upon your divine will to strike the rats, doing {playerDamage}.")
                        foe2Health -= playerDamage
                        if foe2Health <= 0:
                            print("The rat swarm is vanquished!")
                            foe2IsVanquished = True
                    else:
                        print("Your attack misses. The rats go into a fighting frenzy!")

        elif playerAction == "w":                               # describe moving to Room 1
            if foe2IsVanquished is False:
                print("You cannot retreat while in combat with the rats.")
            else:
                nowInRoom = 1
                print("You return from whence you cam heading out of the dungeon")
        elif playerAction == "e":                               # describe moving to Room 3
            if foe2IsVanquished is False:
                print("You cannot retreat while in combat with the rats.")
            else:
                nowInRoom = 3
        elif playerAction == "s":                               # describe moving to Room 4
            if foe2IsVanquished is False:
                print("You cannot retreat while in combat with the rats.")
            else:
                nowInRoom = 4
        elif playerAction == "c": displayCharacterSheet()
        else:
            print("That's not a valid option.")

    elif nowInRoom == 3:                                        # Moving into room 3
        clear_screen()
        # Describe the room
        print('''
Venturing deeper into the cave, you find yourself in a small, unexpected garden oasis.
The air is filled with the sweet scent of blooming flowers, and a gentle stream trickles nearby.
Light shines in through a hole in the cave roof. Amidst the lush greenery, a lone skeleton sits propped
against a stone, its bony fingers tightly clutching an ancient coffer. The scene is eerily serene, yet the
presence of the skeleton hints at untold stories and hidden dangers.''')

        # Offer some options
        print(f'''
You can s[{Fore.YELLOW}M{Style.RESET_ALL}]ell the flowers, [{Fore.YELLOW}D{Style.RESET_ALL}]rink from the stream, [{Fore.YELLOW}E{Style.RESET_ALL}]xamine the skeleton.
Travel [{Fore.YELLOW}W{Style.RESET_ALL}]est or [{Fore.YELLOW}S{Style.RESET_ALL}]outh. [{Fore.YELLOW}I{Style.RESET_ALL}]nspect the coffer or Type [{Fore.YELLOW}C{Style.RESET_ALL}] to view your character sheet.''')
        playerAction = input("What would you like to do? : ").lower()
        if playerAction == "c": displayCharacterSheet()
        elif playerAction == "s": nowInRoom = 5
        elif playerAction == "w": nowInRoom = 2
        elif playerAction == "m":
            print("You plant your nose in the flowers and take in a deep breath. Ahhhhh, you exclaim.")
        elif playerAction == "d":
            print('''
You bend down and lap some fresh water from the babbling stream.
Absolutely nothing untoward happens... that you know of...''')
        elif playerAction == "e":
            diceRoll = random.randint(1, 20) + playerWisdom
            if diceRoll >= 8:
                print(f'''
You roll {diceRoll} perception.
Inspecting the skeleton, can tell that this once-adventurer fell to some beast, long forgotten.
Their body shows signs of quite a struggle that ultimately ended with some very sharp claws.''')
            else:
                print("This skeleton has been here for quite some time. I wonder what killed them?")
        elif playerAction == "i":
            print("The coffer is held tightly in the skeleton's grasp... perhaps you could pry it loose?")
            playerAction = input(f"Sure, let's try to pry it [{Fore.YELLOW}L{Style.RESET_ALL}]oose: ").lower()
            if playerAction == "l":
                diceRoll = random.randint(1, 20) + playerStrength
                if diceRoll >= 12:
                    print(f'''
You roll a {diceRoll}!
With your brutish strength, you pry the coffer from the skeleton\'s bony hands and easily open it.
The coffer contains 50 pieces of the kings gold coin - more than enough to make this trip a
financial success!''')
                else:
                    print(f'''
You roll a {diceRoll}.
Try as you might, you just can't wrest the coffer from the skeleton's grasp.''')

    elif nowInRoom == 4:                                        # Move to Room 4
        # Describe the room
        print('''
Carefully making your way into this next room, you find yourself standing on a precarious, slippery ledge.
Below, a vast chasm stretches out, its depths shrouded in darkness. The sound of distant water echoes up from
the abyss, and the ledge beneath your feet feels unstable, threatening to give way at any moment.''')

        diceRoll = random.randint(1,20)                # Make a reflex save or slip over the edge
        if hasTorches is False: diceRoll += -2              # Penalty for no torches
        diceRoll += playerDexterity                         # Add DEX to the roll
        if diceRoll >= 12:
            print(f'''
You roll a {diceRoll} and make a reflex save!
Although quite perilous, you are sure-footed and make it across the chasm into the next room.''')
            nowInRoom = 5                                   # Succeed, move to Room 5
        else:
            print(f'''
You roll a {diceRoll} and fail a reflex save.
The precarious ledge is quite slippery and you lose your footing! You slide over the edge and down into
the chasm taking 4 damage''', end = '')
            nowInRoom = 2                                   # Fail, move back to room 2
            playerHealth += -4                              # And take damage ;)
            if playerHealth <= 0:
                print("and here your adventure ends. Perhaps another, luckier soul will find your loot!")
                exploringTheDungeon = False
            else:
                print('''. At the bottom, you brush yourself off and find a path back up.''')
    elif nowInRoom == 5:                                    # On to the final room!  Woot!!!
        # Describe the room
        print('''
As you step into the final room of the dungeon, a foul stench assaults your senses. In the dim light,
you spot a large, menacing creature lurking in the shadows. Its body is a grotesque fusion of a wolf and a chicken,
with sharp claws, a beak, and glowing eyes that track your every move. The Foulfur lets out a low growl, its
feathers bristling as it prepares to attack.''')
        isEngagedWithTheFoulfur = True
        while isEngagedWithTheFoulfur is True:              # Offer some options
            print(f'''
You can [{Fore.YELLOW}A{Style.RESET_ALL}]ttack the Foulfur, [{Fore.YELLOW}R{Style.RESET_ALL}]un away, [{Fore.YELLOW}S{Style.RESET_ALL}]peak with the creature, [{Fore.YELLOW}D{Style.RESET_ALL}]rink the health potion,
[{Fore.YELLOW}U{Style.RESET_ALL}]se your torch to intimidate the FoulFur, or [{Fore.YELLOW}C{Style.RESET_ALL}] to view your character sheet.''')
            playerAction = input("What would you like to do? : ").lower()
            if playerAction == "c":                         # Show the character sheet
                displayCharacterSheet()
            elif playerAction == "d":                       # Drink the health potion
                if hasPotion is True:
                    playerHealth += 8
                    print(f"You drink the potion and feel invigorated. You now have {playerHealth} health.")
                    hasPotion = False
                else:
                    print("You don't have a potion to drink.")
            elif playerAction == "a":                               # Attack
                playerDiceRoll = random.randint(1, 20) + playerInititive  # roll initiative
                if hasTorches is False: playerDiceRoll -= 2         # Penalty for no torches
                creatureDiceRoll = random.randint(1, 20)
                diceRoll = random.randint(1, 20) + playerAttack     # Player's Attack Roll
                if hasTorches is False: diceRoll += -2              # Penalty for no torches
                creatureDamage = random.randint(1, 4)         # Creature's Damage Roll
                if playerDiceRoll >= creatureDiceRoll:              # Player attacks first
                    if diceRoll >= 12:
                        if playerClass == "f":
                            playerDamage = random.randint(1, 8) + 2
                            print(f"You swing your sword and strike the Foulfur, doing {playerDamage}.")
                        elif playerClass == "w":
                            playerDamage = random.randint(1, 8) + 2
                            print(f"You cast a magic spell and strike the Foulfur, doing {playerDamage}.")
                        elif playerClass == "r":
                            playerDamage = random.randint(1, 4) + random.randint(1, 4)+ 2
                            print(f"You sneak up on the Foulfur and strike, doing {playerDamage}.")
                        elif playerClass == "c":
                            playerDamage = random.randint(1, 8) + 2
                            print(f"You call upon your divine will to strike the Foulfur, doing {playerDamage}.")
                        foe5Health -= playerDamage
                    else:
                        print("Argh! Your attack misses, doing no damage to the Foulfur.")
                    if foe5Health <= 0:
                        print("The Foulfur is vanquished!")
                        print('''
As the beast collapses, you notice a modest trove of treasure amongst her belongings.
You find 50 gold coins and a sword that bristles with a magical aura.''')
                        isEngagedWithTheFoulfur = False
                        exploringTheDungeon = False
                    else:
                        playerHealth -= creatureDamage
                        if playerHealth <= 0:
                            print(f"The Foulfur strikes you doing {creatureDamage} points of damage. You fall down and the world goes dark.")
                            exploringTheDungeon = False
                        else:
                            print(f"The Foulfur strikes you doing {creatureDamage} points of damage. You have {playerHealth} left.")
                else:                                               # Foulfur attacks first
                    playerHealth -= creatureDamage
                    if playerHealth <= 0:
                        print(f"The Foulfur strikes you doing {creatureDamage} points of damage. You fall down and the world goes dark.")
                        exploringTheDungeon = False
                    else:
                        print(f"The Foulfur strikes you doing {creatureDamage} points of damage. You have {playerHealth} left.")
                        if diceRoll >= 12:
                            if playerClass == "f":
                                playerDamage = random.randint(1, 8) + 2
                                print(f"You swing your sword and strike the Foulfur, doing {playerDamage}.")
                            elif playerClass == "w":
                                playerDamage = random.randint(1, 8) + 2
                                print(f"You cast a magic spell and strike the Foulfur, doing {playerDamage}.")
                            elif playerClass == "r":
                                playerDamage = random.randint(1, 4) + random.randint(1, 4) + 2
                                print(f"You sneak up on the Foulfur and strike, doing {playerDamage}.")
                            elif playerClass == "c":
                                playerDamage = random.randint(1, 8) + 2
                                print(f"You call upon your divine will to strike the Foulfur, doing {playerDamage}.")
                            else:
                                playerDamage = 0
                                print("Argh! Your attack misses, doing no damage to the Foulfur.")
                            foe5Health -= playerDamage
                        if foe5Health <= 0:
                            print("The Foulfur is vanquished!")
                            print('''
As the beast collapses, you notice a modest trove of treasure amongst her belongings.
You find 50 gold coins and a sword that bristles with a magical aura.''')
                            isEngagedWithTheFoulfur = False
                            exploringTheDungeon = False
            elif playerAction == "r":                       # Run away
                if foe5Health >= 6:
                    playerHealth += -1
                    print("The Foulfur is too quick and catches you before you can escape.")
                    print(f"You take 1 point of damage as the beast swings at you. You have {playerHealth} left.")
                else:
                    print("You manage to escape the Foulfur by running to the North.")
                    isEngagedWithTheFoulfur = False
                    nowInRoom = 3
            elif playerAction == "s":                       # Speak with the creature
                diceRoll = random.randint(1, 20) + playerIntelligence
                if diceRoll >= 16:
                    print('''
You mimic the Foulfur's guttural barks and feather motions attempting to speak with her.
The Foulfur seems to understand and tells you that she is a guardian of the cave and, seeing
that you are not a threat, allows you to pass down a tunnel to the east.
The Foulfur offers you 10 gold pieces and a shiny magic sword as a reward for your bravery.''')
                    isEngagedWithTheFoulfur = False
                    exploringTheDungeon = False
                else:
                    playerHealth += -1
                    print(f'''
You merely anger the Foulfur who takes a swipe at you with her powerful tail
doing 1 point of damage. You have {playerHealth} left.''')
            elif playerAction == "u":                       # Use the torch
                diceRoll = random.randint(1, 20) + playerCharisma
                if diceRoll >= 14:
                    print(f'''
You roll a {diceRoll} and brandish your torch at the Foulfur.
The beast is frightened by the fire and backs away, allowing you to pass to the east.''')
                    isEngagedWithTheFoulfur = False
                    exploringTheDungeon = False
                else:
                    playerHealth += -1
                    print(f'''
You roll a {diceRoll} and brandish your torch at the Foulfur.
The beast is not impressed and takes a swipe at you with her powerful tail
doing 1 point of damage. You have {playerHealth} left.''')
            else:
                print("That's not a valid option.")

# End of while exploringTheDungeon
print('''
You head east down a narrow tunnel and see light up ahead. As you emerge from the cave, you find yourself
in a clearing on the edge of a dense forest. The sun is setting, casting long shadows across the landscape.
The dungeon is behind you and glory awaits your return to the village of Honeywood.

Congratulations!
    You have successfully navigated the Five Room Dungeon!''')

# Roll credits
