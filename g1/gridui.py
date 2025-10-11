import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Login")
root.geometry("280x100")

# Add a label with the joke setup
label1 = tk.Label(root, text="Name:")
label2 = tk.Label(root, text="Email:")
label3 = tk.Label(root, text="Password:")
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
label3.grid(row=2, column=0)
entry1.grid(row=0, column=1, pady = 2, padx = 2)
entry2.grid(row=1, column=1, pady = 2, padx = 2)
entry3.grid(row=2, column=1, pady = 2, padx = 2)

# Run the application
root.mainloop()