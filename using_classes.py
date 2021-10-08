"""class Player:
    max_hp = 4000

    def start(self):
        print("hello", self)


player1 = Player()
print(player1.max_hp)

player2 = Player()
print(Player.max_hp)

Player.max_hp = 5000
player3 = Player()
print(Player.max_hp)
player3.start()
"""


class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.score = 0


player1 = Player("Aaron", 1200)
player2 = Player("Irene", 1300)
print("p1 :", player1.name, "-- Hp:", player1.hp, "Score:", player1.score)
print("p2:", player2.name, "-- Hp:", player2.hp, "Score:", player2.score)

player1.hp += 500
player1.score += 10
print("p1 :", player1.name, "-- Hp:", player1.hp, "Score:", player1.score)
print("p2:", player2.name, "-- Hp:", player2.hp, "Score:", player2.score)
