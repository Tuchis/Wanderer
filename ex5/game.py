"""
The Module to make possible running of the main.py
"""

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

    def show_equipment(self):
        """
        Function to show show inventory
        """
        print(f"Your inventory: {', '.join(x.name for x in self.inventory)}")

    def add_item(self, item):
        """
        Function that adds items to the inventory
        """
        self.inventory.append(item)

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

    def get_details(self):
        """
        Function that prints out the details about the room
        """
        print(self.name)
        print("-"*20)
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
        return [[self] + [room[0] for room in self.linked_rooms if room[1] == side]][0][-1]


class Friend():
    """
    Friend class. Not used in the program
    """
    def __init__(self, name, description):
        """
        Init function
        """
        self.name, self.description = name, description

    def set_conversation(self, conversation):
        """
        Function that sets conversation for the friend
        """
        self.conversation = conversation

    def describe(self):
        """
        Function that prints out the info about friend
        """
        print(f"{self.name} is here!")
        print(self.description)

    def talk(self):
        """
        Function that prints out the conversation line of the friend
        """
        print(f"[{self.name} says]: {self.conversation}")

class Enemy():
    _defeated_enemies = 0

    def __init__(self, name, description):
        """
        Init function
        """
        self.name, self.description = name, description

    def set_conversation(self, conversation):
        """
        Function that sets conversation for the friend
        """
        self.conversation = conversation

    def set_weakness(self, weakness):
        """
        Function that sets the weakness of the enemy
        """
        self.weakness = weakness

    def describe(self):
        """
        Function that prints out the info about enemy
        """
        print(f"{self.name} is here!")
        print(self.description)

    def talk(self):
        """
        Function that prints out the conversation line of the enemy
        """
        print(f"[{self.name} says]: {self.conversation}")

    def fight(self, fight_with):
        """
        Function that returns the outcome of the fight with the enemy
        """
        return fight_with == self.weakness

    def get_defeated(self):
        """
        Function that counts defeated enemies by hero
        """
        self.__class__._defeated_enemies += 1
        return self.__class__._defeated_enemies

class Item():
    """
    Item class
    """
    def __init__(self, name):
        """
        Init function
        """
        self.name = name

    def set_description(self, description):
        """
        Function to set the description for the item
        """
        self.description = description

    def describe(self):
        """
        Function that prints out the info about the item
        """
        print(f"The {self.name} is here! - {self.description}")

    def get_name(self):
        """
        Function that returns the name of the item
        """
        return self.name