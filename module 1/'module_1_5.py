# 2023/09/24 00:00|Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи"
immutable_var = 1, 2, "Ilya", True
print(immutable_var)
# immutable_var [0] = 3 изменить не получится, так как кортеж относиться к неизменяемому типу данных
mutable_list = [3, 4, "Bezikov", True]
mutable_list [0:-1] = [10, 15, "Dmitryevich", False]
print(mutable_list)