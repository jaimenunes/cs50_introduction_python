# students = ['Harry', 'Ron', 'Hermione']

# for student in students:
#     print(student)


# for i in range(len(students)):
#     print(students[i])

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

for student in students:
    print(f'{student} --> {students[student]}')