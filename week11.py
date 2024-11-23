#task 1
list1 = input("1st list: ").split()
list2 = input("2nd list: ").split()
print([x for x in list1 if x not in list2])

#task 2
import os

def list_files_in_directory(directory):
    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        return files
    except FileNotFoundError:
        return f"The directory {directory} does not exist."
    except PermissionError:
        return f"Permission denied to access {directory}."
directory = "C:/Users/kenba/OneDrive/Рабочий стол/python-labs"
files = list_files_in_directory(directory)
print("Files in directory:", files)

#task 3
number = int(input())
number = abs(number)
digit_sum = 0
for digit in str(number):
    digit_sum += int(digit)
print(digit_sum)

#task 4
string = input()
character = input()
count = 0
for char in string:
    if char == character:
        count += 1
print(character, "vstrechaetcya:", count, "raza")

#task 5
a = int(input())
b = int(input())
a, b = b, a
print(a, b)

#task 6
numbers = list(map(int, input("enter numbers").split()))
divisible = list(filter(lambda x: x % 15 == 0, numbers))
print(divisible)

#task 7
m = int(input())
sequence = []
for i in range(m):
    sequence.append(int(input()))
if len(sequence) == len(set(sequence)):
    print("unique")
else:
    print("not unique")