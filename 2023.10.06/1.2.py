from decimal import Decimal
from numbers import Number
from datetime import date, time, datetime

# Переменные для аннотаций
Charges = dict[date, float]

class PowerMeter:
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
        # словарь не пустой, для тестов
        self.charges: Charges = {
            date(2023, 7, 1): 219.75,
            date(2023, 8, 1): 221.75,
            date(2023, 9, 1): 111.75,
        }
        
    
    def meter(self, power: Number) -> Decimal:
        """Вычисляет и возвращает стоимость согласно тарифному плану, действующему в текущий момент
        
        :param power: суммарная потребленная мощность
        :return charge: стоимость согласно тарифному плану
        """
        now = datetime.now()
        if self.tariff2_starts.hour <= now.time().hour < self.tariff2_ends.hour:
            charge = Decimal(power * self.tariff2)
        else:
            charge = Decimal(power * self.tariff1)
    
        key = date(now.year, now.month, 1)
        
        if key in self.charges:
            self.charges[key] += round(charge, 2)
        else:
            self.charges[key] = round(charge, 2)
        return Decimal(charge)

        
    def __repr__(self):
        name = type(self).__name__
        power = sum(float(value) for value in self.charges.values())
        return f'<{name}: {power} кВт/ч>'
    
    
    def __str__(self):
        str_charges = ''
        for dt, power in self.charges.items():
            str_charges += f'({dt.strftime("%B")[:3]}) {power}\n' 
        return str_charges


# >>> pm = PowerMeter()
# >>> pm
# <PowerMeter: 553.25 кВт/ч>
# >>> pm.__str__()
# '(Jul) 219.75\n(Aug) 221.75\n(Sep) 111.75\n'
# >>> print(pm)
# (Jul) 219.75
# (Aug) 221.75
# (Sep) 111.75

# >>> pm.meter(4.5)
# Decimal('21.599999999999997868371792719699442386627197265625')
# >>> pm.__str__()
# '(Jul) 219.75\n(Aug) 221.75\n(Sep) 111.75\n(Oct) 21.60\n'
# >>> pm.meter(5)
# Decimal('24')
# >>> pm.__str__()
# '(Jul) 219.75\n(Aug) 221.75\n(Sep) 111.75\n(Oct) 45.60\n'
# >>> print(pm)
# (Jul) 219.75
# (Aug) 221.75
# (Sep) 111.75
# (Oct) 45.60

# >>> pm.__repr__()
# '<PowerMeter: 598.85 кВт/ч>'
# >>>