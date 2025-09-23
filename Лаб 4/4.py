2 Вариант
heights = [170, 180, 175, 190, 165, 190, 178]

max_height = max(heights)
count = heights.count(max_height)

print("Максимальный рост:", max_height)
print("Количество учеников с таким ростом:", count)

matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]

row_sums = [sum(row) for row in matrix]

print("Матрица:")
for row in matrix:
    print(row)

print("Суммы строк:", row_sums)
