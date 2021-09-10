def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(4))


def tri_recursion(k):
  if(k > 0):
     return k + tri_recursion(k - 1)
  else:
     return 0





