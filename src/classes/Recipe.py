from src.classes.File import *


class Recipe:

    # list of ID, name, type, description, ingredients, healthy, price,

    def __init__(self, recipe_id, recipe_name, ingredients, method, meal_type, region, cost, cookTime,
                 serving, chefID):
        self.recipe_id = recipe_id
        self.recipe_name = recipe_name
        self.ingredients = ingredients
        self.method = method
        self.meal_type = meal_type
        self.region = region
        self.cost = cost
        self.cookTime = cookTime
        self.serving = serving
        self.chef_id = chefID

    def get_recipe_id(self):
        return self.recipe_id

    def get_recipe_name(self):
        return self.recipe_name

    def get_ingredients(self):
        return self.ingredients

    def get_method(self):
        return self.method

    def get_chef_name(self):
        return self.chef_name

    def get_meal_type(self):
        return self.meal_type

    def get_region(self):
        return self.region

    def get_cost(self):
        return self.cost

    def set_recipe_id(self, recipe_id):
        self.recipe_id = recipe_id

    def set_recipe_name(self, recipe_name):
        self.recipe_name = recipe_name

    def set_ingredients(self, ingredients):
        self.ingredients = ingredients

    def set_method(self, method):
        self.method = method

    def set_chef_name(self, chef_name):
        self.chef_name = chef_name

    def set_meal_type(self, meal_type):
        self.meal_type = meal_type

    def set_region(self, region):
        self.region = region

    def set_cost(self, cost):
        self.cost = cost

    def add_recipe(self):
        fileWriter('Database/recipes.csv',
                   [self.recipe_id, self.recipe_name, self.ingredients, self.method, self.meal_type,
                    self.region, self.cost, self.cookTime, self.serving, self.chef_id])


    def edit_recipe(self):
        pass

    def delete_recipe(self):
        pass
