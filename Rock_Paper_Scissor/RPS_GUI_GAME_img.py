import random
import time
import tkinter as tk
from tkinter.font import Font

win = tk.Tk()
win.title("Stone Paper Scissor")
win.resizable('False','False')

frame = tk.Frame(win, width=500, height=250,bd=3,relief = 'ridge', background="Lightblue").grid(column=0,row=0,rowspan=2,columnspan=3)
frame2 = tk.Frame(win, width=500, height=170, background="Lightblue").grid(column=0, row=2, rowspan=2, columnspan=3)
frame3 = tk.Frame(win, width=500, height=100,bd=3,relief = 'ridge', background="Lightblue").grid(column=0, row=4, rowspan=1,columnspan=3)

My_font = Font(size=14)
My_font2 = Font(size=16)

rok = "ROCK"
pap = "PAPER"
sci = "SCISSOR"
value = None

op = ["ROCK", "PAPER", "SCISSOR"]

Rock_Img2 = tk.PhotoImage(file="Rock.png")
Rock_Img2 = Rock_Img2.subsample(5,5)
Paper_Img2 = tk.PhotoImage(file="Paper.png")
Paper_Img2 = Paper_Img2.subsample(5,5)
Scissor_Img2 = tk.PhotoImage(file="Scissor.png")
Scissor_Img2 = Scissor_Img2.subsample(5,5)
arrow_Img = tk.PhotoImage(file="arrow.png")
arrow_Img = arrow_Img.subsample(7,7)


def _Rock():
    you_val.config(image=Rock_Img2)
    a = random.choice(op)

    for i in range(10):
        com_val.config(image=Rock_Img2)
        com_val.update_idletasks()
        time.sleep(0.05)
        com_val.config(image=Paper_Img2)
        com_val.update_idletasks()
        time.sleep(0.05)
        com_val.config(image=Scissor_Img2)
        com_val.update_idletasks()
        time.sleep(0.05)

    if a == pap:
        com_val.config(image=Paper_Img2)
        com_val.update_idletasks()
        com_Box.configure(state='normal')
        com_Box.delete(1.0, "end")
        com_Box.insert(1.0, "\n\t\tComputer Win !!!")
        com_Box.configure(state='disabled')
    elif a == sci:
        com_val.config(image=Scissor_Img2)
        com_val.update_idletasks()
        com_Box.configure(state='normal')
        com_Box.delete(1.0, "end")
        com_Box.insert(1.0, "\n\t\t You Win !!!")
        com_Box.configure(state='disabled')
    else:
        com_val.config(image=Rock_Img2)
        com_val.update_idletasks()
        com_Box.configure(state='normal')
        com_Box.delete(1.0, "end")
        com_Box.insert(1.0, "\n\t\t Its Draw !!!")
        com_Box.configure(state='disabled')


rock_Img = tk.PhotoImage(file="Rock.png")
rock_Img = rock_Img.subsample(2,2)
Rimg_lab = tk.Button(frame, image=rock_Img, background="Lightblue", relief="groove", command=_Rock,activebackground = 'cyan')
Rimg_lab.grid(column=0, row=0, sticky="S")

rock_Lab = tk.Label(frame, text="Rock", background="Lightblue",font=My_font)  # flat, groove, raised, ridge, solid, or sunken
rock_Lab.grid(column=0, row=1, sticky="N")


def _Paper():
    you_val.config(image=Paper_Img2)
    a = random.choice(op)

    for i in range(10):
        com_val.config(image=Rock_Img2)
        com_val.update_idletasks()
        time.sleep(0.05)
        com_val.config(image=Paper_Img2)
        com_val.update_idletasks()
        time.sleep(0.05)
        com_val.config(image=Scissor_Img2)
        com_val.update_idletasks()
        time.sleep(0.05)

    if a == sci:
        com_val.config(image=Scissor_Img2)
        com_val.update_idletasks()
        com_Box.configure(state='normal')
        com_Box.delete(1.0, "end")
        com_Box.insert(1.0, "\n\t\tComputer Win !!!")
        com_Box.configure(state='disabled')
    elif a == rok:
        com_val.config(image=Rock_Img2)
        com_val.update_idletasks()
        com_Box.configure(state='normal')
        com_Box.delete(1.0, "end")
        com_Box.insert(1.0, "\n\t\t You Win !!!")
        com_Box.configure(state='disabled')
    else:
        com_val.config(image=Paper_Img2)
        com_val.update_idletasks()
        com_Box.configure(state='normal')
        com_Box.delete(1.0, "end")
        com_Box.insert(1.0, "\n\t\t Its Draw !!!")
        com_Box.configure(state='disabled')


