# 9-11 Start with your work from Exercise 9-8 (page 178). Store the classes
# User, Privileges, and Admin in one module. Create a separate file,
# make an Admin instance, and call show_privileges() to show that
# everything is working correctly.


from userPrivileges import Admin, Privileges

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
