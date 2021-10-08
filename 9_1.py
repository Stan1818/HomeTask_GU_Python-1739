import time


class TrafficLight:

    def __init__(self):
        self.__color = ['Красный', 'Желтый', 'Зеленый']

    def run(self):
        i = 0
        while i != 3:
            if self.__color[i] == 'Красный':
                print(self.__color[i])
                time.sleep(7)
            elif self.__color[i] == 'Желтый':
                print(self.__color[i])
                time.sleep(3)
            elif self.__color[i] == 'Зеленый':
                print(self.__color[i])
                time.sleep(2)
            i = i + 1
        print('*' * 25, 'FINISH', '*' * 25)


a = TrafficLight()
a.run()
print(a._TrafficLight__color[1])
