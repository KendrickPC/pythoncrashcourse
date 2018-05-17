# 9-3 Users:
# Make a class called User. Create two attributes called first_name 
# and last_name, and then create several other attributes that are 
# typically stored in a user profile. 
# Make a method called describe_user() that prints a summary of the 
# users information. Make another method called greet_user() that 
# prints a personalized greeting to the user.
# Create several instances representing different users, and call 
# both methods for each user.


class User(object):
    def __init__(self, first_name, last_name, username, email, location_city):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location_city = location_city.title()

    def describe_user(self):
        print("\n" + self.first_name + " " +self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location_city)

    def greet_user(self):
        message = "\nWelcome "+ self.first_name + " " + self.last_name
        print(message)

kendersonChang = User('kenneth', 'chang', 'kendrickpc', 'kennethpchang@gmail.com', 'taipei')
kendersonChang.describe_user()
kendersonChang.greet_user()

robbieDoyen = User('robbie', 'doyen', 'doyenrobbie', 'doyen@codetaiwan.org', 'taipei')
robbieDoyen.describe_user()
robbieDoyen.greet_user()

woodrowChen = User('woody', 'chen', 'woodrow', 'woodrow@codetaiwan.org', 'taipei')
woodrowChen.describe_user()
woodrowChen.greet_user()