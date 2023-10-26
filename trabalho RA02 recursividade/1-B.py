
def A(n):
    if n >= 2:
       return A(n - 1)**-1
    else:
       return 2

print(A(1))

