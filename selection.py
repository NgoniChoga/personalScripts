EDU = [1, 2, 3, 4, 5]
AS = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
BCOM = [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68]

groups = {}
temp = 1

#remove duplicates
for z in EDU:
    if z in BCOM:
        BCOM.remove(z)

#3-2-1
while len(EDU) > 0:
    temp_list = []
    for i in range(3):
        temp_list.append(BCOM.pop(0))

    for j in range(2):
        temp_list.append(AS.pop(0))

    temp_list.append(EDU.pop(0))

    groups[temp] = temp_list
    temp += 1

#4-2-0
while len(AS) > 2 and len(BCOM) > 4:
    temp_list = []
    for i in range(4):
        temp_list.append(BCOM.pop(0))

    for j in range(2):
        temp_list.append(AS.pop(0))  

    groups[temp] = temp_list
    temp += 1

print(groups)
print("Remainders {}".format(BCOM + AS))