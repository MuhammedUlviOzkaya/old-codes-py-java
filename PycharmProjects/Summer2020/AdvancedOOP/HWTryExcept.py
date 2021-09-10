"""list = ["345","sadas","324a","14","kemal"]

for i in list:
    try:
        i = int(i)
        print(i)
    except:
        pass
    """


def isEven(num):
    if num % 2 == 0:
        return num
    else:
        raise ValueError

num_list = [34,2,1,3,33,100,61,1800]

for x in num_list:
    try:
        print(isEven(x))
    except ValueError:
        pass