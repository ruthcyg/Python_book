# Define the list of names
names = ['Ruth', 'Johnson', 'Olu', 'Riya', 'OghaleOghene', 'Matthew']

# Sort the list by the last letter of each name using a lambda function
sorted_names = sorted(names, key=lambda name: name[-1])

# Print the sorted list
print(sorted_names)