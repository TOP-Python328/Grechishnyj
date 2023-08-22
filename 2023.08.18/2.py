def taxi_cost(distanse: int, wait_time: int=0) -> int | None:
    """Функция вычисляет и возвращает значение стоимости поезки в такси"""
    
    if distanse < 0 or wait_time < 0:
        return None
       
    base_cost = 80
    dist_cost = distanse / 150 * 6
    wait_cost = wait_time * 3
    fine_cost = 80 
    
    return round(base_cost + dist_cost + wait_cost if distanse else wait_cost + base_cost + fine_cost)

# >>> taxi_cost(1500)
# 140

# >>> taxi_cost(2560)
# 182

# >>> taxi_cost(0, 5)
# 175

# >>> taxi_cost(42130, 8)
# 1789

# >>> print(taxi_cost(-300))
# None

# >>> taxi_cost(distanse=1500, wait_time=5)
# 155

# >>> taxi_cost(wait_time=5, distanse=1500)
# 155

# >>> taxi_cost(wait_time=5)
# TypeError: taxi_cost() missing 1 required positional argument: 'distanse'