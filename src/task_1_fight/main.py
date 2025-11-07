import dataclasses


@dataclasses.dataclass
class Warrior:
    health: int = 50
    attack: int = 5

    @property
    def is_alive(self) -> bool:
        return self.health > 0


@dataclasses.dataclass
class Knight(Warrior):
    attack: int = 7


def fight(
    warrior_1: Warrior,
    warrior_2: Warrior,
) -> bool:  # sourcery skip: remove-redundant-if
    """Fight between two warriors.

    Return True if first_warrior is alive, False otherwise.
    """
    while warrior_1.is_alive and warrior_2.is_alive:
        warrior_2.health -= warrior_1.attack
        if warrior_2.is_alive:
            warrior_1.health -= warrior_2.attack

    return warrior_1.is_alive
