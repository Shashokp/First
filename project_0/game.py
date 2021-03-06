import numpy as np

def random_predict(number:int=1) -> int:
    """randomly guess the number

    Args:
        number (int, optional): fictional number. Defaults to 1.

    Returns:
        int: number of retries
    """
    
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)

print(f'Количество попыток: {random_predict()}')