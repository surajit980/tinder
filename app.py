from dbhelper import DBHelper #import database
from tkinter import *  #import tkinter for gui
from tkinter import messagebox

class tinder:

    def __init__(self):
        # connect to database
        self.db = DBHelper()
        #gui window function call
        self.load_gui_window(self.load_login_gui)
        self.user_data=None

        
    #gui window here describe gui size title background etc
    def load_gui_window(self,gui_type):
        self.root=Tk()

        self.root.title("tinder")
        self.root.configure(background="#FF5357")

        #gui size declare
        self.root.maxsize(400,600)
        self.root.minsize(400,600)

        gui_type()

        self.root.mainloop()
    
    #login gui function here show all the requirement field in gui for login
    def load_login_gui(self):
        self.label1=Label(self.root,text="Tinder",bg="#FF5357",fg="#fff")
        self.label1.pack(pady=(20,30))
        self.label1.configure(font=("Times",32,"bold"))

        self.label2=Label(self.root,text="LogIn to Proceed",bg="#FF5357",fg="#fff")
        self.label2.pack(pady=(30,20))
        self.label2.configure(font=("Times",20,"italic"))

        self.label3=Label(self.root,text="Enter Email",bg="#FF5357",fg="#fff")
        self.label3.pack(pady=(10,5))
        self.label3.configure(font=("Times",14,"italic"))

        self.email_input=Entry(self.root)
        self.email_input.pack(pady=(2,10),ipadx=70,ipady=5)
        self.email_input.configure(font=("Times",15,"italic"))

        self.label4=Label(self.root,text="Enter Password",bg="#FF5357",fg="#fff")
        self.label4.pack(pady=(20,5))
        self.label4.configure(font=("Times",14,"italic"))

        self.password_input=Entry(self.root,show="*")
        self.password_input.pack(pady=(2,20),ipadx=70,ipady=5)
        self.password_input.configure(font=("Times",15,"italic"))

        self.login_btn=Button(text="Log In",command=lambda:self.login())
        self.login_btn.pack(pady=(40,5),ipadx=70)
        self.login_btn.configure(font=("Times",10,))

        self.label5=Label(self.root,text="OR",bg="#FF5357",fg="#fff")  
        self.label5.pack()
        self.label5.configure(font=("Times",10))

        self.register_btn=Button(text="Register")
        self.register_btn.pack(pady=(5,10),ipadx=70)
        self.register_btn.configure(font=("Times",10))

    #login function here if email and password are correct then show a message login successful 
    #and load a new gui if wrong then message wrong email and password and reload same gui
    def login(self):
        email=self.email_input.get()
        password=self.password_input.get()
        data=self.db.search(email,password)

        self.email_input.delete(0,"end")
        self.password_input.delete(0,"end")

        if len(data)==1:
            self.user_data=data[0]
            messagebox.showinfo("login message","you have logged in successfully")
            self.root.destroy()
            self.load_gui_window(self.load_user_profile_gui)
        else:           
            messagebox.showerror("login message","incorrect email/password please enter a valid one")



    #user profile function here load all information about user those are insert in database       
    def load_user_profile_gui(self):
        self.header_menu()
        self.label6=Label(self.root,text="Hello "+self.user_data[1],bg="#FF5357",fg="#fff")
        self.label6.pack(pady=(20,30))
        self.label6.configure(font=("Times",14,"bold"))

        self.logout_btn=Button(text="Log Out",command=lambda:self.logout())
        self.logout_btn.pack(pady=(40,5),ipadx=70)
        self.logout_btn.configure(font=("Times",10,))



    #logout function here after clicking this button go back log in gui
    def logout(self):
        self.user_data=None
        self.root.destroy()
        self.load_gui_window(self.load_login_gui)
    



    #header menu that is use for menu bar
    def header_menu(self):
        menu = Menu(self.root)
        self.root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Home", menu=filemenu)
        filemenu.add_command(label="My Profile")
        filemenu.add_command(label="Edit Profile")
        filemenu.add_command(label="View Profile")
        filemenu.add_command(label="LogOut")

        helpmenu = Menu(menu)
        menu.add_cascade(label="Proposals", menu=helpmenu)
        helpmenu.add_command(label="My Proposals")
        helpmenu.add_command(label="My Requests")
        helpmenu.add_command(label="My Matches")


        

obj=tinder()