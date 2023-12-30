
# from functools import reduce

# numbers = [1, 2, 3, 4, 5]

# squared_numbers = map(lambda x: x ** 2, numbers)

# sum_of_squares = reduce(lambda x, y: x + y, squared_numbers)

# print(sum_of_squares) 

# students = [ {'name': 'John', 'age': 21}, {'name': 'Alice', 'age': 19}, {'name': 'Bob', 'age': 20} ] 
# sorted_students = sorted(students, key=lambda student: student['name']) 
# print(sorted_students)
# from functools import reduce

# # List of patient records
# patients = [
#     {'name': 'John', 'age': 40, 'gender': 'Male', 'temperature': 98.6, 'heart_rate': 75},
#     {'name': 'Alice', 'age': 32, 'gender': 'Female', 'temperature': 99.2, 'heart_rate': 82},
#     {'name': 'Bob', 'age': 55, 'gender': 'Male', 'temperature': 97.9, 'heart_rate': 68},
#     {'name': 'Eve', 'age': 28, 'gender': 'Female', 'temperature': 98.8, 'heart_rate': 90}
# ]

# # Use filter() and lambda to filter male patients
# male_patients = list(filter(lambda patient: patient['gender'] == 'Male', patients))

# # Use reduce() and lambda to calculate the sum of heart rates for male patients
# sum_heart_rate_male = reduce(lambda x, y: x + y['heart_rate'], male_patients, 0)

# # Calculate the average heart rate of male patients
# average_heart_rate_male = sum_heart_rate_male / len(male_patients)
# print("Average heart rate of male patients:", average_heart_rate_male)

# # Use reduce() and lambda to find the patient with the highest temperature
# patient_highest_temperature = reduce(lambda x, y: x if x['temperature'] > y['temperature'] else y, patients)
# print("Patient with the highest temperature:", patient_highest_temperature)

# # Use reduce() and lambda to concatenate the names of all patients
# patient_names = reduce(lambda x, y: x + ', ' + y['name'], patients, '')
# print("Concatenated names of all patients:", patient_names)

# List of patient records
patients = [
    {'name': 'John', 'age': 40, 'gender': 'Male', 'temperature': 97.6},
    {'name': 'Alice', 'age': 32, 'gender': 'Female', 'temperature': 99.2},
    {'name': 'Bob', 'age': 55, 'gender': 'Male', 'temperature': 97.9},
    {'name': 'Eve', 'age': 28, 'gender': 'Female', 'temperature': 98.8}
]

# Use filter() and lambda to filter patients based on age
age_threshold = 40
elderly_patients = list(filter(lambda patient: patient['age'] >= age_threshold, patients))
print("Elderly Patient:", elderly_patients)


# Use filter() and lambda to filter patients based on temperature
temperature_threshold = 98.5
patients_with_fever = list(filter(lambda patient: patient['temperature'] > temperature_threshold, patients))
print("patients with fever :" , patients_with_fever)

