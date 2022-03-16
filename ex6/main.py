import game
import characters
import items

global hero
hero = game.Hero("UCUkivets", 1)

ucu = game.UCU("UCU")
ucu.set_description(
    "Ukrainian Catholic University - the most helpful place in the L'viv")
# ucu.set_item()

park = game.Room("Stryiskyi Park")
park.set_description("The park to calm your nerves after tests")
park.set_item(items.bottle)

silpo = game.Room("Sil'po")
silpo.set_description("The source of all goods at the campus of UCU")
silpo.set_character(characters.tanya)

zelena = game.Room("Zelena St.")
zelena.set_description("Zelena St. is a green street, with a lot of busses")
zelena.set_character(characters.grandma)

center = game.Room("Stometrivka")
center.set_description("The loudest place in the town, but with a fountain")
center.set_character(characters.gopnik)

nalyv = game.Room("Nalyvaika St.")
nalyv.set_description(
    "You see the name of the street, there is nothing to say more")
nalyv.set_character(characters.drinker)

lnu = game.Concert("LNU")
lnu.set_description(
    "There is a huge concert in front of LNU. That is, of course, Okean Elzy")

rynok = game.Room("Ploscha Rynok")
rynok.set_description(
    "Street full of coffee and photographers with newsletters")
rynok.set_character(characters.zhora)

ucu.link_room(park, "north")
park.link_room(silpo, "west")
park.link_room(zelena, "north")
zelena.link_room(center, "north")
center.link_room(nalyv, "west")
nalyv.link_room(lnu, "west")
center.link_room(rynok, "east")

current_room = ucu
backpack = []

while hero.dead == False:

    print("\n")
    current_room.get_details()

    if isinstance(current_room, game.UCU):
        ucu.ready_to_exam(hero)

    if isinstance(current_room, game.Concert):
        current_room.concert(hero)
        current_room = current_room.move('east')
        continue

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_room = current_room.move(command)

    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()

    elif command == "fight":
        if isinstance(inhabitant, characters.Enemy):
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()

            # Do I have this item?
            if fight_with in hero.return_equipment():
                if inhabitant.fight(fight_with, hero) == True:
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    current_room.character = None
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    hero.kill()
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")

    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            hero.add_item(item)
            current_room.set_item(None)
        else:
            print("There's nothing here to take!")

    elif command == "items":
        hero.show_equipment()

    elif command == "help":
        if isinstance(inhabitant, characters.Friend):
            if inhabitant.help(hero):
                current_room.character = None
        else:
            print("Sorry, you can't help here anyone")

    else:
        print("I don't know how to " + command)
