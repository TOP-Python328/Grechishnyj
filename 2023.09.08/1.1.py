from datetime import datetime as dt, timedelta as td


def schedule(
        dt_first: dt, 
        week_day: int, 
        *week_days: int, 
        total_days: int, 
        dt_format: str='%d/%m/%Y'
    ) -> list[str]:
    """Функция расчитывает график дат еженедельно повторяющихся событий."""
    
    week_days = week_day, *week_days
    list_days = [dt_first.strftime(dt_format)]
    

    while len(list_days) < total_days:
        for day in week_days:
            this_day = dt_first + td(days=1)
            if this_day.isoweekday() == day:
                list_days.append(this_day.strftime(dt_format))   
        dt_first = dt_first + td(days=1)
    
    return list_days
    

# >>> vacations = [
# ...     (dt(2023, 5, 1), td(weeks=1)),
# ...     (dt(2023, 7, 17), td(weeks=1))
# ... ]
# >>> py328 = schedule(dt(2023, 4, 1), 6, week_days = 7, total_days = 70)
# >>> len(py328)
# 70
# >>> py328[28:32]
# ['08/07/2023', '09/07/2023', '15/07/2023', '16/07/2023']