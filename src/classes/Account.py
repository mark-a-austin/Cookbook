from src.classes.File import *
class Account:

    def __init__(self, account_id, email, firstname, lastname, username, password):
        self.account_id = account_id
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.__password = password
        self.created_recipes = []  # Branches of all their recipes

    def get_account_id(self):
        return self.account_id

    def get_email(self):
        return self.email

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_created_recipes(self):
        return self.created_recipes

    def setAccountID(self, aID):
        self.account_id = aID

    def setEmail(self, email):
        self.email = email

    def setFirstName(self, fstName):
        self.firstname = fstName

    def setLastName(self, lstName):
        self.lastname = lstName

    def getUsername(self, username):
        self.username = username

    def getPassword(self, password):
        self.__password = password

    def login(self, username):
        details = self.getCredentials(username)
        updateList = [self.account_id, self.email,self.firstname, self.lastname, self.username, self.__password]
        for i in range(0,(len(updateList)-1)):
            updateList[i] = details[i]


    def getCredentials(self,username):
        accounts = fileReader('Database/accounts.csv')
        for i in accounts:
            if i[4] == username:
                print("he")
                return i
        return []





