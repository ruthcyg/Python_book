# import requests

# # Lambda function to fetch the title of a web page
# get_page_title = lambda url: requests.get(url).text.split('<title>')[1].split('</title>')[0]

# # Example URLs
# urls = [
#     'https://www.example.com',
#     'https://www.google.com',
#     'https://www.nonexistenturl123456789.com'
# ]

# # Fetch page titles using lambda function with exception handling
# for url in urls:
#     try:
#         title = get_page_title(url)
#         print(f"Title of {url}: {title}")
#     except (requests.exceptions.RequestException, IndexError):
#         print(f"Error retrieving the title of {url}")
"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

# import requests

# # Lambda function to fetch the title of a web page
# get_page_title = lambda url: requests.get(url).text.split('<title>')[1].split('</title>')[0]

# # Example URLs
# urls = [
#     'https://www.example.com',
#     'https://www.google.com',
#     'https://www.nonexistenturl123456789.com'
# ]

# # Fetch page titles using lambda function with exception handling
# for url in urls:
#     try:
#         title = get_page_title(url)
#         print(f"Title of {url}: {title}")
#     except (requests.exceptions.RequestException, IndexError):
#         print(f"Error retrieving the title of {url}")

# import tkinter as tk

# # Fake patient data for demonstration
# patient_data = [
#     {'id': 1, 'name': 'John Doe', 'age': 45},
#     {'id': 2, 'name': 'Alice Smith', 'age': 32},
#     {'id': 3, 'name': 'Sarah Johnson', 'age': 50},
#     {'id': 4, 'name': 'Michael Brown', 'age': 28},
# ]

# def search_patients():
#     # Get the entered search criteria from the GUI
#     criteria = search_entry.get()
    
#     # Perform the search based on the criteria
#     results = [patient for patient in patient_data if criteria.lower() in patient['name'].lower()]
    
#     # Display the search results in the GUI
#     patient_listbox.delete(0, tk.END)  # Clear previous results
#     for patient in results:
#         patient_listbox.insert(tk.END, f"ID: {patient['id']}, Name: {patient['name']}")

# def display_patient_info():
#     # Get the selected patient's ID from the GUI
#     selected_index = patient_listbox.curselection()
#     if selected_index:
#         selected_patient = patient_data[selected_index[0]]
        
#         # Retrieve and display the patient's information based on the selected patient ID
#         patient_info_label.config(text=f"Name: {selected_patient['name']}, Age: {selected_patient['age']}")
#     else:
#         patient_info_label.config(text="")

# def record_vital_signs():
#     # Get the selected patient's ID from the GUI
#     selected_index = patient_listbox.curselection()
#     if selected_index:
#         selected_patient = patient_data[selected_index[0]]
        
#         # Logic to record and store the vital signs for the selected patient
#         # Update the GUI with the recorded values
#         vital_signs_label.config(text=f"Recorded vital signs for Patient ID: {selected_patient['id']}")
#     else:
#         vital_signs_label.config(text="")

# def administer_medication():
#     # Get the selected patient's ID from the GUI
#     selected_index = patient_listbox.curselection()
#     if selected_index:
#         selected_patient = patient_data[selected_index[0]]
        
#         # Logic to administer medication to the selected patient
#         # Update the medication administration status in the GUI
#         medication_label.config(text=f"Administered medication to Patient ID: {selected_patient['id']}")
#     else:
#         medication_label.config(text="")

# def handle_task_completion():
#     # Get the selected task's ID from the GUI
#     selected_task = task_listbox.get(tk.ACTIVE)
    
#     # Logic to mark the task as completed and update the task management system
#     # Update the GUI to reflect the task completion status
#     task_completion_label.config(text=f"Completed task: {selected_task}")

# # Create the main application window
# window = tk.Tk()

# # GUI components and layout
# search_entry = tk.Entry(window)
# search_entry.pack()

# search_button = tk.Button(window, text="Search", command=search_patients)
# search_button.pack()

# patient_listbox = tk.Listbox(window)
# patient_listbox.bind('<<ListboxSelect>>', lambda event: display_patient_info())
# patient_listbox.pack()

# patient_info_label = tk.Label(window)
# patient_info_label.pack()

# record_button = tk.Button(window, text="Record Vital Signs", command=record_vital_signs)
# record_button.pack()

# vital_signs_label = tk.Label(window)
# vital_signs_label.pack()

# administer_button = tk.Button(window, text="Administer Medication", command=administer_medication)
# administer_button.pack()

