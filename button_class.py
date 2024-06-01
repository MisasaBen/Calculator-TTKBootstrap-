import ttkbootstrap as tb


class Button:
    def __init__(self, root, label, row, column, padx, pady, width, callback):
        self.button = tb.Button(root, text=label, width=width, command=lambda: callback(label))
        self.button.grid(row=row, column=column, padx=padx, pady=pady)
