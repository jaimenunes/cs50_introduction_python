# students = ['Harry', 'Ron', 'Hermione']

# for student in students:
#     print(student)


# for i in range(len(students)):
#     print(students[i])

# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor", 
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin"
# }

# for student in students:
    # print(f'{student} --> {students[student]}')

students = [
    {
        "name": "Hermione",
        "house": "Gryffindor", 
        "patronus": "Otter"
    },
    {
        "name": "Harry",
        "house": "Gryffindor", 
        "patronus": "Stag"
    },
    {
        "name": "Ron",
        "house": "Gryffindor", 
        "patronus": "Jack Russell Terrier"
    },
    {
        "name": "Hermione",
        "house": "Slytherin", 
        "patronus": None
    },
]

for student in students:
    print(student['name'], student['house'], student['patronus'], sep=", ")