file1 = open('prices.txt', encoding='utf-8')
lines = [[cost.rstrip() for cost in line.split('\t')] for line in file1.readlines()]
total = 0
for costs in lines:
    total += int(costs[1]) * int(costs[2])
print(total)
file1.close()