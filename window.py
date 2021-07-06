import time
import tkinter as tk
from tkinter.constants import NO
import tkinter.ttk as ttk
import ttkthemes
import threading
import datetime
import PIL.ImageTk as ImageTk
import PIL.ImageGrab as ImageGrab
import keyboard  # using module keyboard

n = 0
b = False
def CloseWindow():
    b = True
    window.destroy()

def JieTu():
    global n
    global im
    global label2
    while True:  # making a loop
          # used try so that if user pressed other than the given key error will not be shown
        print("\r你已截图{}张".format(str(n)), end=" ")
        if b or keyboard.is_pressed('F8'):  # if key 'F8' is pressed 
            print('Exit!')
            break
        if keyboard.is_pressed('F6'):  # if key 'F6' is pressed 
            day = datetime.datetime.now()
            img = Jie()
#            im = ImageTk.PhotoImage(image=img)
            img.save("{}.jpg".format(time.strftime("%Y%m%d%H%M%S", time.localtime())))
#            label2.configure(image = im)
            n = n + 1 
            print("\r你已截图{}张\a".format(str(n)), end=" ")
            label1Text.set("你已截图{}张".format(str(n)))
            time.sleep(0.5)
    window.quit()
    quit(0)

def Jie():
    return ImageGrab.grab()

def Button():
    global n
    global im
    global label2
    day = datetime.datetime.now()
    img = Jie()
    im = ImageTk.PhotoImage(image=img)
    img.save("{}.jpg".format(time.strftime("%Y%m%d%H%M%S", time.localtime())))
    label2.configure(image = im)
    n = n + 1 
    print("\r你已截图{}张\a".format(str(n)), end=" ")

window = tk.Tk()
style = ttkthemes.ThemedStyle(window)
style.set_theme("clam")
window.protocol('WM_DELETE_WINDOW', CloseWindow)
win = ttk.Frame(window, width=20, height=20)
label1Text = tk.StringVar()
label1Text.set("你已截图{}张".format(str(n)))
button = ttk.Button(win, text="截图", command=Button)
label1 = ttk.Label(win, textvariable=label1Text).pack()
button.pack()
label2 = ttk.Label(win, width=20, compound='center')
label2.pack()
win.pack()
threading.Thread(target=JieTu).start()
#Jietu()
window.mainloop()
