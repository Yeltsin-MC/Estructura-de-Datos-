
import time
def fibonaci_recurcivo(n):
    if n ==0 or n==1:
        return 1
    else:
        return fibonaci_recurcivo(n-1)+fibonaci_recurcivo(n-2)
tiempo1= time.perf_counter()
fibonaci_recurcivo(6)
tiempo2= time.perf_counter()
print("fibonaci recursivo tardó: ",tiempo2-tiempo1)

def fibonaci(n):
    a=0
    b=1
    for k in range(n+1):
        c=b+a
        a=b
        b=c

    return a
tiempo1= time.perf_counter()
fibonaci(6)
tiempo2= time.perf_counter()
print("fibonaci sin recursividad tardó: ", tiempo2-tiempo1)
