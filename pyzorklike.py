#more important:
#add in an invalid response function if the responses from the user were different than the options given.
#add inventory space, where you can hold only 5 items without a backpack, and 10 items with the backpack.
#pick a random day (1-10) to have a checkpoint village where you can buy better gear
#have a save point system for every checkpoint village so its not completely rougelike lmfao
#more difficult monsters to make up for the user getting better gear
#bosses.... hehehha

#extra:
#adding crit to every monster would be reaallly funny and evil but i would have to write 2 variations of the same move like i did with the player and i don't think ill be able to make that reasonably happen in a time crunch scenario like right now

import os

score = 200

DaggerPrice = 35
IronShortSwordPrice = 60
WoodenBowPrice = 45

SmallBackpackPrice = 30
ImportedLeatherPrice = 55
ImportedIronArmorPrice = 100

LesserHealingPotionPrice = 10
LesserAntidotePrice = 8

listOfLowLevelMonsters = ['Goblin', 'Goblin', 'Goblin', 'Goblin', 'Goblin', 'Goblin', 'Goblin', 'Goblin', 'Goblin', 'Goblin', 'Goblin', 'Goblin', 'Orc', 'Orc', 'Orc', 'Orc', 'Orc', 'Orc', 'Orc', 'Baby Dragon']
listOfRandomOccurance = ['Walking', 'Walking', 'Walking', 'Monster Encounter', 'Monster Encounter', 'Monster Encounter', 'Monster Encounter', 'Monster Encounter', 'SavePoint']
armor = []
weapon = []
listOfItems = []
daysSpent = 1
yourHealthPoints = 100
ironArmorValue = 4
leatherArmorValue = 2
guardingYesOrNo = ['No']
StoreVisited = []
StoreVisitedList = ['None']
MonsterEncountered = []
MonstersEncounteredList = ['Goblin', 'Orc', 'Baby Dragon']
MonsterSpeed = []
MonsterHP = []
AmountofPotionsB = []
AmountofAntidotesB = []
AlimentList = []
backpack = []
deaths = 1

def clear_Screen():
      os.system(
            'cls' if os.name ==
            'nt' else 'clear'
      )

def start_game():
    import time
    
    if deaths == 0:
        newGenstart_game()
    
    if deaths != 0:
        
        time.sleep(1.95)
    
        clear_Screen()
    
        time.sleep(1.5)
    
        print("[PRIDE AND GLUTTONY]")
    
        time.sleep(2.5)
    
        print("\n> Base Code and Concept by Nova (My Online Alias)")
    
        time.sleep(3.5)
    
        print("> Proof-read by Sunky (My Long Distance Boyfriend's Online Alias)")
    
        time.sleep(4.5)
    
        continueGame = input("\n[PRESS ENTER TO CONTINUE OR PLAY]\n")
        if continueGame == "":
            time.sleep(2)
            clear_Screen()
            time.sleep(1)
            setOff = input("You are a knight, staying at a small village, who is planning to set off for an adventure for the first time in hopes of fame and riches. \nYou only have 200G with you at this moment.\n[Enter to Proceed.] \n")
            if setOff == "":
                time.sleep(1)
                clear_Screen()
                time.sleep(1)
                arc1()
        
def newGenstart_game():
    import time
    
    time.sleep(1.95)
    
    clear_Screen()
    
    time.sleep(1.5)
    
    print("[PRIDE AND GLUTTONY]")
    
    time.sleep(2.5)
    
    print("\n> Base Code and Concept by Nova (My Online Alias)")
    
    time.sleep(3.5)
    
    print("> Proof-read by Sunky (My Long Distance Boyfriend's Online Alias)")
    
    time.sleep(4.8)
    
    print("\n[>!!<] DISCLAIMER [>!!<]")
    
    time.sleep(3)
    
    print("\nPride and Gluttony is an experimental turn-based battle monster hunter beat-em-up rage randomizer text input game that is a passion and assigned project.")
    
    time.sleep(4)
    
    print("\nTHIS MEANS:")
    
    time.sleep(2.5)
    
    print("Every playthrough of this game will have their differences,")
    
    time.sleep(3.8)
    
    print("some aspects of the game may not be for you,")
    
    time.sleep(3.5)
    
    print("and that there will be a lot of bugs going forward.")
    
    time.sleep(3.5)
    
    print("\nThis is your time to close the app,")
    
    time.sleep(2)
    
    print("if you are not ready to accept failure")
    
    time.sleep(2)
    
    print("OR,")
    
    time.sleep(2)
    
    print("not used to restarting from the bottom up as it is currently a temporary rouge-like.")
    
    time.sleep(4)
    
    print("\nBy pressing your [ENTER] key, you understand these terms, and you will gain access to the game, [PRIDE AND GLUTTONY].")
    
    time.sleep(4)
    
    print("\nThis is the only time you will get this disclaimer for the game.")
    
    time.sleep(3)
    
    loadingComplete = input("\n[Press Enter to Proceed]\n")
    if loadingComplete == "":
        time.sleep(1)
        clear_Screen()
        time.sleep(1)
        setOff = input("You are a knight, staying at a small village, who is planning to set off for an adventure for the first time in hopes of fame and riches. \nYou only have 200G with you at this moment.\n[Enter to Proceed.] \n")
        if setOff == "":
            time.sleep(5)
            arc1()

def guideOfGame():
    import time
    global StoreVisitedList
    global deaths
    
    time.sleep(1)
    clear_Screen()
    time.sleep(1)
    
    print("[PRIDE AND GLUTTONY GUIDE]\n")
    
    time.sleep(1)
    
    print("[TABLE OF CONTENTS]:")
    print("[WEAPON AND ARMOR GUIDE]")
    print("[STATS GUIDE]")
    print("[BATTLE GUIDE]")
    print("[ENEMY COMPENDIUM]")
    print("[ALIMENTS]")
    print("[PROMPT SHORTCUTS GUIDE]\n")
    
    time.sleep(3)
    
    print("[WEAPONS GUIDE]:")
    
    time.sleep(1.5)
    
    print("This game has it's own battle system with text as input. \nDamage is how much you hurt an enemy with an attack \nCritical Rate (CritRate) is how often a stronger attack happensn \nCritical Damage (CritDMG) is how much you hurt an enemy with a stronger attack. \nEach weapon does different amounts of regular damage and critcal damage within a range \nBut the critcal rate for all of the starter weapons is the same, at 10%.\n")
    
    time.sleep(5)
    
    print("[WEAPONS]:")
    
    time.sleep(1.5)
    
    print("Fists: 0-10DMG, 10% CritRate, 11-15 CritDMG")
    
    time.sleep(1.5)
    
    if 'Blacksmith' in StoreVisitedList:
        print("Iron Dagger: 6-12DMG, 10% CritRate, 18-22 CritDMG")
        print("Iron Shortsword: 6-18DMG, 10% CritRate, 20-30 CritDMG")
        print("Wooden Bow: 6-15DMG, 10% CritRate, 20-30 CritDMG")
        time.sleep(4)
    
    if 'Blacksmith' not in StoreVisitedList:
        print("* You haven't gone to the Blacksmith yet. Go inside the Smithery to unlock this information.")
        time.sleep(1.5)
    
    print("\n[ARMOR GUIDE]:")
    
    time.sleep(1.5)
    
    print("Whenever you're in a battle, getting armor is a pretty good idea. \nThe main thing about this game is NOT to die. \nEvery piece of armor has a defensive value, and the damage is divided by that value.")
    
    time.sleep(3)
    
    print("\n[ARMOR]:")
    
    time.sleep(1.5)
    
    print("No Armor: 0")
    
    if 'General Store' in StoreVisitedList:
        print("Imported Iron Armor: 4")
        print("Imported Leather Armor: 2")
    
    if 'General Store' not in StoreVisitedList:
        print("* You haven't gone into the general store yet. Go into the general store to unlock more information.")
    
    time.sleep(4)
    
    print("\n[STATS GUIDE]:")
    print("Everything sentient in this game has stats. That also includes you. Here are your stats and what each of them mean.\n")
    
    if deaths == 0:
        print("HP: Phyiscal Body Condition, if this reaches 0, it is game over.")
        print("\nSpeed: How fast one is. This dictates the turn order in battle.")
        print("\nSkills: You technically have 2 skills, one regular attack to harm an enemy and one stronger attack.")
        print("\nDamage: Varies depending on your equipment. Every weapon has a base number and higher number. \nLike 1 through 10 for example. That's your regular damage, or DMG.")
        print("\nCritical Damage and Rate: Varies depending on your equipment. \nHas a higher base number and highest number. Like 15 through 20 for example. That's called Critical Damage, or CritDMG. \nHOWEVER, it has a percent chance to happen. That's called Critical Rate, or CritRate.")
    
    if deaths != 0:
        print("HP: Phyiscal Body Condition, if this reaches 0, it is game over.")
        print("\nSpeed: How fast one is. This dictates the turn order in battle, and the chances of you being able to flee from battle.")
        print("\nSkills: You technically have 2 skills, one regular attack to harm an enemy and one stronger attack. Some enemies will have more than 2.")
        print("\nDamage: Varies depending on your equipment. Every weapon has a base number and higher number. That's your regular damage, or DMG.")
        print("\nCritical Damage and Rate: Varies depending on your equipment. \nHas a higher base number and highest number. That's called Critical Damage, or CritDMG. \nHOWEVER, it has a percent chance to happen. That's called Critical Rate, or CritRate.")
        
    time.sleep(7)
    
    print("\n [BATTLE GUIDE]:")
    print("Now that you know about your stats, you can know about the battle system itself.")
    
    time.sleep(3)
    
    print("\n[ATTACKING]:")
    print("Attacking uses the weapons that you have probably bought from earlier to deal DMG or CritDMG depending on CritRate to your opposer in the name of self defense. \nOnce you have killed the enemy (or get their HP to 0), you get Gold from hunting them as a reward. \nThe higher the Gold, the most risky it gets.")
    
    time.sleep(3)
    
    print("\n[ITEMS]:")
    print("Items uses the items that you have probably bought earlier to heal or cure you of aliments. Here are the ones you could buy right now.")
    
    if 'Potions Store' in StoreVisitedList:
        print("Lesser Healing Potions that heal 25HP for 10G")
        print("Lesser Antidotes that heal 10HP and Cure Aliments for 8G\n")
        time.sleep(3)
    
    if 'Potions Store' not in StoreVisitedList:
        print("None. You should probably visit the Potions Store to unlock this information.\n")
        time.sleep(1.5)
    
    if 'General Store' in StoreVisitedList:
        print("*TIP, IF YOU BUY A SMALL BACKPACK, YOUR MAXIMUM INVENTORY INCREASES FROM 5 TO 10\n")
        time.sleep(1.5)
    
    print("[DEFENDING]:")
    print("Defending lets you take less damage, but also has a chance for you to parry IF the opposing attack's damage is lower than your defending value, giving you another turn to act.")
    
    time.sleep(3)
    
    print("\n[FLEEING]:")
    print("Is a battle way too hard for you? Then you can try to run away, but this is dictated by you and the enemy's speed value. \nIf your speed stat is too slow, you can't flee, so you must fight.")
    
    time.sleep(3)
    
    print("\n[ENEMY COMPENDIUM]:")
    
    time.sleep(1.5)
    
    print("On your journey, you will log all of the enemies you have ran into here. \nMost can be pretty weak, but there are some to be careful of.\nJust like you, they also have stats.\nThey have varied HP, varied Speed, and Skills that have varied damage.")
    
    if 'Goblin' in MonstersEncounteredList:
        print("\n[GOBLINS]")
        print("HP: 20-45")
        print("Speed: 7-30")
        print("[SKILLS]:")
        print("Bludgeon: 3-10 DMG")
        time.sleep(3)
    
    if 'Goblin' not in MonstersEncounteredList:
        print("You must defeat a Goblin to unlock this information.")
        time.sleep(1)
    
    if 'Orc' in MonstersEncounteredList:
        print("\n[ORCS]")
        print("HP: 40-65")
        print("Speed: 2-30")
        print("[SKILLS]:")
        print("Bludgeon: 4-20 DMG")
        print("Smackdown: 8-40 DMG")
        time.sleep(3)
    
    if 'Orc' not in MonstersEncounteredList:
        print("You must defeat an Orc to unlock this information.")
        time.sleep(1)
    
    if 'Baby Dragon' in MonstersEncounteredList:
        print("\n[Baby Dragon]")
        print("HP: 40-65")
        print("Speed: 2-30")
        print("[SKILLS]:")
        print("Consecutive Scratching: 6-24 DMG")
        print("Spit Fire: 9-10 DMG with Burn")
        print("Bite: 10-20 DMG")
        print("Burning Bite: 15-25 DMG with Burn")
        time.sleep(5)
    
    if 'Baby Dragon' not in MonstersEncounteredList:
        print("You must defeat a Baby Dragon to unlock this information.")
        time.sleep(1)

    print("\n[ALIMENTS]:")
    print("If you are not careful enough in battle, you might get hit with a side effect from an enemy attack.")
    
    if 'Baby Dragon' in MonstersEncounteredList:
        print("Burn: A 50/50 chance of you taking 2-10 DMG.")

    print("\n[PROMPT SHORTCUTS / ACYRONYMS]:")
    
    time.sleep(1.5)
    
    print("\nSince this is a text input game, you may be prompted to enter in words or numbers on occasion. \nAll of these prompts have shortcuts or acryonyms available as a response, so there is no need for you to enter the full words. \nHere are all of the acronyms or shortcuts listed below.")
    
    time.sleep(3)
    
    print("\n[General Prompt Shortcuts that are used the most in this game]:")
    print("(Y/N): Yes or No, which can be entered in as Y or N")
    print("Leave: can be entered in as L")
    print("[Enter to Clear or Proceed]: Press the Enter key to wipe the command line clean\n")
    
    print("[Directional Prompt Shortcuts that can be used]:")
    print("N, for North")
    print("E, for East")
    print("S, for South")
    print("W, for West\n")
    
    print("[Store Prompt Shortcuts that can be used]:\n")
    if 'Blacksmith' in StoreVisitedList:
        print("[For Starter Blacksmith]:")
        print("Iron Dagger: ID")
        print("Iron Shortsword: ISS")
        print("Wooden Bow: WB")
    
    if 'Blacksmith' not in StoreVisitedList:
        print("* You haven't gone to the Blacksmith yet. Go into the Smithery to unlock more information.")
    
    
    if 'Potions Store' in StoreVisitedList:
        print("\n[For Starter Potions Shop]:")
        print("Lesser Healing Potion: LHP (can be entered in full and plural) *")
        print("Lesser Antidote: LA (can be entered in full and plural) *")
    
    if 'Potions Store' not in StoreVisitedList:
        print("* You haven't gone to the Potions Store yet. Go into the potions store to unlock more information.")
        
    if 'General Store' in StoreVisitedList:
        print("\n[For General Store]:")
        print("Imported Leather Armor: ILA, LA, Leather Armor, or Leather")
        print("Imported Iron Armor: IIA, IA, Iron Armor, or Iron")
        print("Small Backpack: S.Backpack, SB")
        
    if 'General Store' not in StoreVisitedList:
        print("* You haven't gone into the General Store yet. Go into the general store to unlock more information.")
    
    if 'None' in StoreVisitedList:
        print("* You haven't gone into any stores yet. Go into a store to unlock information.")
    
    if deaths != 0:
        print("\n[Battle Prompt Shortcuts that can be used]:")
        print("Attack: A")
        print("Item: I (can be entered in full and plural) *")
        print("Defend: D, S, G, Shield, Guard")
        print("Flee: Run, Run away, F, R\n")
    
    if deaths == 0:
        print("* You only know the basics so far. Die once or make it to the next village to unlock information about battle prompt shortcuts.")
    
    print("You can only unfold this piece of paper in a village.")
    
    time.sleep(1)
    foldpaper = input("[Done Reading Guide? Enter to Proceed.]\n")
    if foldpaper == "":
        print("You folded up the paper.")
        time.sleep(1)
        clear_Screen()
        arc1()
   
