# 9-5. Login Attempts:
# Write a method called increment_ login_attempts() that
# increments the value of login_attempts by 1. Write another method called
# reset_login_attempts() that resets the value of login_ attempts to 0.
# Make an instance of the User class and call
# increment_login_attempts() several times.
# Print the value of login_attempts to make sure it was
# incremented properly, and
# then call reset_login_attempts(). Print login_attempts again
# to make sure it was reset to 0.


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

kendersonChang = User('kenneth', 'chang', 'kendrickpc',
                      'kennethpchang@gmail.com', 'taipei')
kendersonChang.describe_user()
kendersonChang.greet_user()

print("\nMaking 3 login attempts: ")
kendersonChang.increment_login_attempts()
kendersonChang.increment_login_attempts()
kendersonChang.increment_login_attempts()
print("\tLogin attempts: " + str(kendersonChang.login_attempts))

print("\nResetting login attempts: ")
kendersonChang.reset_login_attempts()
print("\tLogin attemps: " + str(kendersonChang.login_attempts))

kendersonPeng = User('kenderson', 'peng', 'kenderson',
                     'kendersonpeng@gmail.com', 'taipei')
kendersonPeng.describe_user()
kendersonPeng.greet_user()

kendrickRamal = User('kendrick', 'ramal', 'brotherkendrick',
                     'kendrickramal@gmail.com', 'taipei')
kendrickRamal.describe_user()
kendrickRamal.greet_user()
