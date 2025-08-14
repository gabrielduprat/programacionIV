nombre="gabriel"
edad=20
peso=70
altura=1.80
print("Hola "+nombre+" tu edad es "+str(edad)+" y tu peso es "+str(peso)+" y tu altura es "+str(altura))

#sumar dos numeros
a=10
b=20
c=a+b
print(c)

#multiplicar dos numeros
a=10
b=20
c=a*b
print(c)

#restar dos numeros
a=10
b=20
c=a-b
print(c)

#dividir dos numeros
a=10
b=20
c=a/b
print(c)

#restar dos numeros
a=10
b=20
c=a%b
print(c)

#comparar dos numeros
a=10
b=20
if a>b:
    print("a es mayor que b")
else:
    print("b es mayor que a")
    
if a<b:
    print("a es menor que b")
else:
    print("b es menor que a")
    
if a==b:
    print("a es igual a b")
else:
    print("a es distinto a b")
    
if a>=b:
    print("a es mayor o igual a b")
else:
    print("b es mayor o igual a a")
    
if a<=b:
    print("a es menor o igual a b")
else:
    print("b es menor o igual a a")
    
if a!=b:
    print("a es distinto a b")
else:
    print("a es igual a b")

#Tabla de multiplicacion ingresando un numero
print("Tabla de multiplicacion")
numero=int(input("Ingrese un numero: "))
for i in range(1,11):
    print(numero,"x",i,"=",numero*i)