from pydantic import BaseModel, Field


class Warrior(BaseModel):
    health: int = 50
    attack: int = 5

    @property
    def is_alive(self) -> bool:
        return self.health > 0

    def receive_damage(self, damage: int) -> int:
        """Receive damage and return the amount of damage that was dealt."""
        damage_fact = min(damage, self.health)
        self.health -= damage_fact

        return damage_fact

    def do_attack(self, target: Warrior) -> int:
        """Do attack and return the amount of damage dealt."""
        return target.receive_damage(self.attack)


class Knight(Warrior):
    attack: int = 7


class Defender(Warrior):
    health: int = 60
    attack: int = 3
    defense: int = 2

    def receive_damage(self, damage: int) -> int:
        damage_after_defence = damage - self.defense
        damage_after_defence = max(damage_after_defence, 0)

        return super().receive_damage(damage_after_defence)


class Vampire(Warrior):
    health: int = 40
    attack: int = 4
    vampirism: int = Field(default=50, description="Percentage of health restored from the inflicted damage.")

    def do_attack(self, target: Warrior) -> int:
        damage_of_target = super().do_attack(target)

        self.health += damage_of_target * self.vampirism // 100

        return damage_of_target


def fight(w1: Warrior, w2: Warrior) -> bool:
    while w1.is_alive and w2.is_alive:
        w1.do_attack(w2)
        if w2.is_alive:
            w2.do_attack(w1)
    return w1.is_alive


class Army(BaseModel):
    # TODO: (?) Rework to queue.Queue
    units: list[Warrior] = Field(default_factory=list)

    def add_units(self, unit_type: type[Warrior], count: int) -> None:
        for _ in range(count):
            self.units.append(unit_type())


class Battle(BaseModel):
    @staticmethod
    def fight(army_1: Army, army_2: Army) -> bool:
        """Fight between two armies.

        Return True if army_1 has units, False otherwise.
        """
        while army_1.units and army_2.units:
            unit_1 = army_1.units[0]
            unit_2 = army_2.units[0]

            if fight(unit_1, unit_2):
                army_2.units.pop(0)
            else:
                army_1.units.pop(0)

        return len(army_1.units) > 0
