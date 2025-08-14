def tabla_multiplicar(numero:int):
    for i in range(1,11):
        print(numero,"x",i,"=",numero*i)

import random
def tabla_multiplicar_aleatorio(numero:int):
    num= random.randint(1,10)
    for i in range(1,num):
        print(numero,"x",i,"=",numero*i)
        

        
