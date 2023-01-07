
def  ordenador_de_lista(lista,largo_lista,contador):
    if contador < largo_lista:
        pequeño= lista[contador]
        posicion =contador
        for i in range(contador+1,largo_lista):
            if lista[i] <pequeño:
                pequeño= lista[i]
                posicion=i



        lista[contador],lista[posicion]=lista[posicion],lista[contador]
        ordenador_de_lista(lista,largo_lista,contador+1)

datos=[4,9,2,7,1,6,3,8,5]
ordenador_de_lista(datos,len(datos),0)
print(datos)
