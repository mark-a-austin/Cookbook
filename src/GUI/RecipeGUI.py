from tkinter import *
from tkinter.font import Font
from tkinter import simpledialog, filedialog, messagebox
from src.classes.File import *
from PIL import Image,ImageTk


class AddRecipe:
    def __init__(self, headFont, lblFont, bntFont, white, grey, blue, black):
        self.tl = Toplevel()
        self.tl.title("New Recipe")
        self.tl.config(bg = white)

        self.lblFonts = Font(family="product sans bold", size="25")

        self.bar = Label(self.tl, bg = blue, width = 190, height = 6)
        self.bar.grid(row = 0, column = 0,columnspan = 3)

        self.logo = ImageTk.PhotoImage(Image.open("../imgs/CookBookNav.png"))
        self.lblHeading = Label(self.tl, image = self.logo, bg = blue)
        self.lblHeading.image = self.logo
        self.lblHeading.grid(row=0,column=0,sticky = 'W', padx = 5)

        self.lblAddNewRecipe = Label(self.tl, bg = blue, fg = white, font = Font(family="product sans bold", size="25"), text = 'New Recipe')
        self.lblAddNewRecipe.grid(row=0,column=1,sticky = 'W')

        self.lblName = Label(self.tl, bg = white, fg = grey, font = self.lblFonts, text = 'Recipe Name')
        self.lblName.grid(row=1,column=0, sticky = 'W', padx = 5, pady = 10)

        self.name = StringVar()
        self.entName = Entry(self.tl, textvariable = self.name, width = 25, bd = 1, bg = white, fg = grey, font = self.lblFonts)
        self.entName.grid(row=2,column=0, sticky = 'W', padx = 5, pady = 10, columnspan = 2)

        self.type = StringVar()
        self.type.set("Please select the type of your food")



if __name__ == "__main__":
    root = Tk()

    headingFont = Font(family="product sans bold", size="45")
    lblFont = Font(family="product sans", size="15")
    bntFont = Font(family="product sans", size="14")

    WHITE = "#FBFBFB"
    GREY = "#707070"
    BLUE = "#7586F2"
    BLACK = "#000000"

    AddRecipe(headingFont, lblFont, bntFont, WHITE, GREY, BLUE, BLACK)
    root.mainloop()