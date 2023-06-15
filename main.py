# импорт для неизменяемости некоторых начальных структур
# from typing import Final

import psycopg2


# класс, описывающий станцию
class Station:
    def __init__(self, station_id: int, name: str, neighbours: list, line: int):
        self.__station_id = station_id
        self.__name = name
        self.__neighbours = neighbours
        self.__line = line
        self.__weight = float('inf')

    @property
    def station_id(self):
        return self.__station_id

    @property
    def name(self):
        return self.__name

    @property
    def neighbours(self):
        return self.__neighbours

    @neighbours.setter
    def neighbours(self, new_value):
        self.__neighbours = new_value

    @property
    def line(self):
        return self.__line

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_value: int):
        self.__weight = new_value


# STATIONS: Final = (
#     Station(1, 'Заельцовская', ['Гагаринская'], 1),
#     Station(2, 'Гагаринская', ['Заельцовская', 'Красный проспект'], 1),
#     Station(3, 'Красный проспект', ['Гагаринская', 'Площадь Ленина', 'Сибирская'], 1),
#     Station(4, 'Площадь Ленина', ['Красный проспект', 'Октябрьская'], 1),
#     Station(5, 'Октябрьская', ['Площадь Ленина', 'Речной вокзал'], 1),
#     Station(6, 'Речной вокзал', ['Октябрьская', 'Студенческая'], 1),
#     Station(7, 'Студенческая', ['Речной вокзал', 'Площадь Маркса'], 1),
#     Station(8, 'Площадь Маркса', ['Студенческая'], 1),
#     Station(9, 'Площадь Гарина-Михайловского', ['Cибирская'], 2),
#     Station(10, 'Сибирская', ['Площадь Гарина-Михайловского', 'Маршала Покрышкина', 'Красный проспект'], 2),
#     Station(11, 'Маршала Покрышкина', ['Сибирская', 'Берёзовая роща'], 2),
#     Station(12, 'Берёзовая роща', ['Маршала Покрышкина', 'Золотая нива'], 2),
#     Station(13, 'Золотая нива', ['Берёзовая роща'], 2)
# )

# STATIONS: Final = (
#     Station(1, 'Заельцовская', [2], 1),
#     Station(2, 'Гагаринская', [1, 3], 1),
#     Station(3, 'Красный проспект', [2, 4, 10], 1),
#     Station(4, 'Площадь Ленина', [3, 5], 1),
#     Station(5, 'Октябрьская', [4, 6], 1),
#     Station(6, 'Речной вокзал', [5, 7], 1),
#     Station(7, 'Студенческая', [8, 6], 1),
#     Station(8, 'Площадь Маркса', [7], 1),
#     Station(9, 'Площадь Гарина-Михайловского', [10], 2),
#     Station(10, 'Сибирская', [9, 11, 3], 2),
#     Station(11, 'Маршала Покрышкина', [10, 12], 2),
#     Station(12, 'Берёзовая роща', [11, 13], 2),
#     Station(13, 'Золотая нива', [12], 2)
# )
#
# DISTANCE: Final = {
#     frozenset([1, 2]): 1,
#     frozenset([2, 3]): 2,
#     frozenset([3, 4]): 2,
#     frozenset([4, 5]): 2,
#     frozenset([5, 6]): 2,
#     frozenset([6, 7]): 4,
#     frozenset([7, 8]): 1,
#     frozenset([9, 10]): 2,
#     frozenset([10, 11]): 2,
#     frozenset([11, 12]): 2,
#     frozenset([12, 13]): 3,
#     frozenset([3, 10]): 3
# }

def data_from_db(table: str, city: str) -> list:
    conn = psycopg2.connect(
        dbname='stations',
        host="localhost",
        user="postgres",
        password="postgres",
        port="5432"
    )
    cur = conn.cursor()

    cur.execute(f"SELECT * FROM {table} WHERE city = '{city}'")
    data = cur.fetchall()

    cur.close()
    conn.close()

    return data


STATIONS = list()

