class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin

    def change_password(self, password):
        self.password = password
        """Driver Code for Task 1"""


"""user1 = User("Bob", "1234", "password")
print(user1.name, user1.pin, user1.password)"""

"""Driver Code for Task 2"""

"""task2 = User("Bob", "1234", "password")
print(task2.name, task2.pin, task2.password)
task2.change_name("karen")
task2.change_pin("3456")
task2.change_password("pass")
print(task2.name, task2.pin, task2.password)
"""


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        # self.change_name("ALICE")

        print(self.name, "has an account balance of:", self.balance)

    def withdraw(self, withdraw_amt):
        # print(self.name, "has withdrawn:", withdraw_amt)
        self.balance -= withdraw_amt

    def deposit(self, deposit_amt):
        # print(self.name, "has deposited:", deposit_amt)
        if deposit_amt >= 0:
            self.balance += deposit_amt
        else:
            print("Please enter the correct amount")

    def transfer_money(self, transfer_amt, user):

        print("\nYou are transferring $", transfer_amt, " to ", user.name)
        print("Authentication required")

        pin_number = input("Enter your Pin:")

        if pin_number != str(self.pin):
            return False

        print("Transfer authorized")
        print("Trasferring $", transfer_amt, "to", user.name)

        self.balance -= transfer_amt
        # print(name, "has an account balance of: ", self.balance)

        user.balance += transfer_amt

    def request_money(self, request_amt, user):
        print("you are requesting$", request_amt, "from ", user.name)
        print("user authentication is required...")
        pin_number = input("Enter Bob's PIN:")
        password = input("Enter your password:")
        if pin_number == str(user.pin) and password == str(user.password):
            print("request authorized")
            print(user.name, "sent $" + str(request_amt))

            user.balance -= request_amt

            self.balance += request_amt

        # else:
           # print("Invalid Pin. Transaction cancelled")
            # print(name, "has an accouunt balance of: ", self.balance)

        # request_money = input("Request amount:")
        # print(pin_number)
        # print(pin)
    # def request_money(self):
     #  if self.pin and self.password:
        #     return True

    """ Driver Code for Task 3"""


user1 = BankUser("Bob", "6789", "pass")
user2 = BankUser("Alice", "7025", "pass")


user2.deposit(5000)
user2.show_balance()
user1.show_balance()


user2.transfer_money(500, user1)


user1.deposit(0)

user2.show_balance()

user1.show_balance()


user2.request_money(250, user1)


user2.show_balance()
user1.show_balance()
