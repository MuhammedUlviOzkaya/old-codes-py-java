import sys

#print(dir(sys))

"""sys.stderr.write("This is an error message.\n")

sys.stderr.flush()

sys.stdout.write("This is a normal message.\n")


print(sys.argv)"""



"""for i in sys.argv:
    print(i)"""

"""print(sys.argv)"""

def find_root(a, b, c):
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print("There is no real root.")

    else:
        x1 = -b - delta ** 0.5
        x2 = -b + delta ** 0.5
        return (x1, x2)

if len(sys.argv == 4):
    print("Finding Root", find_root(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
else:
    sys.stderr.write("Please Enter Valid Values")
    sys.stderr.flush()

