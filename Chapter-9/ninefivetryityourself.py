class User(object):
    def __init__(self, first_name, last_name, username, email, location_city):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location_city = location_city.title()
        self.login_attempts = 0

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("  First Name: " + self.first_name)
        print("  Last Name: " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location_city)

    def greet_user(self):
        message = "\nWelcome " + self.first_name + " " + self.last_name
        print(message)

    def increment_login_attempts(self):
        # increment login attempts to 1
        self.login_attempts += 1

    def reset_login_attempts(self):
        # reset login_attempts to 0
        self.login_attempts = 0
