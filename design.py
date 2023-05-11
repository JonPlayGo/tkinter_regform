from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("Registration")

Reg_text = Label(text="Registration")
Reg_text.place(relx=0.5,rely=0.07, anchor=CENTER)

Email_text = Label(text="Email")
Email_text.place(x=180,y=50)

Email_entry = Entry(width=50)
Email_entry.place(x=40,y=74)

Passwor_text = Label(text="Password")
Passwor_text.place(x=173,y=100)

Password_entry = Entry(width=50)
Password_entry.place(x=40,y=124)

def Get_info():
    Email = Email_entry.get()
    Password = Password_entry.get()
    print(Email , " ", Password)



Registration_button = Button(text="Ok",command=Get_info)
Registration_button.place(relx=0.5,y=160)


root.mainloop()