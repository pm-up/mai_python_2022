drone_list = ["DJI Mavic 2 Pro", "DJI Mavic 2 Zoom", "DJI Mavic 2 Enterprise Advanced", "AUTEL Evo II Pro", "DJI Mini 2", "Autel Evo Nano", "Autel Evo Lite Plus", "Parrot Anafi", "Dji Inspire 2", "DJI Mavic 3", "DJI Mavic Air2s", "Ryze Tello", "Eachine Trashcan"]

drone_weight_list = [903, 900, 920, 980, 249, 249, 600, 540, 1500, 1000, 570, 130, 110]

def correct_name(drone):
    if drone.lower().startswith("dji"):
            producer_proper_name="DJI"
    if drone.lower().startswith("autel"):
            producer_proper_name="Autel"
    if drone.lower().startswith("parrot"):
            producer_proper_name="Parrot"
    if drone.lower().startswith("ryze"):
            producer_proper_name="Ryze"
    if drone.lower().startswith("eachine"):
            producer_proper_name="Eachine"
    return producer_proper_name

#в drone по очереди попадает каждый дрон из списка drone_list
for drone in drone_list:
	print(drone)

#TODO1
#выведите все дроны производителя, название которого введет пользователь через input, и подсчитайте их количество. 
#учтите, что:
#1) DJI и Dji - это один и тот же производитель! такие случаи тоже должны обрабатываться
#2) при выводе исправьте название производителя, если допущена ошибка. правильный вариант названия: DJI, Autel

producer = str(input())
if producer.lower() == "dji":
            producer_proper_name="DJI"
if producer.lower() == "autel":
            producer_proper_name="Autel"
count=0

for drone in drone_list:
    if drone.capitalize().startswith(producer.capitalize()):
        print(drone)
        count += 1
print("The number of drones produced by " + producer_proper_name + " is " + str(count))

#TODO2
#подсчитайте количество моделей дронов каждого производителя из списка drone_list. производители: DJI, Autel, Parrot, Ryze, Eachine

DJI_count = 0                
Autel_count = 0                       
Parrot_count = 0               
Ryze_count = 0                         
Eachine_count = 0

for drone in drone_list:
    if drone.lower().startswith("dji"):
        DJI_count += 1
    if drone.lower().startswith("autel"):                   
        Autel_count += 1
    if drone.lower().startswith("parrot"):                   
        Parrot_count += 1
    if drone.lower().startswith("ryze"):                   
        Ryze_count += 1
    if drone.lower().startswith("eachine"):                   
        Eachine_count += 1
print("The number of drones produced by DJI: " + str(DJI_count) + ", Autel:" + str(Autel_count) + ", Parrot:" + str(Parrot_count) + ", Ryze:" + str(Ryze_count) + ", Eachine:" + str(Eachine_count))

#TODO3
#выведите все дроны из списка, которые нужно регистрировать (масса больше 150 г), и подсчитайте их количество. 
#сделайте то же самое для всех дронов, которые не нужно регистрировать
#для этого вам нужно параллельно обрабатывать два списка: drone_list и drone_weight_list:
#как работает zip, мы разберем на лекции про списки. пока что просто пользуйтесь

print("Drones from the list below are subject to registration:")
for drone, weight in zip(drone_list,  drone_weight_list):
    if weight >= 150:
        proper_name=correct_name(drone)
        tmp = drone.split()[1:]
        drone = proper_name + " " +  (" ".join(tmp))
        print(drone)

print("Drones from the list below are not subject to registration:")
for drone, weight in zip(drone_list,  drone_weight_list):
    if weight < 150:
        proper_name=correct_name(drone)
        tmp = drone.split()[1:]
        drone = proper_name + " " +  (" ".join(tmp))
        print(drone)

#TODO4
#для каждого дрона из списка выведите, нудно ли согласовывать полет при следующих условиях:
#высота 100 м, полет над населенным пунктом, вне закрытых зон, в прямой видимости
#помните, что для дронов тяжелее 150 г согласовывать полет над населенным пунктом - обязательно!

for drone, weight in zip(drone_list, drone_weight_list):
    if weight > 150:
        proper_name=correct_name(drone)
        tmp = drone.split()[1:]
        drone = proper_name + " " +  (" ".join(tmp))
        print(drone + ": Approval is required for the flight!")
    else:
        proper_name=correct_name(drone)
        tmp = drone.split()[1:]
        drone = proper_name + " " +  (" ".join(tmp))
        print(drone + ": Approval is not required for the flight!")

#TODO5*
#модифицируйте решение задания TODO1:
#теперь для введенного пользователем производителя вы должны вывести строку, содержащую перечисление моделей и БЕЗ названия производителя.
#например, пользователь ввел "Autel". ваша программа должна вывести вот такой результат: "Evo II Pro, Evo Nano, Evo Lite Plus". для этого вам понадобится несколько функций работы со строками. решить эту задачу можно несколькими разными способами
#производители те же: DJI, Autel, Parrot, Ryze, Eachine

producer = str(input())
if producer.lower() == "dji":
            producer_proper_name="DJI"
if producer.lower() == "autel":
            producer_proper_name="Autel"
count=0

for drone in drone_list:
    if drone.capitalize().startswith(producer.capitalize()):
        tmp = drone.split()[1:]
        print(" ".join(tmp))
        count += 1  
print("The number of drones produced by " + producer_proper_name + " is " + str(count))

