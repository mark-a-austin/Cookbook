from tkinter import *
from tkinter.font import Font
from tkinter import simpledialog, filedialog, messagebox
from src.GUI.LoginGUI import Login


class GUI:
    WHITE = "#FBFBFB"
    GREY = "#707070"
    BLUE = "#7586F2"

    def __init__(self):
        self.root = Tk()
        self.root.title("Cookbook")
        self.root.config(bg = GUI.WHITE)
        self.root.config(width = 1080, height = 1080)

        self.headingFont = Font(family="Segoe UI Semibold", size="45")
        self.lblFont = Font(family="Segoe UI", size="15")
        self.bntFont = Font(family="Segoe UI", size="14")

        self.LoginFrame = Frame(self.root)
        self.RecipeFrame = Frame(self.root)
        self.frameList = [self.LoginFrame, self.RecipeFrame]
        for frame in self.frameList:
            frame.grid(row=0, column=0, sticky='news')


        self.Login = Login(self.LoginFrame, self.headingFont,self.lblFont, self.bntFont, GUI.WHITE, GUI.GREY, GUI.BLUE)
        self.Login.bntLogin.config(command = self.login())

    def login(self):
        if (Login.login()):
            moveScreen(self.RecipeFrame)
        else:
            messagebox.showerror("User credentials Not Recognised","No accounts for with these credentails please try again!")





    def moveScreen(self, frame):
        frame.tkraise()


if __name__ == "__main__":
    recipeHub = GUI()
    recipeHub.moveScreen(recipeHub.LoginFrame)
    recipeHub.root.mainloop()
