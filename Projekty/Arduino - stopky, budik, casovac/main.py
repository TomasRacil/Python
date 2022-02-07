from GUI.alarmGUI import alarm
from GUI.stopwatchGUI import stopwatch
from GUI import root


def main():
    stopwatch()
    alarm()

    root.mainloop()



if __name__ == '__main__':
    main()