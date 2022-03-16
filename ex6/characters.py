import items


class Character():
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
        Function that prints out the info about enemy
        """
        print(f"{self.name} is here!")
        print(self.description)

    def talk(self):
        """
        Function that prints out the conversation line of the enemy
        """
        print(f"[{self.name} says]: {self.conversation}")


class Enemy(Character):
    def set_level(self, level):
        self.level = level

    def set_weakness(self, weakness):
        """
        Function that sets the weakness of the enemy
        """
        self.weakness = weakness


class Friend(Character):
    """
    Friend class. Not used in the program
    """

    def help_level(self, level):
        self.level = level


class Tanya(Friend):
    def help(self, hero):
        print("Thanks for helping me. Here's some water")
        hero.level_up(self.level)
        hero.add_item(items.water)
        return True


tanya = Tanya("Tanya", "Briefly - Sil'po Girl")
tanya.set_conversation(
    "Hi, I'm carrying five bags of chips, 13 kg of apples, 4 milks, and that is only using my left hand")
tanya.help_level(1)


class Drinker(Friend):
    def help(self, hero):
        if items.water in hero.inventory:
            print(
                "Thank you, young man. Here is something for you. *gives you key*")
            hero.add_item(items.key)
            hero.remove_item(items.water)
            hero.level_up(self.level)
            return True
        else:
            print("You can't help him yet. Find some water")
            return False


drinker = Drinker("Drinker", "Grunky man with a bottle of sidr")
drinker.set_conversation("Grrr... Water... I need water...")
drinker.help_level(2)


class Grandma(Friend):
    def help(self, hero):
        if items.sunflower in hero.inventory:
            print("Oh, I'll offer that to those occupants. Thank you")
            hero.remove_item(items.sunflower)
            hero.level_up(self.level)
            return True
        else:
            print("You can't help her yet. Find something for that old lady")
            return False


grandma = Grandma("Grandma", "Lovely woman that sits besides the road")
grandma.set_conversation("Hello Young Man, what a lovely weather!")
grandma.help_level(4)


class Zhora(Friend):
    def help(self, hero):
        if items.chocolate in hero.inventory:
            print(
                "That's a piece of the best chocolate. Maybe Milka. Thank you. Take that Cacao as a gift")
            hero.remove_item(items.chocolate)
            hero.add_item(items.cacao)
            hero.level_up(self.level)
            return True
        else:
            print("You can't help her yet. Find something for that old lady")
            return False


zhora = Zhora("Zhora", "Brutal man with pure heart. Likes chocolate")
zhora.set_conversation(
    "Nice to meet you. For me, Kinder's Santa is the best chocolate in the world")
zhora.help_level(4)


class Gopnik(Enemy):
    def fight(self, item, hero):
        if self.weakness.name == item:
            print("Ok, I see that you are Blatnyi. Take this sunflower and go")
            hero.add_item(items.sunflower)
            hero.remove_item(items.bottle)
            hero.level_up(self.level)
            return True
        else:
            return False


gopnik = Gopnik("Gopnik",
                "Young man in Adidas suit crouches and eats sunflower seeds")
gopnik.set_conversation("He-he, where's your mobila?")
gopnik.set_weakness(items.bottle)
gopnik.set_level(3)
