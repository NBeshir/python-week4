"""class User:

    def __init__(self, name, email, password):
        self.name = name
        self.name = name
        self.email = email

        self.password = password

    def change_password(self, password):
        self.password = password
        print("your password has been changed to: ", password)


class bankuser(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.balance = 0

    def check_balance(self):
        print(self.name, "has an account balance of:", self.balance)


bankuser1 = bankuser("mimi", "mimi@nucamp.co", "password")
print(bankuser1.balance)
"""


class Superclass:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hi, I am " + self.name)


class Subclass(Superclass):
    def say_hi(self):
        print("just saying hi! ")
        print("hello", self.name + " !")


x = Superclass("Robert")
y = Subclass("John")
print(x)
print(y)
x.say_hi()
y.say_hi()
