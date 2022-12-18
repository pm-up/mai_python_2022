# Напоминание: вам понадобится материал лекций:
# 3 - Списки и кортежи
# 4 - Словари и множества
# 7 и 8 - Классы
# 9 - Работа с файлами

# =====================================
# ЗАДАНИЕ 1: Работа с файлами
# =====================================
# TODO 1-1
#  Прочитайте данные из файла pilot_path.json (лекция 9)

# ВАШ КОД:

import json

with open("pilot_path.json") as f:
    json_data = json.load(f)

# =====================================
# ЗАДАНИЕ 2: Расчет статистик
# =====================================
# TODO 2-1) Подсчитайте, сколько миссий налетал каждый пилот. Выведите результат в порядке убывания миссий
# ИНФОРМАЦИЯ:
# структура данных в файле: {"имя_пилота": "список_миссий":[миссия1, ...]]
# структура одной миссии: {"drone":"модель_дрона", "mission":[список точек миссии]}
# у пилотов неодинаковое количество миссий (и миссии могут быть разной длины). у каждой миссии - произвольная модель дрона

# РЕЗУЛЬТАТ:
# Пилоты в порядке убывания количества миссий: {'pilot3': 6, 'pilot8': 6, 'pilot6': 5, 'pilot2': 5, 'pilot7': 4, 'pilot9': 3, 'pilot5': 3, 'pilot4': 2, 'pilot1': 1}

# ВАШ КОД:

with open("pilot_path.json") as f:
    json_data = json.load(f)
    pilot_mission_dict = {}
    for pilot in json_data:
        pilot_missions_count = 0
        missions = json_data[pilot]
        for missions_tag in missions:
             mission_info = (missions[missions_tag])
             pilot_mission_dict[pilot] = len(mission_info)
    print(f"Пилоты в порядке убывания количества миссий: {dict(sorted(pilot_mission_dict.items(), key=lambda item: item[1], reverse=True))}")


# подсказка: готовый код нужной вам сортировки есть здесь (Sample Solution-1:): https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.php
#print(f"Пилоты в порядке убывания количества миссий: {dict(sorted(pilot_mission_dict.items(), key=lambda item: item[1], reverse=True))}")

# TODO 2-2) Получите и выведите список всех моделей дронов, которые были в файле pilot_path.json
# Подсказка: внутри print используйте str.join(), чтобы соединить элементы списка (множества)

# РЕЗУЛЬТАТ:
# Полеты совершались на дронах следующих моделей: DJI Mavic 2 Pro, DJI Mavic 3, DJI Inspire 2, DJI Mavic 2 Zoom, DJI Mavic 2 Enterprise Advanced

# ВАШ КОД:

list_of_models = []
with open("pilot_path.json") as f:
    json_data = json.load(f)
    for pilot in json_data:
        pilot_missions_count = 0
        missions = json_data[pilot]
        for missions_tag in missions:
            mission_info = (missions[missions_tag])
            for drone_info in mission_info:
                for info_tag in drone_info:
                    if info_tag == "drone":
                        drone_name = drone_info[info_tag]
                        list_of_models.append(drone_name)
    print(f'Полеты совершались на дронах следующих моделей: {", ".join(set(list_of_models))}')

# вывод результата (допишите код)
#print(f'Полеты совершались на дронах следующих моделей: {", ".join(...)}')

# TODO 2-3) Получите список миссий для каждой модели дронов, которые были в файле pilot_path.json,
# и выведите на экран модель дрона и количество миссий, которые он отлетал

# РЕЗУЛЬТАТ:
# Дрон DJI Inspire 2 отлетал 6 миссий
# Дрон DJI Mavic 2 Pro отлетал 6 миссий
# Дрон DJI Mavic 2 Enterprise Advanced отлетал 10 миссий
# Дрон DJI Mavic 3 отлетал 4 миссий
# Дрон DJI Mavic 2 Zoom отлетал 9 миссий

