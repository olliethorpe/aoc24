

with open(r'data\day1.txt') as f:
    data = f.readlines()

first_list = []
second_list = []


for lines in data:
    first, second = lines.split()
    first_list.append(int(first))
    second_list.append(int(second))

first_list.sort()
second_list.sort()


sum = 0
for i, value in enumerate(first_list):
    sec_val = second_list[i]

    sum += ((sec_val - value)**2)**0.5
print(sum)
