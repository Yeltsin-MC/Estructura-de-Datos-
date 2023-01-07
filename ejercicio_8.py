
def potencia(a,b):
    if b==1:
        return a
    else:
        if b%2 ==0:
            mit = potencia(a,int(b/a))
            return mit*mit
        else:
            return a*potencia(a,b-1)
print(potencia(5,9))