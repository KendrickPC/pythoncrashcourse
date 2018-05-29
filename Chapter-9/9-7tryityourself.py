# An administrator is a special kind of user. Write a class called Admin that inherits
# from the User class you wrote in Exercise 9-3 (page 166) or Exercise 9-5 (page 171).
# Add an attribute, privileges, that stores a list of strings like "can add post",
# "can delete post", "can ban user", and so on. WRite a method called show_privileges()
# that lists the administrators set of privileges. Create an instance of Admin,
# and call your method.


from ninefivetryityourself import User

class Admin(User):
    # A username with Admin privileges
    def __init__(self, first_name, last_name, username, email, location_city):
    # Initializing the admin
        super(Admin, self).__init__(first_name, last_name, username, email,
                                    location_city)
        self.privileges = []

    def show_priviledges(self):
        # Display the privileges that the admin has
        print("\nPrivileges:")
        for privilege in self.privileges:
            print("- " + privilege)

kenderson = Admin('kendrick', 'chang', 'kendersonPC', 'kennethpchang@gmail.com',
                  'taipei')
kenderson.describe_user()

kenderson.privileges = [
    'can add post',
    'can delete post',
    'can ban user',
    ]

kenderson.show_priviledges()
