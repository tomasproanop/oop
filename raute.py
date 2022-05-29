# Arbeitsgruppe: Cindy Sanchez und Tomas Proano

length = int(input("Enter an integer: "))

hsh = "#" # defining the symbol used, for this example we use hashes

for i in range(length):   #upper triangle
    for j in range(length - i):
        print(" ", end = '')
    print(hsh)
    hsh += "##"


length -= 1 #upside down triangle to complete a 'Raute'
space = 1
hshNum = ((length * 2) - 1)
hsh = "#" * hshNum
for i in range(length):
    print(" " + space * " " + hsh)
    hshNum -= 2
    hsh = "#" * hshNum
    space += 1
