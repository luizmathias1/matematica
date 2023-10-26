def W(n):
    if n == 1:
        return 2
    
    elif n == 2:
        return 5

    else:
        return W(n - 1) * W (n - 2)

print(W(4))