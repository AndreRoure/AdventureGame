import time

import random


def gameSetup():
    weapons = ["The Powerfull Spear of Queen Aurora",
               "The Almighty Sword of The Forgotten Knight",
               "The Legendary Bow of The Shadow"]
    monsters = ["the Werewolf", "the Dragon", "the Witch", "the army of Orcs",
                "the Barbarians"]
    locations = ["The Military Camp", "The Village of Valen Oak",
                 "The Trading Post"]
    setup = []
    for s in [weapons, monsters, locations]:
        setup.append(random.choice(s))
    return setup


def print_pause(message):
    print(message)
    time.sleep(2)


def validInput(validInput1, validInput2, message):
    while True:
        inpt = input(message).lower()
        if validInput1 in inpt:
            break
        elif validInput2 in inpt:
            break
        else:
            print_pause("Are you speaking the language of dragons? You are not"
                        " making sense.")
    return inpt


def intro(setup):
    print_pause("You are leaving your house when a messager comes running in"
                " your direction.")
    print_pause("'Hurry warrior the kingdom needs your help!'")
    print_pause("'" + setup[2] + " is being attacked by " + setup[1] + "!'")
    print_pause("You get your old sword, mounts your horse, and heads into "
                "your adventure.")


def game():
    setup = gameSetup()
    intro(setup)
    adventureStart(setup)


def playagain():
    input = validInput("y", "n", "Do you want to play again?\n")
    if "y" in input:
        game()


def gameover():
    print_pause("GAME OVER")
    playagain()


def victory(setup):
    print_pause("VICTORY!")
    print_pause("Congratulations on slaying " + setup[1])
    print_pause("You are now the Savior of " + setup[2])
    playagain()


def bossFight(setup, gotWeapon, spidersHelp):
    print_pause("While you are advancing, " + setup[1] +
                " is salying innocent citizens")
    print_pause("It notices you and go for an attack.")

    if gotWeapon:
        print_pause("You reach for " + setup[0])
        print_pause("The enemy is surprised by your powerfull weapon.")
        print_pause("It is inevitable, " + setup[1] + " become easy prey.")
        victory(setup)

    elif spidersHelp:
        print_pause("You go for your sword.")
        print_pause("But the " + setup[1] + " knocks you down.")
        print_pause("You look up expecting certain death.")
        print_pause("But " + setup[1] + " is trapped in webs.")
        print_pause("The spiders retreating to the cavern salute you "
                    "with a strange growl.")
        print_pause("And you go for the easy kill.")
        victory(setup)

    elif gotWeapon is False:
        print_pause("You go for your sword.")
        print_pause("But " + setup[1] + " is much more powerfull.")
        print_pause("You became one of the victims.")
        gameover()


def mine(setup):
    print_pause("You enter the mine.")
    print_pause("You notices something shining in a minecart.")
    print_pause("You go insvestigate.")
    print_pause("You find " + setup[0])
    print_pause("That certainly will be useful agaisnt " + setup[1])
    print_pause("You take the minecart to exit the mountain.")
    gotWeapon = True
    spidersHelp = False
    bossFight(setup, gotWeapon, spidersHelp)


def waydown(setup):
    print_pause("You climb down the mountain.")
    print_pause("As you reach the ground " + setup[1] + " is waiting for you.")
    gotWeapon = False
    spidersHelp = False
    bossFight(setup, gotWeapon, spidersHelp)


def passage(setup):
    print_pause("You climb up the mountain.")
    print_pause("As you reach the top you notice two ways to go on:")
    print_pause("A way down the mountain where you can see your objective.")
    print_pause("And a mine that goes inside the mountain.")
    input = validInput("down", "mine", "Where do you go?\n")
    if "down" in input:
        waydown(setup)
    elif "mine" in input:
        mine(setup)


def run():
    print_pause("You start running.")
    print_pause("The spiders easily trap you.")
    print_pause("You get your sword to fight.")
    print_pause("But webs starts coming from everywhere.")
    print_pause("Sorry... you became spider food.")
    gameover()


def aproach(setup):
    print_pause("You aproach the spiders.")
    print_pause("They rapidly scatter.")
    print_pause("But one stands in the same place.")
    print_pause("You notice it is trapped in a beartrap.")
    print_pause("You help it get free.")
    print_pause("The spiders appreciates the assistance and show you the"
                " way out.")
    spidersHelp = True
    gotWeapon = False
    bossFight(setup, gotWeapon, spidersHelp)


def cavern(setup):
    print_pause("You enter the cavern.")
    print_pause("As you reach the heart of the cavern you notice "
                "strange noises.")
    print_pause("You are surrounded by spiders!")
    print_pause("They start moving towards you.")
    print_pause("You can run or you can aproach them.")
    input = validInput("run", "aproach", "What do you do?\n")

    if "run" in input:
        run()

    elif "aproach" in input:
        aproach(setup)


def adventureStart(setup):
    print_pause("In your way to slay " + setup[1] + ", a mountain posed as"
                " an obstacle.")
    print_pause("You notice two ways to proceed:")
    print_pause("The first is a cavern entrace nearby.")
    print_pause("The other is a passage up the mountain.")
    input = validInput("passage", "cavern", "Where do you go?\n")

    if "passage" in input:
        passage(setup)

    elif "cavern" in input:
        cavern(setup)


game()
