
import random
#Prueba de compartir repositorio
def desordena(lista,largo_list,contador):
    if contador< largo_list:
        numero_random= random.randint(contador, largo_list-1)
        lista[contador],lista[numero_random]=lista[numero_random], lista[contador]
        desordena(lista, largo_list,contador+1)

datos=[1,2,3,4,5,6,7,8,9]
desordena(datos,len(datos),0)
print(datos)
