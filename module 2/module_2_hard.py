#2023/10/04 00:00|Дополнительное практическое задание по модулю*
import random
def first_plase():
    num = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    number = list(range(3,21))
    chiper = random.choice(number)
    return chiper
i = first_plase()
print('Шифр   :', i)
pairnum1 = list(range(1, i))
pairnum2 = list(range(1, i))
pairs = []
result = ''

for k in pairnum1:
    for j in pairnum2:
        pn1 = k
        pn2 = j
        if pn1 >= pn2:
            continue
        else:
            kratno = i % (pn1 + pn2)
            if kratno == 0:
                pairs.append([pn1, pn2])
                result = result + str(pn1) + str(pn2)
print('Пары чисел', *pairs)
print('Введите пароль', result, 'во вторую вставку')
print('Путь свободен!')