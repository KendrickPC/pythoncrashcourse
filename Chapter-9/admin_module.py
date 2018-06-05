class Admin(User):
    # A username with Admin privileges
    def __init__(self, first_name, last_name, username, email, location_city):
        # Initializing the admin
        super(Admin, self).__init__(first_name, last_name, username,
                                    email, location_city)
        self.privileges = Privileges()
