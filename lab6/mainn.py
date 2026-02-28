from abc import ABC, abstractmethod
from random import randint, choice


class Item(ABC):
    def __init__(self, name, health=500):
        self.name = name
        self.health = health

    @abstractmethod
    def attack(self, another_item):
        pass


class Sword(Item):
    def __init__(self, name, attack_power):
        super().__init__(name)
        self.__attack_power = attack_power  
        self._sharp = 0

    def attack(self, another_item):
        damage = self.__attack_power + self._sharp + randint(0, 10)
        another_item.health -= damage
        return f"⚔️ {self.name} б'є на {damage} шкоди. У {another_item.name} HP={another_item.health}"

    def sharpening(self):
        self._sharp += 1
        return f"{self.name} заточено! sharp={self._sharp}"


class Axe(Item):
    def __init__(self, name, attack_power):
        super().__init__(name)
        self.__attack_power = attack_power

    def attack(self, another_item):
        damage = self.__attack_power + randint(0, 20)
        another_item.health -= damage
        return f"🪓 {self.name} рубає на {damage}. У {another_item.name} HP={another_item.health}"


class Bow(Item):
    def __init__(self, name, attack_power, range_power=5):
        super().__init__(name)
        self.__attack_power = attack_power
        self.range_power = range_power

    def attack(self, another_item):
        damage = self.__attack_power + randint(5, 15) + self.range_power
        another_item.health -= damage
        return f"🏹 {self.name} стріляє на {damage}. У {another_item.name} HP={another_item.health}"

    def reload(self):
        self.range_power += 1
        return f"{self.name} підготовлено! range={self.range_power}"


def random_weapon(player_name):
    weapons = [
        Sword(player_name + " Sword", 90),
        Axe(player_name + " Axe", 85),
        Bow(player_name + " Bow", 80)
    ]
    return choice(weapons)



player = random_weapon("Гравець")
enemy = random_weapon("Ворог")

print("🎮 Твоя зброя:", player.name)
print("👾 Зброя ворога:", enemy.name)

turn = 1

while player.health > 0 and enemy.health > 0:
    print(f"\n--- Хід {turn} ---")
    print("1 - Атакувати")
    print("2 - Підсилити")

    choice_user = input("Вибери дію: ")

    if choice_user == "1":
        print(player.attack(enemy))
    else:
        if isinstance(player, Sword):
            print(player.sharpening())
        elif isinstance(player, Bow):
            print(player.reload())
        else:
            print("Сокира не має підсилення 😄")

    if enemy.health <= 0:
        print("\n🏆 ТИ ПЕРЕМІГ!")
        break

    if randint(0, 1) == 0:
        print(enemy.attack(player))
    else:
        if isinstance(enemy, Sword):
            enemy.sharpening()
        elif isinstance(enemy, Bow):
            enemy.reload()

    if player.health <= 0:
        print("\n💀 ВОРОГ ПЕРЕМІГ!")
        break

    turn += 1 

    