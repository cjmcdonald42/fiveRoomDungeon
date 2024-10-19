
def characterSheet():
    print(f"""
    Hail, {characterName}, Hero of {worldName}
    Ancestry: {characterAncestry}   Level: {characterLevel}
    Health: {characterHealth}       Speed: {moveSpeed}

    Ability Scores:
        Strength: {attributeSTR}            Intelligence: {attributeINT}
        Constitution: {attributeCON}        Wisdom: {attributeWIS}
        Dexterity: {attributeDEX}           Charisma: {attributeCHA}
    """)

