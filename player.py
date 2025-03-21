import math

class Player:

    def __init__(self, name, level=1, experience=100):
        self.name = name
        self.level = level
        self.experience = experience

    def gain_experience(self, amount):
        self.experience += amount
        self.level = self.calculate_level()

    def calculate_level(self):
        exp_table = [100, 300, 600, 1000, 1500, 2100, 2800, 3600, 4500, 5500]
        for i, exp in enumerate(exp_table, start=1):
            if self.experience < exp:
                return i
        return len(exp_table) + 1
    
    '''Множитель атаки'''
    def attack(self):
        return self.level * 10 
    
    '''Формула защиты'''
    def defend(self):
        return math.sqrt(self.experience) * 2  
    
    def show_stats(self):
        return (f"Имя: {self.name}, Уровень: {self.level}, Опыт: {self.experience}, "
                f"Атака: {self.attack()}, Защита: {self.defend():.2f}")
    

class Warrior(Player):

    def __init__(self, name, level=1, experience=100, weapon=10, armor=5):
        super().__init__(name, level, experience)
        self.weapon = weapon
        self.armor = armor

    '''Учитываем оружие'''
    def attack(self):
        return (self.level * self.weapon)  

    '''Учитываем броню'''
    def defend(self):
        return math.log(self.experience + 1) * self.armor  

    def show_info(self):
        return (f"{self.show_stats()}, Оружие: {self.weapon}, Броня: {self.armor}")