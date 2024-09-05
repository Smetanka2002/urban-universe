# 2023/09/25 00:00|Практическое задание по теме: "Словари и множества"
my_dict = {"Ilya" : 89321228902, "Dilya" : 89314313124}
print(my_dict)
print(my_dict["Ilya"])
print(my_dict.get("Denis", "Такого ключа нет!"))
my_dict["Misha"] = 891232453
print(my_dict["Misha"])
my_dict.update({"Svetlana" : 8932131232, "Oleg" : 89231212345})
print(my_dict)
a = my_dict.pop("Misha")
print(a)
print(my_dict)


my_set = {1, 2, 1, 2, "Ilya", "Ilya"}
print(my_set)
my_set.add(5)
my_set.add(True)
my_set.remove(1)
print(my_set)