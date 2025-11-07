from pydantic import BaseModel, Field

from task_1_fight.main import Warrior, fight


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
