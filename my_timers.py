
from threading import Timer
from typing import Any

# def timeout():
#     # do your stuff here

# def my_timer():
#     t = Timer(6, timeout)
#     t.start()


class MessageTimer:

    def __init__(self, delay, condition, label):
        self.delay = Timer(delay, self.timeout)
        self.condition = condition
        self.label = label
        self.delay.start()

    def timeout(self):
        self.condition.set('')
        self.label.config(background='#d3e4ef')
    

class CommandTimer:
    def __init__(self, delay, command):
        self.delay = Timer(delay, self.timeout)
        self.command = command
        self.delay.start()

    def timeout(self):
        self.command()

        
