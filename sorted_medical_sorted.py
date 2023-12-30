# Sample data: List of medical terms
medical_terms = ["stethoscope", "scalpel", "gauze", "bandage"]

# Lambda function to sort strings by their length
sorted_terms_by_length = lambda terms: sorted(terms, key=lambda term: len(term))

# Using the lambda function to sort the list
sorted_medical_terms = sorted_terms_by_length(medical_terms)

# Printing the sorted list

print(sorted_medical_terms)