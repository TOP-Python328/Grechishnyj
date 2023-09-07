def central_tendency(num1: float, num2: float, /, *numbers: float) -> dict[str, float]:
    """Функция вычисляет основные меры центральной тенденции для коллекции чисел."""
    sample = (num1, num2, *numbers)
    sorted_sample = sorted(sample)
    length_sample = len(sample)
    center_index = length_sample // 2
    
    product_num_sample = 1
    sum_inverse_sample = 0
    # ИСПОЛЬЗОВАТЬ: оператор not in
    if 0 not in sample:
        for num in sample:
            product_num_sample *= num
            sum_inverse_sample += 1 / num
    else:
        product_num_sample = 0

    # ИСПОЛЬЗОВАТЬ: классическую условную конструкцию
    if length_sample % 2:
        median = float(sorted_sample[center_index])
    else:
        median = (sorted_sample[center_index] + sorted_sample[center_index-1]) / 2
    return {
        'median': median, 
        'arithmetic': sum(sample) / length_sample,
        'geometric': product_num_sample ** (1 / length_sample),
        'harmonic': length_sample / sum_inverse_sample if sum_inverse_sample else 0.0
    }


# >>> central_tendency(1, 2, 3, 4, 5)
# {'median': 3.0, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}

# >>> central_tendency(1, 2, 3, 4)
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.2133638394006434, 'harmonic': 1.9200000000000004}

# >>> sample = [1, 2, 3, 4, 5]
# >>> central_tendency(*sample)
# {'median': 3.0, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}

# >>> sample = [num / 1.2 for num in range(1, 500, 3)]
# >>> central_tendency(*sample)
# {'median': 208.33333333333334, 'arithmetic': 208.33333333333314, 'geometric': inf, 'harmonic': 50.61200774946092}

# >>> central_tendency(1)
# TypeError: central_tendency() missing 1 required positional argument: 'num2'

# >>> central_tendency(1, 0)
# {'median': 0.5, 'arithmetic': 0.5, 'geometric': 0.0, 'harmonic': 0.0}

