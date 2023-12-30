# Recursive function for symptom analysis
def analyze_symptoms(symptoms):
    if not symptoms:
        return "All symptoms analyzed."
    current_symptom, *remaining_symptoms = symptoms
    analysis_result = f"Analyzed symptom: {current_symptom}"
    return analysis_result + "; " + analyze_symptoms(remaining_symptoms)

# Function composition
def compose(*functions):
    def composed_function(patient_record):
        for f in reversed(functions):
            patient_record = f(patient_record)
        return patient_record
    return composed_function

# Lambda functions (pure and immutable)
check_bp = lambda patient: {**patient, 'bp_status': 'High' if int(patient['blood_pressure'].split('/')[0]) > 140 else 'Normal'}
administer_med = lambda patient: {**patient, 'medication_status': f"Administered {patient['medication']} at {patient['dose']}mg"}
check_ecg = lambda patient: {**patient, 'ecg_status': 'Abnormal' if patient['ecg'] == 'True' else 'Normal'}

# Higher-order function for patient care process
def patient_care_process(patient_record):
    composed_care_process = compose(check_bp, administer_med, check_ecg)
    return composed_care_process(patient_record)

def main():
    patient_record = {
        'name': input("Enter patient's name: "),
        'blood_pressure': input("Enter patient's blood pressure (e.g., 120/80): "),
        'medication': input("Enter patient's medication: "),
        'dose': input("Enter medication dose in mg: "),
        'ecg': input("Enter 'True' if ECG is abnormal, else 'False': ")
    }
    symptoms = input("Enter symptoms separated by comma: ").split(',')

    # Apply patient care process
    updated_patient_record = patient_care_process(patient_record)

    # Apply recursive symptom analysis
    symptom_analysis_result = analyze_symptoms(symptoms)

    # Display results
    print("\nUpdated Patient Record:", updated_patient_record)
    print("\nSymptom Analysis:", symptom_analysis_result)

if __name__ == "__main__":
    main()