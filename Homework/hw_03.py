import csv
import json
import re
import os
import touch

class Aircraft:
    def __init__(self, weight):
        self._weight = weight

class UAV:    
    def __init__(self):
        self._has_autopilot = True
        self._missions = []

    @property
    def missions(self):
        return self._missions

    def count_missions(self):
        return(len(self._missions))

	# напишите код для декоратора атрибута _missions
	#...

	# напишите публичный метод count_missions
	#...

class MultirotorUAV(Aircraft, UAV):
    def __init__(self, weight, model, brand):
        super().__init__(weight)
        UAV.__init__(self)
        self.__weight = weight
        self.__model = model
        self.__brand = brand
        self.__incidents = []

    @property
    def incidents(self):
        return self.__incidents

    def add_incident(self, incident):
        self.__incidents.append(incident)

    def get_info(self):
        info = {"weight": self.__weight, "brand": self.__brand}
        return(info)

    def get_model(self):
        full_model_name = self.__brand + " " + self.__model
        return(full_model_name)

    def save_data(self):
        data = {
            "weight": self.__weight,
            "model": self.__model,
            "brand": self.__brand,
            "missions": self._missions,
            "incidents": self.__incidents
        }

        output_filename = 'saved_data/' + str(self.__class__.__name__) + '_' + str(self.__model) + '.json'
        #        Path(output_filename).touch(mode=0o777, exist_ok=True)
        if not os.path.exists("saved_data"):
            os.makedirs("saved_data")        
        with open(output_filename, 'w') as ff:
            json.dump(data, ff, indent=2)

drone_catalog = {
        "DJI Mavic 2 Pro": {"weight":903, "brand":"DJI"},
        "DJI Mavic 2 Zoom": {"weight":900, "brand":"DJI"},
        "DJI Mavic 2 Enterprise Advanced": {"weight":920, "brand":"DJI"},
        "DJI Inspire 2": {"weight":1500, "brand":"DJI"},
        "DJI Mavic 3": {"weight":1000, "brand":"DJI"}
}

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


incidents = []
with open("faa_incidents.csv") as f:
    reader = csv.reader(f)
    lines = list(reader)
    incidents = [line[-1] for line in lines[1:]]

for drone_exmpl in list_of_drone_objects:
    drone = drone_exmpl.get_model()
    drone_name = ' '.join(drone.split(' ')[1:]).lower()

    for incident in incidents:
        if drone_name in incident.lower():
            drone_exmpl.add_incident(incident)

regex_pattern_fmt = r'[A-Z][^\.!?]+({})(?(1)[^\.!?]+[\.!?])'
list_of_drone_objects = sorted(list_of_drone_objects, key=lambda item: len(item.incidents))
for drone in list_of_drone_objects:
    drone_name = ' '.join(drone.get_model().lower().split(' ')[1:]).strip()
    incidents_count = len(drone.incidents)

    print(f"{drone_name}: инцидентов - {incidents_count}")
    if incidents_count == 0:
        continue

    pattern = regex_pattern_fmt.format(drone_name)
    for incident_idx, incident in enumerate(drone.incidents):
        print(f'{incident_idx + 1} - ', end='')
        result = re.search(pattern, incident, flags=re.IGNORECASE)
        print(result.group())
        print(incident)

# TODO 4-2 - После вывода информации об инциденте сохраните всю информацию о дроне в файл .json при помощи метода save_data
# ВАШ КОД:
for drone in list_of_drone_objects:
    drone.save_data()
