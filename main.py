import time


class Pomodoro:
    def __init__(self, focus_minutes=60, focus_sessions=4):
        self.focus_seconds = focus_minutes * 60
        self.break_seconds = int(focus_minutes * 10)
        self.focus_sessions = focus_sessions
        self.is_focus = True
        pass

    def start_timer(self):
        for _ in range(self.focus_sessions):
            if not self.is_focus:
                self.breaktime()
            self.focustime()
        print("Nice work!")

    def focustime(self):
        self.timer(self.focus_seconds, "Focus time")
        self.is_focus = False

    def breaktime(self):
        self.timer(self.break_seconds, "Break time")
        self.is_focus = True

    @staticmethod
    def timer(total_seconds, name):
        for sec in range(total_seconds, 0, -1):
            hours = int(sec / 3600)
            minutes = int(sec / 60) % 60
            seconds = sec % 60
            print(f"{name}: {hours:02}:{minutes:02}:{seconds:02}")
            time.sleep(1)


def main():
    try:
        minutes = int(input("Input focus time in minutes: "))
        sessions = int(input("Input total focus sessions: "))
        pomodoro = Pomodoro(minutes, sessions)
    except ValueError:
        pomodoro = Pomodoro()
    pomodoro.start_timer()


if __name__ == "__main__":
    main()
