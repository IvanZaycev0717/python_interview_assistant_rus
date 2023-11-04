
import tkinter
from PIL import Image
import customtkinter as ctk

from settings import *


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

        self.userstats = UserStatisticsTab(self.notebook.tab('Профиль пользователей'), self.create_new_user)
        self.interview_settings = InterviewSettingsTab(self.notebook.tab('Настройки собеседования'))
        self.interview_pass = InterviewPassTab(self.notebook.tab('Пройти собеседование'))

    def create_new_user(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = CreateNewUser(self)
            self.toplevel_window.focus()
        else:
            self.toplevel_window.lift()
            self.toplevel_window.focus()



class UserStatisticsTab(ctk.CTkFrame):
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

        self.label10 = ctk.CTkLabel(self.particular_stats_frame, text=BASICS, font=('Calibri', 18))
        self.label10.place(x=30, y=60)
        self.progress1 = ctk.CTkProgressBar(
            self.particular_stats_frame,
            width=480,
            height=30,
            fg_color='#e6ffda',
            progress_color='#55e400')
        self.progress1.place(x=30, y=90)
        self.label11 = ctk.CTkLabel(self.particular_stats_frame, text=OOP, font=('Calibri', 18))
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
        self.label13 = ctk.CTkLabel(self.particular_stats_frame, text=STRUCTURES, font=('Calibri', 18))
        self.label13.place(x=30, y=270)
        self.progress4 = ctk.CTkProgressBar(
            self.particular_stats_frame,
            width=480,
            height=30,
            fg_color='#e6ffda',
            progress_color='#55e400')
        self.progress4.place(x=30, y=300)
        self.label14 = ctk.CTkLabel(self.particular_stats_frame, text=ALGHORITMS, font=('Calibri', 18))
        self.label14.place(x=30, y=340)
        self.progress5 = ctk.CTkProgressBar(
            self.particular_stats_frame,
            width=480,
            height=30,
            fg_color='#e6ffda',
            progress_color='#55e400')
        self.progress5.place(x=30, y=370)
        self.label15 = ctk.CTkLabel(self.particular_stats_frame, text=GIT, font=('Calibri', 18))
        self.label15.place(x=30, y=410)
        self.progress6 = ctk.CTkProgressBar(
            self.particular_stats_frame,
            width=480,
            height=30,
            fg_color='#e6ffda',
            progress_color='#55e400')
        self.progress6.place(x=30, y=440)
        self.label16 = ctk.CTkLabel(self.particular_stats_frame, text=SQL, font=('Calibri', 18))
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
        self.title('Python Interview Assistant - Добавить пользователя')
        self.geometry('390x160')
        self.resizable(False, False)


        self.frame = ctk.CTkFrame(self, width=350, height=110, fg_color='#d3e4ef')
        self.frame.pack(side='top', expand=True, fill='both', padx=10, pady=10)
        self.frame.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame.columnconfigure((0, 1), weight=1)

        self.label = ctk.CTkLabel(self.frame, text='Создайте имя пользователя:')
        self.label.grid(row=0, column=0, sticky='ws', padx=10)
        self.enter = ctk.CTkEntry(self.frame, width=350)
        self.enter.grid(row=1, column=0, sticky='wn', padx=10, columnspan=2)
        self.helper = ctk.CTkLabel(self.frame, text='')
        self.helper.grid(row=2, column=0, sticky='wn', padx=10)
        self.save_button = ctk.CTkButton(self.frame, text='Создать')
        self.save_button.grid(row=3, column=0, sticky='wn', padx=10)
        self.cancel_button = ctk.CTkButton(self.frame, text='Отмена', command=self.cancel_button)
        self.cancel_button.grid(row=3, column=1, sticky='en', padx=10)
    
    def cancel_button(self):
        self.destroy()

class InterviewSettingsTab(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.width = 1200
        self.place(x=0, y=0)
        self.columnconfigure((0, ), weight=1)
        self.rowconfigure((0, 1, 2, 3), weight=1)

        self.random_var = ctk.IntVar()
        self.freemode_var = ctk.IntVar()
        self.sound_volume = ctk.IntVar(value=30)
        self.sound_text = ctk.StringVar(value=f'Громкость: {self.sound_volume.get()}%')

        

        self.choose_interview_mode_tab()
        self.choose_random_interview()
        self.choose_free_mode()
        self.toggle_sounds()

        
    
    def draw_line(self, frame):
        self.tab_line = ctk.CTkCanvas(frame, width=5, height=80, bd=0, highlightthickness=0)
        self.tab_line.place(x=400, y=10)
        self.tab_line.create_line(0, 0, 0, 80, width=10)
    
    def draw_label(self, frame, text):
        ctk.CTkLabel(frame, text=text, font=('Calibri', 20)).place(x=20, y=35)
    
    def choose_interview_mode_tab(self):
        self.choose_interview_mode_frame = ctk.CTkFrame(self, fg_color='#e2f7b5', width=1185, height=100)
        self.choose_interview_mode_frame.grid(row=0, column=0, sticky='n', padx=20, pady=20)
        self.draw_label(self.choose_interview_mode_frame, 'Выбор тем собеседования')
        self.draw_line(self.choose_interview_mode_frame)
        self.basics = ctk.CTkCheckBox(
            master=self.choose_interview_mode_frame,
            text=BASICS,
            hover_color='#68a248',
            fg_color='#68a248')
        self.basics.place(x=420, y=15)
        self.oop = ctk.CTkCheckBox(
            master=self.choose_interview_mode_frame,
            text='ООП Python',
            hover_color='#68a248',
            fg_color='#68a248')
        self.oop.place(x=420, y=55)
        self.pep = ctk.CTkCheckBox(
            master=self.choose_interview_mode_frame,
            text='PEP8, PEP257',
            hover_color='#68a248',
            fg_color='#68a248')
        self.pep.place(x=650, y=15)
        self.structures = ctk.CTkCheckBox(
            master=self.choose_interview_mode_frame,
            text=STRUCTURES,
            hover_color='#68a248',
            fg_color='#68a248')
        self.structures.place(x=650, y=55)
        self.alghoritms = ctk.CTkCheckBox(
            master=self.choose_interview_mode_frame,
            text=ALGHORITMS,
            hover_color='#68a248',
            fg_color='#68a248')
        self.alghoritms.place(x=870, y=15)
        self.sql = ctk.CTkCheckBox(
            master=self.choose_interview_mode_frame,
            text=SQL,
            hover_color='#68a248',
            fg_color='#68a248')
        self.sql.place(x=870, y=55)
        self.git = ctk.CTkCheckBox(
            master=self.choose_interview_mode_frame,
            text=GIT,
            hover_color='#68a248',
            fg_color='#68a248')
        self.git.place(x=1100, y=15)

        

    def choose_random_interview(self):
        self.choose_random_interview_frame = ctk.CTkFrame(self, fg_color='#e2f7b5', width=1185, height=100)
        self.choose_random_interview_frame.grid(row=1, column=0, sticky='n', padx=20, pady=20)
        self.draw_label(self.choose_random_interview_frame, 'Последовательность вопросов')
        self.draw_line(self.choose_random_interview_frame)
        self.random_button_off = ctk.CTkRadioButton(
            self.choose_random_interview_frame,
            value=0,
            text='Вопросы задают последовательно',
            variable=self.random_var,
            fg_color='#68a248',
            hover_color='#68a248')
        self.random_button_off.place(x=420, y=40)
        self.random_button_on = ctk.CTkRadioButton(
            self.choose_random_interview_frame,
            value=1,
            text='Вопросы задают случайно',
            variable=self.random_var,
            fg_color='#68a248',
            hover_color='#68a248')
        self.random_button_on.place(x=700, y=40)
    
    def choose_free_mode(self):
        self.choose_free_mode_frame = ctk.CTkFrame(self, fg_color='#e2f7b5', width=1185, height=100)
        self.choose_free_mode_frame.grid(row=2, column=0, sticky='n', padx=20, pady=20)
        self.draw_label(self.choose_free_mode_frame, 'Свободное перемещение по вопросам')
        self.draw_line(self.choose_free_mode_frame)
        self.freemode_button_on = ctk.CTkRadioButton(
            self.choose_free_mode_frame,
            value=1,
            text='Включить свободный выбор вопросов',
            variable=self.freemode_var,
            fg_color='#68a248',
            hover_color='#68a248')
        self.freemode_button_on.place(x=420, y=40)
        self.freemode_button_off = ctk.CTkRadioButton(
            self.choose_free_mode_frame,
            value=0,
            text='Отключить свободный выбор вопросов',
            variable=self.freemode_var,
            fg_color='#68a248',
            hover_color='#68a248')
        self.freemode_button_off.place(x=700, y=40)

    def toggle_sounds(self):
        self.toggle_sounds_frame = ctk.CTkFrame(self, fg_color='#e2f7b5', width=1185, height=100)
        self.toggle_sounds_frame.grid(row=3, column=0, sticky='n', padx=20, pady=20)
        self.draw_label(self.toggle_sounds_frame, 'Управление громкостью собеседования')
        self.draw_line(self.toggle_sounds_frame)

        self.sound_scale = ctk.CTkSlider(
            self.toggle_sounds_frame,
            orientation='horizontal',
            from_=0,
            to=100,
            variable=self.sound_volume,
            width=280,
            command=lambda value: self.sound_text.set(f'Громкость: {self.sound_volume.get()}%'),
            button_color='#68a248',
            button_hover_color='#68a248',
            progress_color='#68a248')
        self.sound_scale.place(x=420, y=40)
        self.sound_label = ctk.CTkLabel(self.toggle_sounds_frame, textvariable=self.sound_text)
        self.sound_label.place(x=710, y=32)

class InterviewPassTab(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.width = 1200
        self.place(x=0, y=0)
        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure((0, 1), weight=1)

        self.create_interview_frame()
        self.create_control_frame()
    
    def create_interview_frame(self):
        self.interview_frame = ctk.CTkFrame(self, fg_color='#ffd38f', width=620, height=400)
        self.interview_frame.grid(row=0, column=0, padx=30, pady=10)

        # first row
        self.begin_button = ctk.CTkButton(
            master=self.interview_frame,
            width=300,
            height=40,
            text='Начать собеседование',
            fg_color='#333f65',
            hover_color='#232e52')
        self.begin_button.place(x=20, y=20)

        self.replay_button = ctk.CTkButton(
            master=self.interview_frame,
            width=150,
            height=40,
            text='Проиграть вопрос',
            fg_color='#333f65',
            hover_color='#232e52')
        self.replay_button.place(x=400, y=20)

        self.mute_button = ctk.CTkButton(
            master=self.interview_frame,
            width=40,
            height=40,
            text='',
            fg_color='#333f65',
            hover_color='#232e52')
        self.mute_button.place(x=560, y=20)

        ctk.CTkLabel(
            master=self.interview_frame,
            text='Теоретический вопрос',
            font=('Calibri', 25)).place(x=20, y=75)
        
        self.theory_textbox = ctk.CTkTextbox(
            master=self.interview_frame,
            width=580,
            height=100
        )
        self.theory_textbox.place(x=20, y=120)
        
        ctk.CTkLabel(
            master=self.interview_frame,
            text='Live coding',
            font=('Calibri', 25)).place(x=20, y=240)
        
        self.coding_button = ctk.CTkButton(
            master=self.interview_frame,
            width=150,
            height=28,
            text='Проиграть вопрос Live coding',
            fg_color='#333f65',
            hover_color='#232e52')
        self.coding_button.place(x=160, y=242)

        self.coding_textbox = ctk.CTkTextbox(
            master=self.interview_frame,
            width=580,
            height=100
        )
        self.coding_textbox.place(x=20, y=280)
    
    def create_control_frame(self):
        self.control_frame = ctk.CTkFrame(self, fg_color='#e6a765', width=620, height=200)
        self.control_frame.grid(row=1, column=0)

        self.positive_button = ctk.CTkButton(
            master=self.control_frame,
            width=260,
            height=70,
            text='Я правильно ответил на вопрос',
            fg_color='#578555',
            hover_color='#2d642a'
        ).place(x=20, y=20)

        self.negative_button = ctk.CTkButton(
            master=self.control_frame,
            width=260,
            height=70,
            text='Я не знаю, следующий вопрос',
            fg_color='#ac1416',
            hover_color='#ce6163'
        ).place(x=340, y=20)

        self.answer_button = ctk.CTkButton(
            master=self.control_frame,
            width=580,
            height=70,
            text='Подсказка',
            fg_color='#c1461e',
            hover_color='#ff662a'
        ).place(x=20, y=110)

    

if __name__ == '__main__':
    main_window = Main('Python Interview Assistant', (1280, 720))
    main_window.mainloop()
