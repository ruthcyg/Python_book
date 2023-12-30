# Sample data: List of patients
patients = [
    {"name": "John", "age": 30, "temperature": 98.6},
    {"name": "Alice", "age": 25, "temperature": 99.1},
    {"name": "Bob", "age": 30, "temperature": 98.4},
    {"name": "Eve", "age": 25, "temperature": 99.6}
]

# Lambda function to sort patients by the length of their name
sorted_patients_by_name_length = lambda patient_list: sorted(
    patient_list, key=lambda patient: len(patient["name"])
)

# Using the lambda function to sort the list
sorted_patients = sorted_patients_by_name_length(patients)

# Printing the sorted list
print (sorted_patients)