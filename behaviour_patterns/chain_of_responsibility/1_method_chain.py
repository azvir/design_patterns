class Creature:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f'{self.name} ({self.attack}/{self.defense})'


class CreatureModifier:
    def __init__(self, creature):
        self.creature = creature
        self.next_modifier = None

    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()


class DoubleAttackCreature(CreatureModifier):
    def handle(self):
        self.creature.attack *= 2
        print(f'Doubling {self.creature.name} attack')
        super().handle()


class IncreaseAttackCreature(CreatureModifier):
    def handle(self):
        if self.creature.attack <= 2:
            self.creature.attack += 1
        super().handle()


class NoBonusesCreature(CreatureModifier):
    def handle(self):
        print(f'No bonuses for you')


if __name__ == "__main__":
    goblin = Creature('Goblin', 1, 1)
    print(goblin)

    root = CreatureModifier(goblin)
    root.add_modifier(NoBonusesCreature(goblin))
    root.add_modifier(DoubleAttackCreature(goblin))
    root.add_modifier(DoubleAttackCreature(goblin))
    root.add_modifier(IncreaseAttackCreature(goblin))
    root.handle()
    print(goblin)

