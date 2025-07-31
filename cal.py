import tkinter as tk

def evaluate_expression():
    try:
        result = str(eval(display.get()))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def on_click(event):
    button_text = event.widget["text"]
    if button_text == "=":
        evaluate_expression()
    elif button_text == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, button_text)

def on_key(event):
    key = event.keysym
    if key in '0123456789':
        display.insert(tk.END, key)
    elif key in ['plus', 'KP_Add']:
        display.insert(tk.END, '+')
    elif key in ['minus', 'KP_Subtract']:
        display.insert(tk.END, '-')
    elif key in ['asterisk', 'KP_Multiply']:
        display.insert(tk.END, '*')
    elif key in ['slash', 'KP_Divide']:
        display.insert(tk.END, '/')
    elif key in ['Return', 'KP_Enter']:
        evaluate_expression()
    elif key == 'BackSpace':
        display.delete(len(display.get()) - 1)
    elif key in ['c', 'C', 'Escape']:
        display.delete(0, tk.END)

root = tk.Tk()
root.title("Colorful Calculator with Keyboard")
root.geometry("320x400")
root.configure(bg="#2e2e2e")
root.bind("<Key>", on_key)

# Display
display = tk.Entry(root, font=("Arial", 22), borderwidth=5, relief="sunken", justify="right", bg="#f0f0f0", fg="#000")
display.pack(fill=tk.BOTH, ipadx=8, ipady=15, pady=10, padx=10)

# Button Frame
button_frame = tk.Frame(root, bg="#2e2e2e")
button_frame.pack()

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

# Colors
button_bg = "#4a4a4a"
button_fg = "#ffffff"
special_bg = "#ff6b6b"   # Clear
equal_bg = "#6bcf6b"     # Equals
operator_bg = "#3c82f6"  # + - * /

for row in buttons:
    row_frame = tk.Frame(button_frame, bg="#2e2e2e")
    row_frame.pack(expand=True, fill="both", pady=2)
    for btn_text in row:
        if btn_text == "C":
            bg_color = special_bg
        elif btn_text == "=":
            bg_color = equal_bg
        elif btn_text in ['/', '*', '-', '+']:
            bg_color = operator_bg
        else:
            bg_color = button_bg

        btn = tk.Button(
            row_frame,
            text=btn_text,
            font=("Arial", 18),
            fg=button_fg,
            bg=bg_color,
            height=2,
            width=5,
            activebackground="#cccccc"
        )
        btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)
        btn.bind("<Button-1>", on_click)

root.mainloop()
