students = ["Hermione", "Harry", "Ron"]
for i in range(len(students)):
    print(i+1, students[i])

students = {
    "Hermione": "Griffindor",
    "Harry": "Griffindor",
    "Ron": "Griffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(student, students[student], sep=", ")

students = [
    {"name": "Hermione", "house": "Griffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Griffindor", "patronus": "Cervo"},
    {"name": "Ron", "house": "Griffindor", "patronus": "tbm nn sei"},
    {"name": "Draco", "house": "Slytherin", "patronus": "sla mano"},
]
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")