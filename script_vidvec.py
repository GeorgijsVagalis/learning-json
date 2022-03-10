import json

file = open("students.json")
data = json.load(file)
print(data)

count = 0
total_age = 0

for student in data["Students"]:
    print(f"{student['Age']} ")
    total_age += int(student["Age"])
    count +=1
print(f"Average age: {total_age/count}")