# ВАШ КОД:

mission_list_DJI_Inspire_2 = []
mission_list_DJI_Mavic_2_Pro = []
mission_list_DJI_Mavic_2_Enterprise_Advanced = []
mission_list_DJI_Mavic_3 = []
mission_list_DJI_Mavic_2_Zoom = []

count_DJI_Mavic_3 = 0
count_DJI_Mavic_2_Zoom = 0
with open("pilot_path.json") as f:
    json_data = json.load(f)
    for pilot in json_data:
        pilot_missions_count = 0
        missions = json_data[pilot]
        for missions_tag in missions:
            mission_info = (missions[missions_tag])
            for drone_info in mission_info:
                if drone_info['drone'] == "DJI Inspire 2":
                    mission_list_DJI_Inspire_2.append(drone_info['mission'])
                if drone_info['drone'] == "DJI Mavic 2 Pro":
                    mission_list_DJI_Mavic_2_Pro.append(drone_info['mission'])
                if drone_info['drone'] == "DJI Mavic 2 Enterprise Advanced":
                    mission_list_DJI_Mavic_2_Enterprise_Advanced.append(drone_info['mission'])
                if drone_info['drone'] == "DJI Mavic 3":
                    mission_list_DJI_Mavic_3.append(drone_info['mission'])
                if drone_info['drone'] == "DJI Mavic 2 Zoom":
                    mission_list_DJI_Mavic_2_Zoom.append(drone_info['mission'])

d = {'DJI Inspire 2':len(mission_list_DJI_Inspire_2), 'DJI Mavic 2 Pro':len(mission_list_DJI_Mavic_2_Pro), 'DJI Mavic 2 Enterprise Advanced':len(mission_list_DJI_Mavic_2_Enterprise_Advanced),'DJI Mavic 3':len(mission_list_DJI_Mavic_3),'DJI Mavic 2 Zoom':len(mission_list_DJI_Mavic_2_Zoom)}
for i in d:
    print(f'Дрон {i} отлетал {d[i]} миссий')

# вывод результата (допишите код)
#print(f'Дрон {...} отлетал {...} миссий')

# =====================================
# ЗАДАНИЕ 3: Создание классов
# =====================================
# Для вас уже написаны заготовки классов Aircraft и UAV
# TODO 3-1) Добавьте в класс UAV защищенный атрибут _=_missions (тип - список списков [[], []]), куда вы будете сохранять все миссии, которые отлетал беспилотник
# TODO 3-2) При помощи декоратора @property сделайте возможность чтения и записи миссий в этот атрибут (лекция 8)
# TODO 3-3) Создайте в классе UAV публичный метод count_missions, который возвращает количество миссий (лекция 7)
# TODO 3-4) Создайте класс MultirotorUAV - наследник классов Aircraft и UAV (лекция 7)

# ВАШ КОД (дополните то, что нужно в классах):
class Aircraft:
    def __init__(self, weight):
        self._weight = weight

class UAV:
    def __init__(self):
        self._has_autopilot = True
        self._missions = []

	# напишите код для декоратора атрибута _missions
    @property
    def missions(self):
        return self._missions

	# напишите публичный метод count_missions
    def count_missions(self):
        return(len(self._missions))

class MultirotorUAV(Aircraft, UAV):
    def __init__(self, weight, model, brand):
        super().__init__(weight)
        UAV.__init__(self)
        self.__weight = weight
        self.__model = model
        self.__brand = brand

	# напишите публичный метод get_info
    def get_info(self):
        info = {"weight": self.__weight, "brand": self.__brand}
        return(info)

	# напишите публичный метод get_model
    def get_model(self):
        full_model_name = self.__brand + " " + self.__model
        return(full_model_name)

