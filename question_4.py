

string = str(input("Entrez un mot: "))
miss_char = int(input("Entrez un nombre: "))
new_string = ""

for char in string:
    if char != string[miss_char]:
        new_string += char

print(new_string)