def arc1():
    global StoreVisitedList
    while True:
        print("Currently, you are standing at the center of this small village with a folded piece of paper you can unfold to read. \nTo the north, there is a blacksmith. \nTo the west, there is a small Potions Store. \nTo the east, there is a small General Store. \nTo the south lies the entrance and exit of the village.\n")
        GoToLocation = input("So, what do you want to do Adventurer? (Pick from N,E,S,W or read folded paper)\n")
        if GoToLocation.casefold() == "North".casefold() or GoToLocation.casefold() == "N".casefold():
            GoNorth()
            StoreVisitedList.remove("None")
            StoreVisitedList.append("Blacksmith")
        if GoToLocation.casefold() == "East".casefold() or GoToLocation.casefold() == "E".casefold():
             GoEast()
             StoreVisitedList.remove("None")
             StoreVisitedList.append("General Store")
        if GoToLocation.casefold() == "South".casefold() or GoToLocation.casefold() == "S".casefold():
             GoSouth()
        if GoToLocation.casefold() == "West".casefold() or GoToLocation.casefold() == "W".casefold():
             GoWest()
             StoreVisitedList.remove("None")
             StoreVisitedList.append("Potions Store")
        if GoToLocation.casefold() == "Unfold".casefold() or GoToLocation.casefold() == "Read".casefold():
            guideOfGame()

def StayInShop():
    if StoreVisited == "North":
        BlackSmith()
    if StoreVisited == "West":
        PotionsStore()
    if StoreVisited == "East":
        GeneralStore()

def GoSouth():
    global weapon
    global armor
    
    ReadyToLeave = input("\nYou walk south to the gates of the village. Are you ready to leave this village? (Y/N)\n")
    if ReadyToLeave.casefold() == "Yes".casefold() or ReadyToLeave.casefold() == "Y".casefold():
        print("\nYou look back at the village. This is your last day at this village, but your dreams are more important to you. You start your adventures.")
        if len(armor) == 0:
            armor.append("No Armor")
        if len(weapon) == 0:
            weapon.append("No Weapon")
        
            clear = input("[Enter to Proceed.]")
            if clear == "":
                clear_Screen()
                startAdventure()

def GoEast():
    print("You walk East to the General Store. Inside there are a small assortment of items to choose from. A petite female shopkeeper greets you warmly.")
    StoreVisited.append('East')
    GeneralStore()

def GeneralStore():
    global score
    global ImportedLeatherPrice
    global SmallBackpackPrice
    global ImportedIronArmorPrice
    global armor
    global backpack

    GeneralStoreInteraction = input(">Welcome! Feel free to take a look.\n(You can look around, or leave.)\n")
    if GeneralStoreInteraction.casefold() == "Look".casefold() or GeneralStoreInteraction.casefold() == "Look Around".casefold() or GeneralStoreInteraction.casefold() == "LA":
        print("You look at the shelving units. The items offered are as followed: \n A small backpack for 30G \n Imported Leather Armor for 55G \n Imported Iron Armor for 100G \n ooor, you could leave\n")
        ItemChosen = input("What item would you like to buy? (S.Backpack, I.Leather Armor, I.Iron Armor)\n")
    if ItemChosen.casefold() == "Imported Leather Armor".casefold() or ItemChosen.casefold() == "ILA".casefold() or ItemChosen.casefold() == "Leather Armor".casefold() or ItemChosen.casefold() == "Leather".casefold():
        ReadyItemChosen = input("Are you sure you want to buy this item? (Y/N)\n")
        if ReadyItemChosen.casefold() == "Yes".casefold() or ReadyItemChosen.casefold() == "Y".casefold():
            if score < ImportedLeatherPrice:
                print("\n>Doesn't look like you have enough. Come back when you do.")
                clear = input("[Enter to clear.]")
                if clear == "":
                    clear_Screen()
                    StoreVisited.clear
                    arc1()
            if score > ImportedLeatherPrice:
                print("\n>Thank you for your purchase, adventurer! It's all yours now.")
                score = score - ImportedLeatherPrice
                print("You paid the Shopkeeper: ", ImportedLeatherPrice, "G.", "\n You have:", score, "G left.")
                armor.append("Leather Armor")
                clear = input("\n[Enter to clear.]")
                if clear == "":
                    clear_Screen()
                    StayInShop()
    if ItemChosen.casefold() == "S.Backpack".casefold() or ItemChosen.casefold() == "SB".casefold() or ItemChosen.casefold() == "Small Backpack":
        ReadyItemChosen = input("Are you sure you want to buy this item? (Y/N)")
        if ReadyItemChosen.casefold() == "Yes".casefold() or ReadyItemChosen.casefold() == "Y".casefold():
            if score < SmallBackpackPrice:
                print("\n>Doesn't look like you have enough. Come back when you do.")
                clear = input("\n[Enter to clear.]")
                if clear == "":
                    clear_Screen()
                    StoreVisited.clear
                    arc1()
            if score > SmallBackpackPrice:
                print("\n>Thank you for your purchase, adventurer! It's all yours now.")
                score = score - SmallBackpackPrice
                print("You paid the Shopkeeper: ", SmallBackpackPrice, "G.", "\n You have:", score, "G left.")
                backpack.append("Small Backpack")
                clear = input("[Enter to clear.]")
                if clear == "":
                    clear_Screen()
                    StayInShop()
    if ItemChosen.casefold() == "Imported Iron Armor".casefold() or ItemChosen.casefold() == "IIA".casefold() or ItemChosen.casefold() == "Iron Armor".casefold() or ItemChosen.casefold() == "Iron".casefold():
        ReadyItemChosen = input("\nAre you sure you want to buy this item? (Y/N)\n")
        if ReadyItemChosen.casefold() == "Yes".casefold() or ReadyItemChosen.casefold() == "Y".casefold():
            if score < ImportedIronArmorPrice:
                print("\n>Doesn't look like you have enough. Come back when you do.")
                clear = input("[Enter to clear.]")
                if clear == "":
                    clear_Screen()
                    StoreVisited.clear
                    arc1()
            if score > ImportedIronArmorPrice:
                print("\n>Thank you for your purchase, adventurer! It's all yours now.")
                score = score - ImportedIronArmorPrice
                print("\nYou paid the Shopkeeper: ", ImportedIronArmorPrice, "G.", "\n You have:", score, "G left.")
                armor.append("Iron Armor")
                clear = input("\n[Enter to clear.]")
                if clear == "":
                    clear_Screen()
                    StayInShop()
    if GeneralStoreInteraction == "Leave":
        print(">See you next time! \n \n You leave the store. \n")
        clear = input("[Enter to clear.]")
        if clear == "":
            clear_Screen()
            StoreVisited.clear
            arc1()    

def GoNorth():
    print("\nYou walk north to the Blacksmith. Inside, there is a small assortment of pre-made weapons to your left. A burly male shopkeeper greets you warmly.")
    print(">'Ey! Welcome to the Smithery.")
    StoreVisited.append('North')
    BlackSmith()

