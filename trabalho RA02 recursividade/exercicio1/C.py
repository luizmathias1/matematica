def B(n):
    if n == 1:
        return 1
    else:
        return B(n-1) + n**2
    
print(f'{B(1)}')