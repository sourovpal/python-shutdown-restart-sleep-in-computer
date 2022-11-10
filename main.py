from tkinter import *
import os
root = Tk()

root.geometry("450x450+600+150")
root.resizable(False, False)
root.config(bg="#ffffff")

# 
def restarttime():
    os.system("shutdown /r /t 30")
# 
def restart():
    os.system("shutdown /r /t 1")

def shutdown():
    os.system("shutdown /s /t 1")

def sleep():
    os.system("shutdown /h")

imgPower = PhotoImage(file='power.png')
btnPower = Button(root, image=imgPower, bd=0, bg="#ffffff", activebackground="#ffffff", cursor="hand2", command=restarttime)
btnPower.place(x=30, y=50)

imgRestart = PhotoImage(file='restart.png')
btnRestart = Button(root, image=imgRestart, bd=0, bg="#ffffff", activebackground="#ffffff", cursor="hand2")
btnRestart.place(x=240, y=50)

imgSleep = PhotoImage(file='sleep.png')
btnSleep = Button(root, image=imgSleep, bd=0, bg="#ffffff", activebackground="#ffffff", cursor="hand2", command=sleep)
btnSleep.place(x=30, y=240)

imgExit = PhotoImage(file='exit.png')
btnExit = Button(root, image=imgExit, bd=0, bg="#ffffff", activebackground="#ffffff", cursor="hand2", command=root.destroy)
btnExit.place(x=240, y=240)

# imgLogout = PhotoImage(file='exit.png')
# btnLogout = Button(root, image=imgLogout, bd=0, bg="#ffffff", activebackground="#ffffff", cursor="hand2")
# btnLogout.place(x=30, y=430)





root.mainloop()