# =====================================
# ЗАДАНИЕ 4: Работа с экземплярами классов
# =====================================
# TODO 4-1) Создайте экземпляры класса MultirotorUAV для всех моделей дронов, которые были в файле pilot_path.json
# Подсказка: созданные экземпляры класса MultirotorUAV сохраните в список для последующего использования
# TODO 4-2) При создании каждого экземпляра задайте ему как приватные атрибуты массу и производителя из справочника дронов drone_catalog в соответствии с моделью дрона
# TODO 4-3) А также добавьте ему миссии, найденные для этой модели дрона на шаге 2-3
# Напоминание: миссии находятся в атрибуте missions (с декоратором, и поэтому он публично доступен) в классе UAV

# каталог дронов уже готов для вас:
drone_catalog = {
	"DJI Mavic 2 Pro": {"weight":903, "brand":"DJI"},
	"DJI Mavic 2 Zoom": {"weight":900, "brand":"DJI"},
	"DJI Mavic 2 Enterprise Advanced": {"weight":920, "brand":"DJI"},
	"DJI Inspire 2": {"weight":1500, "brand":"DJI"},
	"DJI Mavic 3": {"weight":1000, "brand":"DJI"}
}

# ВАШ КОД:
DJI_Mavic_2_Pro = MultirotorUAV(drone_catalog["DJI Mavic 2 Pro"]["weight"], "Mavic 2 Pro", drone_catalog["DJI Mavic 2 Pro"]["brand"])
DJI_Mavic_2_Zoom = MultirotorUAV(drone_catalog["DJI Mavic 2 Zoom"]["weight"], "Mavic 2 Zoom", drone_catalog["DJI Mavic 2 Zoom"]["brand"])
DJI_Mavic_2_Enterprise_Advanced = MultirotorUAV(drone_catalog["DJI Mavic 2 Enterprise Advanced"]["weight"], "Mavic 2 Enterprise Advanced", drone_catalog["DJI Mavic 2 Enterprise Advanced"]["brand"])
DJI_Inspire_2 = MultirotorUAV(drone_catalog["DJI Inspire 2"]["weight"], "Inspire 2", drone_catalog["DJI Inspire 2"]["brand"])
DJI_Mavic_3 = MultirotorUAV(drone_catalog["DJI Mavic 3"]["weight"], "Mavic 3", drone_catalog["DJI Mavic 3"]["brand"])

DJI_Mavic_2_Pro.missions.extend(mission_list_DJI_Mavic_2_Pro)
DJI_Mavic_2_Zoom.missions.extend(mission_list_DJI_Mavic_2_Zoom)
DJI_Mavic_2_Enterprise_Advanced.missions.extend(mission_list_DJI_Mavic_2_Enterprise_Advanced)
DJI_Inspire_2.missions.extend(mission_list_DJI_Inspire_2)
DJI_Mavic_3.missions.extend(mission_list_DJI_Mavic_3)

list_of_drone_objects = [DJI_Mavic_2_Pro, DJI_Mavic_2_Zoom, DJI_Mavic_2_Enterprise_Advanced, DJI_Inspire_2, DJI_Mavic_3]


# TODO 4-4
# Напишите код, который выводит информацию по заданной модели дрона. Состав информации: масса, производитель, количество отлетанных миссий
# (название модели пользователь вводит с клавиатуры в любом регистре, но без опечаток)
# Подсказка: для этого вам необходимо вернуться в ЗАДАНИЕ 3 и добавить в класс два публичных метода: get_info(), который выводит нужную информацию,
# и get_model, который позволит получить название модели дрона

# РЕЗУЛЬТАТ:
# Информация о дроне DJI Mavic 2 Pro: масса 903, производитель DJI, количество миссий 6

# ВАШ КОД:
user_unput = input("Введите модель дрона (полностью) в любом регистре\n")
drone_name = ((user_unput.lower()).title()).replace("Dji", "DJI")

for drone in list_of_drone_objects:
    if drone_name == drone.get_model():
        print(f"Информация о дроне {drone_name}: масса {(drone.get_info())['weight']}, производитель {(drone.get_info())['brand']}, количество миссий {drone.count_missions()}")
