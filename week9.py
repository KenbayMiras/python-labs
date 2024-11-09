#task1
list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for x in list_a:
    if x < 5:
        print(x)

#task2
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common_elements = list(set(a) & set(b))
print(common_elements)

#task3
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_d = dict(sorted(d.items(), key=lambda item: item[1]))
sorted_d_r = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
print(sorted_d)
print(sorted_d_r)

#task4
dict_a = {1:10, 2:20}
dict_b = {3:30, 4:40}
dict_c = {5:50, 6:60}

dicta = dict(dict_a) | dict(dict_b) | dict(dict_c)
print(dicta)

#task5
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
top_keys = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
print(top_keys)

#task6
n = input("Enter a number: ")
b = int(input("Enter a base: "))
if b == 2:
    print(int(n, 2))
    print(str(n))
elif b == 8:
    print(int(n, 8))
    print(str(n))
elif b == 10:
    print(int(n))
    print(str(n))
elif b == 16:
    print(int(n, 16))
    print(str(n))

#task7
n = 6
triangle = []
for i in range(n):
    row = [1] * (i + 1)
    for j in range(1, i):
        row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    triangle.append(row)
for row in triangle:
    print(" " * (n - len(row)), " ".join(map(str, row)))


