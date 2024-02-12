class Weapon:
    def __init__(self, name, weapon_type, damage, value):
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value


iron_sword = Weapon("Iron Sword", "sharp", 5, 10)
short_bow = Weapon("Short Bow", "ranged", 4, 8)
unarmed = Weapon("Unarmed", "blunt", 2, 0)
