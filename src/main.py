from tkinter import *
from tkinter.font import Font
from tkinter import simpledialog, filedialog, messagebox
from src.GUI.LoginGUI import Login
from src.GUI.SignUpGUI import SignUp
from src.GUI.HomeGUI import Home
from src.GUI.DisplayRecipeGUI import DisplayRecipe
from src.classes.Account import Account
from src.WebScrapingFood import *


class GUI:
    WHITE = "#FBFBFB"
    GREY = "#707070"
    BLUE = "#7586F2"
    BLACK = '#000000'
    YELLOW = '#FFAE03'

    def __init__(self):
        self.root = Tk()
        self.root.title("Cookbook")
        self.root.config(bg = GUI.WHITE)
        self.root.config(width = 1080, height = 1080)

        self.Account = Account(-1, "", "", "", "", "")

        self.titleFont = Font(family="product sans bold", size = "55")
        self.headingFont = Font(family="product sans bold", size="45")
        self.lblFont = Font(family="product sans", size="15")
        self.bntFont = Font(family="product sans", size="14")

        self.LoginFrame = Frame(self.root)
        self.SignUpFrame = Frame(self.root)
        self.HomeFrame = Frame(self.root)
        self.RecipeFrame = Frame(self.root)
        self.frameList = [self.LoginFrame, self.SignUpFrame, self.HomeFrame, self.RecipeFrame]
        for frame in self.frameList:
            frame.grid(row=0, column=0, sticky='news')


        self.Login = Login(self.LoginFrame, self.headingFont,self.lblFont, self.bntFont, GUI.WHITE, GUI.GREY, GUI.BLUE)
        self.Login.bntLogin.config(command = self.login)
        self.Login.bntSignUp.config(command = lambda : self.moveScreen(self.SignUpFrame))

        self.SignUp = SignUp(self.SignUpFrame, self.headingFont,self.lblFont, self.bntFont, GUI.WHITE, GUI.GREY, GUI.BLUE)
        self.SignUp.bntSignUp.config(command =  self.signup)
        self.SignUp.bntLogin.config(command = lambda: self.moveScreen(self.LoginFrame))

        self.Home = Home(self.HomeFrame, self.headingFont, self.lblFont, self.bntFont, self.titleFont, GUI.WHITE, GUI.GREY, GUI.BLUE, GUI.BLACK, GUI.YELLOW)
        self.Home.bntAddRecipe.config(command= self.createRecipe)
        self.Home.bntLogout.config(command= lambda : self.moveScreen(self.LoginFrame))
        self.Home.bntAddUrl.config(command = self.get_URL)
        self.Home.viewRecipes.treeview.bind("<Double-1>", lambda e: self.moveScreen(self.RecipeFrame))

        self.Recipe = DisplayRecipe(self.RecipeFrame, self.headingFont, self.lblFont, self.bntFont, self.titleFont, GUI.WHITE, GUI.GREY, GUI.BLUE, GUI.BLACK, GUI.YELLOW)
        self.Recipe.bntPizza.config(command = lambda : self.moveScreen(self.HomeFrame))

    def login(self):
        if (Login.login(self.Login)):
            self.Account.login(self.Login.getUsername())
            self.Login.clearField()
            self.moveScreen(self.HomeFrame)

        else:
            messagebox.showerror("User credentials Not Recognised","No accounts for with these credentails please try again!")

    def signup(self):
        if(self.SignUp.signup()):
            self.Account.login(self.SignUp.getEmail())
            self.SignUp.clearField()
            self.moveScreen(self.HomeFrame)
             #moving the screeen
    def createRecipe(self):
        self.Home.createRecipe(self.Account.get_account_id())

    def get_URL(self):
        sucess = scrape(self.Home.entSearchRecipe.get())
        if sucess:
            messagebox.showinfo("Success","Your recipe was added to the database")
            self.Home.populateTreeview()
        else:
            messagebox.showerror("Error", "Your url was not supported")



    def moveScreen(self, frame):
        frame.tkraise()


if __name__ == "__main__":
    recipeHub = GUI()
    recipeHub.moveScreen(recipeHub.LoginFrame)
    recipeHub.root.mainloop()
