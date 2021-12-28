
nbr = int(input("Entrez un nombre: "))
total = nbr

for elem in range(1, nbr):
    nbr -= 1
    total *= nbr
print(total)


