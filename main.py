import time


class Pomodoro:
    def __init__(self, focus_minutes):
        self.focus_minutes = focus_minutes
        self.break_minutes = focus_minutes / 6
        self.is_focus = True
        pass

    def focus_start(self):
        if self.is_focus:
            pass

    @staticmethod
    def timer(self, minutes):
        min_to_sec = minutes * 60
        for sec in range(min_to_sec, 0, -1):
            pass

pomodoro = Pomodoro(63)
pomodoro.focus_start()