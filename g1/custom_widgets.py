import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Events")
root.geometry("280x200")

# Create a frame to hold the widgets
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Add function for button
def color_button():
    root.configure(bg="green")

button = tk.Button(root, text="Change Background", command=color_button)
button.pack(pady=10)

# Song Lyric list
ham = ["hamster dance 1", "hamster dance 2", "hamster dance 3", "hamster dance 4",]

i = 0
def cycle():
    global i
    if i < len(ham) - 1:
        i += 1
    else:
        i = 0
    lyric_label.config(text=ham[i])

button = tk.Button(root, text="Change Lyric", command=cycle)
button.pack(pady=15)

lyric_label = tk.Label(root, text=ham[0])
lyric_label.pack(pady=10)

count_label = tk.Label(root, text="You have clicked this button 0 times")
count_label.pack(pady=10)

c = 0
def count():
    global c
    c += 1
    count_label.config(text=f"You have clicked this button {c} times")

button = tk.Button(root, text="count", command=count, cursor="hand2")
button.pack(pady=20)

# Start the main event loop
root.mainloop()