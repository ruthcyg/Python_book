# Re-executing the modified lambda function to filter female patients under 40

patients = [
    {'name': 'John', 'age': 40, 'gender': 'Male'},
    {'name': 'Alice', 'age': 32, 'gender': 'Female'},
    {'name': 'Bob', 'age': 55, 'gender': 'Male'}
]

filtered_patients = filter(lambda patient: patient['age'] < 40 and patient['gender'] == 'Female', patients)

# Collecting the names of the filtered patients
filtered_patient_names = [patient['name'] for patient in filtered_patients]

print(filtered_patient_names)
