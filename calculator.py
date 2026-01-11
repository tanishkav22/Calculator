import tkinter as tk

# Create main window
window = tk.Tk()
window.title("Basic Calculator")
window.geometry("300x400")
window.resizable(False, False)

# Entry box to display input
entry = tk.Entry(window, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
entry.pack(fill="x", padx=10, pady=10)

# Function to add value to entry
def button_click(value):
    entry.insert(tk.END, value)

# Function to clear entry
def clear():
    entry.delete(0, tk.END)

# Function to calculate result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Frame for buttons
buttons_frame = tk.Frame(window)
buttons_frame.pack()

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

# Create buttons dynamically
for row in buttons:
    frame = tk.Frame(buttons_frame)
    frame.pack(expand=True, fill="both")
    for btn in row:
        if btn == '=':
            tk.Button(frame, text=btn, font=("Arial", 18),
                      command=calculate).pack(side="left", expand=True, fill="both")
        else:
            tk.Button(frame, text=btn, font=("Arial", 18),
                      command=lambda b=btn: button_click(b)).pack(side="left", expand=True, fill="both")

# Clear button
tk.Button(window, text="Clear", font=("Arial", 18), bg="lightcoral",
          command=clear).pack(fill="both", padx=10, pady=10)

# Run the app
window.mainloop()
