from player import Warrior

def main():
    '''Создаем героя'''
    name = input("Введите имя вашего героя: ")
    weapon = int(input("Введите силу оружия: "))
    armor = int(input("Введите уровень брони: "))
    hero = Warrior(name, weapon=weapon, armor=armor)

    while True:
        print("Текущая статистика:")
        print(hero.show_info())

        xp = input("Введите количество опыта для получения (или 'выход' для завершения): ")
        if xp.lower() == "выход":
            print("До свидания!")
            break
        if xp.isdigit():
            hero.gain_experience(int(xp))
        else:
            print("Некорректный ввод. Пожалуйста, введите число.")

if __name__ == "__main__":
    main()