# medication_label = tk.Label(window)
# medication_label.pack()

# task_listbox = tk.Listbox(window)
# task_listbox.bind('<<ListboxSelect>>', lambda event: handle_task_completion())
# task_listbox.pack()

# task_completion_label = tk.Label(window)
# task_completion_label.pack()

# # Run the main application loop
# window.mainloop()

# from flask import Flask, jsonify, request
# from werkzeug.middleware.dispatcher import DispatcherMiddleware
# from werkzeug.serving import run_simple
# import tkinter as tk

# app = Flask(__name__)

# # Rest of the code...

# @app.route('/patients/<patient_id>', methods=['GET'])
# def get_patient_details(patient_id):
#     # Logic to retrieve the details of a specific patient from the database
#     # Return the patient details as a JSON response
#     patient = {
#         'id': patient_id,
#         'name': 'John Doe',
#         'age': 45,
#         'blood_pressure': '120/80',
#         # Other patient details
#     }
#     return jsonify(patient)


# @app.route('/patients', methods=['GET'])
# def get_all_patients():
#     # Logic to retrieve all patient records from the database
#     # Return the list of patient records as a JSON response
#     all_patients = [
#         {'id': 'ABC123', 'name': 'John Doe', 'age': 45},
#         {'id': 'DEF456', 'name': 'Jane Smith', 'age': 32},
#         # Other patient records
#     ]
#     return jsonify(all_patients)


# @app.route('/patients/<patient_id>', methods=['PUT'])
# def update_patient_details(patient_id):
#     # Extract the updated data from the request body
#     updated_data = request.get_json()
    
#     # Logic to update the details of a specific patient in the database
#     # Return a success message as a JSON response
#     # Example updated_data: {'name': 'Jane Doe', 'age': 50, 'blood_pressure': '130/90'}
#     # Update the patient details in the database
#     return jsonify({'message': 'Patient details updated successfully'})


# @app.route('/patients', methods=['POST'])
# def create_patient_record():
#     # Extract the new patient data from the request body
#     new_patient_data = request.get_json()
    
#     # Logic to create a new patient record in the database
#     # Return the newly created patient ID as a JSON response
#     # Example new_patient_data: {'name': 'Jane Doe', 'age': 50, 'blood_pressure': '130/90'}
#     # Create the patient record in the database and generate a new patient ID
#     new_patient_id = 'ABC123'  # Example patient ID
#     return jsonify({'id': new_patient_id, 'message': 'Patient record created successfully'})


# @app.errorhandler(404)
# def page_not_found(e):
#     # Handle invalid routes
#     return jsonify({'message': 'Route not found'}), 404


# # Lambda entry point
# def lambda_handler(event, context):
#     # Use DispatcherMiddleware to handle the routing
#     application = DispatcherMiddleware(app, {
#         '/dev': app,
#         '/stage': app,
#         '/prod': app
#     })
    
#     # Use run_simple to run the Flask app in Lambda
#     run_simple(event['requestContext']['domainName'], event['requestContext']['path'], application)

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score

# # Generate and save sample patient data to 'patient_data.csv'
# data = {
#     'age': [40, 32, 55, 28],
#     'blood_pressure': [120, 130, 140, 110],
#     'cholesterol': [200, 220, 180, 210],
#     'glucose': [90, 95, 100, 88],
#     'smoker': ['No', 'No', 'Yes', 'No'],
#     'diabetes': ['No', 'No', 'Yes', 'No'],
#     'bmi': [33.33, 24.62, 39.29, 25.45],  # BMI values corresponding to the age and blood pressure
#     'risk_level': ['Low', 'Low', 'High', 'Low']
# }

# df = pd.DataFrame(data)
# df.to_csv('patient_data.csv', index=False)
# # Load the modified dataset (assuming it is stored in a CSV file)
# dataset = pd.read_csv('patient_data.csv')


# # Preprocess the dataset (data cleaning, feature engineering, transformation)
# def preprocess_data(data):
#     # Example data cleaning: Remove rows with missing values
#     data = data.dropna()

#     # Example transformation: Encode categorical variables 'smoker' and 'diabetes'
#     data = pd.get_dummies(data, columns=['smoker', 'diabetes'], drop_first=True)

#     return data


# # Define a lambda function for feature selection (including 'bmi')
# select_features = lambda data: data[['age', 'blood_pressure', 'cholesterol', 'glucose', 'bmi', 'smoker_Yes', 'diabetes_Yes']]

