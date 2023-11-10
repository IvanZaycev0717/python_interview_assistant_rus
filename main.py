import math

import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image
import customtkinter as ctk
import fitz

from settings import *



class Main(ctk.CTk):
    def __init__(self, title, size, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.resizable(False, False)
        self.create_user_window = None
        self.hint_window = None

        self.users = ('Masha', 'Petya', 'Vasya')

        self.themes = {
            0: BASICS,
            1: OOP,
            2: PEP8,
            3: STRUCTURES,
            4: ALGHORITMS,
            5: GIT,
            6: SQL
        }

        # DATABASE
        self.database = [
            (8, 0, 'Сильная типизация', 'Что такое сильная типизация?', 'Пример сильной типизации', 1),
            (9, 1, 'Типы данных', 'Какие типы данных в Python', 'Пример Типы данных', 1),
            (10, 0, 'Класс', 'Что такое класс', 'Пример класса', 2),
            (11, 1, 'Режимы доступа', 'Перечислите все режимы доступа', '', 2),
            (12, 0, 'Максимальная длина строки', 'Сколько максимальная длина строки в Python', '', 3),
            (13, 1, 'Docstrings', 'Что такое Docstrings', 'Пример Docstrings класса', 3),
            (14, 0, 'Динамические массивы', 'Динамический массив в Python', 'Создайте динамический массив из 7 элементов. Вставьте 5 элемент цифру 1', 4),
            (15, 1, 'Что такое очередь', 'Как в Python реализуется очередь', 'Создайте очередь и добавьте элемент', 4),
            (16, 0, 'Алгоритм простых чисел', 'Реализуйте простые числа', 'Определить относится ли число к простому', 4),
            (17, 1, 'Алгоритм Левенштейна', 'Что такое Алгоритм Левенштейна', 'Задача', 4),
            (18, 0, 'git commit', 'Что такое git commit', 'Реализуйте git commit', 4),
            (19, 1, 'git pull', 'Что такое git pull', 'Реализуйте git pull', 4),
            (20, 0, 'Создание таблицы', 'Как создать таблицу в SQL', 'Пример создания таблицы', 4),
            (21, 1, 'Удаление таблицы', 'Как удалить таблицу в SQL', 'Пример удаление таблицы', 4),

        ]

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

        self.userstats = UserStatisticsTab(self.notebook.tab('Профиль пользователей'), self.create_new_user, self.users)
        self.interview_settings = InterviewSettingsTab(self.notebook.tab('Настройки собеседования'))
        self.interview_pass = InterviewPassTab(self.notebook.tab('Пройти собеседование'), self.themes, self.database, self.show_hint_window)



    def create_new_user(self):
        if self.create_user_window is None or not self.create_user_window.winfo_exists():
            self.create_user_window = CreateNewUser('Python Interview Assistant - Добавить пользователя')
            self.focus()
            self.create_user_window.focus()
        else:
            self.create_user_window.lift()
            self.create_user_window.focus()
    
    def show_hint_window(self, filepath):
        if self.hint_window is None or not self.hint_window.winfo_exists():
            self.hint_window = HintWindow('Python Interview Assistant - Подсказка', filepath)
            self.focus()
            self.hint_window.focus()
        else:
            self.hint_window.lift()
            self.hint_window.focus()




class UserStatisticsTab(ctk.CTkFrame):
    def __init__(self, parent, create_new_user, users):
        super().__init__(parent)
        self.width = 1000
        self.place(x=0, y=0)
        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure((0, 1), weight=1)
        self.create_new_user = create_new_user
        self.users = users

        self.user_var = tk.StringVar(value='==Выберите пользователя==')

        self.create_widgets()

        # EVENTS
        self.combobox1.bind("<<ComboboxSelected>>", lambda event: print(self.user_var.get()))

    def create_widgets(self):
        # PINK SCREEN
        self.choose_user_frame = ctk.CTkFrame(self, fg_color='#ffcccc', width=600, height=300)
        self.choose_user_frame.grid(row=0, column=0, sticky='n', padx=20, pady=20)
        self.label1 = ctk.CTkLabel(self.choose_user_frame, text='Управление пользователями', font=('Calibri', 25))
        self.label1.place(x=30, y=10)
        self.label2 = ctk.CTkLabel(self.choose_user_frame, text='Выберите пользователя', font=('Calibri', 18))
        self.label2.place(x=30, y=50)
        self.combobox1 = ttk.Combobox(
            self.choose_user_frame,
            textvariable=self.user_var,
            state="readonly")
        self.combobox1.configure(values=self.users)
        self.combobox1.place(x=30, y=80, width=250, height=35)
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
    def __init__(self, parent, themes, database, show_hint_window):
        super().__init__(parent)
        self.width = 1200
        self.place(x=0, y=0)
        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure((0, 1), weight=1)
        self.database = database
        self.themes = themes
        self.show_hint_window = show_hint_window


        self.question_key = None

        self.context_menu = tk.Menu(self, tearoff=0)
        self.context_menu.add_command(label="Копировать", command=lambda: self.focus_get().event_generate("<<Copy>>"))

        self.create_interview_frame()
        self.create_control_frame()
        self.create_treeview_frame()

        # Events
        self.context_menu_event_loop(self.theory_textbox)
        self.context_menu_event_loop(self.coding_textbox)
        self.treeview_events()

    
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
        self.control_frame = ctk.CTkFrame(self, fg_color='#ffd38f', width=620, height=200)
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
            hover_color='#ff662a',
            command=self.push_hint_button
        ).place(x=20, y=110)

    def create_treeview_frame(self):
        self.control_frame = ctk.CTkFrame(self, fg_color='#ffd38f', width=530, height=615)
        self.control_frame.grid(row=0, column=1, rowspan=2, pady=10)

        self.question_tree = ttk.Treeview(
            master=self.control_frame,
        )
        
        self.question_tree.heading('#0', text='Темы и вопросы собеседования', anchor=tk.W)

        # adding data
        for theme_id, theme_title in self.themes.items():
            self.question_tree.insert('', tk.END, text=theme_title, iid=theme_id, open=True)

        # adding children of first node
        for data in self.database:
            self.question_tree.insert('', tk.END, text=f'Вопрос {data[0] - 7}. {data[2]}', iid=data[0], open=False)
            match data[0]:
                case 8 | 9: self.question_tree.move(data[0], 0, data[1])
                case 10 | 11: self.question_tree.move(data[0], 1, data[1])
                case 12 | 13: self.question_tree.move(data[0], 2, data[1])
                case 14 | 15: self.question_tree.move(data[0], 3, data[1])
                case 16 | 17: self.question_tree.move(data[0], 4, data[1])
                case 18 | 19: self.question_tree.move(data[0], 5, data[1])
                case 20 | 21: self.question_tree.move(data[0], 6, data[1])


        self.question_tree.place(x=20, y=20, width=490, height=580)

    def push_hint_button(self):
        if isinstance(self.question_key, int):
            self.show_hint_window(filepath=f'knowledge/{self.database[self.question_key][5]}.pdf')
            # subprocess.Popen(["start", "", f'knowledge/{self.database[self.question_key][5]}.pdf'], shell=True)
    
    def context_menu_event_loop(self, text_box):
        text_box.bind("<Button-3>", lambda event: self.context_menu.post(event.x_root, event.y_root))
        text_box.bind("<Control-c>", lambda event: self.copy_text)
    
    def treeview_events(self):
        self.question_tree.bind('<<TreeviewSelect>>', self.item_select)
    
    def insert_question_in_textfield(self, question_key):
        if question_key is not None:
            self.theory_textbox.delete('1.0', 'end')
            self.coding_textbox.delete('1.0', 'end')
            self.theory_textbox.insert('1.0', self.database[question_key][3])
            self.coding_textbox.insert('1.0', self.database[question_key][4])
        else:
            self.theory_textbox.delete('1.0', 'end')
            self.coding_textbox.delete('1.0', 'end')
    
    def item_select(self, event):
        for i in self.question_tree.selection():
            self.question_key = self.question_tree.item(i)['text'].split('. ')[0].strip('Вопрос ')
            self.question_key = int(self.question_key) - 1 if self.question_key.isdigit() else None
            self.insert_question_in_textfield(self.question_key)
    
    def copy_text(event):
        widget = event.widget
        selected_text = widget.clipboard_get()
        if widget.tag_ranges("sel"):
            selected_text = widget.get("sel.first", "sel.last")
        widget.clipboard_clear()
        widget.clipboard_append(selected_text)
    

