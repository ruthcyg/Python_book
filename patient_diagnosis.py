# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0 / 9.0

# Lambda functions for diagnosis and treatment recommendation
diagnose = lambda bp: (
    "Consult a doctor" if int(bp.split('/')[0]) < 90 or int(bp.split('/')[1]) < 60
    else "Normal Blood Pressure"
)

recommend_treatment = lambda diagnosis, symptoms: (
    "Emergency! Seek immediate medical attention" if "chest pain" in symptoms or "difficulty breathing" in symptoms or diagnosis == "Consult a doctor"
    else "Consult a doctor for further evaluation" if any(symptom in symptoms for symptom in ["severe headaches", "dizziness", "nausea", "vomiting", "blurred vision", "anxiety", "confusion", "buzzing in the ears", "nosebleeds", "abnormal heart rhythm"])
    else "Maintain a healthy lifestyle"
)

# Lambda function for checking vitals
check_vitals = lambda patient: (
    f"Name: {patient['name']}, "
    f"Heart Rate: {patient['heart_rate']} bpm, "
    f"Blood Pressure: {patient['blood_pressure']}, "
    f"Height: {patient['height']} meters, "
    f"Weight: {patient['weight']} kg, "
    f"Temperature: {patient['temperature']}°F / {fahrenheit_to_celsius(patient['temperature']):.1f}°C, "
    f"Pulse: {patient['pulse']} bpm"
)

def get_input(prompt, input_type=float):
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print("Invalid input, please enter a number.")

def main():
    # Get user input for patient's details
    patient_record = {
        'name': input("Enter patient's name: "),
        'heart_rate': get_input("Enter patient's heart rate (bpm): ", int),
        'blood_pressure': input("Enter patient's blood pressure (e.g., 120/80): "),
        'height': get_input("Enter patient's height in meters (e.g., 1.75): "),
        'weight': get_input("Enter patient's weight in kilograms (e.g., 70): "),
        'temperature': get_input("Enter patient's body temperature in Fahrenheit (e.g., 98.6): "),
        'pulse': get_input("Enter patient's pulse (bpm): ", int)
    }

    # Check vitals
    vital_summary = check_vitals(patient_record)
    print("\nVital Summary:")
    print(vital_summary)

    # Diagnose
    diagnosis = diagnose(patient_record['blood_pressure'])
    print("Diagnosis:", diagnosis)

    # Prompt for symptoms
    symptoms_input = input("Enter any symptoms you are experiencing (separate by comma, e.g., nausea, dizziness): ")
    symptoms = [symptom.strip().lower() for symptom in symptoms_input.split(',')]

    # Recommend treatment
    treatment = recommend_treatment(diagnosis, symptoms)
    print("Recommended Treatment:", treatment)

if __name__ == "__main__":
    main()