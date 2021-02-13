from tkinter import *
from tkinter.font import Font
from tkinter import simpledialog, filedialog, messagebox
from src.classes.File import *


class Login:

    def __init__(self, root,headFont,  lblFont, bntFont, white, grey, blue):
        self.root = root
        self.root.config(bg=white)
        self.blueBox = Label(self.root, text = "", bg = blue, fg = blue, bd = 0, width = 90, height = 30)
        self.blueBox.grid(row=0,column=1)

        self.loginFrame = LabelFrame(self.root, text="", font=lblFont, bg = white, fg = grey, bd = 0)
        self.loginFrame.grid(row=0,column=0, padx = 20)

        self.lblLogin = Label(self.loginFrame , text = "Login", font = headFont, bg = white, fg = grey)
        self.lblLogin.grid(row=0,column=0, sticky = "W", columnspan = 2, padx = 5, pady = 50)


        self.lblUsername = Label(self.loginFrame, text = "Username", font = lblFont, bg = white, fg = grey )
        self.lblUsername.grid(row=1,column=0, padx = 5, sticky = 'W', columnspan = 2)

        self.username = StringVar()

        self.entUsername = Entry(self.loginFrame, textvariable = self.username, font = lblFont, bd = 5, bg = white, width = 40)
        self.entUsername.grid(row=2,column = 0, padx = 5, columnspan = 2)

        self.lblPassword = Label(self.loginFrame, text="Password", font=lblFont, bg=white, fg=grey)
        self.lblPassword.grid(row=3, column=0, padx=5, sticky='W', columnspan = 2)

        self.password = StringVar()
        self.entPassword = Entry(self.loginFrame, textvariable=self.password, font=lblFont, bd=5, bg=white, width=40, show = '•')
        self.entPassword.grid(row=4, column=0, padx=5, columnspan = 2)

        self.bntLogin = Button(self.loginFrame, text = "Login", width = 40, bg = blue, fg = white, font = bntFont, relief = FLAT, bd = 1)
        self.bntLogin.grid(row=5,column=0,padx=5, pady = 20, columnspan = 2)

        self.lblNoAccount = Label(self.loginFrame, text = "Don't have an account?", bg = white, fg = grey ,font = bntFont)
        self.lblNoAccount.grid(row=6,column = 0, sticky = 'W', padx = 5)

        self.bntSignUp = Button(self.loginFrame, text = "Sign Up", bg = white, fg = blue, font = bntFont, relief = FLAT)
        self.bntSignUp.grid(row=6,column=1,sticky='W')

    def clearField(self):
        self.username.set("")
        self.password.set("")

    def getUsername(self):
        return self.username.get()
    def getPassword(self):
        return self.password.get()

    def login(self):
        username = self.getUsername() #index 4
        password = self.getPassword() #index 5

        getAccounts = fileReader("Database/accounts.csv")
        for i in getAccounts:
            print(i[4] == username)
            if (username == i[4]) and (password == i[5]):
                self.clearField()
                return True;

        return False



