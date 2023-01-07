
import time
def factorial_recursivo(n):
    if n==1:
        return 1
    return n*factorial_recursivo(n-1)

tiempo1=time.perf_counter()
N= factorial_recursivo(5)
tiempo2= time.perf_counter()
print(N,"fue calculado en un tiempo de :",tiempo2-tiempo1)

def factorial(n):
    b=1
    for i in range(n,1,-1):
        b=b*i
    return b

tiempo1=time.perf_counter()
numero= factorial(5)
tiempo2=time.perf_counter()
print(numero,"fue calculado en un tiempo de :",tiempo2-tiempo1)
