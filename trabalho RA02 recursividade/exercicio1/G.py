def T(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3 
    else:
        return( T(n-1) + 2 * T(n-2) + 3 * T(n-3))
print(T(4))