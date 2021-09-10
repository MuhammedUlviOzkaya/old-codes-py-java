"""var1 = "Ulvi"
var2 = "Muhammed"

st1 = "{1} {0}".format(var1, var2)
st2 = "{} {}".format(var2, var1)

print(st1, st2, sep="\n")

st3 = "{ad} {soyad}".format(ad = var1, soyad = var2)

print(st3)"""

var1 = "Buz"
var2 = "Sprays"

""" RIGHT """
sta1 = "V{:<15}V".format(var1)
print(sta1)

""" LEFT """
sta2 = "|{:>15}|".format(var1)
print(sta2)

""" CENTER """
sta3 = "|{:^15}|".format(var1)
print(sta3)

