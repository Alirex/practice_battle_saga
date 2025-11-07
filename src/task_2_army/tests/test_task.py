from task_1_fight.main import Knight, Warrior
from task_2_army.main import Army, Battle


def test_army() -> None:
    army_1 = Army()
    army_2 = Army()
    army_1.add_units(Warrior, 20)
    army_2.add_units(Warrior, 21)
    battle = Battle()
    battle.fight(army_1, army_2)
    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)
    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)
    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)
    army_4 = Army()
    army_4.add_units(Warrior, 30)
    battle = Battle()

    assert battle.fight(my_army, enemy_army)
    assert battle.fight(my_army, enemy_army)
