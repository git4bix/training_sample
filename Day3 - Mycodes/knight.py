class Character:
    def __init__(self, health=10, strenght=10, defense=10):
        self.health = health
        self.strength = strenght
        self.defense = defense

    def attack(self, other):
        damage = self.strenght - other.defense
        other.health -= damage

class Knight:
    def __init__(self, health =10, defense=10):
        self.health = health
        self.defense = defense

    def attack(self, other):
        damage = self.defense - other.defense
        other.health -= damage


player = Knight(defense=20)
enemy = Character()

if hasattr(player,"attack"):
    print(enemy.health)