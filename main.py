from player import Player

def main():
    
    '''Создаем игрока'''
    name = input("Введите имя вашего героя: ")
    player = Player(name)

    while True:
        print("Текущая статистика:")
        print(player.show_stats())
        xp = input("Введите количество опыта для получения (или 'выход' для завершения): ")
        if xp.lower() == 'выход':
            print("До свидания!")
            break
        if xp.isdigit():
            player.gain_experience(int(xp))
        else:
            print("Некорректный ввод. Пожалуйста, введите число.")

if __name__ == "__main__":
    main()