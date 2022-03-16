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

water = Item("water")
water.set_description("The healing potion, that cures your souls injuries")

bottle = Item("bottle")
bottle.set_description("Dangerous bottle, that may be great at scaring enemies")

key = Item("old key")
key.set_description("Old key, that may open some interesting places")

sunflower = Item("sunflower")
sunflower.set_description("The crunchy seeds, that look great in the graves of russian soldiers")

chocolate = Item("chocolate")
chocolate.set_description("The bar of great dark chocolate. Great for melting")

cacao = Item("cacao")
cacao.set_description("Your favorite drink. Always makes you feel better")