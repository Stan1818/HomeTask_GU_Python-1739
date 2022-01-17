class Stacks:
    def __init__(self, max):
        self.max = max
        self.stack = [[]]

    def __str__(self):
        return str(self.stack)

    def count_st(self):
        return print(f'Число стеков {len(self.stack)}')

    def size_st(self):
        size = 0
        for stack in self.stack:
            size += len(stack)
        return print(f'Число элементов {size}')

    def clear(self):
        self.stack.clear()
        self.stack = [[]]

    def add(self, stack):
        if len(self.stack[len(self.stack) - 1]) < self.max:
            self.stack[len(self.stack) - 1].append(stack)
        else:
            self.stack.append([])
            self.stack[len(self.stack) - 1].append(stack)

    def delete(self):
        result = self.stack[len(self.stack) - 1].pop()
        if len(self.stack[len(self.stack) - 1]) == 0:
            self.stack.pop()
        return result


if __name__ == '__main__':
    s = Stacks(3)
    print(s)
    s.add('s1')
    s.add('s2')
    s.add('s3')
    s.add('s4')
    s.add('s5')
    s.add('s6')
    s.add('s7')
    print(s)
    s.count_st()
    s.size_st()
    s.clear()
    print(s)

    s.add('s1')
    s.add('s2')
    s.add('s3')
    s.add('s4')
    s.add('s5')
    s.add('s6')
    s.add('s7')
    print(s)
    s.delete()
    print(s)
