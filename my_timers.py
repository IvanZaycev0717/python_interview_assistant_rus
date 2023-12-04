from abc import ABC, abstractmethod
from threading import Timer


class MyTimerInterface(ABC):
    """Abstract class for custom timers."""

    @abstractmethod
    def timeout(self):
        """Performs user's commands when time has ended."""
        pass


class MessageTimer(MyTimerInterface):
    """Class for changing an error message when time has ended."""

    def __init__(self, delay, condition, label):
        self.delay = Timer(delay, self.timeout)
        self.condition = condition
        self.label = label
        self.delay.start()

    def timeout(self):
        self.condition.set('')
        self.label.config(background='#d3e4ef')


class CommandTimer(MyTimerInterface):
    """Class for performing of command when time has ended."""

    def __init__(self, delay, command):
        self.delay = Timer(delay, self.timeout)
        self.command = command
        self.delay.start()

    def timeout(self):
        self.command()
