students = [
  {'name': 'John', 'age': 21},
  {'name': 'Alice', 'age': 19},
  {'name': 'Bob', 'age': 20}
]

sorted_students_by_name = sorted(students, key=lambda student: student['name'])

# Display the sorted list
print(sorted_students_by_name)