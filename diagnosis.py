# Define the lambda function for diagnosis
diagnose = lambda bp: (
    "High Blood Pressure" if int(bp.split('/')[0]) > 140 or int(bp.split('/')[1]) > 90 
    else "Normal Blood Pressure"
)

def get_valid_bp_input(prompt):
    while True:
        bp_input = input(prompt)
        try:
            systolic, diastolic = map(int, bp_input.split('/'))
            if systolic <= 0 or diastolic <= 0:
                raise ValueError("Blood pressure values must be positive.")
            return bp_input
        except ValueError:
            print("Invalid input. Please enter blood pressure in the format 'systolic/diastolic' (e.g., 120/80).")

def main():
    # Prompt for blood pressure input with error handling
    blood_pressure = get_valid_bp_input("Enter your blood pressure (systolic/diastolic, e.g., 120/80): ")

    # Diagnose using the lambda function
    diagnosis = diagnose(blood_pressure)

    # Print the diagnosis
    print(f"Blood Pressure: {blood_pressure}, Diagnosis: {diagnosis}")

if __name__ == "__main__":
    main()