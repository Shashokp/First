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
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    j = 0
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    # random_array = np.random.randint(1, 101, size=(10000))  # загадали списоконлайн переводчик чисел
    while j<1000:
        j += 1
        count_ls.append(random_predict())

    score = int(np.mean(count_ls))
    print(score)    

if __name__ == '__main__':
    score_game(random_predict)
