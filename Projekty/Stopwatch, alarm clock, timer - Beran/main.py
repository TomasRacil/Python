from GUI import root,stopwatchWidgets,alarm,timerWidget
from Controls import time


def main():
    #Functions call 
    time() 
    stopwatchWidgets()
    timerWidget()
    alarm()

    root.mainloop()


if __name__ == '__main__':
    main()