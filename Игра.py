import random
import logging

logging.basicConfig(filename='Ugadaika.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

def polsovatel():
    while True:
        try:
            k=int(input("Введите максимальное число для загадывания: "))
            n=int(input("Введите количество попыток: "))
            if n<1 or k<1:
                print("Нужно ввести положительные числа, которые больше 0.")
                logging.error(f"!Нужно ввести положительные числа: {k}, {n}")
            else:
                return k,n
        except ValueError:
            print("Нужно ввести натуральные числа.")
            logging.error(f"!Нужно ввести натуральные числа: {k}, {n}")

def play(k,n):
    secret=random.randint(1, k)
    logging.info(f'Компьютер загадал число от 1 до {k} ({secret}). Количество попыток: {n}')
    print(f"Компьютер загадал число от 1 до {k}. Количество попыток: {n}.")
    for popitka in range(1, n + 1):
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
    k,n = polsovatel()
    play(k, n)