from tkinter import *
from tkinter.font import Font
from tkinter import simpledialog, filedialog, messagebox
from tkinter import ttk
from src.classes.File import *
from src.GUI.NavBar import NavBar
from src.GUI.RecipeGUI import *
from src.GUI.TreeviewMaker import *
from PIL import Image, ImageTk

class Home:
    def __init__(self, root, headFont, lblFont, bntFont, titleFont, white, grey, blue, black,yellow):
        self.root = root
        self.root.config(bg=white)

        self.headFont = headFont
        self.lblFont = lblFont
        self.bntFont = bntFont
        self.titleFont = titleFont
        self.white = white
        self.grey = grey
        self.blue = blue
        self.black = black
        self.yellow = yellow

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
        self.RecipeCategory.grid(row=3,column=0, sticky = 'W', padx = 10, pady = 5, rowspan = 3)

        self.lblRecipes = Label(self.RecipeCategory, text = 'Recipes', font =   Font(family = "product san", size ="30"), bg = white, fg = black)
        self.lblRecipes.grid(row=0,column=0, pady=10, padx = 10)



        self.addIcon = ImageTk.PhotoImage(Image.open("imgs/addIcon.png"))
        self.bntAddRecipe = Button(self.RecipeCategory, image = self.addIcon, bg = white, relief = FLAT, fg = white)
        self.bntAddRecipe.grid(row=1, padx = 5)

        self.pizzaLogo = ImageTk.PhotoImage(Image.open("Buttons/pizza.png"))
        self.bntPizza = Button(self.RecipeCategory, image=self.pizzaLogo, bg=white, relief = FLAT)
        self.bntPizza.grid(row=2, padx = 5, pady = 5)

        self.desertLogo = ImageTk.PhotoImage(Image.open("Buttons/desert.png"))
        self.bntDesert = Button(self.RecipeCategory, image = self.desertLogo, bg = white, relief = FLAT)
        self.bntDesert.grid(row=3,padx=5,pady=5)

        self.saladLogo = ImageTk.PhotoImage(Image.open("Buttons/salad.png"))
        self.bntSalad = Button(self.RecipeCategory, image=self.saladLogo, bg=white, relief=FLAT)
        self.bntSalad.grid(row=4, padx=5, pady=5)

        self.noodleLogo = ImageTk.PhotoImage(Image.open("Buttons/noodle.png"))
        self.bntNoodle = Button(self.RecipeCategory, image=self.noodleLogo, bg=white, relief=FLAT)
        self.bntNoodle.grid(row=5, padx=5, pady=5)

        self.kebabLogo = ImageTk.PhotoImage(Image.open("Buttons/kebab.png"))
        self.bntKebab = Button(self.RecipeCategory, image=self.kebabLogo, bg=white, relief=FLAT)
        self.bntKebab.grid(row=6, padx=5, pady=5)

        self.cakeLogo = ImageTk.PhotoImage(Image.open("Buttons/cake.png"))
        self.bntCake = Button(self.RecipeCategory, image=self.cakeLogo, bg=white, relief=FLAT)
        self.bntCake.grid(row=7, padx=5, pady=5)

        self.pastaLogo = ImageTk.PhotoImage(Image.open("Buttons/pasta.png"))
        self.bntPasta = Button(self.RecipeCategory, image=self.pastaLogo, bg=white, relief=FLAT)
        self.bntPasta.grid(row=8, padx=5, pady=5)

        self.Recipe = LabelFrame(self.root, text='', bg = white, bd = 0)
        self.Recipe.grid(row=3,column=1)

        self.searchRecipe = StringVar()
        self.searchRecipe.set("Search recipes and more")
        self.entSearchRecipe = Entry(self.Recipe, textvariable = self.searchRecipe, width = 50, bg = white, fg = grey, bd = 1, font = lblFont)
        self.entSearchRecipe.grid(row=0,column=0)

        self.RecipeStyle = ttk.Style()
        self.RecipeStyle.configure('AP.Treeview.Heading', font= self.titleFont, bg = white, fg = black)
        self.RecipeStyle.theme_use('alt')
        self.RecipeStyle.configure('AP.Treeview', font = self.titleFont, rowheight = 40)

        self.viewRecipes = TreeviewMaker(self.Recipe, ['Recipe ID', 'Name','Cook Time','Serving'], ['Name','Cook Time','Serving'], 50, 150, 'AP.Treeview')
        self.viewRecipes.treeview.grid(row=1, pady = 10)


    def createRecipe(self, id):
        self.newRecipe = AddRecipe(id, self.headFont, self.lblFont, self.bntFont, self.white, self.grey, self.blue, self.black, self.yellow)


