from tkinter import *
from tkinter.font import Font
from tkinter import simpledialog, filedialog, messagebox
from src.classes.File import *
from PIL import Image, ImageTk
from src.classes.Recipe import *
import ast


class AddRecipe:
    def __init__(self,userID, headFont, lblFont, bntFont, white, grey, blue, black, yellow):
        self.ID = userID
        self.tl = Toplevel()
        self.tl.title("New Recipe")
        self.tl.config(bg = white)

        self.lblFonts = Font(family="product sans bold", size="25")

        self.tobSection = LabelFrame(self.tl, bg = blue, text='', bd = 0)
        self.tobSection.grid(row=0,column=0,columnspan=2)

        self.bar = Label(self.tobSection, bg = blue, width = 190, height = 6)
        self.bar.grid(row = 0, column = 0,columnspan = 3)

        self.logo = ImageTk.PhotoImage(Image.open("imgs/CookBookNav.png"))
        self.lblHeading = Label(self.tobSection, image = self.logo, bg = blue)
        self.lblHeading.image = self.logo
        self.lblHeading.grid(row=0,column=0,sticky = 'W', padx = 5)

        self.lblAddNewRecipe = Label(self.tobSection, bg = blue, fg = white, font = Font(family="product sans bold", size="25"), text = 'New Recipe')
        self.lblAddNewRecipe.grid(row=0,column=1,sticky = 'W')

        self.lblName = Label(self.tl, bg = white, fg = black, font = self.lblFonts, text = 'Recipe Name')
        self.lblName.grid(row=1,column=0, sticky = 'W', padx = 5, pady = 10)

        self.name = StringVar()
        self.entName = Entry(self.tl, textvariable = self.name, width = 25, bd = 1, bg = white, fg = grey, font = self.lblFonts)
        self.entName.grid(row=2,column=0, sticky = 'W', padx = 5, pady = 10)

        self.lblType = Label(self.tl, text = 'Type', font = self.lblFonts, bg = white, fg = black)
        self.lblType.grid(row=1,column=1,sticky='W')

        self.type = StringVar()
        self.type.set("Please select the type of your food")
        self.foodTypes = ['Pizza','Chicken','Pancakes','Pastas']
        self.omType = OptionMenu(self.tl, self.type, *self.foodTypes)
        self.omType['menu'].config(bg = white, fg = grey, font = self.lblFonts)
        self.omType.config(bg = white, fg = grey, font = self.lblFonts, width = 30)
        self.omType.grid(row=2,column=1,sticky='W')

        self.lblDifficulty = Label(self.tl, text='Difficultly', fg = black, bg = white, font = self.lblFonts)
        self.lblDifficulty.grid(row=3,column=0,sticky='W',padx=5)


        self.difficulty = StringVar()
        self.difficulty.set("Please select the difficulty")
        self.foodDifficulty = ['Easy','Medium','Hard','Master Chef']
        self.omDifficulty = OptionMenu(self.tl, self.difficulty, *self.foodDifficulty)
        self.omDifficulty.config(bg = white, fg = grey, font = self.lblFonts, width = 23)
        self.omDifficulty['menu'].config(bg = white, fg = grey, font = self.lblFonts)
        self.omDifficulty.grid(row=4,column=0,sticky='W',padx=5)

        self.lblCost = Label(self.tl, text = 'Cost', fg = black, bg = white, font = self.lblFonts)
        self.lblCost.grid(row=3, column=1,sticky='W',padx=5)

        self.cost = StringVar()
        self.cost.set('£')
        self.entCost = Entry(self.tl, textvariable = self.cost, font = self.lblFonts, bg = white, fg = grey, bd = 1)
        self.entCost.grid(row=4,column=1,sticky='W', padx = 5)



        self.lblIngredients = Label(self.tl, text = 'Ingredients', font = self.lblFonts, bg = white, fg = black)
        self.lblIngredients.grid(row=5,column=0,sticky='W')

        self.IngredientsBox = LabelFrame(self.tl, bg=white, bd=0)
        self.IngredientsBox.grid(row=6, column=0, columnspan=2)

        self.ingredientsScroll = Scrollbar(self.IngredientsBox, bg = white)
        self.ingredientsScroll.pack(side = RIGHT, fill = Y)

        self.ingredients = Text(self.IngredientsBox, bg = white, fg = black, width = 72, height = 5, font = self.lblFonts)
        self.ingredients.pack(side=LEFT, fill=Y)

        self.ingredientsScroll.config(command = self.ingredients.yview)
        self.ingredients.config(yscrollcommand=self.ingredientsScroll.set)

        self.lblMethod = Label(self.tl, text = 'Method', font = self.lblFonts, bg = white, fg = black)
        self.lblMethod.grid(row=7,column=0,sticky='W',padx=5)

        self.MethodBox = LabelFrame(self.tl, bg=white, bd=0)
        self.MethodBox.grid(row=8, column=0, columnspan=2)

        self.methodScroll = Scrollbar(self.MethodBox, bg=white)
        self.methodScroll.pack(side=RIGHT, fill=Y)

        self.method = Text(self.MethodBox, bg=white, fg=black, width=72, height=5, font=self.lblFonts)
        self.method.pack(side=LEFT, fill=Y)

        self.methodScroll.config(command=self.ingredients.yview)
        self.method.config(yscrollcommand=self.ingredientsScroll.set)

        self.lblCookTime = Label(self.tl, text ='Cook Time (minutes)', font = self.lblFonts, fg = black, bg = white)
        self.lblCookTime.grid(row=9,column=0,sticky='W',padx=5)

        self.CookTime = IntVar(self.tl, 1)
        self.spCookTime = Spinbox(self.tl, textvariable = self.CookTime, from_ = 1, to_ = 180, font = self.lblFonts, state = 'readonly', width = 15)
        self.spCookTime.grid(row=10,column=0,sticky='W',padx=5)
        self.spCookTime.bind('<MouseWheel>', self.quanCookTime)

        self.lblServing = Label(self.tl, text = 'Servings', font = self.lblFonts, fg = black, bg = white)
        self.lblServing.grid(row=9,column=1,sticky='W',padx=5)

        self.Serve = IntVar(self.tl, 1)
        self.spServe = Spinbox(self.tl, textvariable = self.Serve ,from_ = 1, to = 100, font = self.lblFonts, state = 'readonly', width = 10)
        self.spServe.grid(row=10,column=1,sticky='W', padx=5)
        self.spServe.bind('<MouseWheel>', self.quanServings)

        self.lblRegion = Label(self.tl, text = 'Region', font = self.lblFonts, bg = white, fg = black)
        self.lblRegion.grid(row=9, column = 1,padx=5)

        self.region = StringVar()
        self.region.set("Select the region")
        self.regionList = ['Chinese','Japanense','Middle Eastern','English','American','African','Mexcian','Italian']
        self.omRegion = OptionMenu(self.tl, self.region, *self.regionList)
        self.omRegion.config(bg=white, fg=grey, font=self.lblFonts, width=20)
        self.omRegion['menu'].config(bg=white, fg=grey, font=self.lblFonts)
        self.omRegion.grid(row=10, column=1, sticky='E', padx=5)

        self.bntCancel = Button(self.tl, font = self.lblFonts, bg = black, fg = white, width  =15, text = 'Cancel')
        self.bntCancel.grid(row=11,column=0,pady=15)
        self.bntCancel.config(command = self.destory)

        self.bntAdd = Button(self.tl, font = self.lblFonts, bg = yellow, fg = white, width = 15, text = 'Add', command = self.add)
        self.bntAdd.grid(row=11,column=1,pady=11)


    def quanCookTime(self, event):
        if event.num == 5 or event.delta == 120:
            self.spCookTime.invoke('buttondown')
        else:
            self.spCookTime.invoke('buttonup')

    def quanServings(self, event):
        if event.num == 5 or event.delta == 120:
            self.spServe.invoke('buttondown')
        else:
            self.spServe.invoke('buttonup')

    def destory(self):
        self.tl.destroy()

    def getIngredients(self):
        baseText = self.ingredients.get('1.0', END)
        return ast.literal_eval(baseText.split("\n")[0:len(baseText.split("\n"))-1])

    def getMethod(self):
        baseText = self.method.get('1.0', END).split("\n")
        return ast.literal_eval(baseText[0:len(baseText)-1])

    def add(self):
        newRecipe = Recipe(self.getID(), self.name.get(), self.getIngredients(), self.getMethod(), self.type.get() , self.region.get(),self.cost.get()[1:len(self.cost.get())], self.CookTime.get(), self.Serve.get(),self.ID)
        newRecipe.add_recipe()
        messagebox.showinfo("Recipe Added", "Recipe was successfully added")

    def getID(self):
        getAccounts = fileReader("Database/recipes.csv")
        return getAccounts[len(getAccounts) - 1][0]




if __name__ == "__main__":
    root = Tk()

    headingFont = Font(family="product sans bold", size="45")
    lblFont = Font(family="product sans", size="15")
    bntFont = Font(family="product sans", size="14")

    WHITE = "#FBFBFB"
    GREY = "#707070"
    BLUE = "#7586F2"
    BLACK = "#000000"
    YELLOW = '#FFAE03'

    AddRecipe(2,headingFont, lblFont, bntFont, WHITE, GREY, BLUE, BLACK, YELLOW)
    root.mainloop()