for i in data_from_db('stations', 'Санкт-Петербург'):
    STATIONS.append(Station(i[0], i[1], i[2], i[3]))

DISTANCE = dict()

for i in data_from_db('distance', 'Санкт-Петербург'):
    DISTANCE[frozenset(i[1])] = i[2]

TRANSFERS = list()

for i in data_from_db('distance', 'Санкт-Петербург'):
    if i[4] is True:
        TRANSFERS.append(set(i[1]))


# STATIONS = data_from_db('stations', 'Санкт-Петербург')

# кортеж, содержащий информацию о станциях Петербургского метрополитена
# STATIONS: Final = (
#     Station(1, 'Девяткино', [2], 1),
#     Station(2, 'Гражданский проспект', [1, 3], 1),
#     Station(3, 'Академическая', [2, 4], 1),
#     Station(4, 'Политехническая', [3, 5], 1),
#     Station(5, 'Площадь Мужества', [4, 6], 1),
#     Station(6, 'Лесная', [5, 7], 1),
#     Station(7, 'Выборгская', [8, 6], 1),
#     Station(8, 'Площадь Ленина', [7, 9], 1),
#     Station(9, 'Чернышевская', [8, 10], 1),
#     Station(10, 'Площадь Восстания', [9, 11, 43], 1),
#     Station(11, 'Владимирская', [10, 12, 51], 1),
#     Station(12, 'Пушкинская', [11, 13, 65], 1),
#     Station(13, 'Технологический институт - 1', [12, 14, 30], 1),
#     Station(14, 'Балтийская', [13, 15], 1),
#     Station(15, 'Нарвская', [14, 16], 1),
#     Station(16, 'Кировский завод', [15, 17], 1),
#     Station(17, 'Автово', [16, 18], 1),
#     Station(18, 'Ленинский проспект', [17, 19], 1),
#     Station(19, 'Проспект Ветеранов', [18], 1),
#     Station(20, 'Парнас', [21], 2),
#     Station(21, 'Проспект Просвещения', [20, 22], 2),
#     Station(22, 'Озерки', [21, 23], 2),
#     Station(23, 'Удельная', [22, 24], 2),
#     Station(24, 'Пионерская', [23, 25], 2),
#     Station(25, 'Чёрная речка', [24, 26], 2),
#     Station(26, 'Петроградская', [25, 27], 2),
#     Station(27, 'Горьковская', [26, 28], 2),
#     Station(28, 'Невский проспект', [27, 29, 42], 2),
#     Station(29, 'Сенная площадь', [28, 30, 50, 64], 2),
#     Station(30, 'Технологический институт - 2', [29, 31, 13], 2),
#     Station(31, 'Фрунзенская', [30, 32], 2),
#     Station(32, 'Московские ворота', [31, 33], 2),
#     Station(33, 'Электросила', [32, 34], 2),
#     Station(34, 'Парк Победы', [33, 35], 2),
#     Station(35, 'Московская', [34, 36], 2),
#     Station(36, 'Звёздная', [35, 37], 2),
#     Station(37, 'Купчино', [36], 2),
#     Station(38, 'Беговая', [39], 3),
#     Station(39, 'Зенит', [38, 40], 3),
#     Station(40, 'Приморская', [39, 41], 3),
#     Station(41, 'Василеостровская', [40, 42], 3),
#     Station(42, 'Гостиный двор', [41, 43, 28], 3),
#     Station(43, 'Маяковская', [42, 44, 10], 3),
#     Station(44, 'Площадь Александра Невского - 1', [43, 45, 53], 3),
#     Station(45, 'Елизаровская', [44, 46], 3),
#     Station(46, 'Ломоносовская', [45, 47], 3),
#     Station(47, 'Пролетарская', [46, 48], 3),
#     Station(48, 'Обухово', [47, 49], 3),
#     Station(49, 'Рыбацкое', [48], 3),
#     Station(50, 'Спасская', [51, 29, 64], 4),
#     Station(51, 'Достоевская', [50, 52, 11], 4),
#     Station(52, 'Лиговский проспект', [51, 53], 4),
#     Station(53, 'Площадь Александра Невского - 2', [52, 54, 44], 4),
#     Station(54, 'Новочеркасская', [53, 55], 4),
#     Station(55, 'Ладожская', [54, 56], 4),
#     Station(56, 'Проспект Большевиков', [55, 57], 4),
#     Station(57, 'Улица Дыбенко', [56], 4),
#     Station(58, 'Комендантский проспект', [59], 5),
#     Station(59, 'Старая Деревня', [58, 60], 5),
#     Station(60, 'Крестовский остров', [59, 61], 5),
#     Station(61, 'Чкаловская', [60, 62], 5),
#     Station(62, 'Спортивная', [61, 63], 5),
#     Station(63, 'Адмиралтейская', [62, 64], 5),
#     Station(64, 'Садовая', [63, 65, 29, 50], 5),
#     Station(65, 'Звенигородская', [64, 66, 12], 5),
#     Station(66, 'Обводный канал', [65, 67], 5),
#     Station(67, 'Волковская', [66, 68], 5),
#     Station(68, 'Бухарестская', [67, 69], 5),
#     Station(69, 'Международная', [68, 70], 5),
#     Station(70, 'Проспект Славы', [69, 71], 5),
#     Station(71, 'Дунайская', [70, 72], 5),
#     Station(72, 'Шушары', [71], 5)
# )

