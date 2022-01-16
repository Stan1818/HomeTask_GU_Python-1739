class QueueClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


class Tasks:
    def __init__(self):
        self.logs = []
        self.cur_tasks = QueueClass()
        self.revision_tasks = QueueClass()

    def add_current_task(self, item):
        self.cur_tasks.to_queue(item)

    def current_task(self):
        return print(f'Текущая задача: {self.cur_tasks.elems[len(self.cur_tasks.elems) - 1]}')

    def resolve_task(self):
        task = self.cur_tasks.from_queue()
        self.logs.append(task)

    def rev_task(self):
        task = self.cur_tasks.from_queue()
        self.revision_tasks.to_queue(task)

    def from_rev(self):
        task = self.revision_tasks.from_queue()
        self.cur_tasks.to_queue(task)

    def current_revision(self):
        return print(f'Задачи в доработке: {self.revision_tasks.elems[len(self.revision_tasks.elems) - 1]}')

    def view_logs(self):
        return print(f'Закрытые задачи: {self.logs}')


if __name__ == '__main__':
    tasks = Tasks()
    tasks.add_current_task("t1")
    tasks.add_current_task("t2")
    tasks.add_current_task("t3")
    tasks.add_current_task("t4")
    tasks.add_current_task("t5")
    tasks.add_current_task("t6")
    tasks.add_current_task("t7")
    tasks.current_task()
    tasks.resolve_task()
    tasks.current_task()
    tasks.rev_task()
    tasks.current_task()
    tasks.current_revision()
    tasks.resolve_task()
    tasks.current_task()
    tasks.view_logs()
