# Import necessary modules
import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Label Widget Example")

# Create a static text label
static_label = tk.Label(root, text="This is a static text label.")
static_label.pack()

# Create a dynamic text label using a textvariable
dynamic_text = tk.StringVar()
dynamic_text.set("This is a dynamic text label.")
dynamic_label = tk.Label(root, textvariable=dynamic_text)
dynamic_label.pack()

# Create a message widget
message = tk.Message(root, text="This is a message widget, useful for displaying multi-line text.")
message.pack()

# Create a frame to hold widgets
frame = tk.Frame(root, bd=2, relief=tk.SUNKEN)
frame.pack(padx=10, pady=10)

# Add labels to the frame
label1 = tk.Label(frame, text="Label inside frame - 1")
label1.pack()

label2 = tk.Label(frame, text="Label inside frame - 2")
label2.pack()

# Create a labelframe to hold widgets
labelframe = tk.LabelFrame(root, text="This is a LabelFrame", padx=10, pady=10)
labelframe.pack(padx=10, pady=10)

# Add a label to the labelframe
label_in_labelframe = tk.Label(labelframe, text="Label inside LabelFrame")
label_in_labelframe.pack()

# Create an entry widget for user input
entry = tk.Entry(root)
entry.pack()

# Create a button to fetch the entry data and display it in a label
def show_entry_data():
    entry_data = entry.get()
    dynamic_text.set(entry_data)

button = tk.Button(root, text="Show Entry Data", command=show_entry_data)
button.pack()



# Run the application
root.mainloop()