# словарь с информацией о времени прохождения перегона
# (или пешего перехода) между соседними станциями (в минутах)
# DISTANCE: Final = {
#     frozenset([1, 2]): 4,
#     frozenset([2, 3]): 3,
#     frozenset([3, 4]): 2,
#     frozenset([4, 5]): 2,
#     frozenset([5, 6]): 3,
#     frozenset([6, 7]): 4,
#     frozenset([7, 8]): 2,
#     frozenset([8, 9]): 3,
#     frozenset([9, 10]): 3,
#     frozenset([10, 11]): 2,
#     frozenset([11, 12]): 2,
#     frozenset([12, 13]): 2,
#     frozenset([13, 14]): 2,
#     frozenset([14, 15]): 3,
#     frozenset([15, 16]): 4,
#     frozenset([16, 17]): 2,
#     frozenset([17, 18]): 3,
#     frozenset([18, 19]): 2,
#     frozenset([20, 21]): 3,
#     frozenset([21, 22]): 3,
#     frozenset([22, 23]): 3,
#     frozenset([23, 24]): 3,
#     frozenset([24, 25]): 3,
#     frozenset([25, 26]): 3,
#     frozenset([26, 27]): 2,
#     frozenset([27, 28]): 4,
#     frozenset([28, 29]): 2,
#     frozenset([29, 30]): 2,
#     frozenset([30, 31]): 2,
#     frozenset([31, 32]): 3,
#     frozenset([32, 33]): 2,
#     frozenset([33, 34]): 2,
#     frozenset([34, 35]): 3,
#     frozenset([35, 36]): 5,
#     frozenset([36, 37]): 3,
#     frozenset([38, 39]): 4,
#     frozenset([39, 40]): 4,
#     frozenset([40, 41]): 4,
#     frozenset([41, 42]): 4,
#     frozenset([42, 43]): 3,
#     frozenset([43, 44]): 3,
#     frozenset([44, 45]): 4,
#     frozenset([45, 46]): 3,
#     frozenset([46, 47]): 4,
#     frozenset([47, 48]): 3,
#     frozenset([48, 49]): 4,
#     frozenset([50, 51]): 4,
#     frozenset([51, 52]): 2,
#     frozenset([52, 53]): 2,
#     frozenset([53, 54]): 3,
#     frozenset([54, 55]): 3,
#     frozenset([55, 56]): 4,
#     frozenset([56, 57]): 3,
#     frozenset([58, 59]): 4,
#     frozenset([59, 60]): 3,
#     frozenset([60, 61]): 3,
#     frozenset([61, 62]): 2,
#     frozenset([62, 63]): 3,
#     frozenset([63, 64]): 3,
#     frozenset([64, 65]): 2,
#     frozenset([65, 66]): 3,
#     frozenset([66, 67]): 2,
#     frozenset([67, 68]): 3,
#     frozenset([68, 69]): 3,
#     frozenset([69, 70]): 2,
#     frozenset([70, 71]): 3,
#     frozenset([71, 72]): 3,
#     frozenset([10, 43]): 3,
#     frozenset([11, 51]): 3,
#     frozenset([12, 65]): 3,
#     frozenset([13, 30]): 2,
#     frozenset([28, 42]): 4,
#     frozenset([29, 50]): 4,
#     frozenset([29, 64]): 3,
#     frozenset([44, 53]): 3,
#     frozenset([50, 64]): 3
# }