class CreateNewUser(ctk.CTkToplevel):
    def __init__(self, title):
        super().__init__()
        self.title(title)
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

class HintWindow(ctk.CTkToplevel):
    def __init__(self, title, filepath):
        super().__init__()
        self.title(title)
        self.geometry('580x520+440+180')
        self.resizable(width=0, height=0)
        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure((0, 1), weight=1)

        self.file = filepath
        self.current_page = 0
        self.numPages = None 

        self.pages_amount = ctk.StringVar()


        # Top Frame
        self.top_frame = ctk.CTkFrame(self, width=580, height=460)
        self.top_frame.grid(row=0, column=0)
        self.top_frame.grid_propagate(False)

        # Bottom Frame
        self.bottom_frame = ctk.CTkFrame(self, width=580, height=50, fg_color='transparent')
        self.bottom_frame.grid(row=1, column=0)
        self.bottom_frame.rowconfigure((0,), weight=1)
        self.bottom_frame.columnconfigure((0, 1, 2, 3), weight=1)

        # Vertical Scrolbar
        self.scrolly = ctk.CTkScrollbar(self.top_frame, orientation='vertical')
        self.scrolly.grid(row=0, column=1, sticky='ns')

        # Horizontal Scrolbar
        self.scrollx  = ctk.CTkScrollbar(self.top_frame, orientation='horizontal')
        self.scrollx .grid(row=1, column=0, sticky='we')

        # Show PDF
        self.output = ctk.CTkCanvas(self.top_frame, bg='#ECE8F3', width=560, height=435)
        self.output.configure(yscrollcommand=self.scrolly.set, xscrollcommand=self.scrollx.set)
        self.output.grid(row=0, column=0)
        self.scrolly.configure(command=self.output.yview)
        self.scrollx.configure(command=self.output.xview)

        # Buttons and page label
        self.upbutton = ctk.CTkButton(self.bottom_frame, text='Предыдущая страница', width=140, command=self.previous_page)
        self.upbutton.grid(row=0, column=0, padx=5, pady=8)
        self.downbutton = ctk.CTkButton(self.bottom_frame, text='Следующая страница', width=140, command=self.next_page)
        self.downbutton.grid(row=0, column=1, pady=8)
        self.page_label = ctk.CTkLabel(self.bottom_frame, textvariable=self.pages_amount)
        self.page_label.grid(row=0, column=2, padx=5)


        if self.file:
            self.miner = PDFMiner(self.file)
            data, numPages = self.miner.get_metadata()
            self.current_page = 0
            if numPages:
                self.numPages = numPages
                self.display_page()
    
    def display_page(self):
        if 0 <= self.current_page < self.numPages:
            self.img_file = self.miner.get_page(self.current_page)
            self.output.create_image(0, 0, anchor='nw', image=self.img_file)
            self.stringified_current_page = self.current_page + 1
            self.page_label['text'] = str(self.stringified_current_page) + ' of ' + str(self.numPages)
            region = self.output.bbox(tk.ALL)
            self.output.configure(scrollregion=region)
            self.pages_amount.set(f'Страница: {self.stringified_current_page} из {self.numPages}')
    
    def next_page(self):
        if self.current_page <= self.numPages - 1:
            self.current_page += 1
            self.display_page()

    
    def previous_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.display_page()

class PDFMiner:
    def __init__(self, filepath):
        self.filepath= filepath
        self.pdf = fitz.open(self.filepath)
        self.first_page = self.pdf.load_page(0)
        self.width, self.height = self.first_page.rect.width, self.first_page.rect.height
        zoomdict = {800:0.8, 700:0.6, 600:1.0, 500:1.0}
        width = int(math.floor(self.width / 100.0) * 100)
        self.zoom = zoomdict[width]
    
    def get_metadata(self):
        metadata = self.pdf.metadata
        numPages = self.pdf.page_count
        return metadata, numPages

    def get_page(self, page_num):
        page = self.pdf.load_page(page_num)
        if self.zoom:
            mat = fitz.Matrix(self.zoom, self.zoom)
            pix = page.get_pixmap(matrix=mat)
        else:
            pix = page.get_pixmap()
        px1 = fitz.Pixmap(pix, 0) if pix.alpha else pix
        imgdata = px1.tobytes("ppm")
        return PhotoImage(data=imgdata)

    def get_text(self, page_num):
        page = self.pdf.load_page(page_num)
        text = page.getText('text')
        return text

if __name__ == '__main__':
    main_window = Main('Python Interview Assistant', (1280, 720))
    main_window.mainloop()