# # Define a lambda function for target variable selection
# select_target = lambda data: data['risk_level']

# # Split the dataset into training and testing sets
# preprocessed_data = preprocess_data(dataset)
# features = select_features(preprocessed_data)
# target = select_target(preprocessed_data)
# X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# # Train a machine learning model (Random Forest Classifier in this case)
# model = RandomForestClassifier()
# model.fit(X_train, y_train)

# # Evaluate the model
# y_pred = model.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
# print("Accuracy:", accuracy)

# # Update the new data dictionary to match the column names (including 'bmi')
# new_data = {
#     'age': [35],
#     'blood_pressure': [125],
#     'cholesterol': [195],
#     'glucose': [92],
#     'bmi': [28.0],  # BMI value for the new patient
#     'smoker': ['No'],
#     'diabetes': ['No']
# }

# # Use the trained model for prediction (you should preprocess new_data similarly)
# new_patient_data = preprocess_data(pd.DataFrame(new_data))
# selected_features = select_features(new_patient_data)
# prediction = model.predict(selected_features)

# print("Prediction for new patient:", prediction[0])

# Import pandas as pd
# Import pandas as pd
import pandas as pd

# Import train_test_split from sklearn.model_selection
from sklearn.model_selection import train_test_split

# Import RandomForestClassifier from sklearn.ensemble
from sklearn.ensemble import RandomForestClassifier

# Import accuracy_score from sklearn.metrics
from sklearn.metrics import accuracy_score

# Generate and save sample patient data to 'patient_data.csv'
data = {
    'age': [40, 32, 55, 28],
    'blood_pressure': [120, 130, 140, 110],
    'cholesterol': [200, 220, 180, 210],
    'glucose': [90, 95, 100, 88],
    'smoker': ['No', 'No', 'Yes', 'No'],
    'diabetes': ['No', 'No', 'Yes', 'No'],
    'bmi': [33.33, 24.62, 39.29, 25.45],  # BMI values corresponding to the age and blood pressure
    'risk_level': ['Low', 'Low', 'High', 'Low']
}

# Create a pandas DataFrame from the data dictionary
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('patient_data.csv', index=False)

# Load the modified dataset (assuming it is stored in a CSV file)
dataset = pd.read_csv('patient_data.csv')


# Preprocess the dataset (data cleaning, feature engineering, transformation)
def preprocess_data(data):
    # Example data cleaning: Remove rows with missing values
    data = data.dropna()

    # Example transformation: Encode categorical variables 'smoker' and 'diabetes'
    data = pd.get_dummies(data, columns=['smoker', 'diabetes'], drop_first=True)

    return data


# Define a lambda function for feature selection (including 'bmi')
select_features = lambda data: data[['age', 'blood_pressure', 'cholesterol', 'glucose', 'bmi', 'smoker_Yes', 'diabetes_Yes']]

# Define a lambda function for target variable selection
select_target = lambda data: data['risk_level']

# Split the dataset into training and testing sets
preprocessed_data = preprocess_data(dataset)
features = select_features(preprocessed_data)
target = select_target(preprocessed_data)
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Train a machine learning model (Random Forest Classifier in this case)
model = RandomForestClassifier(random_state=42)  # Add a random_state parameter for reproducibility
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Update the new data dictionary to match the column names (including 'bmi')
# new_data = {
#     'age': [35],
#     'blood_pressure': [125],
#     'cholesterol': [195],
#     'glucose': [92],
#     'bmi': [28.0],  # BMI value for the new patient
#     'smoker_Yes': [0],  # Use 0 or 1 instead of 'No' or 'Yes'
#     'diabetes_Yes': [0]
# }
# Option 1: Change the keys in the new data dictionary
new_data = {
    'age': [35],
    'blood_pressure': [125],
    'cholesterol': [195],
    'glucose': [92],
    'bmi': [28.0],  # BMI value for the new patient
    'smoker': ['No'], # Use 'No' or 'Yes' instead of 0 or 1
    'diabetes': ['No']
}

# Option 2: Change the columns argument in the pd.get_dummies function
data = pd.get_dummies(data, columns=['smoker_Yes', 'diabetes_Yes'], drop_first=True)

# Use the trained model for prediction (you should preprocess new_data similarly)
new_patient_data = preprocess_data(pd.DataFrame(new_data))
selected_features = select_features(new_patient_data)
prediction = model.predict(selected_features)

print("Prediction for new patient:", prediction[0])
