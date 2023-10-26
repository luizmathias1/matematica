def T(x):
    if x == 2:
        return("nao pertence")
    elif x-3 == x // 2 :   
        print(x)
        return("pertence")
    else:
        return(T(x-1))
    
print(T(12))