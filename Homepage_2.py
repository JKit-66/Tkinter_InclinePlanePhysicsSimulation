#coding=utf-8
import Tkinter as tk
import subprocess
import math, time, tkMessageBox
from PIL import Image, ImageTk
import sys

root = tk.Tk()

root.title(" Welcome " )
root.geometry("850x500")

root.iconbitmap("Homepage (2).ico" )
root.configure(bg = 'navajowhite')



image= Image.open("Home_2.gif")
#New.gif

my_img = ImageTk.PhotoImage(image)


global logo
def eq():
    root1 = tk.Toplevel()
    root1.title("Equations")
    root1.configure(bg = 'white')
   
    logo_kkk = tk.PhotoImage(file="EQ.GIF")

    w1 = tk.Label(root1, image=logo_kkk).pack(side="left")
 
    root1.resizable(False, False)
    root1.mainloop()



global logo_1
def th():
    root2 = tk.Toplevel()
    root2.title("Theory")
    #root_2.configure(bg = 'white')
    
    logo_fff = tk.PhotoImage(file="Screenshot (31).GIF")

    w1 = tk.Label(root2, image=logo_fff).pack(side="left")

    root2.resizable(False, False)
    root2.mainloop()



def next_1():
    global root
    variables = {}
    root.destroy()
    execfile ("new final animation (final version yeah).py" , variables)



canvas_main = tk.Canvas (root, width = 850, height = 500)
canvas_main.pack()


pic_nex = Image.open("next.png")
pic_nex = pic_nex.resize((35, 35), Image.ANTIALIAS)
pic_next = ImageTk.PhotoImage(pic_nex)







anvas_bg = canvas_main.create_image(0, 0, anchor = "nw", image = my_img)




button_th = tk.Button (canvas_main, text = "Theory", command = th)
button_th.config(font = ("Courier", "16"))
button_eq = tk.Button (canvas_main, text = "Equations",  command = eq)
button_eq.config(font = ("Courier", "16"))


button_th.place (x = 28, y = 360, width=165,anchor = "nw")
button_th.configure (relief = "solid", borderwidth = 1)
button_eq.place (x = 28, y = 409, width=165,anchor = "nw")
button_eq.configure (relief = "solid", borderwidth = 1)



button_next = tk.Button(canvas_main , text = " Next " , image = pic_next ,   compound = tk.RIGHT, relief = "solid",font = ("Adobe Song Std", "16"), command = next_1)
button_next.configure(height = 45, width = 110, borderwidth =1)
button_next.place(x = 706, y = 400, anchor = "nw")

root.resizable(False, False)
root.mainloop()
