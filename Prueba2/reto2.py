# Operadores aritmeticos
a = 10
b= 3

c = a + b    # operador de suma
d = a - b    #operador de resta
e = a * b    #operador de multilicacion
f = a / b    # operador de division
g = a // b   #division entera, muestra la parate entera solamente, descarta el residuo
h = a & b    #division residuo, muestra solo el residuo
i = a ** b   # operador portencia

#Operadores de asignacion

j = a       # el valor de a se asigna a 'j'
print (j)

b += a      # el balor de b se le suma el valor de a
print(b)

c -= b      #el valor de c se le resta el valor de b
print(c)

e *= b      # el valor de e se le multiplica por el valor de b
print(e)

f /= b      # el valor de f se le divide por el valor de b
print(f)

g %= b      # el valor de g se le  divide tipo residuo por el valor de b
print(g)

h **= b     # el valor de h se le eleva por el valor de b
print(h)

i //= b     # el valor de i se le divide tipo entero por el valor de b
print(i)

# Operadores de comparacion

a == b      # se uasa para determinar la igualdad
a != b      # variables diferentes
a < b       # variable menor que
a > b       # variable mayor que
a >= b      # variable mayor igual que
a <= b      # variable menor igual  que



# Condicionales
if a == b:
    print('son iguales')

else:
    print('No son iguales')

if a != b:
    print("son diferentes")
else:
    print('son iguales')

if a < b:
    print('a es menor que b')
else:
    print('a es mayor que b')
if a > b:
    print('a es mayor que b')
else:
    print('a es menor que b')
if a >= b:
    print('a es mayor o igual  que b')
else:
    print('a es menor o igual que b')


t =0
while t < 20:
    print(t)
    t+=1




#Operadores Logicos

d = a and b     # operador and
print(d)

e = a or b      # operador or

#a not b     # operador no

a = True
b = False
c = True

d = a and b    
print(d)

e = a or b     
print(e)

f = not a
print(f)


# Iterativas
nume = 0
for i in range(5):
    nume += i
    print(nume)

num = []
for k in range(10):
    num.append(k)
print (num)


#Excepciones:

try:
    a =10/3
except:
    a > 1
finally:
    print("No se puede dividir, a es mayor de 1")

numeros = list(range(10, 56))

lista_numeros =[]

for n in numeros:
    if n % 2 == 0 and n !=16 and n % 3 != 0:
        lista_numeros.append(n)
         
print(lista_numeros)


