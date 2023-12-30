# Re-defining the sample data and lambda function after execution state reset

# Sample data: List of patients with their heart rates
patients = [
    {"name": "John", "heart_rate": 75},
    {"name": "Alice", "heart_rate": 85},
    {"name": "Bob", "heart_rate": 65},
    {"name": "Eve", "heart_rate": 90}
]

# Lambda function to sort patients by heart rate
sorted_patients_by_heart_rate = lambda patient_list: sorted(patient_list, key=lambda patient: patient["heart_rate"])

# Using the lambda function to sort the list
sorted_patients = sorted_patients_by_heart_rate(patients)

# Printing the sorted list


print(sorted_patients)