paper_Img = tk.PhotoImage(file="Paper.png")
paper_Img = paper_Img.subsample(2,2)
Pimg_lab = tk.Button(frame, image=paper_Img, background="Lightblue", relief="groove", command=_Paper,activebackground = 'cyan')
Pimg_lab.grid(column=1, row=0, sticky="S")

Paper_Lab = tk.Label(frame, text="Paper", background="Lightblue", font=My_font)
Paper_Lab.grid(column=1, row=1, sticky="N")


def _Scissor():
    you_val.config(image=Scissor_Img2)
    a = random.choice(op)

    for i in range(10):
        com_val.config(image=Rock_Img2)
        com_val.update_idletasks()
        time.sleep(0.05)
        com_val.config(image=Paper_Img2)
        com_val.update_idletasks()
        time.sleep(0.05)
        com_val.config(image=Scissor_Img2)
        com_val.update_idletasks()
        time.sleep(0.05)

    if a == rok:
        com_val.config(image=Rock_Img2)
        com_val.update_idletasks()
        com_Box.configure(state='normal')
        com_Box.delete(1.0, "end")
        com_Box.insert(1.0, "\n\t\tComputer Win !!!")
        com_Box.configure(state='disabled')
    elif a == pap:
        com_val.config(image=Paper_Img2)
        com_val.update_idletasks()
        com_Box.configure(state='normal')
        com_Box.delete(1.0, "end")
        com_Box.insert(1.0, "\n\t\t You Win !!!")
        com_Box.configure(state='disabled')
    else:
        com_val.config(image=Scissor_Img2)
        com_val.update_idletasks()
        com_Box.configure(state='normal')
        com_Box.delete(1.0, "end")
        com_Box.insert(1.0, "\n\t\t Its Draw !!!")
        com_Box.configure(state='disabled')


scissor_Img = tk.PhotoImage(file="Scissor.png")
scissor_Img = scissor_Img.subsample(2,2)
Simg_lab = tk.Button(frame, image=scissor_Img, background="Lightblue", command=_Scissor, relief="groove",activebackground = 'cyan')
Simg_lab.grid(column=2, row=0, sticky="S")

Scissor_Lab = tk.Label(frame, text="Scissor", background="Lightblue", font=My_font)
Scissor_Lab.grid(column=2, row=1, sticky="N")

you_Lab = tk.Label(frame2, text="YOU  Choose\t   ",image = arrow_Img ,compound = 'right', foreground="Red", background="Lightblue", font=My_font)
you_Lab.grid(column=0, row=2, padx=2, columnspan=2)

you_val = tk.Label(frame2, background="Lightblue")
you_val.grid(column=2, row=2, padx=2)

com_Lab = tk.Label(frame2, text="COMPUTER  Choose ",image = arrow_Img ,compound = 'right', foreground="Red", background="Lightblue", font=My_font)
com_Lab.grid(column=0, row=3, padx=2, columnspan=2)

com_val = tk.Label(frame2, background="Lightblue")
com_val.grid(column=2, row=3, padx=2)

com_Box = tk.Text(frame3, foreground="Blue", width=40, height=3, font=My_font2, background="Lightgreen")
com_Box.insert(1.0, "\n\t\"Click on ICON of your Action !!! \"")
com_Box.grid(column=0, row=4, padx=4, columnspan=3)
com_Box.configure(state='disabled')

win.mainloop()
