from tkinter import *
from tkinter.font import Font
from tkinter import simpledialog, filedialog, messagebox


class Login:

    def __init__(self, root,headFont,  lblFont, bntFont, white, grey, blue):
        self.root = root
        self.root.config(bg=white)
        self.loginFrame = LabelFrame(self.root, text="", font=lblFont, bg = white, fg = grey, bd = 0)
        self.loginFrame.grid(row=1,column=0)

        self.lblLogin = Label(self.loginFrame , text = "Login", font = headFont, bg = white, fg = grey)
        self.lblLogin.grid(row=0,column=0, sticky = "W", columnspan = 2, padx = 5)


        self.lblUsername = Label(self.loginFrame, text = "Username", font = lblFont, bg = white, fg = grey )
        self.lblUsername.grid(row=1,column=0, padx = 5, sticky = 'W')

        self.username = StringVar()

        self.entUsername = Entry(self.loginFrame, textvariable = self.username, font = lblFont, bd = 5, bg = white, width = 40)
        self.entUsername.grid(row=2,column = 0, padx = 5)

        self.lblPassword = Label(self.loginFrame, text="Password", font=lblFont, bg=white, fg=grey)
        self.lblPassword.grid(row=3, column=0, padx=5, sticky='W')

        self.password = StringVar()
        self.entPassword = Entry(self.loginFrame, textvariable=self.password, font=lblFont, bd=5, bg=white, width=40, show = '•')
        self.entPassword.grid(row=4, column=0, padx=5)

        self.bntLogin = Button(self.loginFrame, text = "Login", width = 40, bg = blue, fg = white, font = bntFont, relief = FLAT, bd = 1)
        self.bntLogin.grid(row=5,column=0,padx=5, pady = 20)