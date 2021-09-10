def paralellogram(total):
    if total % 2 != 0:
        print("Paralellogram width must be an even number.")
    else:
            for i in range(int(total)):
                if i <= total / 2 - 1:
                    print(" " * (int((total / 2 - 1) - i)), "/", " " * 2 * i, "\\", sep="")
                else:
                    print(" " * int(i - (total / 2)), "\\", " " * int((total - 2 * i) + total - 2), "/", sep="")

paralellogram(1500)
