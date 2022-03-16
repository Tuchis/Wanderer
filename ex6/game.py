"""
The Module to make possible running of the script.py
"""
import time
import items


class Hero():
    """
    Hero class. Not used in the program
    """

    def __init__(self, name, level):
        """
        Init function
        """
        self.name, self.level = name, level
        self.inventory = []
        self.dead = False

    def show_equipment(self):
        """
        Function to show show inventory
        """
        print(f"Your inventory: {', '.join(x.name for x in self.inventory)}")
        print(f"Your level is: {self.level}")

    def return_equipment(self):
        return [item.name for item in self.inventory]

    def add_item(self, item):
        """
        Function that adds items to the inventory
        """
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    def level_up(self, level=1):
        self.level += level

    def kill(self):
        self.dead = True


class Room():
    """
    Room class. Contains information about every 'level' of a game
    """

    def __init__(self, name):
        """
        Init function
        """
        self.name = name
        self.linked_rooms = []
        self.character = None
        self.item = None

    def set_description(self, description):
        """
        Function that sets description of the room
        """
        self.description = description

    def link_room(self, room, side):
        """
        Function that links rooms with sides of the world
        """
        self.linked_rooms.append([room, side])
        sides = [["north", "south"], ["south", "north"], ["east", "west"],
                 ["west", "east"]]
        for elem in sides:
            if elem[0] == side:
                opposite_side = elem[1]
        room.linked_rooms.append([self, opposite_side])

    def get_details(self):
        """
        Function that prints out the details about the room
        """
        print(self.name)
        print("-" * 20)
        print(self.description)
        for room in self.linked_rooms:
            print(f"The {room[0].name} is {room[1]}")

    def set_character(self, character):
        """
        The function that sets a certain character into certain room
        """
        self.character = character

    def get_character(self):
        """
        Function that returns info about character in the room
        """
        return self.character

    def set_item(self, item):
        """
        The function that sets a certain item into certain room
        """
        self.item = item

    def get_item(self):
        """
        Function that returns info about item in the room
        """
        return self.item

    def move(self, side):
        """
        Function that realizes movement between rooms
        """
        return \
            [[self] + [room[0] for room in self.linked_rooms if
                       room[1] == side]][
                0][-1]


class UCU(Room):
    def ready_to_exam(self, hero):
        if hero.level >= 10 and items.cacao in hero.inventory and items.key in hero.inventory:
            print("Hooray. You passed the EXAM. You have 100 points. Have a rest now")
            hero.kill()
        else:
            print(f"You have to get ready to EXAM. You need at least level 10 "
                  f"and have something good to drink. Also, you need an old "
                  f"key for your suitcase to get your laptop\n"
                  f"When you have that, get back into UCU")


class Concert(Room):
    def concert(self, hero):
        hero.add_item(items.chocolate)
        hero.level_up(2)
        print(
            "OMG. You are at Okean Elzy concert. Congratulations. Sing that lyrics and you will get free gift")
        time.sleep(5)
        lyrics = ["Не питай", "Де я був коли тобі було так солодко",
                  "Де я був коли тебе таку незайману", "Підіймали вище неба",
                  "Тільки сам на сам", "Хіба не там", "Просто мені",
                  "Так хочеться", "Бути там де і ти", "Так хочеться",
                  "Жити в тебе в полоні", "І бачити",
                  "Як тікають від мене сни",
                  "В твої долоні"]
        for line in lyrics:
            print(line)
            time.sleep(3)
