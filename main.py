
from PIL import Image
import customtkinter as ctk


class Main(ctk.CTk):
    def __init__(self, title, size, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.resizable(False, False)
        self.toplevel_window = None

        # Notebook
        self.notebook = ctk.CTkTabview(
            self,
            segmented_button_fg_color='black',
            segmented_button_selected_color='green',
            segmented_button_selected_hover_color='green',
            text_color='white',
            segmented_button_unselected_color='black',
            segmented_button_unselected_hover_color='black')
        self.notebook.pack(padx=20, pady=20, side='left', fill='both', expand=True)

        self.notebook.add(name='Профиль пользователей')
        self.notebook.add(name='Настройки собеседования')
        self.notebook.add(name='Пройти собеседование')
        self.notebook.set('Профиль пользователей')

        self.userstats = UserStatistics(self.notebook.tab('Профиль пользователей'), self.create_new_user)

        self.mainloop()

    def create_new_user(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = CreateNewUser(self)
        else:
            self.toplevel_window.lift()
            self.toplevel_window.focus()



class UserStatistics(ctk.CTkFrame):
    def __init__(self, parent, create_new_user):
        super().__init__(parent)
        self.width = 1000
        self.place(x=0, y=0)
        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure((0, 1), weight=1)
        self.create_new_user = create_new_user

        self.create_widgets()

    def create_widgets(self):
        # PINK SCREEN
        self.choose_user_frame = ctk.CTkFrame(self, fg_color='#ffcccc', width=600, height=300)
        self.choose_user_frame.grid(row=0, column=0, sticky='n', padx=20, pady=20)
        self.label1 = ctk.CTkLabel(self.choose_user_frame, text='Управление пользователями', font=('Calibri', 25))
        self.label1.place(x=30, y=10)
        self.label2 = ctk.CTkLabel(self.choose_user_frame, text='Выберите пользователя', font=('Calibri', 18))
        self.label2.place(x=30, y=50)
        self.combobox1 = ctk.CTkComboBox(
            self.choose_user_frame,
            width=250,
            height=35,
            fg_color='#ffe1e2',
            button_color='#d07979',
            button_hover_color='#92465f')
        self.combobox1.place(x=30, y=80)
        self.label3 = ctk.CTkLabel(self.choose_user_frame, text='Вы можете создать нового пользователя', font=('Calibri', 18))
        self.label3.place(x=30, y=200)

        self.button1_img = ctk.CTkImage(
            light_image=Image.open('images/add.png').resize((30, 30)),
            dark_image=Image.open('images/add.png').resize((30, 30))
        )
        self.button2_img = ctk.CTkImage(
            light_image=Image.open('images/delete.png').resize((30, 30)),
            dark_image=Image.open('images/delete.png').resize((30, 30))
        )
        self.button1 = ctk.CTkButton(
            self.choose_user_frame,
            width=250,
            height=35,
            fg_color='#d07979',
            hover_color='#92465f',
            text='Создать пользователя',
            image=self.button1_img,
            text_color='black',
            command=self.create_new_user)
        self.button1.place(x=30, y=240)

        self.button2 = ctk.CTkButton(
            self.choose_user_frame,
            width=200,
            height=35,
            fg_color='#d07979',
            hover_color='#92465f',
            text='Удалить пользователя',
            image=self.button2_img,
            text_color='black')
        self.button2.place(x=320, y=80)


        # YELLOW SCREEN
        self.global_stats_frame = ctk.CTkFrame(self, fg_color='#fff1c8', width=400, height=250)
        self.global_stats_frame.grid(row=1, column=0, sticky='e', padx=20, pady=20)
        self.label4 = ctk.CTkLabel(self.global_stats_frame, text='Глобальная статистика', font=('Calibri', 25))
        self.label4.place(x=30, y=10)
        self.label5 = ctk.CTkLabel(self.global_stats_frame, text='Последний вход', font=('Calibri', 18))
        self.label5.place(x=30, y=60)
        self.label6 = ctk.CTkLabel(self.global_stats_frame, text='Время собеседований', font=('Calibri', 18))
        self.label6.place(x=30, y=110)
        self.label7 = ctk.CTkLabel(self.global_stats_frame, text='Правильных ответов', font=('Calibri', 18))
        self.label7.place(x=30, y=160)
        self.label8 = ctk.CTkLabel(self.global_stats_frame, text='Процент завершения', font=('Calibri', 18))
        self.label8.place(x=30, y=210)

        # GREEN SCREEN
        self.particular_stats_frame = ctk.CTkFrame(self, fg_color='#d7e4d1', width=550)
        self.particular_stats_frame.grid(row=0, column=1, rowspan=2, sticky='nsew', padx=20, pady=20)
        self.label9 = ctk.CTkLabel(self.particular_stats_frame, text='Детальный прогресс по собеседованиям', font=('Calibri', 25))
        self.label9.place(x=30, y=10)

        self.label10 = ctk.CTkLabel(self.particular_stats_frame, text='Базовый синтаксис Python', font=('Calibri', 18))
        self.label10.place(x=30, y=60)
        self.progress1 = ctk.CTkProgressBar(
            self.particular_stats_frame,
            width=480,
            height=30,
            fg_color='#e6ffda',
            progress_color='#55e400')
        self.progress1.place(x=30, y=90)
        self.label11 = ctk.CTkLabel(self.particular_stats_frame, text='Объекто-ориентированное программирование (ООП)', font=('Calibri', 18))
        self.label11.place(x=30, y=130)
        self.progress2 = ctk.CTkProgressBar(
            self.particular_stats_frame,
            width=480,
            height=30,
            fg_color='#e6ffda',
            progress_color='#55e400')
        self.progress2.place(x=30, y=160)
        self.label12 = ctk.CTkLabel(self.particular_stats_frame, text='Правила оформления кода (PEP8, PEP257)', font=('Calibri', 18))
        self.label12.place(x=30, y=200)
        self.progress3 = ctk.CTkProgressBar(
            self.particular_stats_frame,
            width=480,
            height=30,
            fg_color='#e6ffda',
            progress_color='#55e400')
        self.progress3.place(x=30, y=230)
        self.label13 = ctk.CTkLabel(self.particular_stats_frame, text='Структуры данных на Python', font=('Calibri', 18))
        self.label13.place(x=30, y=270)
        self.progress4 = ctk.CTkProgressBar(
            self.particular_stats_frame,
            width=480,
            height=30,
            fg_color='#e6ffda',
            progress_color='#55e400')
        self.progress4.place(x=30, y=300)
        self.label14 = ctk.CTkLabel(self.particular_stats_frame, text='Алгоритмы на Python', font=('Calibri', 18))
        self.label14.place(x=30, y=340)
        self.progress5 = ctk.CTkProgressBar(
            self.particular_stats_frame,
            width=480,
            height=30,
            fg_color='#e6ffda',
            progress_color='#55e400')
        self.progress5.place(x=30, y=370)
        self.label15 = ctk.CTkLabel(self.particular_stats_frame, text='Git', font=('Calibri', 18))
        self.label15.place(x=30, y=410)
        self.progress6 = ctk.CTkProgressBar(
            self.particular_stats_frame,
            width=480,
            height=30,
            fg_color='#e6ffda',
            progress_color='#55e400')
        self.progress6.place(x=30, y=440)
        self.label16 = ctk.CTkLabel(self.particular_stats_frame, text='Базы данных и SQL запросы', font=('Calibri', 18))
        self.label16.place(x=30, y=480)
        self.progress7 = ctk.CTkProgressBar(
            self.particular_stats_frame,
            width=480,
            height=30,
            fg_color='#e6ffda',
            progress_color='#55e400')
        self.progress7.place(x=30, y=510)

class CreateNewUser(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        self.label = ctk.CTkLabel(self, text="ToplevelWindow")
        self.label.pack(padx=20, pady=20)

if __name__ == '__main__':
    Main('Python Interview Assistant', (1280, 720))
