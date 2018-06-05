# 9-12. Multiple Modules: Store the User class in one module, and store the
# Privileges and Admin classes in a separate module. In a separate file, create
# an Admin instance and call show_privileges() to show that everything is still
# working correctly.


from user_module import User
from privileges_modules import Privileges
from admin_module import Admin

adminKen = Admin('kenneth', 'chang', 'antdoggy', 'k_chang@gmail.com',
                 'taipei')
adminKen.describe_user()

ken_privileges = [
    'can scrape the entire database',
    'can delete accounts based on his mood',
    'can sell user data',
    ]
adminKen.privileges.privileges = ken_privileges

print("\nThe Admin " + adminKen.username + " has the following privileges: ")
adminKen.privileges.show_privileges()
