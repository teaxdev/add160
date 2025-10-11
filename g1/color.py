import tkinter as tk

# Function to change the button color when pressed
def on_button_press(event):
    event.widget.config(bg="#33A329", fg="#FFFFFF")  # White background, green text
    event.widget.update_idletasks()

# Function to reset the button color when released
def on_button_release1(event):
    event.widget.config(bg="red", fg='#FFFFFF')  # Green background, white text

def on_button_release2(event):
    event.widget.config(bg="blue", fg='#FFFFFF')

def on_button_release3(event):
    event.widget.config(bg="yellow", fg='black')

# Create the main window
root = tk.Tk()
root.title("color buttons!")
root.geometry("300x150")

label = tk.Label(root, text="Each button will change to green when pressed")
label.pack(pady=20)

# I use label instead of button because buttons didn't change with the functions.
button1 = tk.Label(root, text="Red", bg = 'red', fg='white')
button2 = tk.Label(root, text="BLUE!!!!", bg = 'blue', fg='white')
button3 = tk.Label(root, text="yellow", bg = 'yellow', fg='black')
button1.pack(padx=10, pady = 5)
button2.pack(padx=10, pady = 5)
button3.pack(padx=10, pady = 5)

button1.bind("<ButtonPress-1>", on_button_press)
button1.bind("<ButtonRelease-1>", on_button_release1)
button2.bind("<ButtonPress-1>", on_button_press)
button2.bind("<ButtonRelease-1>", on_button_release2)
button3.bind("<ButtonPress-1>", on_button_press)
button3.bind("<ButtonRelease-1>", on_button_release3)

# Run the application
root.mainloop()