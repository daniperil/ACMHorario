import math
#%%
## Representación binaria de punto flotante 64 bits IE754

numero = float(input("Ingrese el número"))
signo = 1
exponente = 11
mantisa = 52
r = ""
## 1-Signo

if(numero>0):
        r = "0"+ r
else:
        r = "1" + r
binario = ""
## 2-Hallar parte binaria de parte entera
numero = abs(numero)
entero = numero
X = int(entero)
if(X >0):
    while(X > 0):
        if(X % 2 == 0):
            binario = "0" + binario
        else:
            binario = "1" + binario
        X = int(math.floor(X/2))
else:
    if(X ==0):
        binario = "0"
    else:
        binario = "No se pudo convertir el número. Ingrese solo numeros positivos"
print(binario)
print(len(binario))
## 3-Hallar parte binaria al decimal 
entera = int(numero)
decimal = numero - entera
print(decimal)
print(decimal*2)
respuesta = ""
while(decimal != 0):
        if(decimal*2>1):
            decimal = decimal*2-int(decimal*2)
            respuesta = "1" + respuesta
        else:
            decimal = decimal*2
            respuesta = "0" + respuesta

print(respuesta)
print("c")
##4 - Encontrar el numero del exponente 2

longitud = len(binario) - 1
print(len(binario))
longitud = 127 + longitud
if(longitud >0):
    while(longitud > 0):
        if(longitud % 2 == 0):
            r = r + "0" 
        else:
            r = r + "1"
        longitud = int(math.floor(longitud/2))
else:
    if(longitud ==0):
        r = "0"
    else:
        r = "No se pudo convertir el número. Ingrese solo numeros positivos"

print("d")
print(r)
##5- Poner la mantissa

binario = binario.replace('1', '',1)
final = binario + respuesta
xfinal = r+final
if(len(xfinal)<64):
    while(len(xfinal)<64):
        xfinal = xfinal + "0"
print("e")
print(xfinal)
