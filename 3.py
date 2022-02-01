from timeit import timeit

s = 'from collections import deque'
count = 10000
print('list.append', timeit('lst.append(1000)', 'lst = list(range(1000))', number=count), 'deque.append',
      timeit('my_deque.append(9999)', s + '\nmy_deque = deque(list(range(100000)))', number=count))
print('list.pop', timeit('lst.pop()', 'lst = list(range(1000000))', number=count), 'deque.pop',
      timeit('my_deque.pop()', s + '\nmy_deque = deque(list(range(1000000)))', number=count))
print('list.extend', timeit('lst.extend(add)', 'lst = list(range(1000))\n'
                                               'add = list(range(500, 700))', number=count), 'deque.extend',
      timeit('my_deque.extend(add)',
             s + '\nmy_deque = deque(list(range(1000)))\n'
                 'add = list(range(500, 700))', number=count))

print('*' * 50)
print('list.insert(appendleft)', timeit('lst.insert(0, 555)', 'lst = list(range(1000))', number=count), 'deque.appendleft',
      timeit('my_deque.appendleft(555)', s + '\nmy_deque = deque(list(range(1000)))', number=count))

print('list.popleft', timeit('lst.pop(0)', 'lst = list(range(100000))', number=count), 'deque.popleft',
      timeit('my_deque.popleft()', s + '\nmy_deque = deque(list(range(100000)))', number=count))

'''
В соответствии с замерами работает быстрее deque

list.append 0.0006171000131871551 deque.append 0.00061779998941347
list.pop 0.0004186000151094049 deque.pop 0.00039909998304210603
list.extend 0.045217800012324005 deque.extend 0.015736500005004928
**************************************************
list.insert(appendleft) 0.021682099992176518 deque.appendleft 0.000391399982618168
list.popleft 2.50617730000522 deque.popleft 0.0003915000124834478

'''