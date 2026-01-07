import tkinter as tk

# Function to increment the counter
def increment_counter():
    global counter
    counter += 1
    counter_label.config(text=f"Counter: {counter}")

# Initialize the count
counter = 0

# Create the main window
window = tk.Tk()
window.title("Counter Popup")  # Window title
window.geometry("300x150")  # Set window size (width x height)

# Add a label to display "Test"
test_label = tk.Label(window, text="Test", font=("Arial", 20))
test_label.pack(pady=10)  # Add padding along the Y-axis

# Add a label to display the counter
counter_label = tk.Label(window, text=f"Counter: {counter}", font=("Arial", 16))
counter_label.pack(pady=10)

# Add a button to increment the counter
increment_button = tk.Button(window, text="Click Me!", font=("Arial", 14), command=increment_counter)
increment_button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()