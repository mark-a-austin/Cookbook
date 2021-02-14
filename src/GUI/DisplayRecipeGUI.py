from tkinter import *
from tkinter.font import Font
from tkinter import simpledialog, filedialog, messagebox
from tkinter import ttk
from src.classes.File import *
from src.GUI.NavBar import NavBar
from src.GUI.RecipeGUI import *
from src.GUI.TreeviewMaker import *
from PIL import Image, ImageTk

class DisplayRecipe:
    def __init__(self, root, headFont, lblFont, bntFont, titleFont, white, grey, blue, black, yellow):
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

        self.Top = LabelFrame(self.root, text='', bg=blue, fg=blue, bd=0)
        self.Top.grid(row=0, column=0, columnspan=3)

        self.navBar = NavBar(self.Top, white, grey, blue, black)
        self.navBar.navBar.grid(row=0, column=0, columnspan=2)

        self.RecipeCategory = LabelFrame(self.root, text='', font=headFont, bg=white, fg=black, bd=0)
        self.RecipeCategory.grid(row=1, column=0, sticky='W', padx=10, pady=5, rowspan=3)

        self.lblRecipes = Label(self.RecipeCategory, text='Recipes', font=Font(family="product san", size="30"),
                                bg=white, fg=black)
        self.lblRecipes.grid(row=0, column=0, pady=10, padx=10)

        self.addIcon = ImageTk.PhotoImage(Image.open("imgs/addIcon.png"))
        self.bntAddRecipe = Button(self.RecipeCategory, image=self.addIcon, bg=white, relief=FLAT, fg=white)
        self.bntAddRecipe.grid(row=1, padx=5)

        self.pizzaLogo = ImageTk.PhotoImage(Image.open("Buttons/pizza.png"))
        self.bntPizza = Button(self.RecipeCategory, image=self.pizzaLogo, bg=white, relief=FLAT)
        self.bntPizza.grid(row=2, padx=5, pady=5)

        self.desertLogo = ImageTk.PhotoImage(Image.open("Buttons/desert.png"))
        self.bntDesert = Button(self.RecipeCategory, image=self.desertLogo, bg=white, relief=FLAT)
        self.bntDesert.grid(row=3, padx=5, pady=5)

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

        self.Recipe = LabelFrame(self.root, text ='', bg = white, fg = white, bd = 0)
        self.Recipe.grid(row=1,column=1)



        self.Name = Label(self.Recipe, text = "Handmade Pizza with\n  Spinach and Mushrooms", font = Font(family="product sans bold", size = "25"), bg =  white, fg = black)
        self.Name.grid(row=0, column = 1)

        self.Des = Label(self.Recipe, text = "This cheesy vegan garlic mushroom\n and spinach pizza is perfect when you \n want a dinnner that's not only delicous\n but also healthy!", font = self.lblFont, bg = white, fg = black)
        self.Des.grid(row=1,column=1, sticky = 'N')

        self.pizzaCir = ImageTk.PhotoImage(Image.open("imgs/pizza.png"))
        self.lblPizza = Label(self.Recipe, image = self.pizzaCir, bg = white)
        self.lblPizza.image = self.pizzaCir
        self.lblPizza.grid(row=0,column=0,rowspan=2)

        self.lblServing = Label(self.Recipe, text = 'Serving: 2', font = self.lblFont, bg = white, fg = black)
        self.lblServing.grid(row=2,column=1,sticky='W')

        self.lblCookTime = Label(self.Recipe, text = "Cook Time: 20 mins", font = self.lblFont, bg = white, fg = black)
        self.lblCookTime.grid(row=2,column=1,sticky='E')

        self.lblInstructions = Label(self.Recipe, text = 'Instructions', bg = white, fg = black, font = Font(family="product sans bold", size = "25"))
        self.lblInstructions.grid(row=3,column=0,padx=5,sticky='W')

        self.RecipeIngredients = Text(self.Recipe, bg = white, fg = black, font = lblFont,height = 9, width = 70)
        self.RecipeIngredients.grid(row=4,column=0,columnspan=2)

        self.Instructions = """1. Heat your oven to 200°C\n 2. Roll out your pizza dough with a rolling pin. Place the pizza dough\n onto a baking sheet lined with parchment paper. (You can also use a \npizza pan or pizza stone)\n3. If using frozen spinach, simply thaw and squeeze the liquid\n4. If you using fresh spinach, bring salted water to a boil in a pot.\n Add cook for 1-2 minutes until it start to wilt. Then squeeze the spinach \nwell and chop roughly. \n5. Heat up a little oil in a small pan and roast garlic for 30 seconds while\nstirring. Then add the cream chees along with the spinach. Season with\nsalt and pepper to taste and stir to combine.\n6. Spread the spinach cream mixture over your pizza dough followed\nby vegan cheese.\n7. Bake the pizza for about 10-15 minutes until cheese is melted.\n8. In the meantime, fry mushrooms in a pan with some oil for 6-8\nminutes until golden browned. Add a little salt to taste.\n9. Toast pine nuts in another pan without adding any oil\n10. When you pizza is done top with mushrooms and pine nuts if using.\n11. Enjoy!"""
        self.RecipeIngredients.insert('1.0', self.Instructions)
        self.RecipeIngredients.config(state='disabled')

        self.Ingredientlb = LabelFrame(self.root, text ='', bg = white, fg = white, bd = 0)
        self.Ingredientlb.grid(row=1,column=2)


        self.Ingredients = Label(self.Ingredientlb, text = 'Ingredients', font =Font(family="product sans bold", size = "25"), fg = black ,bg =white)
        self.Ingredients.grid(row=0, pady = 5, sticky = 'W')

        self.IngredientsPic = ImageTk.PhotoImage(Image.open("imgs/ingredients.png"))
        self.lblIngredient = Label(self.Ingredientlb, image = self.IngredientsPic, bg = white)
        self.lblIngredient.image = self.IngredientsPic
        self.lblIngredient.grid(row=1)




