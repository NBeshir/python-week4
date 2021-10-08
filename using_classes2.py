class User:
    def __init__(self, name, email, password):
        self.name = name
        self.name = name
        self.email = email

        self.password = password

    def change_password(self, password):
        self.password = password
        print("your password has been changed to: ", password)


user1 = User("Jane", "jane@nucamp.co", "password")
print(user1.name)
print(user1.password)
user1.change_password("123")
