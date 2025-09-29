from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

# ========================================= Function to handle login =========================================
def handle_login():
    email = email_input.get()
    password = password_input.get()

    if email == 'habibtariq175@gmail.com' and password == '12345':
        messagebox.showinfo('Login Successful', 'Welcome to Flipkart!')
    else:
        messagebox.showerror('Login Failed', 'Invalid email or password.')


# ========================================= Main Window =========================================
root = Tk()
root.title('Login Form')
root.maxsize(400, 400)
root.minsize(400, 400)
root.geometry('400x400')                              # Set the window size
root.configure(bg='#0096DC')                        # Set the background color

img = Image.open('Python GUI/flipcart.png')
resied_img = img.resize((100, 100))                   # Resize the image
final_img = ImageTk.PhotoImage(resied_img)

img_lable = Label(root, image=final_img)              # Create a label to hold the image
img_lable.pack(pady=(10, 10))                         # pack() is Geometry manager , jo khud ba khud apne aap ko adjust kar leta hai
             # | 
             # | pady is used to give padding in y direction


# === Flipkart Text Label ===
txt_lable = Label(root, text='Flipkart', fg='white', bg='#0096DC', font=('Verdana', 24))             
txt_lable.pack(pady=(0, 20))                          # pady=(top, bottom)


# === Email Label ===
email_lable = Label(root, text='Enter Email:', fg='white', font=('Verdana', 12), bg='#0096DC')
email_lable.pack()


# === Email Input Box === 
email_input = Entry(root, width=20, borderwidth=3, font=('Verdana', 12))
email_input.pack(ipady=6, pady=(1,15))                 # ipady is used to give padding inside the box


# === Password Label === 
password_lable = Label(root, text='Enter Password:', fg='white', font=('Verdana', 12), bg='#0096DC')
password_lable.pack()


# === Password Input Box === 
password_input = Entry(root, width=20, borderwidth=3, font=('Verdana', 12))
password_input.pack(ipady=6, pady=(1,15))                 # ipady is used to give padding inside the box


# === Login Button === 
login_btn = Button(root, text='Login Here!', fg = 'white', bg = 'Black', font=('Verdana', 12), height=10, width=15, command=handle_login)
login_btn.pack(pady=(10,10))


root.mainloop()                                       # Keep the window open