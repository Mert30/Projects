import speedtest
from tkinter import *

def Analyze():
    speed = speedtest.Speedtest()
    speed.get_servers()
    download_speed = str(round(speed.download() / (10**6),3)) + " Mbps"
    upload_speed = str(round(speed.upload() / (10**6),3)) + " Mbps"
    label_download_speed.config(text = download_speed)
    label_upload_speed.config(text = upload_speed)

def Exit():
    exit()
    
root = Tk()
root.geometry("310x250")
root.resizable(False,False)
root.title("Internet Speed Test")
root.config(bg = "#FAEBD7")

Label(root, text = "Internet Speed Test", font = ("Arial,bold", 22), bg = "#87CEFA", fg = "Black", width = 30).pack(pady = 10)

l1 = Label(root, text = "Download Speed : ", font = ("Arial,bold", 15), bg = "#FAEBD7")
l1.place(x = 10, y = 80)
label_download_speed = Label(root, text = "0", font = ("Arial,bold", 15), bg = "#FAEBD7", fg = "#708090")
label_download_speed.place(x = 180, y = 80)

l2 = Label(root, text = "Upload Speed : ", font = ("Arial,bold", 15), bg = "#FAEBD7")
l2.place(x = 10, y = 130)
label_upload_speed = Label(root, text = "0", font = ("Arial,bold", 15), bg = "#FAEBD7", fg = "#708090")
label_upload_speed.place(x = 180, y = 130)

button1 = Button(root, text = "Check", 
                 font = ("Arial,bold", 15), bd = 5, bg = "#87CEFA", 
                 fg = "Black", activebackground = "#8B8386", activeforeground = "White", command = Analyze)

button1.place(x = 60, y = 190)

button2 = Button(root, text = "EXIT", 
                 font = ("Arial,bold", 15), bd = 5, bg = "#87CEFA", 
                 fg = "Black", activebackground = "#8B8386", activeforeground = "White", command = Exit)

button2.place(x = 180, y = 190)

root.mainloop()