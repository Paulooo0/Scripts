import csv

# with open('students.csv') as file:
#     for line in file:
#         name, house = line.rstrip().split(',')
#         print(f'{name} is in {house}')

#______________________________________

# students = []

# with open('students.csv') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({'name' : row['name'], 'home' : row['home']})
        
# for student in sorted(students, key=lambda student: student['name']):
#     print(f'{student["name"]} is from {student["home"]}')

#______________________________________

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'home'])
    writer.writerow({'name' : name, 'home' : home})