import tkinter as tk

# Function to evaluate the expression
def evaluate_expression():
    try:
        result.set(eval(entry.get()))
    except Exception as e:
        result.set("Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create a StringVar to hold the expression/result
result = tk.StringVar()

# Create the Entry widget to input expression
entry = tk.Entry(root, textvariable=result, font=('Helvetica', 20, 'bold'), bd=10, insertwidth=4, width=15, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for numbers and operators
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create and place buttons
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=('Helvetica', 15, 'bold'), bd=5, padx=10, pady=10, command=lambda t=text: entry.insert(tk.END, t))
    button.grid(row=row, column=col, sticky='nsew')

# Create the Clear button
clear_button = tk.Button(root, text='C', font=('Helvetica', 15, 'bold'), bd=5, padx=10, pady=10, command=lambda: entry.delete(0, tk.END))
clear_button.grid(row=5, column=0, columnspan=3, sticky='nsew')

# Create the Evaluate button
eval_button = tk.Button(root, text='=', font=('Helvetica', 15, 'bold'), bd=5, padx=10, pady=10, command=evaluate_expression)
eval_button.grid(row=5, column=3, sticky='nsew')

# Configure row and column weights
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
