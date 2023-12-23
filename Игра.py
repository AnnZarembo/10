import random
import logging

logging.basicConfig(filename='Ugadaika.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

def polsovatel():
    while True:
        try:
            n=int(input("Введите максимальное число для загадывания: "))
            k=int(input("Введите количество попыток: "))
            if k<1 or n<1:
                print("Нужно ввести положительные числа, которые больше 0.")
                logging.error(f"!Нужно ввести положительные числа: {n}, {k}")
            else:
                return n,k
        except ValueError:
            print("Нужно ввести натуральные числа.")
            logging.error(f"!Нужно ввести натуральные числа: {n}, {k}")

def play(n,k):
    secret=random.randint(1, n)
    logging.info(f'Компьютер загадал число от 1 до {n} ({secret}). Количество попыток: {k}')
    print(f"Компьютер загадал число от 1 до {n}. Количество попыток: {k}.")
    for popitka in range(1, k + 1):
        dogadka = int(input(f"Попытка {popitka}. Угадайте число: "))
        logging.info(f'Попытка {popitka}: {dogadka}')
        if dogadka > secret:
            print("Загаданное число меньше")
            logging.info("Загаданное число меньше")
        elif dogadka < secret:
            print("Загаданное число больше")
            logging.info("Загаданное число больше")
        else:
            print("Вы угадали!")
            logging.info('Игра завершена: победа')
            return
    print(f"Попытки закончились. Загаданное число: {secret}")
    logging.info('Вы проиграли :(')
if __name__ == "__main__":
    n,k = polsovatel()
    play(n,k)