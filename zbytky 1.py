img = PhotoImage(file='picture_1.png')
Label(root,image=img,bg='white').place(x=50,y=50)

label =Label(root, text="Zdravím všechny!", font=('Arial', 18))
label.pack(padx=20,pady=20)

textbox =Text(root, height=10, font=('Arial', 14))
textbox.pack()

myentry =Entry(root)
myentry.pack()

button = tk.Button(root, text='Klikni na mě!', font=('Arial', 18))
button.pack(padx=30, pady=30);