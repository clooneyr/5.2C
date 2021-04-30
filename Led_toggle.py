from tkinter import*
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

## hard ware
led = LED(14)
led2 = LED(15)
led3= LED(18)

##GUI Definitions ##
win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size =12, weight = "bold")

## EVENT FUNCTIONS ##

def ledToggle():
	if led.is_lit:
		led.off()
		ledButton["Text"] = "Turn LED on"
	else:
		led.on()
		led2.off()
		led3.off()
		ledButton["Text"] = "Turn LED off"
def ledToggle2():
	if led2.is_lit:
		led2.off()
		ledButton["Text"] = "Turn LED on"
	else:
		led2.on()
		led3.off()
		led.off()
		ledButton["Text"] = "Turn LED off"
		
def ledToggle3():
	if led3.is_lit:
		led3.off()
		ledButton["Text"] = "Turn LED on"
	else:
		led3.on()
		led2.off()
		led.off()
		ledButton["Text"] = "Turn LED off"
		
		
def close():
    RPi.GPIO.cleanup()
    win.destroy()

### WIDGETS ###
ledButton = Button(win, text = 'Turn ORANGE ON', font = myFont, command = ledToggle, bg = 'orange', height = 1, width = 24)
ledButton.grid(row = 0, column = 1)
ledButton2 = Button(win, text = 'Turn PURPLE ON', font = myFont, command = ledToggle2, bg = 'purple', height = 1, width = 24)
ledButton2.grid(row = 1, column = 1)
ledButton3 = Button(win, text = 'Turn GREEN ON', font = myFont, command = ledToggle3, bg = 'green', height = 1, width = 24)
ledButton3.grid(row = 2, column = 1)


exitButton = Button(win, text = 'Exit', font = myFont, command = close, bg = 'red', height = 1, width = 10)
exitButton.grid(row = 4, column = 1)

win.protocol("WM_DELETE_WINDOW", close) #exit cleanly
