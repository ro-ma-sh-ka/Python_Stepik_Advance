# task1
def comparator(average):
    return sum(average)/len(average)


numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]

print(min(numbers, key=comparator), max(numbers, key=comparator), sep='\n')

# task2
from math import sqrt

def comparator(distance):
    return sqrt(distance[0] ** 2 + distance[1] ** 2)


points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]

print(sorted(points, key=comparator))

# task3
def comparator(element):
    return min(element) + max(element)

numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]

print(sorted(numbers, key=comparator))

# task4
def comparator(number):
    return number[num]

athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

num = int(input())
athletes.sort(key=comparator)
for a, b, c, d in athletes:
    print(a, b, c, d)
#print(*[athlet for athlet in athletes])