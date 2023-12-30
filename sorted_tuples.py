# Sample data: List of tuples with patient names and ages
patients = [("Alice", 30), ("Bob", 25), ("Eve", 35)]

# Lambda function to sort patients by age
sorted_patients_by_age = lambda patient_list: sorted(patient_list, key=lambda patient: patient[1])

# Using the lambda function to sort the list
sorted_patients = sorted_patients_by_age(patients)

# Printing the sorted list
print (sorted_patients)