# функция нахождения объекта класса Station по его ID
def find_station_by_id(id_of_station: int) -> Station:
    return list(filter(lambda x: x.station_id == id_of_station, STATIONS))[0]


# функция нахождения расстояния в DISTANCE нужного перегона (перехода)
def find_distance(station1_id: int, station2_id: int) -> int:
    return DISTANCE[frozenset([station1_id, station2_id])]


# функция подсчёта весов станций по весам рёбер (алгоритм Дейкстры)
def loop(finish: int, queue: list, path: dict, passed_nodes: list) -> dict:
    if queue:
        station = find_station_by_id(queue.pop(0))
        passed_nodes.append(station.station_id)

        gen_not_passed_neighbours = (x for x in station.neighbours if x not in passed_nodes)

        for i in gen_not_passed_neighbours:
            queue.append(i)

            if find_station_by_id(i).weight >= \
                    station.weight + find_distance(station.station_id, i):
                find_station_by_id(i).weight = \
                    station.weight + find_distance(station.station_id, i)
                path[find_station_by_id(i).station_id] = station.station_id

        return loop(finish, queue, path, passed_nodes)

    else:
        return path


# функция, переворачивающая полученный путь
# нужна такая функция, потому что loop() выдаёт путь в обратном порядке
def reverse_path(dict_path: dict, result: list, station_id: int, finish_id: int) -> list:
    result.append(station_id)

    if station_id == finish_id:
        return result
    else:
        return reverse_path(dict_path, result, dict_path[station_id], finish_id)


# функция, получающая правильный путь
def starting(start: int, finish: int) -> list:
    find_station_by_id(start).weight = 0
    result_of_loop = loop(finish, [start], {}, [])
    result_of_starting = reverse_path(result_of_loop, [], finish, start)
    return list(reversed(result_of_starting))
    # print(loop(finish, [start], {}, []))


start_station_str: str = input("Starting station: ")
start_station: int = list(filter(lambda x: x.name == start_station_str.title(), STATIONS))[0].station_id
finish_station_str: str = input("End station: ")
finish_station: int = list(filter(lambda x: x.name == finish_station_str.title(), STATIONS))[0].station_id

final_path: list = starting(start_station, finish_station)
# print('Path:', final_path)

all_weights: list = list(map(lambda x: x.weight, STATIONS))
# print('Weight:', all_weights[finish_station - 1])


def ui(path):
    print(f"Время в пути (в минутах): {all_weights[finish_station - 1]}")
    print(f"Начало пути - станция {STATIONS[path[0] - 1].name} "
          f"(линия {STATIONS[path[0] - 1].line})")
    for i in range(len(path) - 1):
        if {path[i], path[i+1]} in TRANSFERS:
            print(f"Пересадка между станциями "
                  f"'{STATIONS[path[i] - 1].name}' (линия {STATIONS[path[i] - 1].line}) и "
                  f"'{STATIONS[path[i+1] - 1].name}' (линия {STATIONS[path[i+1] - 1].line})")
            # print(f"Пересадка между станциями {path[i]} и {path[i+1]}")

    print(f"Конец пути - станция {STATIONS[path[len(path) - 1] - 1].name} "
          f"(линия {STATIONS[path[len(path) - 1] - 1].line})")


ui(final_path)
