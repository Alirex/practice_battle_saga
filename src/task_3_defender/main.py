from pydantic import BaseModel, Field


class Warrior(BaseModel):
    health: int = 50
    attack: int = 5

    @property
    def is_alive(self) -> bool:
        return self.health > 0

    def receive_damage(self, damage: int) -> None:
        self.health -= damage


class Knight(Warrior):
    attack: int = 7


class Defender(Warrior):
    health: int = 60
    attack: int = 3
    defense: int = 2

    def receive_damage(self, damage: int) -> None:
        damage_fact = damage - self.defense
        if damage_fact > 0:
            self.health -= damage_fact


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


def fight(w1: Warrior, w2: Warrior) -> bool:
    while w1.is_alive and w2.is_alive:
        w2.receive_damage(w1.attack)
        if w2.is_alive:
            w1.receive_damage(w2.attack)
    return w1.is_alive