def BlackSmith():
    global score
    global DaggerPrice 
    global IronShortSwordPrice
    global WoodenBowPrice
    global weapon

    SmitheryInteraction = input("\n>I offer pre-made weapons and custom-made at a price. Is there anythin' you need?\n (You can only look at the Pre-Made Weapons currently.)")
    if SmitheryInteraction.casefold() == "Pre-Made Weapons".casefold() or SmitheryInteraction.casefold() == "PMW".casefold():
        print(">Take your time adventurer. A weapon is an extension of your body and soul. It can take some time to get used to, so you better choose 'er correctly.")
        print("\n The pre-made weapons the blacksmith offers to you are: \n An iron short-sword for 60G \n An iron dagger for 35G \n A wooden bow, its quiver filled to the brim with iron tipped arrows for 45G\n ooor, you could leave.\n")
        WeaponChosen = input("What weapon would you choose to buy? (Dagger, Short-Sword, Wooden Bow, or leave)\n")  
        if WeaponChosen.casefold() == "Iron Dagger".casefold() or WeaponChosen.casefold() == "ID".casefold():
            ReadyWeaponChosen = input("Are you sure you want to buy this weapon? It will cost you: 35G (Y/N) \n")
            if ReadyWeaponChosen.casefold() == "Yes".casefold() or ReadyWeaponChosen.casefold() == "Y":
                if score < DaggerPrice:
                    print(">Ah, I see you can't afford it. Come back after you have enough.")
                    clear = input("[Enter to clear.]")
                    if clear == "":
                        clear_Screen()
                        StoreVisited.clear
                        arc1()
                if score > DaggerPrice:
                    print(">Good choice adventurer. She's quite quick and nimble one.")
                    score = score - DaggerPrice
                    print("You paid the Blacksmith: ", DaggerPrice, "G.", "\nYou have: ", score ,"G left.")
                    weapon.append("Dagger")
                    clear = input("[Enter to clear.]")
                    if clear == "":
                        clear_Screen()
                        StayInShop()
            if ReadyWeaponChosen.casefold() == "No".casefold() or ReadyWeaponChosen.casefold() == "N".casefold():
                print(">Take your time, young adventurer.")
                if clear == "":
                    clear_Screen()
                    StayInShop()
        if WeaponChosen.casefold() == "Iron Shortsword".casefold() or WeaponChosen.casefold() == "ISS".casefold():
                ReadyWeaponChosen = input("Are you sure you want to buy this weapon? It will cost you: 60G (Y/N)\n")
                if ReadyWeaponChosen.casefold() == "Yes".casefold() or ReadyWeaponChosen.casefold() == "Y".casefold():
                    if score < IronShortSwordPrice:
                        print(">Ah, I see you can't afford it. Come back after you have enough.")
                        clear = input("[Enter to clear.]")
                        if clear == "":
                            clear_Screen()
                            StoreVisited.clear
                            arc1()
                    if score > IronShortSwordPrice:
                        print(">Good choice adventurer. She's the old and reliable of the three.")
                        score = score - IronShortSwordPrice
                        print("You paid the Blacksmith: ", IronShortSwordPrice, "G", "\nYou have: ", score, "G left.")
                        weapon.append("Iron Shortsword")
                        clear = input("[Enter to clear.]")
                        if clear == "":
                            clear_Screen()
                            StayInShop()
                if ReadyWeaponChosen.casefold() == "No".casefold() or ReadyWeaponChosen.casefold() == "N".casefold():
                    print(">Take your time, young adventurer.")
                    if clear == "":
                        clear_Screen()
                        StayInShop()
        if WeaponChosen.casefold() == "Wooden Bow".casefold() or WeaponChosen.casefold() == "WB".casefold():
            ReadyWeaponChosen = input("Are you sure you want to buy this weapon? It will cost you: 45G (Y/N)\n")
            if ReadyWeaponChosen.casefold() == "Yes".casefold() or ReadyWeaponChosen.casefold() == "Y".casefold():
                if score < WoodenBowPrice:
                    print(">Ah, I see you can't afford it. Come back after you have enough.")
                    clear = input("[Enter to clear.]")
                    if clear == "":
                        clear_Screen()
                        StoreVisited.clear
                        arc1()
                    if score > WoodenBowPrice:
                        print(">Good choice adventurer. She's the old and reliable of the three.")
                        score = score - WoodenBowPrice
                        print("You paid the Blacksmith: ", WoodenBowPrice, "G", "\nYou have: ", score, "G left.")
                        weapon.append("Wooden Bow")
                        if clear == "":
                            clear_Screen()
                            StayInShop()
            if ReadyWeaponChosen.casefold() == "No".casefold() or ReadyWeaponChosen.casefold() == "N".casefold():
                print(">Take your time, young adventurer.")
                if clear == "":
                    clear_Screen()
                    StayInShop()
        if WeaponChosen.casefold() == "Leave".casefold() or WeaponChosen.casefold() == "L".casefold() or WeaponChosen.casefold() == "E".casefold():
            Goodbye = input(">I wish you luck on your quest, young adventurer. \n[Enter to Clear.]")
            if Goodbye == "":
                clear_Screen()
                StoreVisited.clear
                arc1()

def GoWest():
    print("You enter a small potions store and was promptly greeted by an older lady, presumably in her 80s.\n\n>Well hello there young adventurer. Welcome to my tiny potions store.\n\nThere are shelves full of various of potions.\nThe following you can purchase as of this moment are: Lesser Health Potions for 10G, and Lesser Antidotes for 8G.")
    StoreVisited.append('West')
    PotionsStore()

def PotionsStore():
    global score
    global LesserHealingPotionPrice
    global LesserAntidotePrice
    PotionChosen = input("\nWhat potion will you buy? (Lesser Healing Potions for 10G, Lesser Antidotes for 8G, ooor, you could leave)\n")
    if PotionChosen.casefold() == "Lesser Healing Potions".casefold() or PotionChosen.casefold() == "LHP".casefold() or PotionChosen.casefold() == "Lesser Healing Potion":
        AmountofPotions = int(input("\nHow many potions would you buy? (MUST BE A NUMBER.)\n"))
        NewPotionPrice = LesserHealingPotionPrice * AmountofPotions
        if AmountofPotions == 0:
            print("You cannot buy 0 potions.")
            clear = input("[Enter to clear.]")
            if clear == "":
                clear_Screen()
                StayInShop()
        if AmountofPotions == 1:
            ReadyPotionChosen = input("Are you sure you want to buy this potion? (Y/N)\n")
            if ReadyPotionChosen.casefold() == "Yes".casefold() or ReadyPotionChosen.casefold() == "Y".casefold():
                score = score - NewPotionPrice
                print(">Thank you kind youngster.\nYou paid the Shopkeeper: ", NewPotionPrice, "G.", "\nYou have: ", score, "G left.\n")
                print("You have: ")
                print(AmountofPotions)
                print("Potion(s).")
                AmountofPotionsB.append(AmountofPotions)
                listOfItems.append("Lesser Healing Potion")
                clear = input("[Enter to clear.]")
                if clear == "":
                    clear_Screen()
                    StayInShop()
        if AmountofPotions > 1:
            ReadyPotionChosen = input("Are you sure you want to buy these potions? (Y/N)\n")
            if ReadyPotionChosen.casefold() == "Yes".casefold() or ReadyPotionChosen.casefold() == "Y".casefold():
                print(">Thank you kind youngster.\nYou paid the Shopkeeper: ", NewPotionPrice, "G.", "\nYou have: ", score, "G left.\n")
                print("You have: ")
                print(AmountofPotions)
                print(" Potions.")
                listOfItems.append("Lesser Healing Potions")
                AmountofPotionsB.append(AmountofPotions)
                clear = input("\n[Enter to clear.]")
                if clear == "":
                    clear_Screen()
                    StayInShop()
        if score < NewPotionPrice:
            print("You cannot buy anything here. \n >Come back when you have enough money, okay?")
            clear = input("[Enter to clear.]")
            if clear == "":
                clear_Screen()
                StoreVisited.clear
                arc1()
    if PotionChosen.casefold() == "Lesser Antidote".casefold() or PotionChosen.casefold() == "LA".casefold() or PotionChosen.casefold() == "Lesser Antidotes":
        AmountofAntidotes = int(input("How many Antidotes would you buy? (MUST BE A NUMBER.)"))
        NewAntidotePrice = LesserAntidotePrice * AmountofAntidotes
        if AmountofAntidotes == 0:
            print("You cannot buy 0 antidotes.")
            clear = input("[Enter to clear.]")
            if clear == "":
                clear_Screen()
                StayInShop()
        if AmountofAntidotes == 1:
            ReadyPotionChosen = input("Are you sure you want to buy this Antidote? (Y/N)")
            if ReadyPotionChosen.casefold() == "Yes".casefold() or ReadyPotionChosen.casefold() == "Y".casefold():
                score = score - NewAntidotePrice
                print(">Thank you kind youngster.\nYou paid the Shopkeeper: ", NewAntidotePrice, "G.", "\n You have: ", score, "G left.")
                print("You have: ")
                print(AmountofAntidotes)
                print(" Antidote(s).")
                listOfItems.append("Lesser Antidote")
                AmountofAntidotesB.append(AmountofAntidotes)
                clear = input("\n[Enter to clear.]")
                if clear == "":
                    clear_Screen()
                    StayInShop()
        if AmountofAntidotes > 1:
            ReadyPotionChosen = input("Are you sure you want to buy these Antidotes? (Y/N)")
            if ReadyPotionChosen.casefold() == "Yes".casefold() or ReadyPotionChosen.casefold() == "Y".casefold():
                score = score - NewAntidotePrice
                print(">Thank you kind youngster.\nYou paid the Shopkeeper: ", NewAntidotePrice, "G.", "\n You have: ", score, "G left.")
                print("You have: ")
                print(AmountofAntidotes)
                print(" Antidotes.")
                listOfItems.append("Lesser Antidotes")
                AmountofAntidotesB.append(AmountofAntidotes)
                clear = input("\n[Enter to clear.]")
                if clear == "":
                    clear_Screen()
                    StayInShop()
        if score < NewAntidotePrice:
            print("You cannot buy anything here. \n >Come back when you have enough money, okay?")
            clear = input("[Enter to clear.]")
            if clear == "":
                clear_Screen()
                arc1()
                StoreVisited.clear
        if PotionChosen.casefold() == "Leave".casefold() or PotionChosen.casefold() == "L".casefold():
            Goodbye = input(">I wish you luck on your quest, young adventurer. [Enter to Proceed.]")
            if Goodbye == "":
                clear_Screen()
                StoreVisited.clear
                arc1()

def startAdventure():

    print("Day")
    print(daysSpent)
    print("of the Journey for hopes of fame and riches\n")

    clear = input("[Enter to clear.]")
    if clear == "":
        clear_Screen()
        adventuring()

