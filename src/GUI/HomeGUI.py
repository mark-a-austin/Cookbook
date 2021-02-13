from tkinter import *
from tkinter.font import Font
from tkinter import simpledialog, filedialog, messagebox
from src.classes.File import *
from src.GUI.NavBar import NavBar
from PIL import Image, ImageTk

class Home:
    def __init__(self, root, headFont, lblFont, bntFont, titleFont, white, grey, blue, black,yellow):
        self.root = root
        self.root.config(bg=white)

        self.Top = LabelFrame(self.root, text='', bg = blue, fg = blue, bd = 0)
        self.Top.grid(row=0,column=0,columnspan=3)

        self.navBar = NavBar(self.Top, white,grey,blue,black)
        self.navBar.navBar.grid(row= 0, column = 0,columnspan=2)

        self.box = Label(self.Top, bg = blue, fg = blue, width = 228, height = 14)
        self.box.grid(row=1,column=0,columnspan = 3, rowspan = 2)

        self.mascot = ImageTk.PhotoImage(Image.open("imgs/mascot.png"))
        self.lblMascot = Label(self.Top, image = self.mascot, bg = blue)
        self.lblMascot.image = self.mascot
        self.lblMascot.grid(row=0,column=1,rowspan = 3)

        self.title1 = Label(self.Top, text ="     10 Minute", bg = blue, fg = white, font = titleFont)
        self.title1.grid(row=1, column=0, sticky ='S', padx = 30)

        self.title2 = Label(self.Top, text=" Meals",bg=blue, fg = white, font = titleFont)
        self.title2.grid(row=2,column=0,sticky='N',padx=25)

        self.RecipeCategory = LabelFrame(self.root, text = '', font = headFont, bg = white, fg = black, bd = 0)
        self.RecipeCategory.grid(row=3,column=0, sticky = 'W', padx = 10, pady = 5)

        self.lblRecipes = Label(self.RecipeCategory, text = 'Recipes', font =   Font(family = "product san", size ="30"), bg = white, fg = black)
        self.lblRecipes.grid(row=0,column=0, pady=10, padx = 10)

        self.addIcon = ImageTk.PhotoImage(Image.open("imgs/addIcon.png"))
        self.bntAddRecipe = Button(self.RecipeCategory, image = self.addIcon, bg = white, relief = FLAT)
        self.bntAddRecipe.grid(row=1,column=0, padx = 5)

        self.Recipe = LabelFrame(self.root, text='', bg = white, bd = 0)
        self.Recipe.grid(row=3,column=1)





        self.searchRecipe = StringVar()
        self.entSearchRecipe = Entry(self.Recipe, textvariable = self.searchRecipe, width = 50, bg = white, fg = grey, bd = 1, font = lblFont)
        self.entSearchRecipe.grid(row=0,column=0)



