from tkinter import *
from tkinter import messagebox
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk

root =Tk()


root.geometry('925x500+300+200')
root.title('Přihlášení')
root.configure(bg='#fff')
root.resizable(False,False)

def signin():
    username=user.get()
    password=code.get()

    if username=='admin' and password=='1234':
        menu=Toplevel(root)
        menu.title('Menu')
        menu.geometry('925x500+300+200')
        menu.config(bg='white')
        menu.resizable(False,False)

        heading=Label(menu,text='Menu', font='Arial 30 bold', bg='white', fg='#57a1f8')
        heading.pack(pady=10)
        Button(menu,width=39,pady=7,text='Textové pole', bg='#57a1f8',fg='white',border=0).place(x=35,y=204)
        Button(menu,width=20,pady=7,text='Kliknutím otevřeš', bg='white',fg='black',border=0).place(x=380,y=70)
        
        
        menu.mainloop()
        root.destroy()
        
            #screen=Toplevel(root)
            #screen.title('Časovač')
            #screen.geometry('400x600')
            #screen.config(bg='white')
            #screen.resizable(False,False)

            #heading=Label(screen,text='Časovač', font='Arial 30 bold', bg='white', fg='#57a1f8')
            #heading.pack(pady=10)

            # Label(screen,font=('Arial',15,'bold'), text='Aktuální čas').place(x=65,y=70)
            
            # current_time=Label(screen,font=('Arial',15,'bold'), text)
            
            #hrs=StringVar()
            #Entry(screen,textvariable=hrs,width=2,font='Arial 50').place(x=30,y=155)
            #hrs.set('00')

            #mins=StringVar()
            #Entry(screen,textvariable=mins,width=2,font='Arial 50').place(x=150,y=155)
            #mins.set('00')

            #sec=StringVar()
            #Entry(screen,textvariable=sec,width=2,font='Arial 50').place(x=270,y=155)
            #sec.set('00')
            ###### https://youtu.be/KTlT9saZFYc?list=PLl316cKxhMxtOWHa88kDqm42uWz1aqGfD&t=628
            
            # Button(screen,width=35,pady=7,text='Tajné infomace', bg='#57a1f8',fg='white',border=0).place(x=20,y=50)

            #screen.mainloop()
    elif username!= 'admin' and password!='1234':
        messagebox.showerror('Špatné přihlášení', 'Heslo a přihlašovací jméno bylo zadáno špatně. Zkuste to znovu.')
    elif password!='1234':
        messagebox.showerror('Špatné přihlášení', 'Heslo bylo zadáno špatně. Zkuste to znovu.')
    elif username!='admin':
        messagebox.showerror('Špatné přihlášení', 'Přihlašovací jméno bylo zadáno špatně. Zkuste to znovu')

img = PhotoImage(file='login.png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg='white')
frame.place(x=480,y=70)

heading=Label(frame,text='Přihlášení',fg='#57a1f8',bg='white',font=('Arial', 23, 'bold'))
heading.place(x=100,y=5)

#--------------------------------
def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Přihlašovací jméno')
user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHej UI Light', 11))
user.place(x=30,y=80)
user.insert(0,'Přihlašovací jméno')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

#----------------------------------
def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Heslo')
code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHej UI Light', 11))
code.place(x=30,y=150)
code.insert(0,'Heslo')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

#-------------------------------

Button(frame,width=39,pady=7,text='Přihlásit se', bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
label=Label(frame,text='Nemáš účet?',fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

sing_up= Button(frame,width=11,text='Registrovat se',border=0,bg='white',cursor='hand2', fg='#57a1f8')
sing_up.place(x=215,y=270)

# https://youtu.be/X9reTI_Mckk?t=1229

mainloop()