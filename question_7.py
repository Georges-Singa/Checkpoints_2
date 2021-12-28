from math import sqrt

C = 50
H = 30 
finish_list = []

for i in range(3):
    D = int(input("D-{}: ".format(i+1)))
    result = int(sqrt((2 * C * D) / H))
    finish_list.append(result)

print(finish_list)
