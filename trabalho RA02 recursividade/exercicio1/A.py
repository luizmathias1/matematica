def S(n):
    if n >= 2:
       return(S(n-1) + 10)
    else:
       return  10


print(f'{S(2)}')