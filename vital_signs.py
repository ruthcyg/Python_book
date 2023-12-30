# Define the lambda function
check_vitals = lambda patient: (
    f"Name: {patient['name']}, "
    f"Heart Rate: {patient['heart_rate']} bpm, "
    f"Blood Pressure: {patient['blood_pressure']}, "
    f"Height: {patient['height']} meters, "
    f"Weight: {patient['weight']} kg, "
    f"Temperature: {patient['temperature']}°F"
)

def get_input(prompt, input_type=float):
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print("Invalid input, please enter a number.")

def main():
    # Get user input for patient's details
    name = input("Enter patient's name: ")
    heart_rate = get_input("Enter patient's heart rate (bpm): ", int)
    blood_pressure = input("Enter patient's blood pressure (e.g., 120/80): ")
    height = get_input("Enter patient's height in meters (e.g., 1.75): ")
    weight = get_input("Enter patient's weight in kilograms (e.g., 70): ")
    temperature = get_input("Enter patient's body temperature in Fahrenheit (e.g., 98.6): ")

    # Create a patient record
    patient_record = {
        'name': name,
        'heart_rate': heart_rate,
        'blood_pressure': blood_pressure,
        'height': height,
        'weight': weight,
        'temperature': temperature
    }

    # Use the lambda function to check vitals
    vital_summary = check_vitals(patient_record)

    # Print a more descriptive summary
    print("\nHere is your vital signs summary:")
    print(vital_summary)

if __name__ == "__main__":
    main()
