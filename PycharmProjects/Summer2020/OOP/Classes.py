class Soldier():
    health = 100
    name = "Buz Sprays"
    weapon = "Gun"


print(Soldier.health)

Soldier.weight = 90           #you can add something this way

print(Soldier.weight)


class Order():
    company = ''
    quantity = 0
    date = ''

chocolate = Order()
chocolate.company = "Buz"

book = Order()
book.company = "Doz Graffiti Shop"
book.quantity = 1000


print("Chocolate company is", chocolate.company, "\nBook company is", book.company, "and the amount of book is {}".format(book.quantity))





