      #task1
user_input = input("enter something:")

output_list = list(user_input.lower())

print(output_list)

#task1.2
input_list = [('p', 2), ('u', 1), ('l', 1), (' ', 1), ('f', 1), ('i', 2), ('c', 1), ('t', 1), ('o', 1), ('n', 1)]

vowels = {'a', 'e', 'i', 'o', 'u'}

list_vow, list_cons, list_sym = [], [], []

for char, count in input_list:
    if char in vowels:
        list_vow.append((char, count))
    elif char.isalpha():
        list_cons.append((char, count))
    else:
        list_sym.append((char, count))

print("list_vow =", list_vow)
print("list_cons =", list_cons)
print("list_sym =", list_sym)


#task2.1
student_name = "Adam"
assignment_scores = [82, 56, 44, 30]
lab_scores = [78.20, 77.20]
test_scores = [78, 77]

student = {
    'name': student_name,
    'assignment': assignment_scores,
    'lab': lab_scores,
    'test': test_scores
}


print(student)

#task2.2
student = {
    'name': 'Adam',
    'assignment': [82, 56, 44, 30],
    'lab': [78.20, 77.20],
    'test': [78, 77]
}
print(student['assignment'][3])

total_assignments = 4
total_labs = 2
total_tests = 2

submitted_count = (
    len(student['assignment']) + len(student['lab']) +len(student['test'])
)

submission_check = {student['name']: submitted_count}

print(submission_check)


#task2.3
student_name = "Adam"
assignment_scores = [82, 56, 44, 30]
lab_scores = [78.20, 77.20]
test_scores = [78, 77]

student = {
    'name': student_name,
    'assignment': assignment_scores,
    'lab': lab_scores,
    'test': test_scores
}

avg_assaignments = sum(assignment_scores) / len(assignment_scores)
avg_labs = sum(lab_scores) / len(lab_scores)
avg_tests = sum(test_scores) / len(test_scores)

print((0.3 * avg_assaignments) + (0.5 * avg_labs) + (0.5 * avg_tests))


#task2.4
student1 = {
    'name': 'Adam',
    'assignment': [82, 56, 44, 30],
    'test': [78, 77],
    'lab': [78.20, 77.20],
    'final_grade': 70.25
}

student2 = {
    'name': 'Kevin',
    'assignment': [82, 30],
    'test': [],
    'lab': [78.2],
    'final_grade': 0
}

students = {}

students[student1['name']] = {
    'assignment': student1['assignment'],
    'test': student1['test'],
    'lab': student1['lab'],
    'final_grade': student1['final_grade']
}

students[student2['name']] = {
    'assignment': student2['assignment'],
    'test': student2['test'],
    'lab': student2['lab'],
    'final_grade': student2['final_grade']
}

print(students)
