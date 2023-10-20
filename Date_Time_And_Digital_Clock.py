from tkinter import Label, Tk
import time

window = Tk()
window.title("Date Time And Digital Clock - Made by M£RT AYDIN")
window.geometry("1450x200")
window.resizable(True,True)

text= ("Roboto", 80, 'bold')
background = "#ff1493"
foreground= "#c0c0c0"
border = 40

label = Label(window, font=text, bg=background, fg=foreground, bd=border)
label.grid(row=0, column=1)

def digitalClock():
   time_live = time.strftime("(%d/%m/%Y) <--> (%X)")  # %X  ==  %H:%M:%S 
   label.config(text = time_live)
   label.after(200, digitalClock)

digitalClock()
window.mainloop()