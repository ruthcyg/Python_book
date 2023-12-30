# Import the modules
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Define a lambda expression to calculate the average of vital signs
calculate_average_vital_signs = lambda *vital_signs: sum(vital_signs) / len(vital_signs) if len(vital_signs) > 0 else None

# Define a lambda expression to plot the vital signs as a line chart
plot_vital_signs = lambda heart_rates, respiratory_rates, oxygen_levels,temperature: (
    # Create a figure and an axis
    (fig := plt.subplots())[1].set(title="Vital Signs", xlabel="Time", ylabel="Value"),
    # Plot the vital signs as lines with different colors and labels
    [fig[1].plot(data, color=color, label=label) for data, color, label in zip(
        (heart_rates, respiratory_rates, oxygen_levels, temperature),
        ("red", "blue", "green", "orange"),
        ("Heart Rate", "Respiratory Rate", "Oxygen Level", "Temperature")
    )],
    # Set the legend
    fig[1].legend(),
    # Display the figure on the GUI
    (canvas := FigureCanvasTkAgg(fig[0], master=window)).draw(),
    canvas.get_tk_widget().grid(row=5, column=0, columnspan=4, padx=10, pady=10)
)[-1]

# Create a GUI window
window = tk.Tk()
window.title("Vital Signs Calculator")

# Create labels for the vital signs
tk.Label(window, text="Heart Rate").grid(row=0, column=0, padx=10, pady=10)
tk.Label(window, text="Respiratory Rate").grid(row=0, column=1, padx=10, pady=10)
tk.Label(window, text="Oxygen Level").grid(row=0, column=2, padx=10, pady=10)
tk.Label(window, text="Temperature").grid(row=0, column=3, padx=10, pady=10)

# Create entries for the vital signs
heart_rate_entry = tk.Entry(window)
heart_rate_entry.grid(row=1, column=0, padx=10, pady=10)
respiratory_rate_entry = tk.Entry(window)
respiratory_rate_entry.grid(row=1, column=1, padx=10, pady=10)
oxygen_level_entry = tk.Entry(window)
oxygen_level_entry.grid(row=1, column=2, padx=10, pady=10)
temperature_entry = tk.Entry(window)
temperature_entry.grid(row=1, column=3, padx=10, pady=10)

# Create a text box for the output
output_text = tk.Text(window, width=40, height=10)
output_text.grid(row=4, column=0, columnspan=5, padx=10, pady=10)

# Define a lambda expression to calculate and display the average vital signs
calculate_and_display = lambda: (
    # Get the input data as lists of floats
    (heart_rates := [float(x) for x in heart_rate_entry.get().split(",")]),
    (respiratory_rates := [float(x) for x in respiratory_rate_entry.get().split(",")]),
    (oxygen_levels := [float(x) for x in oxygen_level_entry.get().split(",")]),
    (temperature := [float(x) for x in temperature_entry.get().split(",")]),
    # Calculate the average vital signs using the lambda expression
    (average_heart_rate := calculate_average_vital_signs(*heart_rates)),
    (average_respiratory_rate := calculate_average_vital_signs(*respiratory_rates)),
    (average_oxygen_level := calculate_average_vital_signs(*oxygen_levels)),
    (average_temperature := calculate_average_vital_signs(*temperature)),
    # Format the output using f-strings
    (output := f"""Average Heart Rate: {average_heart_rate}
Average Respiratory Rate: {average_respiratory_rate}
Average Oxygen Level: {average_oxygen_level} Average Temperature: {average_temperature}"""),
    # Display the output on the text box
    output_text.delete(1.0, tk.END),
    output_text.insert(tk.END, output),
    # Plot the vital signs as a line chart
    plot_vital_signs(heart_rates, respiratory_rates, oxygen_levels,temperature)
)[-1]

# Create a button to trigger the calculation and display
tk.Button(window, text="Calculate and Display", command=calculate_and_display).grid(row=2, column=0, columnspan=5, padx=10, pady=10)

# Start the main loop of the GUI
window.mainloop()

# import tkinter as tk
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.figure import Figure
# import matplotlib.pyplot as plt  # Import pyplot module

# # Define a lambda function to calculate the average of vital signs
# calculate_average = lambda *vs: sum(vs) / len(vs) if vs else None

# # Define a lambda function to plot the vital signs as a line chart
# plot_vital_signs = lambda heart_rates, respiratory_rates, oxygen_levels, ax: (
#     ax.clear(),
#     ax.plot(heart_rates, color="red", label="Heart Rate"),
#     ax.plot(respiratory_rates, color="blue", label="Respiratory Rate"),
#     ax.plot(oxygen_levels, color="green", label="Oxygen Level"),
#     ax.set(title="Vital Signs", xlabel="Time", ylabel="Value"),
#     ax.legend()
# )

# # Define a lambda function to update the figure and canvas
# update_figure = lambda fig, canvas: (
#     canvas.draw(),
#     canvas.get_tk_widget().grid(row=5, column=0, columnspan=4, padx=10, pady=10)
# )

# # Define a lambda function to get the input data as lists of floats
# get_input_data = lambda entry: list(map(float, entry.get().split(",")))

# # Create a GUI window
# window = tk.Tk()
# window.title("Vital Signs Calculator")
# window.configure(bg='#f0f0f0')

# modern_font = ('Helvetica', 12)

# # Create the Matplotlib figure and axis
# fig, ax = Figure(figsize=(5, 4)), plt.subplot()

# # Create labels for the vital signs
# tk.Label(window, text="Heart Rate", font=modern_font, bg='#f0f0f0').grid(row=0, column=0)
# tk.Label(window, text="Respiratory Rate", font=modern_font, bg='#f0f0f0').grid(row=0, column=1)
# tk.Label(window, text="Oxygen Level", font=modern_font, bg='#f0f0f0').grid(row=0, column=2)

# # Create entries for the vital signs
# heart_rate_entry = tk.Entry(window, font=modern_font)
# respiratory_rate_entry = tk.Entry(window, font=modern_font)
# oxygen_level_entry = tk.Entry(window, font=modern_font)
# heart_rate_entry.grid(row=1, column=0)
# respiratory_rate_entry.grid(row=1, column=1)
# oxygen_level_entry.grid(row=1, column=2)

# # Create a text box for the output
# output_text = tk.Text(window, width=40, height=10, font=modern_font)
# output_text.grid(row=3, column=0, columnspan=4)

# # Initialize the canvas for Matplotlib
# canvas = FigureCanvasTkAgg(fig, master=window)

# # Define a lambda function to calculate and display the average vital signs
# calculate_and_display = lambda: (
#     heart_rates := get_input_data(heart_rate_entry),
#     respiratory_rates := get_input_data(respiratory_rate_entry),
#     oxygen_levels := get_input_data(oxygen_level_entry),
#     averages := [calculate_average(*vs) for vs in [heart_rates, respiratory_rates, oxygen_levels]],
#     output := "Average Heart Rate: {:.2f}\nAverage Respiratory Rate: {:.2f}\nAverage Oxygen Level: {:.2f}".format(*averages),
#     output_text.delete(1.0, tk.END),
#     output_text.insert(tk.END, output),
#     plot_vital_signs(heart_rates, respiratory_rates, oxygen_levels, ax),
#     update_figure(fig, canvas)
# )

# # Create a button to trigger the calculation and display
# calculate_button = tk.Button(window, text="Calculate and Display", font=modern_font, bg='#40e0d0', command=calculate_and_display)
# calculate_button.grid(row=2, column=0, columnspan=4)

# # Start the main loop of the GUI
# window.mainloop()


