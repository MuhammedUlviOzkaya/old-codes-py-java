armors = {"iron" : 10, "steel" : 20}

chars = {"Sova" : {"weapon" : "bow",
                   "power" : 30,
                   "hp" : 100,
                   "armor" : armors["iron"]},
         "Viper" : {"weapon" : "gun",
                    "power" : 30,
                    "hp" : 100,
                    "armor" : armors["steel"]}
}

def hit(offensive, attacked):
    power = offensive["power"]
    hp = attacked["hp"]
    armor = attacked["armor"]
    damage = power - armor
    hp -= damage
    attacked["hp"] = hp
    print("Damage Taken: {}".format(damage),"New Hp: {}".format(hp),sep="\n")

hit(chars["Sova"], chars["Viper"])
print("="*30)
hit(chars["Viper"], chars["Sova"])