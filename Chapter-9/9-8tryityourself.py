# PEP8 Verified

# Privileges: Write a separate Privileges class. The class should have one attribute,
# privileges, that stores a list of strings as described in Exercise 9-7. Move the
# show_privileges() method to this class. Make a Privileges instance as an attribute
# in the Admin class. Create a new instance of Admin and use your method to show its
# privileges.


from ninefivetryityourself import User

class Admin(User):
    # A username with Admin privileges
    def __init__(self, first_name, last_name, username, email, location_city):
    # Initializing the admin
        super(Admin, self).__init__(first_name, last_name, username,
                                    email, location_city)
        self.privileges = Privileges()

class Privileges():
    """A class to store the Admin's privileges"""
    def __init__(self, privileges=[]):
        self.privileges =  privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("  - " + privilege)
        else:
            print("\tThis user has no privilege(s) on the server at this time.")

kenderson = Admin('kenneth', 'chang', 'kendersonCP', 'kennethpchang@gmail.com',
                  'taipei')
kenderson.describe_user()
kenderson.privileges.show_privileges()

print("\nAdding privileges...")

kenderson_privileges = [
    'cleared to reset passwords',
    'cleared to moderate discussions',
    'cleared to ban accounts',
    ]

kenderson.privileges.privileges = kenderson_privileges
kenderson.privileges.show_privileges()
