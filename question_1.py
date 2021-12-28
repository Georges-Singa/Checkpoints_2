
nbr_min = 2000
nbr_max = 3200
list_nbr = []

for nbr in range(nbr_min, nbr_max):
    if nbr % 7 == 0:
        if nbr % 5 == 0:
            list_nbr.append(nbr)
print(list_nbr)

