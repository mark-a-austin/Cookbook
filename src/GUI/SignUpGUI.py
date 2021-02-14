from tkinter import *
from tkinter.font import Font
from tkinter import simpledialog, filedialog, messagebox
from src.classes.File import *
from PIL import Image,ImageTk

class SignUp:
    def __init__(self, root, headFont,  lblFont, bntFont, white, grey, blue):
        self.root = root
        self.root.config(bg=white)

        self.blueBox = LabelFrame(self.root, text="", bg=blue, fg=white, bd=0, width=60, height=30)
        self.blueBox.grid(row=0, column=0)


        self.logo = Image.open("imgs/CookBook.png")
        self.logoPH = ImageTk.PhotoImage(self.logo)

        self.box = Label(self.blueBox, text="", bg=blue, fg=blue, bd=0, width=70, height=43, font=lblFont)
        self.box.grid(row=0, column=0)

        self.lblLogo = Label(self.blueBox, image=self.logoPH, bg=blue)
        self.lblLogo.image = self.logoPH
        self.lblLogo.grid(row=0, column=0)

        self.signupFrame = LabelFrame(self.root, text="", font = lblFont, bg = white, fg = grey, bd = 0)
        self.signupFrame.grid(row=0,column=1,padx=20)

        self.lblSignUp = Label(self.signupFrame, text = "Sign Up", font = headFont, bg = white, fg = grey)
        self.lblSignUp.grid(row=0,column=0, padx = 5, sticky = 'W', pady = 35)

        self.lblFirstname = Label(self.signupFrame, text = "First name", bg = white, fg = grey, font = lblFont)
        self.lblFirstname.grid(row=1,column=0, padx = 5, sticky = 'W')

        self.lblLastName = Label(self.signupFrame, text = "Last name", bg = white, fg = grey, font = lblFont)
        self.lblLastName.grid(row=1,column=1,padx=5,sticky='W')

        self.firstName = StringVar()
        self.entFirstName = Entry(self.signupFrame, textvariable = self.firstName, font = lblFont, bd = 2, bg = white, fg = grey, width = 30)
        self.entFirstName.grid(row=2,column=0,padx = 10, sticky = 'W')

        self.lastName = StringVar()
        self.entLastName = Entry(self.signupFrame, textvariable = self.lastName, font = lblFont, bd = 2, bg = white, fg = grey, width = 25)
        self.entLastName.grid(row=2,column=1,padx=5,sticky='W')

        self.lblEmail = Label(self.signupFrame, text = "E-Mail", font = lblFont, bg = white, fg = grey)
        self.lblEmail.grid(row=3, sticky = 'W', padx = 5)

        self.email = StringVar()
        self.entEmail = Entry(self.signupFrame, textvariable = self.email, font = lblFont, bg = white, fg = grey, bd =3, width = 57)
        self.entEmail.grid(row=4,sticky = 'W', column = 0, columnspan = 2, padx = 5)

        self.lblPassword = Label(self.signupFrame, text="Create Password", font = lblFont, bg = white, fg = grey)
        self.lblPassword.grid(row=5,sticky = 'W', padx = 5)

        self.password = StringVar()
        self.entPassword = Entry(self.signupFrame, textvariable = self.password,font = lblFont, bg = white, fg = grey, bd = 3, show = '•', width = 57 )
        self.entPassword.grid(row=6,column=0, columnspan = 2, padx = 5, sticky = 'W')

        self.bntSignUp = Button(self.signupFrame, text = "Sign Up", bg = blue, font = bntFont,  fg = white, width = 57, bd = 1, relief = FLAT)
        self.bntSignUp.grid(row=7,column=0,columnspan=2,padx=5,pady=20, sticky = 'S')

        self.lblHaveAccount = Label(self.signupFrame, text = "Already have an account?", font = bntFont, fg = grey, bg = white)
        self.lblHaveAccount.grid(row=8,column=0,padx=5,sticky='W')

        self.bntLogin = Button(self.signupFrame,text="Login in",bg = white, fg = blue, font = bntFont, relief = FLAT)
        self.bntLogin.grid(row =8, column=1,padx = 5, sticky = 'W')

    def clearField(self):
        self.firstName.set("")
        self.lastName.set("")
        self.email.set("")
        self.password.set("")

    def getFirstName(self):
        return self.firstName.get()

    def getLastName(self):
        return self.lastName.get()

    def getEmail(self):
        return self.email.get()

    def getPassword(self):
        return self.password.get()

    def signup(self):
        firstname = self.getFirstName()
        lastname = self.getLastName()
        email = self.getEmail()
        password = self.getPassword()
        userID = int(self.getID()) + 1

        if (not(self.checkForAccount(email,password)) or not(self.checkForClear([firstname,lastname,email,password]))):
            messagebox.showerror("Error Adding Account","There is already a user with those credentials!")
            return False;
        else:
            fileWriter("Database/accounts.csv",[userID,email,firstname,lastname,email,password])
            return True;

    def checkForClear(self, list):
        for i in list:
            if i == "":
                return False;
        return True;



    def getID(self):
        getAccounts = fileReader("Database/accounts.csv")
        return getAccounts[len(getAccounts) - 1][0]

    def checkForAccount(self, username, password):
        getAccounts = fileReader("Database/accounts.csv")
        for i in getAccounts:
            print(i[4] == username)
            if  ( i[4] == username):
                self.clearField()
                return False;

        return True;