def adventuring():
    import random
    global listOfRandomOccurance
    global listOfLowLevelMonsters
    global daysSpent
    global MonsterSpeed
    global MonsterEncountered
    global MonsterHP
    
    yourSpeedPoints = range(10,30)
    randomizedPlayerSpeed = random.choice(yourSpeedPoints)

    goblinHealthPoints = range(20,45)
    goblinSpeedPoints = range(7,30)

    orcHealthPoints = range(40,65)
    orcSpeedPoints = range(2,30)

    babyDragonHealthPoints = range(50,75)
    babyDragonSpeedPoints = range(40,60)

    #PSEUDO CODE, pick a random occurance, print the occurance, if its a monster encounter, the user must DEFEAT this monster, if it isn't a monster encounter, have the user keep walking then go to the next day. Some time in the future, I want some kind of "checkpoint" for the user.
    randomizedOccurance = random.choice(listOfRandomOccurance)
    randomizedLowLevelMonsters = random.choice(listOfLowLevelMonsters)
    randomizedGoblinHP = random.choice(goblinHealthPoints)
    randomizedGoblinSP = random.choice(goblinSpeedPoints)
    randomizedOrcHP = random.choice(orcHealthPoints)
    randomizedOrcSP = random.choice(orcSpeedPoints)
    randomizedBabyDragonHP = random.choice(babyDragonHealthPoints)
    randomizedBabyDragonSP = random.choice(babyDragonSpeedPoints)

    if randomizedOccurance == 'Walking':
        print("Walking . . . (No Monster Encounters yet.)\n")
        clear = input("[Enter to clear.]")
        if clear == "":
            clear_Screen()
            daysSpent += 1
            startAdventure()
    
    if randomizedOccurance != 'Walking . . .':
        print("COMBAT LOG \n")
        print("You ran into a ")
        print(randomizedLowLevelMonsters)
        print("!")
        print("\n")
        if 'Goblin' in randomizedLowLevelMonsters:
            print("Goblin HP: ")
            print(randomizedGoblinHP)
            print("\nGoblin Speed: ")
            print(randomizedGoblinSP)
            if randomizedGoblinSP > randomizedPlayerSpeed:
                MonsterEncountered.append('Goblin')
                MonsterHP.append(randomizedGoblinHP)
                MonsterSpeed.append(randomizedGoblinSP)
                GoblinTurn()
            if randomizedPlayerSpeed > randomizedGoblinSP:
                MonsterEncountered.append('Goblin')
                MonsterHP.append(randomizedGoblinHP)
                MonsterSpeed.append(randomizedGoblinSP)
                playerTurn()
        if 'Orc' in randomizedLowLevelMonsters:
            print("Orc HP: ")
            print(randomizedOrcHP)
            print("Orc Speed: ")
            print(randomizedOrcSP)
            if randomizedOrcSP > randomizedPlayerSpeed:
                MonsterEncountered.append('Orc')
                MonsterHP.append(randomizedOrcHP)
                MonsterSpeed.append(randomizedOrcSP)
                OrcTurn()
            if randomizedPlayerSpeed > randomizedOrcSP:
                MonsterEncountered.append('Orc')
                MonsterHP.append(randomizedOrcHP)
                MonsterSpeed.append(randomizedOrcSP)
                playerTurn()
        if 'Baby Dragon' in randomizedLowLevelMonsters:
            print("Baby Dragon HP: ")
            print(randomizedBabyDragonHP)
            print("Baby Dragon Speed: ")
            print(randomizedBabyDragonSP)
            if randomizedBabyDragonSP > randomizedPlayerSpeed:
                MonsterEncountered.append('Baby Dragon')
                MonsterHP.append(randomizedBabyDragonHP)
                MonsterSpeed.append(randomizedBabyDragonSP)
                BabyDragonTurn()
            if randomizedPlayerSpeed > randomizedBabyDragonSP:
                MonsterEncountered.append('Baby Dragon')
                MonsterHP.append(randomizedBabyDragonHP)
                MonsterSpeed.append(randomizedBabyDragonSP)
                playerTurn()

def playerTurn():
    import random
    import time
    global guardingYesOrNo
    global MonsterSpeed
    global armor
    global MonsterHP
    global MonsterEncountered
    global score
    global daysSpent
    global AlimentList
    global weapon
    global yourHealthPoints

    trueMonsterEncountered = MonsterEncountered[0]
    MonsterTrueSpeed = MonsterSpeed[0]

    burnDMG = range(2,10)
    burnDMGR = random.choice(burnDMG)

    yourSpeedPoints = range(10,30)
    randomizedPlayerSpeed = random.choice(yourSpeedPoints)

    chanceOfBurn = range(0,100)
    randomizedChanceOfBurn = random.choice(chanceOfBurn)
 
    if 'Burn' in AlimentList:
        if randomizedChanceOfBurn >= 51:
                if yourHealthPoints > 0:
                    yourHealthPoints = yourHealthPoints - burnDMGR
                    print("You're burning up badly. Use an antidote.\n")
                    print("Your HP:")
                    print(yourHealthPoints)
                    print("Damage Taken by Burn:")
                    print(burnDMGR)
                if yourHealthPoints < 0:
                    burntSelf = input("You burnt yourself into a chrisp. Game over.")
                    if burntSelf == "":
                        clear_Screen()
                        start_game()
        if randomizedChanceOfBurn <= 50:
            print("You are burning, but you aren't taking any damage.")

    battleChoice = input("\nIt is your turn. \n The options you have are: \n \n [Attack] \n [Items] \n [Defend] \n [Flee] \n \n")

    if battleChoice.casefold() == "Attack".casefold() or battleChoice.casefold() == "A".casefold():
        
        if 'Iron Dagger' in weapon:
            ironDagger()

        if 'Iron Shortsword' in weapon:
            ironShortSword()
        
        if 'Wooden Bow' in weapon:
            woodenBow()
        
        if 'No Weapon' in weapon:
            fists()

    if battleChoice.casefold() == "Items".casefold() or battleChoice.casefold() == "Item".casefold() or battleChoice.casefold() == "I":
        print("You have the following items, choose 1 to use or go back:")
        itemChoice = input(listOfItems) #Add a space between list and actual input.
        if itemChoice.casefold() == "Back".casefold() or itemChoice.casefold() == "B".casefold() or itemChoice.casefold() == "".casefold():
            playerTurn()
        if itemChoice.casefold() == "Lesser Antidote".casefold() or battleChoice.casefold() == "Lesser Antidotes".casefold() or battleChoice.casefold() == "LA":
            if "Lesser Antidote" in listOfItems:
                listOfItems.remove("Lesser Antidote")
                print("You used the lesser antidote, healed for 10HP and cured yourself of any aliments.")
                yourHealthPoints += 10
                AlimentList.clear
                if 'Goblin' in trueMonsterEncountered:
                    GoblinTurn()
                if 'Orc' in trueMonsterEncountered:
                    OrcTurn()
                if 'Baby Dragon' in trueMonsterEncountered:
                    BabyDragonTurn()
        if itemChoice.casefold() == "Lesser Healing Potions".casefold() or battleChoice.casefold() == "Lesser Healing Potion".casefold() or battleChoice.casefold() == "LHP":
            if "Lesser Healing Potion" in listOfItems:
                listOfItems.remove("Lesser Healing Potion")
                print("You used the lesser healing potion and healed for 25HP.")
                yourHealthPoints += 25
                if 'Goblin' in trueMonsterEncountered:
                    GoblinTurn()
                if 'Orc' in trueMonsterEncountered:
                    OrcTurn()
                if 'Baby Dragon' in trueMonsterEncountered:
                    BabyDragonTurn()
    
    if battleChoice.casefold() == "Defend".casefold() or battleChoice.casefold() == "Shield".casefold() or battleChoice.casefold() == "Guard".casefold() or battleChoice.casefold() == "G".casefold() or battleChoice.casefold() == "D".casefold() or battleChoice.casefold() == "S".casefold():
        print("You guarded.")
        guardingYesOrNo.remove('No')
        guardingYesOrNo.append('Yes')
        if 'Goblin' in trueMonsterEncountered:
            GoblinTurn()
        if 'Orc' in trueMonsterEncountered:
            OrcTurn()
        if 'Baby Dragon' in trueMonsterEncountered:
            BabyDragonTurn()
    #Guarding doesn't actually work...

    if battleChoice.casefold() == "Run".casefold() or battleChoice.casefold() == "Flee".casefold() or battleChoice.casefold() == "F".casefold() or battleChoice.casefold() == "R".casefold() or battleChoice.casefold() == "Run Away".casefold():
        print("You tried to run away.")
        time.sleep(0.5)
        print(" . ")
        time.sleep(0.5)
        print(" ! ")
        if randomizedPlayerSpeed > MonsterTrueSpeed:
            ranAway = input("\nYou successfully ran away. You gain nothing from this battle! \n[Enter to proceed.]")
            if ranAway == "":
                daysSpent += 1
                startAdventure()
        if randomizedPlayerSpeed <= MonsterTrueSpeed:
            print("You couldn't run away. Better luck next time.")
            time.sleep(0.5)
            print(" . ")
            time.sleep(0.5)
            failedFlee = input(" . \n[Enter to proceed.]")
            if failedFlee == "":
                if 'Goblin' in trueMonsterEncountered:
                    GoblinTurn()
                if 'Orc' in trueMonsterEncountered:
                    OrcTurn()
                if 'Baby Dragon' in trueMonsterEncountered:
                    BabyDragonTurn()

