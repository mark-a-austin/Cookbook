class Account:

    def __init__(self, account_id, email, firstname, lastname, username, password):
        self.account_id = account_id
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.created_recipes = list();  # Branches of all their recipes

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





