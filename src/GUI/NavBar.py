from tkinter import *
from tkinter.font import Font
from tkinter import simpledialog, filedialog, messagebox
from src.classes.File import *
from PIL import Image,ImageTk


class NavBar:
    def __init__(self, pos, white, grey, blue, black):
        self.root = pos
        self.root.config(bg = white)

        self.navBarFont = Font(family="product sans bold", size = "20")

        self.navBar = LabelFrame(self.root, text ='', bg = blue, bd = 0)
        self.navBar.grid(row=0,column=0)

        self.logo = ImageTk.PhotoImage(Image.open("imgs/CookBookNav.png"))

        self.lblLogo = Label(self.navBar, image = self.logo, bg = blue)
        self.lblLogo.image = self.logo
        self.lblLogo.grid(row = 0,column=0)

        self.bntYourRecipes = Button(self.navBar, text = "Your Recipes", font = self.navBarFont, bg = blue, fg = black, relief = FLAT, width = 20)
        self.bntYourRecipes.grid(row = 0, column = 1)

        self.bntTrending = Button(self.navBar, text = "Trending", font = self.navBarFont, bg = blue, fg = black, relief = FLAT, width = 15)
        self.bntTrending.grid(row=0,column=2)

        self.lblFiller = Label(self.navBar, font = self.navBarFont, bg = blue, fg = blue, width = 47)
        self.lblFiller.grid(row=0,column=3, padx = 5)



if __name__ == "__main__":
    root = Tk()

    headingFont = Font(family="product sans bold", size="45")
    lblFont = Font(family="product sans", size="15")
    bntFont = Font(family="product sans", size="14")

    WHITE = "#FBFBFB"
    GREY = "#707070"
    BLUE = "#7586F2"
    BLACK = "#000000"

    NavBar(root, WHITE, GREY, BLUE, BLACK)
    root.mainloop()
