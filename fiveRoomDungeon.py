# Initialize the world
worldName = "Kingdom of Embar"

# Initialize a blank character
characterAncestry = ""
characterBackground = ""
characterClass = ""
attributeSTR = 0
attributeCON = 0
attributeDEX = 0
attributeINT = 0
attributeWIS = 0
attributeCHA = 0
characterHealth = 0
moveSpeed = 0

# Build a new character
characterName = input("What is your name, hero? : ")
characterLevel = 1

# Choose an Ancestry
print(f"""
From which Ancestry does your character descend?
    1: Human
        The Humans of {worldName} are versatile and resourceful.
    2: Elf
        The Elves of {worldName} are skillful and long-lived.
    3: Dwarf
        The Dwarfs of {worldName} are hardy and strong.
""")
ancestryChoice = input("Would you like to be an Elf, a Dwarf, or a Human? : ")

# If you choose Human
if ancestryChoice == "1":
    characterAncestry = "Human"
    moveSpeed = "25"
    health = "8"
    print("""
        You have six ability scores:
        1: Strength        4: Intelligence
        2: Constitution    5: Wisdom
        3: Dexterity       6: Charisma
        
        You may boost any two scores.
        
        """)
    isBoosting = True
    while isBoosting is True:
        abilityChoice1 = input("Pick your first score to boost: ")
        abilityChoice2 = input("Pick your second score to boost: ")
        if abilityChoice1 == abilityChoice2:
            print("You cannot boost the same score twice")
        else:
            # Boost first choice
            if abilityChoice1 == "1":
                attributeSTR += 2
            if abilityChoice1 == "2":
                attributeCON += 2
            if abilityChoice1 == "3":
                attributeDEX += 2
            if abilityChoice1 == "4":
                attributeINT += 2
            if abilityChoice1 == "5":
                attributeWIS += 2
            if abilityChoice1 == "6":
                attributeCHA += 2
            #Boost second choice
            if abilityChoice2 == "1":
                attributeSTR += 2
            if abilityChoice2 == "2":
                attributeCON += 2
            if abilityChoice2 == "3":
                attributeDEX += 2
            if abilityChoice2 == "4":
                attributeINT += 2
            if abilityChoice2 == "5":
                attributeWIS += 2
            if abilityChoice2 == "6":
                attributeCHA += 2
            # Done with the loop
            isBoosting = False

# If you choose Elf
elif ancestryChoice == "2":
    characterAncestry = "Elf"
    moveSpeed = "30"
    health = "6"
    print("""
        You have six ability scores:
        1: Strength        4: Intelligence
        2: Constitution    5: Wisdom
        3: Dexterity       6: Charisma

        You may boost your Dexterity or your Intelligence
        And you may boost one other score of your choice.

        """)
    # First Ability Boost is Dex or Int
    isBoosting = True
    while isBoosting is True:
        abilityChoice1 = input("Would you like to boost your Dexterity or your Intelligence: ")
        if abilityChoice1 == "3" :
            attributeDEX += 2
            isBoosting = False
        elif abilityChoice1 == "4" :
            attributeINT += 2
            isBoosting = False
        else:
            print("You must choose Dexterity or Intelligence")

    # Second Ability Boost is a free
    isBoosting = True
    while isBoosting is True:
        abilityChoice2 = input("Pick your second score to boost: ")
        if abilityChoice2 == "3" or abilityChoice2 == "4":
            print("You cannot boost the same score twice")
        else:
            # Free Boost
            if abilityChoice2 == "1":
                attributeSTR += 2
            if abilityChoice2 == "2":
                attributeCON += 2
            if abilityChoice2 == "5":
                attributeWIS += 2
            if abilityChoice2 == "6":
                attributeCHA += 2
            # Done with the loop
            isBoosting = False

# If you choose Dwarf
elif ancestryChoice == "3":
    characterAncestry = "Dwarf"
    moveSpeed = "20"
    health = "10"
    print("""
        You have six ability scores:
        1: Strength        4: Intelligence
        2: Constitution    5: Wisdom
        3: Dexterity       6: Charisma

        You may boost your Strength or your Constitution
        And you may boost one other score of your choice.

        """)
    # First Ability Boost is Str or Con
    isBoosting = True
    while isBoosting is True:
        abilityChoice1 = input("Would you like to boost your Strength or your Constitution: ")
        if abilityChoice1 == "1" :
            attributeSTR += 2
            isBoosting = False
        elif abilityChoice1 == "2" :
            attributeCON += 2
            isBoosting = False
        else:
            print("You must choose Strength or Constitution")

    # Second Ability Boost is a free
    isBoosting = True
    while isBoosting is True:
        abilityChoice2 = input("Pick your second score to boost: ")
        if abilityChoice2 == "1" or abilityChoice2 == "2":
            print("You cannot boost the same score twice")
        else:
            # Free Boost
            if abilityChoice2 == "3":
                attributeDEX += 2
            if abilityChoice2 == "4":
                attributeINT += 2
            if abilityChoice2 == "5":
                attributeWIS += 2
            if abilityChoice2 == "6":
                attributeCHA += 2
            # Done with the loop
            isBoosting = False
