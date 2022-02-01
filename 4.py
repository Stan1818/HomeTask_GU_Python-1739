from timeit import timeit

s = 'from collections import OrderedDict'
print('Генерация DICT - ', timeit('{i:i for i in range(1000)}', number=1000), 'ORDER_DICT - ',
      timeit('OrderedDict((i, i) for i in range(1000))', s, number=1000))
print('Добавление DICT - ', timeit('for i in range(1001, 2000): d[i]=i', 'd={i:i for i in range(1000)}', number=1000),
      'ORDER_DICT - ',
      timeit('for i in range(1001, 2000):ord_d[i]=i', s + '\nord_d=OrderedDict((i, i) for i in range(1000))',
             number=1000))
print('Удаление DICT - ', timeit('d.popitem()', 'd={i:i for i in range(1000)}', number=1000), 'ORDER_DICT - ',
      timeit('ord_d.popitem()', s + '\nord_d=OrderedDict((i, i) for i in range(1000))', number=1000))


"""
Генерация DICT -   0.04906900000059977    ORDER_DICT -    0.2073759999984759
Добавление DICT -  0.061020400004053954   ORDER_DICT -    0.09326870000222698
Удаление DICT -    8.699999307282269e-05  ORDER_DICT -    0.00013079999916953966

Обычный словарь работает быстрее в Python 3.10


"""