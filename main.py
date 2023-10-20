import customtkinter as ctk


class Main(ctk.CTk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')

        self.mainloop()

if __name__ == '__main__':
    Main('Python Interview Assistant', (600, 600))
