def res():
    while True:

        a = str(input())
        a = a.replace(",",".")
        a = float(a)
        res = a - 1002.92
        res = str(res)
        res = res.replace(".",",")
        print(res)

res()