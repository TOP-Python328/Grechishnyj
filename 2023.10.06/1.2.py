from decimal import Decimal
from numbers import Number
from datetime import date, time, datetime

# Переменные для аннотаций
Charges = dict[date, float]

class PowerMetr:
    """Описывает двухтарифный счётчик потребленной электрической мощности""" 
    
    def __init__(self):
        """
        :attr tariff1: первый тариф 
        :attr tariff2: второй тариф
        :attr tariff2_starts: время начала действия второго тарифа
        :attr tariff2_ends: время окончания действия второго тарифа
        """
        self.tariff1: Number = 6.51
        self.tariff2: Number = 4.80
        self.tariff2_starts: time = time(7)
        self.tariff2_ends: time = time(23)
        self.charges: Charges = {}
        
    
    def meter(self, power: Number) -> Decimal:
        """Вычисляет и возвращает стоимость согласно тарифному плану, действующему в текущий момент
        
        :param power: суммарная потребленная мощность
        :return charge: стоимость согласно тарифному плану
        """

        now = datetime.now()
        if self.tariff2_starts.hour <= now.time().hour < self.tariff2_ends.hour:
            charge = power * self.tariff2
        else:
            charge = power * self.tariff1

        key = date(now.year, now.month, 1)
        if key in self.charges:
            self.charges[key] += round(charge, 2)
        else:
            self.charges[key] = round(charge, 2)
            

        print(f'{self.charges=}')
        return charge

# >>> pm = PowerMetr()
# >>> pm.meter(5)
# self.charges={datetime.date(2023, 10, 1): 24.0}
# 24.0
# >>> pm.meter(5)
# self.charges={datetime.date(2023, 10, 1): 48.0}
# 24.0
# >>> pm.meter(3.324)
# self.charges={datetime.date(2023, 10, 1): 63.96}
# 15.955199999999998