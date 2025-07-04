students = [
    {"name": "Ahmed", "grades": [80, 75, 90]},
    {"name": "Laila", "grades": [85, 88, 92]},
    {"name": "Omar", "grades": [70, 65, 78]}
]

for student in students:
    avg = sum(student["grades"]) / len(student["grades"])
    print(student["name"], "average grade:", avg)