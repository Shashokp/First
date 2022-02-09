'''Игра компьютер угадает число меньше чем за 20 попыток'''

import numpy as np

def random_predict() -> int:
    min = 1
    max = 101

    number = np.random.randint(min, max)
    # number = 77
    count = 0
    while True:
        count+=1
        mid = round((min+max) / 2)
        
        if mid > number:
            max = mid
        
        elif mid < number:
            min = mid

        else:
            #print(f"Компьютер угадал число за {count} попыток. Это число {number}")
            return(count) #break #конец игры выход из цикла   
        
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали списоконлайн переводчик чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")    

if __name__ == '__main__':
    score_game(random_predict)