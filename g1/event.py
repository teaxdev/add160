import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Events")
root.geometry("280x100")

# Create a frame to hold the widgets
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Add function for button
def color_button():
    root.configure(bg="green")

button = tk.Button(root, text="Change Background", command=color_button)
button.pack(pady=10)


# Start the main event loop
root.mainloop()