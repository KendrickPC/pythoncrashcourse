class Privileges():
    """A class to store the Admin's privileges"""
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("  - " + privilege)
        else:
            print("\tThis user has no privilege(s) on the server at\
                  this time.")
