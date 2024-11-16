#task1
a = input()
w = ""
for i in a:
    w = i + w
if (a == w):
    print("Yes")
else:
    print("No")
print(w)

#task2
s = int(input())
days = s // (24*60*60)
remaining_seconds = s % (24*60*60)

hours = remaining_seconds // (60*60)
remaining_seconds %= (60*60)

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60
print(f"{days}:{hours:02}:{minutes:02}:{seconds:02}")

#task3
nums_b = input()
nums = [int(num.strip()) for num in nums_b.split(",")]
nums_t = tuple(nums)
print(nums)
print(nums_t)

#task4
l = ["Kenbay", 99, "score", "Miras"]
print(l[0], l[-1])

#task5
file = input()
if "." in file:
    extension = file.split(".")[-1]
    if extension:
        print(f"The file extension is: {extension}")
    else:
        raise ValueError("File extension cannot be determined.")
else:
    raise ValueError("File extension cannot be determined.")

#task6
n = int(input("number: "))
n1 = n
n2 = n * 10 + n
n3 = n * 100 + n * 10 + n

count = n1 + n2 + n3
print(count)

#task7
nums = [111, 222, 333, 444, 555, 666, 777, 237, 888, 999]
for i in nums:
    if i % 2 == 0:
        print(i)
    if i == 237:
        break
    else:
        continue