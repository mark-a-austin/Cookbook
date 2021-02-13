from datetime import date


class Branch:

    # used for origin branch
    def __init__(self, branch_id, chef_id):
        self.branch_id = branch_id
        self.chef_id = chef_id
        self.original_date = date.today()
        self.edited_date = date.today()

    def get_branch_id(self):
        return self.branch_id

    def get_chef_id(self):
        return self.chef_id

    def get_original_date(self):
        return self.original_date

    def get_edited_date(self):
        return self.edited_date

    def set_branch_id(self, branch_id):
        self.branch_id = branch_id

    def set_edited_date(self, edited_date):
        self.edited_date = edited_date




