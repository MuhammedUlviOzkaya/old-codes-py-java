import random
class Enemy():
    def __init__(self):
        self.isAlive = True
        self.health = random.randint(30, 70)
        self.shield = random.randint(0, 10)
        self.power = random.randint(20, 50)

    def hit(self, player):
        damage = self.power - player.shield
        player.health -= damage
        print("Damage Taken: {}".format(damage))
        if player.health <= 0:
            player.isAlive = False


class Player():
    def __init__(self):
        self.isAlive = True
        self.health = 250
        self.shield = 20
        self.power = 55

    def hit(self, enemy):
        damage = self.power - enemy.shield
        enemy.health -= damage
        print("Damage Given: {}".format(damage))
        if enemy.health <= 0:
            enemy.isAlive = False
            enemies.remove(enemy)


enemies = list()
for i in range(10):
    enemies.append(Enemy())

Buz = Player()

while True:
    print(">>>>| Buz Conditions    ----->>>>>     Health: {}".format(Buz.health))
    if Buz.isAlive == False:
        print("Game Over :(")
        quit()
    if not enemies:
        print("Congratulations! You have destroyed them all!!")
        quit()
    for i in enemies:
        print("{}. Enemy   ---->>>>    Health: {} ----- Power: {} ----- Shield: {}".format((enemies.index(i)+1), i.health, i.power, i.shield))

    selection = int(input("Select an enemy 1 - 10: "))
    enemy = enemies[selection-1]
    Buz.hit(enemy)
    enemy.hit(Buz)
