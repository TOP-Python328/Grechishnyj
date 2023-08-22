def numbers_strip(numbers: list[float], n: int=1, *, copy=False) -> list:
    """Функция удаляет N минимальных и N максимальных чисел из списка"""

    work_list = numbers.copy() if copy else numbers
    
    for _ in range(n):
        work_list.remove(min(work_list))
        work_list.remove(max(work_list))
        
    return work_list
    
    

# >>> sample = [1, 2, 3, 4]
# >>> sample_stripped = numbers_strip(sample)
# >>> sample_stripped
# [2, 3]
# >>> sample is sample_stripped
# True

# >>> sample = [10, 20, 30, 40, 50]
# >>> sample_stripped = numbers_strip(sample, 2, copy=True)
# >>> sample_stripped
# [30]
# >>> sample is sample_stripped
# False

# >>> sample = [-10.56, -10.05, 10.30, -40.25, 50.62, 2.15, 65.36, 65]
# >>> sample_stripped = numbers_strip(sample, round(len(sample) / 3), copy=True)
# >>> sample_stripped
# [10.3, 2.15]
# >>> sample is sample_stripped
# False