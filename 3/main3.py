import numpy as np
inbothcompartements = []
data = []
with open("./input") as file:
    for line in file.readlines():
        firsthalf = line[slice(0,len(line)//2)]
        lasthalf = line[slice(len(line) // 2, len(line))]
        data.append(line)
        for index, char in enumerate(firsthalf):
            if char in lasthalf and not char in firsthalf[0:index]:
                inbothcompartements.append(char)
                continue
priorithis = []

for char in inbothcompartements:
    ascichar= ord(char) # Convert to asci
    if ascichar > 96:
        priorithis.append(ascichar-96) # small a is 97 in ASCII and 1 in our system
    else:
        priorithis.append(ascichar-65+27 ) # Huge A is 65 in ASCII and 27 in our system
print(np.sum(priorithis))

# Part 2
sol = []
for index, line in enumerate(data[::3]):
    nextline = data[3*index +1]
    overnextline = data[3*index+2]
    for char in line:
        if char in nextline and char in overnextline:
            sol.append(char)
            break
partwoprios = []
for char in sol:
    ascichar= ord(char) # Convert to asci
    if ascichar > 96:
        partwoprios.append(ascichar-96) # small a is 97 in ASCII and 1 in our system
    else:
        partwoprios.append(ascichar-65+27 ) # Huge A is 65 in ASCII and 27 in our system
print(np.sum(partwoprios))
