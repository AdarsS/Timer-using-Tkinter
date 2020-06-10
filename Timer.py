import tkinter as tk
import time
from datetime import datetime, timedelta


def setcount(entry3, entry2, entry1):
    global hrs
    global mins
    global secs
    global totalsecs
    hrs = int(entry1)
    mins = int(entry2)
    secs = int(entry3)
    totalsecs = 3600 * hrs + 60 * mins + secs
    countdown()


def countdown() :
    ltotalsecs = totalsecs
    while ltotalsecs != 0 :
        sec = timedelta(seconds=int(ltotalsecs))
        d = datetime(1, 1, 1) + sec
        label3['text']= d.second
        label2['text'] = d.minute
        label1['text'] = d.hour
        root.update()

        # delay for a second
        time.sleep(1)
        # decrement the local seconds total
        ltotalsecs -= 1
        if ltotalsecs == 0 :
            exit(0)


root = tk.Tk()
root.title("Timer")
HEIGHT = 75
WIDTH = 275

canvas = tk.Canvas(height=HEIGHT, width=WIDTH)
canvas.pack()

background_image5 = tk.PhotoImage(file='Background.png')
background_image_5label = tk.Label(root, image=background_image5)
background_image_5label.place(x=0, y=0, relwidth=1, relheight=1)

label1 = tk.Label(root, bg='white', text='', font=30)
label1.place(relx=.25, height=35, width=35)

label2 = tk.Label(root, bg='white', text='', font=30)
label2.place(relx=.45, height=35, width=35)

label3 = tk.Label(root, bg='white', font=30)
label3.place(relx=.65, height=35, width=35)

entry1 = tk.Entry(root)
entry1.place(relx=.35, rely=.65, height=25, width=25)

entry2 = tk.Entry(root)
entry2.place(relx=.45, rely=.65, height=25, width=25)

entry3 = tk.Entry(root)
entry3.place(relx=.55, rely=.65, height=25, width=25)

button = tk.Button(root, text='✔', command=lambda : setcount(entry3.get(),entry2.get(),entry1.get()))
button.place(relx=.65, rely=.65)

root.mainloop()