def GoblinTurn():
    import random
    global yourHealthPoints
    global ironArmorValue
    global leatherArmorValue
    global guardingYesOrNo
    global armor
    global deaths
    global MonsterEncountered
    global MonsterHP
    global MonsterSpeed

    guardingFromAttacksRange = range(5,10)
    guardingFromAttack = random.choice(guardingFromAttacksRange)

    goblinAttack1 = range(3,10)
    randomizedGoblinAttack1 = random.choice(goblinAttack1)

    chanceToWaitGoblin = (1,100)
    randomizedChanceToWaitGoblin = random.choice(chanceToWaitGoblin)

    gobTurn = input("It is the goblin's turn. [Enter to proceed.]")
    if gobTurn == "":
        if randomizedChanceToWaitGoblin >= 30:
            gobWaited = input("The Goblin Waited. [Enter to proceed.]")
            if gobWaited == "":
                playerTurn()
        if randomizedChanceToWaitGoblin <= 31:
            gobAttack = input("Bludgeon [Enter to proceed.]")
            if gobAttack == "":
                if 'Iron Armor' in armor:
                    if 'Yes' in guardingYesOrNo:
                        if yourHealthPoints > 0:
                            ironReducedGoblinAttack1 = randomizedGoblinAttack1 / ironArmorValue
                            newGoblinDMG1 = ironReducedGoblinAttack1 - guardingFromAttack
                            yourHealthPoints = yourHealthPoints - newGoblinDMG1
                            if guardingFromAttack >= randomizedGoblinAttack1:
                                proceed = input("You guarded the previous turn, and parried the enemy's attack! \nYou gain player advantage! [Enter to proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')    
                                    playerTurn()
                            if guardingFromAttack < randomizedGoblinAttack1:
                                print("You took:\n")
                                print(newGoblinDMG1)
                                print("HP.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')
                                    playerTurn()  
                    if 'No' in guardingYesOrNo:
                        if yourHealthPoints > 0:
                            yourHealthPoints = yourHealthPoints - ironReducedGoblinAttack1
                            print("You took:\n")
                            print(ironReducedGoblinAttack1)
                            print("HP.")
                            print("\nYou have:")
                            print(yourHealthPoints)
                            proceed = input("HP left. \n[Enter to Proceed.]")
                            if proceed == "":
                                playerTurn()
                elif 'Leather Armor' in armor:
                    if 'Yes' in guardingYesOrNo:
                        if yourHealthPoints > 0:
                            leatherReducedGoblinAttack1 = randomizedGoblinAttack1 / leatherArmorValue
                            newGoblinDMG1 = leatherReducedGoblinAttack1 - guardingFromAttack
                            yourHealthPoints = yourHealthPoints - newGoblinDMG1
                            if guardingFromAttack >= randomizedGoblinAttack1:
                                proceed = input("You guarded in the previous turn, and parried the enemy's attack! \nYou gain player advantage! \n[Enter to proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')    
                                    playerTurn()
                            if guardingFromAttack < randomizedGoblinAttack1:
                                print("You took:\n")
                                print(newGoblinDMG1)
                                print("HP.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')
                                    playerTurn()  
                    if 'No' in guardingYesOrNo:
                        if yourHealthPoints > 0:
                            yourHealthPoints = yourHealthPoints - leatherReducedGoblinAttack1
                            print("You took:\n")
                            print(leatherReducedGoblinAttack1)
                            print("HP.")
                            print("\nYou have:")
                            print(yourHealthPoints)
                            proceed = input("HP left. \n[Enter to Proceed.]")
                            if proceed == "":
                                playerTurn()     
                elif 'No Armor' in armor:
                    if 'Yes' in guardingYesOrNo:
                        if yourHealthPoints > 0:
                            newGoblinDMG1 = randomizedGoblinAttack1 - guardingFromAttack
                            yourHealthPoints = yourHealthPoints - newGoblinDMG1
                            if guardingFromAttack >= randomizedGoblinAttack1:
                                proceed = input("You guarded in the previous turn, and parried the enemy's attack! \nYou gain player advantage! [Enter to proceed.]")
                                if proceed == "":    
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')
                                    playerTurn()
                            if guardingFromAttack < randomizedGoblinAttack1:
                                print("You took:\n")
                                print(newGoblinDMG1)
                                print("HP.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')
                                    playerTurn()  
                    if 'No' in guardingYesOrNo:
                        if yourHealthPoints > 0:
                            yourHealthPoints = yourHealthPoints - randomizedGoblinAttack1
                            print("You took:\n")
                            print(randomizedGoblinAttack1)
                            print("HP.")
                            print("\nYou have:")
                            print(yourHealthPoints)
                            proceed = input("HP left. \n[Enter to Proceed.]")
                            if proceed == "":
                                playerTurn()        
                if yourHealthPoints < 0:
                    goblinDeath = input("You were bludgeoned to death by a goblin. \nA cruel and stupid way to go out. Game over. [Enter to Proceed.]")
                    if goblinDeath == "":
                        deaths =+ 1
                        MonsterEncountered.clear
                        MonsterHP.clear
                        MonsterSpeed.clear
                        clear_Screen()
                        start_game()

def OrcTurn():
    import random
    global yourHealthPoints
    global ironArmorValue
    global leatherArmorValue
    global guardingYesOrNo
    global armor
    global MonsterEncountered
    global MonsterHP
    global MonsterSpeed
    global deaths

    guardingFromAttacksRange = range(5,15)
    guardingFromAttack = random.choice(guardingFromAttacksRange)

    listOfOrcAttacks = ['Bludgeon', 'Smackdown']
    randomizedOrcAttack = random.choice(listOfOrcAttacks)

    orcAttack1 = range(4,20)
    randomizedOrcAttack1 = random.choice(orcAttack1)

    chanceToWaitOrc = (1,100)
    randomizedChanceToWaitOrc = random.choice(chanceToWaitOrc)

    orcTurn = input("It is the Orc's turn. [Enter to proceed.]")
    if orcTurn == "":
        if randomizedChanceToWaitOrc >= 40:
            orcWaited = input("The Orc Waited. [Enter to proceed.]")
            if orcWaited == "":
                playerTurn()
        if randomizedChanceToWaitOrc <= 41:
            if randomizedOrcAttack == 'Smackdown':
                orcAttack = input("Smackdown [Enter to proceed.]")
                if orcAttack == "":
                    if 'Iron Armor' in armor:
                        if 'Yes' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                randomizedOrcAttack2 = randomizedOrcAttack1 + randomizedOrcAttack1
                                ironReducedOrcAttack2 = randomizedOrcAttack2 / ironArmorValue
                                newOrcDMG1 = ironReducedOrcAttack2 - guardingFromAttack
                                yourHealthPoints = yourHealthPoints - newOrcDMG1
                            if guardingFromAttack >= randomizedOrcAttack2:
                                proceed = input("You guarded the previous turn, and parried the enemy's attack! \nYou gain player advantage! [Enter to proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')    
                                    playerTurn()
                            if guardingFromAttack < randomizedOrcAttack2:
                                print("You took:\n")
                                print(newOrcDMG1)
                                print("HP.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')
                                    playerTurn()  
                        if 'No' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                ironReducedOrcAttack2 = randomizedOrcAttack2 / ironArmorValue
                                yourHealthPoints = yourHealthPoints - ironReducedOrcAttack2
                                print("You took:\n")
                                print(ironReducedOrcAttack2)
                                print("HP.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    playerTurn()
                    elif 'Leather Armor' in armor:
                        if 'Yes' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                randomizedOrcAttack2 = randomizedOrcAttack1 + randomizedOrcAttack1
                                leatherReducedOrcAttack2 = randomizedOrcAttack2 / leatherArmorValue
                                newOrcDMG1 = leatherReducedOrcAttack2 - guardingFromAttack
                                yourHealthPoints = yourHealthPoints - newOrcDMG1
                            if guardingFromAttack >= randomizedOrcAttack2:
                                proceed = input("You guarded the previous turn, and parried the enemy's attack! \nYou gain player advantage! [Enter to proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')    
                                    playerTurn()
                            if guardingFromAttack < randomizedOrcAttack2:
                                print("You took:\n")
                                print(newOrcDMG1)
                                print("HP.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')
                                    playerTurn()  
                        if 'No' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                leatherReducedOrcAttack2 = randomizedOrcAttack2 / leatherArmorValue
                                yourHealthPoints = yourHealthPoints - leatherReducedOrcAttack2
                                print("You took:\n")
                                print(leatherReducedOrcAttack2)
                                print("HP.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    playerTurn()     
                    elif 'No Armor' in armor:
                        if 'Yes' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                randomizedOrcAttack2 = randomizedOrcAttack1 + randomizedOrcAttack1
                                newOrcDMG1 = randomizedOrcAttack2 - guardingFromAttack
                                yourHealthPoints = yourHealthPoints - newOrcDMG1
                            if guardingFromAttack >= randomizedOrcAttack1:
                                proceed = input("You guarded the previous turn, and parried the enemy's attack! \nYou gain player advantage! [Enter to proceed.]")
                                if proceed == "":    
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')
                                    playerTurn()
                            if guardingFromAttack < randomizedOrcAttack1:
                                print("You took:\n")
                                print(newOrcDMG1)
                                print("HP.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')
                                    playerTurn()  
                        if 'No' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                randomizedOrcAttack2 = randomizedOrcAttack1 + randomizedOrcAttack1
                                yourHealthPoints = yourHealthPoints - newOrcDMG1
                                print("You took:\n")
                                print(randomizedOrcAttack1)
                                print("HP.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    playerTurn()        
                if yourHealthPoints < 0:
                    orcDeath = input("You were smacked down to death by an orc. \nA cruel way to go out. Game over. [Enter to Proceed.]")
                    if orcDeath == "":
                        start_game()
            if randomizedOrcAttack == 'Bludgeon':
                orcAttack = input("Bludgeon [Enter to proceed.]")
                if orcAttack == "":
                    if 'Iron Armor' in armor:
                        if 'Yes' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                ironReducedOrcAttack1 = randomizedOrcAttack1 / ironArmorValue
                                newOrcDMG1 = ironReducedOrcAttack1 - guardingFromAttack
                                yourHealthPoints = yourHealthPoints - newOrcDMG1
                            if guardingFromAttack >= randomizedOrcAttack1:
                                proceed = input("You guarded the previous turn, and parried the enemy's attack! \nYou gain player advantage! [Enter to proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')    
                                    playerTurn()
                            if guardingFromAttack < randomizedOrcAttack1:
                                print("You took:\n")
                                print(newOrcDMG1)
                                print("HP.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')
                                    playerTurn()  
                        if 'No' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                ironReducedOrcAttack1 = randomizedOrcAttack1 / ironArmorValue
                                yourHealthPoints = yourHealthPoints - ironReducedOrcAttack1
                                print("You took:\n")
                                print(ironReducedOrcAttack1)
                                print("HP.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    playerTurn()
                    elif 'Leather Armor' in armor:
                        if 'Yes' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                leatherReducedOrcAttack1 = randomizedOrcAttack1 / leatherArmorValue
                                newOrcDMG1 = leatherReducedOrcAttack1 - guardingFromAttack
                                yourHealthPoints = yourHealthPoints - newOrcDMG1
                            if guardingFromAttack >= randomizedOrcAttack1:
                                proceed = input("You guarded the previous turn, and parried the enemy's attack! \nYou gain player advantage! [Enter to proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')    
                                    playerTurn()
                            if guardingFromAttack < randomizedOrcAttack1:
                                print("You took:\n")
                                print(newOrcDMG1)
                                print("HP.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')
                                    playerTurn()  
                            if 'No' in guardingYesOrNo:
                                if yourHealthPoints > 0:
                                    yourHealthPoints = yourHealthPoints - leatherReducedOrcAttack1
                                    print("You took:\n")
                                    print(leatherReducedOrcAttack1)
                                    print("HP.")
                                    print("\nYou have:")
                                    print(yourHealthPoints)
                                    proceed = input("HP left. \n[Enter to Proceed.]")
                                    if proceed == "":
                                        playerTurn()     
                    elif 'No Armor' in armor:
                        if 'Yes' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                newOrcDMG1 = randomizedOrcAttack1 - guardingFromAttack
                                yourHealthPoints = yourHealthPoints - newOrcDMG1
                            if guardingFromAttack >= randomizedOrcAttack1:
                                proceed = input("You guarded the previous turn, and parried the enemy's attack! \nYou gain player advantage! [Enter to proceed.]")
                                if proceed == "":    
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')
                                    playerTurn()
                            if guardingFromAttack < randomizedOrcAttack1:
                                print("You took:\n")
                                print(newOrcDMG1)
                                print("HP.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')
                                    playerTurn()  
                        if 'No' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                yourHealthPoints = yourHealthPoints - randomizedOrcAttack1
                                print("You took:\n")
                                print(randomizedOrcAttack1)
                                print("HP.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    playerTurn()        
                if yourHealthPoints < 0:
                    orcDeath = input("You were bludgeoned to death by an orc. \nA cruel and stupid way to go out. Game over. [Enter to Proceed.]")
                    if orcDeath == "":
                        deaths =+ 1
                        MonsterEncountered.clear
                        MonsterHP.clear
                        MonsterSpeed.clear
                        clear_Screen()
                        start_game()

def BabyDragonTurn():
    import random
    global yourHealthPoints
    global ironArmorValue
    global leatherArmorValue
    global guardingYesOrNo
    global armor
    global AlimentList
    global deaths
    global MonsterEncountered
    global MonsterHP
    global MonsterSpeed

    guardingFromAttacksRange = range(5,15)
    guardingFromAttack = random.choice(guardingFromAttacksRange)

    listOfBDAttacks = ['Consecutive Scratching', 'Spit Fire', 'Bite', 'Burning Bite']
    randomizedBDAttack = random.choice(listOfBDAttacks)

    BDAttack1 = range(2,8) #Consecutive Scratching
    randomizedBDAttack1 = random.choice(BDAttack1)
    BDAttack3 = range(9,10) #Spit Fire
    randomizedBDAttack3 = random.choice(BDAttack3)
    BDAttack5 = range(10,20) #Bite
    randomizedBDAttack5 = random.choice(BDAttack5)
    BDAttack7 = range(15,25) #Burning Bite
    randomizedBDAttack7 = random.choice(BDAttack7)

    chanceToWaitBD = (1,100)
    randomizedChanceToWaitBD = random.choice(chanceToWaitBD)

    babyDragonTurn = input("It is the Baby Dragon's turn. [Enter to proceed.]")
    if babyDragonTurn == "":
        if randomizedChanceToWaitBD >= 55:
            bdWaited = input("The Baby Dragon Waited. [Enter to proceed.]")
            if bdWaited == "":
                playerTurn()
        if randomizedChanceToWaitBD <= 56:
            if randomizedBDAttack == 'Bite':
                bdAttack = input("Bite [Enter to proceed.]")
                if bdAttack == "":
                    if 'Iron Armor' in armor:
                        if 'Yes' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                ironReducedBDAttack5 = randomizedBDAttack5 / ironArmorValue
                                newBDDMG1 = ironReducedBDAttack5 - guardingFromAttack
                                yourHealthPoints = yourHealthPoints - newBDDMG1
                            if guardingFromAttack >= randomizedBDAttack5:
                                proceed = input("You guarded the previous turn, and parried the enemy's attack! \nYou gain player advantage! [Enter to proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')    
                                    playerTurn()
                            if guardingFromAttack < randomizedBDAttack5:
                                print("You took:\n")
                                print(newBDDMG1)
                                print("DMG.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')
                                    AlimentList.append('Burn')
                                    playerTurn()  
                        if 'No' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                ironReducedBDAttack5 = randomizedBDAttack5 / ironArmorValue
                                yourHealthPoints = yourHealthPoints - ironReducedBDAttack5
                                print("You took:\n")
                                print(ironReducedBDAttack5)
                                print("DMG.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    AlimentList.append('Burn')
                                    playerTurn()
                    elif 'Leather Armor' in armor:
                        if 'Yes' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                leatherReducedBDAttack5 = randomizedBDAttack5 / leatherArmorValue
                                newBDDMG1 = leatherReducedBDAttack5 - guardingFromAttack
                                yourHealthPoints = yourHealthPoints - newBDDMG1
                            if guardingFromAttack >= randomizedBDAttack5:
                                proceed = input("You guarded the previous turn, and parried the enemy's attack! \nYou gain player advantage! [Enter to proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')    
                                    playerTurn()
                            if guardingFromAttack < randomizedBDAttack5:
                                print("You took:\n")
                                print(newBDDMG1)
                                print("DMG.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')
                                    AlimentList.append('Burn')
                                    playerTurn()  
                        if 'No' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                leatherReducedBDAttack5 = randomizedBDAttack5 / leatherArmorValue
                                yourHealthPoints = yourHealthPoints - leatherReducedBDAttack5
                                print("You took:\n")
                                print(leatherReducedBDAttack5)
                                print("DMG.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    AlimentList.append('Burn')
                                    playerTurn()     
                    elif 'No Armor' in armor:
                        if 'Yes' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                newBDDMG1 = randomizedBDAttack5 - guardingFromAttack
                                yourHealthPoints = yourHealthPoints - newBDDMG1
                            if guardingFromAttack >= randomizedBDAttack5:
                                proceed = input("You guarded the previous turn, and parried the enemy's attack! \nYou gain player advantage! [Enter to proceed.]")
                                if proceed == "":    
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')
                                    playerTurn()
                            if guardingFromAttack < randomizedBDAttack5:
                                print("You took:\n")
                                print(newBDDMG1)
                                print("DMG.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')
                                    AlimentList.append('Burn')
                                    playerTurn()  
                        if 'No' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                yourHealthPoints = yourHealthPoints - randomizedBDAttack5
                                print("You took:\n")
                                print(randomizedBDAttack5)
                                print("DMG.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    AlimentList.append('Burn')
                                    playerTurn()
            if randomizedBDAttack == 'Spit Fire':
                bdAttack = input("Spit Fire [Enter to proceed.]")
                if bdAttack == "":
                    if 'Iron Armor' in armor:
                        if 'Yes' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                ironReducedBDAttack3 = randomizedBDAttack3 / ironArmorValue
                                newBDDMG1 = ironReducedBDAttack3 - guardingFromAttack
                                yourHealthPoints = yourHealthPoints - newBDDMG1
                            if guardingFromAttack >= randomizedBDAttack3:
                                proceed = input("You guarded the previous turn, and parried the enemy's attack! \nYou gain player advantage! [Enter to proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')    
                                    playerTurn()
                            if guardingFromAttack < randomizedBDAttack3:
                                print("You took:\n")
                                print(newBDDMG1)
                                print("DMG.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')
                                    AlimentList.append('Burn')
                                    playerTurn()  
                        if 'No' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                ironReducedBDAttack3 = randomizedBDAttack3 / ironArmorValue
                                yourHealthPoints = yourHealthPoints - ironReducedBDAttack3
                                print("You took:\n")
                                print(ironReducedBDAttack3)
                                print("DMG.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    AlimentList.append('Burn')
                                    playerTurn()
                    elif 'Leather Armor' in armor:
                        if 'Yes' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                leatherReducedBDAttack3 = randomizedBDAttack3 / leatherArmorValue
                                newBDDMG1 = leatherReducedBDAttack3 - guardingFromAttack
                                yourHealthPoints = yourHealthPoints - newBDDMG1
                            if guardingFromAttack >= randomizedBDAttack3:
                                proceed = input("You guarded the previous turn, and parried the enemy's attack! \nYou gain player advantage! [Enter to proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')    
                                    playerTurn()
                            if guardingFromAttack < randomizedBDAttack3:
                                print("You took:\n")
                                print(newBDDMG1)
                                print("DMG.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')
                                    AlimentList.append('Burn')
                                    playerTurn()  
                        if 'No' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                leatherReducedBDAttack3 = randomizedBDAttack3 / leatherArmorValue
                                yourHealthPoints = yourHealthPoints - leatherReducedBDAttack3
                                print("You took:\n")
                                print(leatherReducedBDAttack2)
                                print("DMG.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    AlimentList.append('Burn')
                                    playerTurn()     
                    elif 'No Armor' in armor:
                        if 'Yes' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                newBDDMG1 = randomizedBDAttack3 - guardingFromAttack
                                yourHealthPoints = yourHealthPoints - newBDDMG1
                            if guardingFromAttack >= randomizedBDAttack3:
                                proceed = input("You guarded the previous turn, and parried the enemy's attack! \nYou gain player advantage! [Enter to proceed.]")
                                if proceed == "":    
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')
                                    playerTurn()
                            if guardingFromAttack < randomizedBDAttack3:
                                print("You took:\n")
                                print(newBDDMG1)
                                print("DMG.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')
                                    AlimentList.append('Burn')
                                    playerTurn()  
                        if 'No' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                yourHealthPoints = yourHealthPoints - randomizedBDAttack3
                                print("You took:\n")
                                print(randomizedBDAttack2)
                                print("DMG.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    AlimentList.append('Burn')
                                    playerTurn()
            if randomizedBDAttack == 'Consecutive Scratching':
                bdAttack = input("Consecutive Scratching [Enter to proceed.]")
                if bdAttack == "":
                    if 'Iron Armor' in armor:
                        if 'Yes' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                randomizedBDAttack2 = randomizedBDAttack1 + randomizedBDAttack1 + randomizedBDAttack1
                                ironReducedBDAttack2 = randomizedBDAttack2 / ironArmorValue
                                newBDDMG1 = ironReducedBDAttack2 - guardingFromAttack
                                yourHealthPoints = yourHealthPoints - newBDDMG1
                            if guardingFromAttack >= randomizedBDAttack2:
                                proceed = input("You guarded the previous turn, and parried the enemy's attack! \nYou gain player advantage! [Enter to proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')    
                                    playerTurn()
                            if guardingFromAttack < randomizedBDAttack2:
                                print("You took:\n")
                                print(newBDDMG1)
                                print("DMG.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')
                                    playerTurn()  
                        if 'No' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                randomizedBDAttack2 = randomizedBDAttack1 + randomizedBDAttack1 + randomizedBDAttack1
                                ironReducedBDAttack2 = randomizedBDAttack2 / ironArmorValue
                                yourHealthPoints = yourHealthPoints - ironReducedBDAttack2
                                print("You took:\n")
                                print(ironReducedBDAttack2)
                                print("DMG.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    playerTurn()
                    elif 'Leather Armor' in armor:
                        if 'Yes' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                randomizedBDAttack2 = randomizedBDAttack1 + randomizedBDAttack1 + randomizedBDAttack1
                                leatherReducedBDAttack2 = randomizedBDAttack2 / leatherArmorValue
                                newBDDMG1 = randomizedBDAttack2 - guardingFromAttack
                                yourHealthPoints = yourHealthPoints - newBDDMG1
                            if guardingFromAttack >= randomizedBDAttack2:
                                proceed = input("You guarded the previous turn, and parried the enemy's attack! \nYou gain player advantage! [Enter to proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')    
                                    playerTurn()
                            if guardingFromAttack < randomizedBDAttack2:
                                print("You took:\n")
                                print(newBDDMG1)
                                print("DMG.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')
                                    playerTurn()  
                        if 'No' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                randomizedBDAttack2 = randomizedBDAttack1 + randomizedBDAttack1 + randomizedBDAttack1
                                leatherReducedBDAttack2 = randomizedBDAttack2 / leatherArmorValue
                                yourHealthPoints = yourHealthPoints - leatherReducedBDAttack2
                                print("You took:\n")
                                print(leatherReducedBDAttack2)
                                print("DMG.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    playerTurn()     
                    elif 'No Armor' in armor:
                        if 'Yes' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                randomizedBDAttack2 = randomizedBDAttack1 + randomizedBDAttack1 + randomizedBDAttack1
                                newBDDMG1 = randomizedBDAttack2 - guardingFromAttack
                                yourHealthPoints = yourHealthPoints - newBDDMG1
                            if guardingFromAttack >= randomizedBDAttack2:
                                proceed = input("You guarded the previous turn, and parried the enemy's attack! \nYou gain player advantage! [Enter to proceed.]")
                                if proceed == "":    
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')
                                    playerTurn()
                            if guardingFromAttack < randomizedBDAttack2:
                                print("You took:\n")
                                print(newBDDMG1)
                                print("DMG.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')
                                    playerTurn()  
                        if 'No' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                randomizedBDAttack2 = randomizedBDAttack1 + randomizedBDAttack1 + randomizedBDAttack1
                                yourHealthPoints = yourHealthPoints - randomizedBDAttack2
                                print("You took:\n")
                                print(randomizedBDAttack2)
                                print("DMG.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    playerTurn()        
            if randomizedBDAttack == 'Burning Bite':
                bdAttack = input("Burning Bite [Enter to proceed.]")
                if bdAttack == "":
                    if 'Iron Armor' in armor:
                        if 'Yes' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                ironReducedBDAttack7 = randomizedBDAttack7 / ironArmorValue
                                newBDDMG1 = ironReducedBDAttack7 - guardingFromAttack
                                yourHealthPoints = yourHealthPoints - newBDDMG1
                            if guardingFromAttack >= randomizedBDAttack7:
                                proceed = input("You guarded the previous turn, and parried the enemy's attack! \nYou gain player advantage! [Enter to proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')    
                                    playerTurn()
                            if guardingFromAttack < randomizedBDAttack7:
                                print("You took:\n")
                                print(newBDDMG1)
                                print("DMG.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')
                                    AlimentList.append('Burn')
                                    playerTurn()  
                        if 'No' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                ironReducedBDAttack7 = randomizedBDAttack7 / ironArmorValue
                                yourHealthPoints = yourHealthPoints - ironReducedBDAttack7
                                print("You took:\n")
                                print(ironReducedBDAttack7)
                                print("DMG.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    AlimentList.append('Burn')
                                    playerTurn()
                    elif 'Leather Armor' in armor:
                        if 'Yes' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                leatherReducedBDAttack7 = randomizedBDAttack7 / leatherArmorValue
                                newBDDMG1 = leatherReducedBDAttack7 - guardingFromAttack
                                yourHealthPoints = yourHealthPoints - newBDDMG1
                            if guardingFromAttack >= randomizedBDAttack7:
                                proceed = input("You guarded the previous turn, and parried the enemy's attack! \nYou gain player advantage! [Enter to proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')    
                                    playerTurn()
                            if guardingFromAttack < randomizedBDAttack7:
                                print("You took:\n")
                                print(newBDDMG1)
                                print("DMG.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')
                                    AlimentList.append('Burn')
                                    playerTurn()  
                        if 'No' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                leatherReducedBDAttack7 = randomizedBDAttack7 / leatherArmorValue
                                yourHealthPoints = yourHealthPoints - leatherReducedBDAttack7
                                print("You took:\n")
                                print(leatherReducedBDAttack7)
                                print("DMG.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    AlimentList.append('Burn')
                                    playerTurn()     
                    elif 'No Armor' in armor:
                        if 'Yes' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                newBDDMG1 = randomizedBDAttack7 - guardingFromAttack
                                yourHealthPoints = yourHealthPoints - newBDDMG1
                            if guardingFromAttack >= randomizedBDAttack7:
                                proceed = input("You guarded the previous turn, and parried the enemy's attack! \nYou gain player advantage! [Enter to proceed.]")
                                if proceed == "":    
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')
                                    playerTurn()
                            if guardingFromAttack < randomizedBDAttack7:
                                print("You took:\n")
                                print(newBDDMG1)
                                print("DMG.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    guardingYesOrNo.remove('Yes')
                                    guardingYesOrNo.append('No')
                                    AlimentList.append('Burn')
                                    playerTurn()  
                        if 'No' in guardingYesOrNo:
                            if yourHealthPoints > 0:
                                yourHealthPoints = yourHealthPoints - randomizedBDAttack7
                                print("You took:\n")
                                print(randomizedBDAttack7)
                                print("DMG.")
                                print("\nYou have:")
                                print(yourHealthPoints)
                                proceed = input("HP left. \n[Enter to Proceed.]")
                                if proceed == "":
                                    AlimentList.append('Burn')
                                    playerTurn()            
            if yourHealthPoints < 0:
                bdDeath = input("You were scorched to death by a baby dragon. \nA cruel and stupid way to go out. Game over. [Enter to Proceed.]")
                if bdDeath == "":
                    deaths =+ 1
                    MonsterEncountered.clear
                    MonsterHP.clear
                    MonsterSpeed.clear
                    clear_Screen()
                    start_game()

def ironShortSword():
    import time
    import random

    ironShortSwordRandomized = range(6,18)
    randomizedShortSwordDMG = random.choice(ironShortSwordRandomized)
    
    global MonsterHP
    global MonsterSpeed

    trueMonsterSpeed = MonsterSpeed[0]
    trueMonsterHP = MonsterHP[0]
    trueMonsterEncountered = MonsterEncountered[0]

    critDamageShortSword = range(20,30)
    randomizedCritDamageShortSword = random.choice(critDamageShortSword)

    decideCritlist = ['No Crit', 'No Crit', 'No Crit', 'No Crit', 'No Crit', 'No Crit', 'No Crit', 'No Crit', 'No Crit', 'Crit']
    decideCrit = random.choice(decideCritlist)  

    yourSpeedPoints = range(10,30)
    randomizedPlayerSpeed = random.choice(yourSpeedPoints)

    goblinReward = range(10,25)
    randomizedGobReward = random.choice(goblinReward)
    orcReward = range(20,80)
    randomizedOrcReward = random.choice(orcReward)
    babyDragonReward = range(80,200)
    randomizedBabyDragonReward = random.choice(babyDragonReward)

    if decideCrit == 'No Crit':
        print("\nSlashing.")
        time.sleep(0.3)
        print(' . ')
        time.sleep(0.3)
        print(' ! ')

        if randomizedPlayerSpeed > trueMonsterSpeed:
            trueMonsterHP = trueMonsterHP - randomizedShortSwordDMG #Only does it once correctly
            print("\nYou successfully slashed at the ")
            print(trueMonsterEncountered)
            print("\nDamage done:")
            print(randomizedShortSwordDMG)
            if 'Goblin' in trueMonsterEncountered:
                print("Goblin HP:")
                print(trueMonsterHP)
                GoblinTurn()
            if 'Orc' in trueMonsterEncountered:
                print("Orc HP:")
                print(trueMonsterHP)
                OrcTurn()
            if 'Baby Dragon' in trueMonsterEncountered:
                print("Baby Dragon HP:")
                print(trueMonsterHP)
                BabyDragonTurn()
        
        if randomizedPlayerSpeed < trueMonsterSpeed:
            print("You missed.")
            if 'Goblin' in trueMonsterEncountered:
                print("Goblin HP:")
                print(trueMonsterHP)
                GoblinTurn()
            if 'Orc' in trueMonsterEncountered:
                print("Orc HP:")
                print(trueMonsterHP)
                OrcTurn()
            if 'Baby Dragon' in trueMonsterEncountered:
                print("Baby Dragon HP:")
                print(trueMonsterHP)
                BabyDragonTurn()
    
    if decideCrit == 'Crit':
        print("\nPiercing.")
        time.sleep(0.3)
        print(' . ')
        time.sleep(0.3)
        print(' ! ')

        if randomizedPlayerSpeed > trueMonsterSpeed:
            trueMonsterHP = trueMonsterHP - randomizedCritDamageShortSword
            print("\nYou successfully pierced the ")
            print(trueMonsterEncountered)
            print("!")
            time.sleep(0.3)
            print("\nIt's a critical hit!")
            time.sleep(0.3)
            print("\nDamage done:")
            print(randomizedCritDamageShortSword)
            if trueMonsterEncountered == "Goblin":
                print("Goblin HP:")
                print(trueMonsterHP)
                GoblinTurn()
            if trueMonsterEncountered == "Orc":
                print("Orc HP:")
                print(trueMonsterHP)
                OrcTurn()
            if trueMonsterEncountered == "Baby Dragon":
                print("Baby Dragon HP:")
                print(trueMonsterHP)
                BabyDragonTurn()
        
        if randomizedPlayerSpeed < trueMonsterSpeed:
            print("You missed.")
            if trueMonsterEncountered == "Goblin":
                print("Goblin HP:")
                print(trueMonsterHP)
                GoblinTurn()
            if trueMonsterEncountered == "Orc":
                print("Orc HP:")
                print(trueMonsterHP)
                OrcTurn()
            if trueMonsterEncountered == "Baby Dragon":
                print("Baby Dragon HP:")
                print(trueMonsterHP)
                BabyDragonTurn()
    
    if trueMonsterHP < 0:
        print("The ")
        print(trueMonsterEncountered)
        print(" has been felled!\n")
        print("You gain: ")

        if trueMonsterEncountered == "Goblin":
            print(randomizedGobReward)
            score =+ randomizedGobReward
            print("You now have: ")
            print(score)
            print("G.")

        if trueMonsterEncountered == "Orc":
            print(randomizedOrcReward)
            score =+ randomizedOrcReward
            print("You now have: ")
            print(score)
            print("G.")

        if trueMonsterEncountered == "Baby Dragon":
            print(randomizedBabyDragonReward)
            score =+ randomizedBabyDragonReward
            print("You now have: ")
            print(score)
            print("G.")
            
        felledEnemy = input("\n[Enter to proceed.]")
        felledEnemy == ""
        MonsterEncountered.clear
        MonsterHP.clear
        MonsterSpeed.clear
        clear_Screen()
        daysSpent += 1
        startAdventure()

def woodenBow():
    import time
    import random

    global MonsterHP
    global MonsterSpeed

    trueMonsterSpeed = MonsterSpeed[0]
    trueMonsterHP = MonsterHP[0]
    trueMonsterEncountered = MonsterEncountered[0]

    woodenBowRandomized = range(6,15)
    randomizedWoodenBowDMG = random.choice(woodenBowRandomized)
    
    critDamageWoodenBow = range(20,30)
    randomizedCritWoodenBow = random.choice(critDamageWoodenBow)
    
    decideCritlist = ['No Crit', 'No Crit', 'No Crit', 'No Crit', 'No Crit', 'No Crit', 'No Crit', 'No Crit', 'No Crit', 'Crit']
    decideCrit = random.choice(decideCritlist)  

    yourSpeedPoints = range(10,30)
    randomizedPlayerSpeed = random.choice(yourSpeedPoints)

    goblinReward = range(10,25)
    randomizedGobReward = random.choice(goblinReward)
    orcReward = range(20,80)
    randomizedOrcReward = random.choice(orcReward)
    babyDragonReward = range(80,200)
    randomizedBabyDragonReward = random.choice(babyDragonReward)
    
    if decideCrit == 'No Crit':
        print("\nNocking Arrow.")
        time.sleep(0.3)
        print(' . ')
        time.sleep(0.3)
        print(' ! ')
        time.sleep(0.3)

        print("\nPulling Back.")
        time.sleep(0.2)
        print(' . ')
        time.sleep(0.2)
        print(' ! ')

        print("\nShooting.")
        time.sleep(0.4)
        print(' . ')
        time.sleep(0.4)
        print(' ! ')
        
        if randomizedPlayerSpeed > trueMonsterSpeed:
            trueMonsterHP = trueMonsterHP - randomizedWoodenBowDMG #Only does it once correctly
            print("\nYou successfully shot at the ")
            print(trueMonsterEncountered)
            print("\nDamage done:")
            print(randomizedWoodenBowDMG)
            if 'Goblin' in trueMonsterEncountered:
                print("Goblin HP:")
                print(trueMonsterHP)
                GoblinTurn()
            if 'Orc' in trueMonsterEncountered:
                print("Orc HP:")
                print(trueMonsterHP)
                OrcTurn()
            if 'Baby dragon' in trueMonsterEncountered:
                print("Baby Dragon HP:")
                print(trueMonsterHP)
                BabyDragonTurn()
        
        if randomizedPlayerSpeed < trueMonsterSpeed:
            print("You missed.")
            if 'Goblin' in trueMonsterEncountered:
                print("Goblin HP:")
                print(trueMonsterHP)
                GoblinTurn()
            if 'Orc' in trueMonsterEncountered:
                print("Orc HP:")
                print(trueMonsterHP)
                OrcTurn()
            if 'Baby Dragon' in trueMonsterEncountered:
                print("Baby Dragon HP:")
                print(trueMonsterHP)
                BabyDragonTurn()
    
    if decideCrit == 'Crit':
        print("\nNocking Arrow.")
        time.sleep(0.3)
        print(' . ')
        time.sleep(0.3)
        print(' ! ')
        time.sleep(0.3)

        print("\nPulling Back as far as possible.")
        time.sleep(0.2)
        print(' . ')
        time.sleep(0.2)
        print(' ! ')

        print("\nShooting.")
        time.sleep(0.4)
        print(' . ')
        time.sleep(0.4)
        print(' ! ')

        if randomizedPlayerSpeed > trueMonsterSpeed:
            trueMonsterHP = trueMonsterHP - randomizedCritWoodenBow
            print("\nYou successfully shot at the ")
            print(trueMonsterEncountered)
            print("!")
            time.sleep(0.3)
            print("\nIt's a critical hit!")
            time.sleep(0.3)
            print("\nDamage done:")
            print(randomizedCritWoodenBow)
            if 'Goblin' in trueMonsterEncountered:
                print("Goblin HP:")
                print(trueMonsterHP)
                GoblinTurn()
            if 'Orc' in trueMonsterEncountered:
                print("Orc HP:")
                print(trueMonsterHP)
                OrcTurn()
            if 'Baby Dragon' in trueMonsterEncountered:
                print("Baby Dragon HP:")
                print(trueMonsterHP)
                BabyDragonTurn()
        
        if randomizedPlayerSpeed < trueMonsterSpeed:
            print("You missed.")
            if 'Goblin' in trueMonsterEncountered:
                print("Goblin HP:")
                print(trueMonsterHP)
                GoblinTurn()
            if 'Orc' in trueMonsterEncountered:
                print("Orc HP:")
                print(trueMonsterHP)
                OrcTurn()
            if 'Baby Dragon' in trueMonsterEncountered:
                print("Baby Dragon HP:")
                print(trueMonsterHP)
                BabyDragonTurn()
    
    if trueMonsterHP < 0:
        print("The ")
        print(trueMonsterEncountered)
        print(" has been felled!\n")
        print("You gain: ")

        if 'Goblin' in trueMonsterEncountered:
            print(randomizedGobReward)
            score =+ randomizedGobReward
            print("You now have: ")
            print(score)
            print("G.")

        if 'Orc' in trueMonsterEncountered:
            print(randomizedOrcReward)
            score =+ randomizedOrcReward
            print("You now have: ")
            print(score)
            print("G.")

        if 'Baby Dragon' in trueMonsterEncountered:
            print(randomizedBabyDragonReward)
            score =+ randomizedBabyDragonReward
            print("You now have: ")
            print(score)
            print("G.")
            
        felledEnemy = input("\n[Enter to proceed.]")
        felledEnemy == ""
        MonsterEncountered.clear
        MonsterHP.clear
        MonsterSpeed.clear
        clear_Screen()
        daysSpent += 1
        startAdventure()

def fists():
    import time
    import random

    global MonsterHP
    global MonsterSpeed

    trueMonsterSpeed = MonsterSpeed[0]
    trueMonsterHP = MonsterHP[0]
    trueMonsterEncountered = MonsterEncountered[0]

    fistDamageRandomized = range(0,10)
    fistRandomizedDMG = random.choice(fistDamageRandomized)
    
    critDamageFist = range(11,15)
    randomizedCritDamageFist = random.choice(critDamageFist)

    decideCritlist = ['No Crit', 'No Crit', 'No Crit', 'No Crit', 'No Crit', 'No Crit', 'No Crit', 'No Crit', 'No Crit', 'Crit']
    decideCrit = random.choice(decideCritlist)  

    yourSpeedPoints = range(10,30)
    randomizedPlayerSpeed = random.choice(yourSpeedPoints)

    goblinReward = range(10,25)
    randomizedGobReward = random.choice(goblinReward)
    orcReward = range(20,80)
    randomizedOrcReward = random.choice(orcReward)
    babyDragonReward = range(80,200)
    randomizedBabyDragonReward = random.choice(babyDragonReward) 

    if decideCrit == 'No Crit':
        print("\nPunching.")
        time.sleep(0.3)
        print(' . ')
        time.sleep(0.3)
        print(' ! ')

        if randomizedPlayerSpeed > trueMonsterSpeed:
            trueMonsterHP = trueMonsterHP - fistRandomizedDMG #Only does it once correctly
            print("\nYou successfully punched the ")
            print(trueMonsterEncountered)
            print("\nDamage done:")
            print(fistRandomizedDMG)
            if 'Goblin' in trueMonsterEncountered:
                print("Goblin HP:")
                print(trueMonsterHP)
                GoblinTurn()
            if 'Orc' in trueMonsterEncountered:
                print("Orc HP:")
                print(trueMonsterHP)
                OrcTurn()
            if 'Baby Dragon' in trueMonsterEncountered:
                print("Baby Dragon HP:")
                print(trueMonsterHP)
                BabyDragonTurn()
        
        if randomizedPlayerSpeed < trueMonsterSpeed:
            print("You missed.")
            if 'Goblin' in trueMonsterEncountered:
                print("Goblin HP:")
                print(trueMonsterHP)
                GoblinTurn()
            if 'Orc' in trueMonsterEncountered:
                print("Orc HP:")
                print(trueMonsterHP)
                OrcTurn()
            if 'Baby Dragon' in trueMonsterEncountered:
                print("Baby Dragon HP:")
                print(trueMonsterHP)
                BabyDragonTurn()
    
    if decideCrit == 'Crit':
        print("\nPunching.")
        time.sleep(0.3)
        print(' . ')
        time.sleep(0.3)
        print(' ! ')

        if randomizedPlayerSpeed > trueMonsterSpeed:
            trueMonsterHP = trueMonsterHP - randomizedCritDamageFist
            print("\nYou successfully punched the ")
            print(trueMonsterEncountered)
            time.sleep(0.3)
            print("\nIt's a critical hit!")
            time.sleep(0.3)
            print("\nDamage done:")
            print(randomizedCritDamageFist)
            if 'Goblin' in trueMonsterEncountered:
                print("Goblin HP:")
                print(trueMonsterHP)
                GoblinTurn()
            if 'Orc' in trueMonsterEncountered:
                print("Orc HP:")
                print(trueMonsterHP)
                OrcTurn()
            if 'Baby Dragon' in trueMonsterEncountered:
                print("Baby Dragon HP:")
                print(trueMonsterHP)
                BabyDragonTurn()
        
        if randomizedPlayerSpeed < trueMonsterSpeed:
            print("You missed.")
            if 'Goblin' in trueMonsterEncountered:
                print("Goblin HP:")
                print(trueMonsterHP)
                GoblinTurn()
            if 'Orc' in trueMonsterEncountered:
                print("Orc HP:")
                print(trueMonsterHP)
                OrcTurn()
            if 'Baby Dragon' in trueMonsterEncountered:
                print("Baby Dragon HP:")
                print(trueMonsterHP)
                BabyDragonTurn()
    
    if trueMonsterHP < 0:
        print("The ")
        print(trueMonsterEncountered)
        print(" has been felled!\n")
        print("You gain: ")

        if 'Goblin' in trueMonsterEncountered:
            print(randomizedGobReward)
            score =+ randomizedGobReward
            print("You now have: ")
            print(score)
            print("G.")

        if 'Orc' in trueMonsterEncountered:
            print(randomizedOrcReward)
            score =+ randomizedOrcReward
            print("You now have: ")
            print(score)
            print("G.")

        if 'Baby Dragon' in trueMonsterEncountered:
            print(randomizedBabyDragonReward)
            score =+ randomizedBabyDragonReward
            print("You now have: ")
            print(score)
            print("G.")
            
        felledEnemy = input("\n[Enter to proceed.]")
        felledEnemy == ""
        MonsterEncountered.clear
        MonsterHP.clear
        MonsterSpeed.clear
        clear_Screen()
        daysSpent += 1
        startAdventure()

def ironDagger():
    import time
    import random

    global MonsterHP
    global MonsterSpeed

    trueMonsterSpeed = MonsterSpeed[0]
    trueMonsterHP = MonsterHP[0]
    trueMonsterEncountered = MonsterEncountered[0]

    decideCritlist = ['No Crit', 'No Crit', 'No Crit', 'No Crit', 'No Crit', 'No Crit', 'No Crit', 'No Crit', 'No Crit', 'Crit']
    decideCrit = random.choice(decideCritlist)  

    ironDaggerRandomized = range(6,12)
    randomizedDaggerDMG = random.choice(ironDaggerRandomized)
    
    critDamageDagger = range(18,22)
    randomizedCritDamageDagger = random.choice(critDamageDagger)

    yourSpeedPoints = range(10,30)
    randomizedPlayerSpeed = random.choice(yourSpeedPoints)

    goblinReward = range(10,25)
    randomizedGobReward = random.choice(goblinReward)
    orcReward = range(20,80)
    randomizedOrcReward = random.choice(orcReward)
    babyDragonReward = range(80,200)
    randomizedBabyDragonReward = random.choice(babyDragonReward) 

    if decideCrit == 'No Crit':
        print("\nSlashing.")
        time.sleep(0.3)
        print(' . ')
        time.sleep(0.3)
        print(' ! ')

        if randomizedPlayerSpeed > trueMonsterSpeed:
            trueMonsterHP = trueMonsterHP - randomizedDaggerDMG #Only does it once correctly
            print("\nYou successfully slashed at the ")
            print(MonsterEncountered)
            print("\nDamage done:")
            print(randomizedDaggerDMG)
            if 'Goblin' in trueMonsterEncountered:
                print("Goblin HP:")
                print(trueMonsterHP)
                GoblinTurn()
            if 'Orc' in trueMonsterEncountered:
                print("Orc HP:")
                print(trueMonsterHP)
                OrcTurn()
            if 'Baby Dragon' in trueMonsterEncountered:
                print("Baby Dragon HP:")
                print(trueMonsterHP)
                BabyDragonTurn()
        
        if randomizedPlayerSpeed < trueMonsterSpeed:
            print("You missed.")
            if 'Goblin' in trueMonsterEncountered:
                print("Goblin HP:")
                print(trueMonsterHP)
                GoblinTurn()
            if 'Orc' in trueMonsterEncountered:
                print("Orc HP:")
                print(trueMonsterHP)
                OrcTurn()
            if 'Baby Dragon' in trueMonsterEncountered:
                print("Baby Dragon HP:")
                print(trueMonsterHP)
                BabyDragonTurn()
    
    if decideCrit == 'Crit':
        print("\nPiercing.")
        time.sleep(0.3)
        print(' . ')
        time.sleep(0.3)
        print(' ! ')

        if randomizedPlayerSpeed > trueMonsterSpeed:
            trueMonsterHP = trueMonsterHP - randomizedCritDamageDagger
            print("\nYou successfully pierced the ")
            print(MonsterEncountered)
            time.sleep(0.3)
            print("It's a critical hit!")
            time.sleep(0.3)
            print("\nDamage done:")
            print(randomizedCritDamageDagger)
            if 'Goblin' in trueMonsterEncountered:
                print("Goblin HP:")
                print(trueMonsterHP)
                GoblinTurn()
            if 'Orc' in trueMonsterEncountered:
                print("Orc HP:")
                print(trueMonsterHP)
                OrcTurn()
            if 'Baby Dragon' in trueMonsterEncountered:
                print("Baby Dragon HP:")
                print(trueMonsterHP)
                BabyDragonTurn()
        
        
        if randomizedPlayerSpeed < trueMonsterSpeed:
            print("You missed.")
            if 'Goblin' in trueMonsterEncountered:
                GoblinTurn()
            if 'Orc' in trueMonsterEncountered:
                OrcTurn()
            if 'Baby Dragon' in trueMonsterEncountered:
                BabyDragonTurn()
    
    if MonsterHP < 0:
        print("The ")
        print(MonsterEncountered)
        print(" has been felled!\n")
        print("You gain: ")

        if 'Goblin' in trueMonsterEncountered:
            print(randomizedGobReward)
            score =+ randomizedGobReward
            print("You now have: ")
            print(score)
            print("G.")

        if 'Orc' in trueMonsterEncountered:
            print(randomizedOrcReward)
            score =+ randomizedOrcReward
            print("You now have: ")
            print(score)
            print("G.")

        if 'Baby Dragon' in trueMonsterEncountered:
            print(randomizedBabyDragonReward)
            score =+ randomizedBabyDragonReward
            print("You now have: ")
            print(score)
            print("G.")
            felledEnemy = input("\n[Enter to proceed.]")
            if felledEnemy == "":
                MonsterEncountered.clear
                MonsterHP.clear
                MonsterSpeed.clear
                clear_Screen()
                daysSpent += 1
                startAdventure()

if __name__ == "__main__":
    start_game()