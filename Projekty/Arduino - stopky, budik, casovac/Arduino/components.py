import pyfirmata    
import time

# Connet Arduino 
board = pyfirmata.Arduino('COM3')

# Define Arduino PINs
PIEZO_PIN = board.get_pin('d:9:p')

def buzzerPlay():
    for i in range(3):
        PIEZO_PIN.write(0.2)
        board.pass_time(0.5)
        PIEZO_PIN.write(0.6)
        board.pass_time(0.5)
        PIEZO_PIN.write(0.8)
        board.pass_time(0.5)
        PIEZO_PIN.write(0)
        time.sleep(1)


# Define Arduino PINs
LED_PIN = 13

def ledShineOn():
    board.digital[LED_PIN].write(1)

def ledShineOff():
    board.digital[LED_PIN].write(0)


it = pyfirmata.util.Iterator(board)
it.start()

board.digital[10].mode = pyfirmata.INPUT

def buttonRead():
    sw = board.digital[6].read()