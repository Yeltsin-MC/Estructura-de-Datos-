
def sumaCursiva(a,b):
    if b==0:
        return a
    else:
        return sumaCursiva(a,b-1)+1
print(sumaCursiva(5,6))