from bs4 import BeautifulSoup
import requests
import csv

# https://www.bbcgoodfood.com/recipes/
# Find your recipe!

nameOfRecipe = ''
prepTime = ''
cookTime = ''
difficulty = ''
servings = ''

listOfIngredients = []
listOfMethods = []

requestURL = 'https://www.bbcgoodfood.com/recipes/best-ever-fluffy-american-pancakes-cherry-berry-syrup'

subStringURL = 'https://www.bbcgoodfood.com/recipes/'

if (subStringURL in requestURL):
    source = requests.get(requestURL).text
    soup = BeautifulSoup(source, 'lxml')

    # Adds each section to a list on html
    sectionList = []
    sectionList.append(soup.find('section', class_="header header--masthead post__header mb-lg"))
    sectionList.append(soup.find('section', class_="recipe__ingredients col-12 mt-md col-lg-6"))
    sectionList.append(soup.find('section', class_="recipe__method-steps mb-lg col-12 col-lg-6"))

    # ###############SECTION 0 ######################

    # #RECIPE NAME
    recipe = soup.find('h1')
    nameOfRecipe = recipe.text

    uls = sectionList[0].find('ul', class_="header__row header__planning mb-xxs list list--horizontal")

    # List for timing
    listOfLi = []
    for li in uls:
        listOfLi.append(li)

    times = listOfLi[0].find('ul')

    # First time is prep and 2nd is cook
    listOfTimes = []
    for li in times:
        listOfTimes.append(li.find('time').text)

    # LIST OF FIRST SECTION
    prepTime = listOfTimes[0]
    cookTime = listOfTimes[1]

    difficulty = listOfLi[1].text
    servings = listOfLi[2].text

    # ###############SECTION 1 ######################

    ul2 = sectionList[1].find('ul')

    for li in ul2:
        listOfIngredients.append(li.text)

    # ###############SECTION 2 ######################

    ul3 = sectionList[2].find('ul')

    for li in ul3:
        listOfMethods.append(li.p.text)

    # Outputs
    print("LIST")
    print(nameOfRecipe)
    print(prepTime)
    print(cookTime)
    print(difficulty)
    print(servings)

    print("INGREDIENTS")
    for ingredients in listOfIngredients:
        print(ingredients)

    print("METHODS")
    for methods in listOfMethods:
        print(methods)

else:
    print("Not a valid BBC site")
