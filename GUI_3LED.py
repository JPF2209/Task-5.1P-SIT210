from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

#Hardware Setting
bLed = LED(18)
rLed = LED(23)
gLed = LED(16)

#Define GUI
win = Tk()
win.title("LED Setter")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

#Defined functions
#Program to set led to certain colour
def ledSet(colour):
	if colour == "blue":
		rLed.off()
		gLed.off()
		bLed.on()
	
	if colour == "red":
		bLed.off()
		gLed.off()
		rLed.on()
	
	if colour == "green":
		rLed.off()
		bLed.off()
		gLed.on()
		
#Function to exit program
def exitProgram():
	RPi.GPIO.cleanup()
	win.destroy()

#Widgets
#Buttons work the same for blue, red and green with the difference being colour specific functions
blueButton = Button(win, text = 'Turn Blue LED On', font = myFont, command = lambda: ledSet("blue"), bg = 'blue', height = 1, width = 24)
blueButton.grid(row = 0, column = 1)
redButton = Button(win, text = 'Turn Red LED On', font = myFont, command = lambda: ledSet("red"), bg = 'red', height = 1, width = 24)
redButton.grid(row = 1, column = 1)
greenButton = Button(win, text = 'Turn Green LED On', font = myFont, command = lambda: ledSet("green"), bg = 'green', height = 1, width = 24)
greenButton.grid(row = 2, column = 1)
exitButton = Button(win, text = 'Exit', font = myFont, command = exitProgram, bg = 'cyan', height = 1, width = 6)
exitButton.grid(row = 3, column = 1)

mainloop()
