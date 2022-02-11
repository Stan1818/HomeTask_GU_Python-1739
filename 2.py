class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка и проверка
    def insert_left(self, check):
        try:
            if check > self.root:
                raise ValueError
        except ValueError:
            print(f'{check} больше корня {self.root}')
            return f'Ошибка'
        # если у узла нет левого потомка
        if self.left_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(check)
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(check)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

        # добавить правого потомка и проверить на валидации

    def insert_right(self, check):
        try:
            if check < self.root:
                raise ValueError
        except ValueError:
            print(f'{check} меньше корня {self.root}')
            return f'Ошибка'
        # если у узла нет правого потомка
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(check)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(check)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


bt = BinaryTree(10)
print(bt.get_root_val())
bt.insert_left(25)
bt.insert_left(3)
bt.insert_right(12)
bt.insert_right(8)
print(bt.get_left_child().get_root_val())
print(bt.get_right_child().get_root_val())
bt.get_right_child().set_root_val(15)
bt.get_right_child().insert_right(2222)
print(bt.get_right_child().get_root_val())
bt.get_right_child().insert_left(1222)
print(bt.get_right_child().get_right_child().get_root_val())