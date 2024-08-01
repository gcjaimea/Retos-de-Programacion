

# Concatenación de cadenas
string1 = "Hola"
string2 = " Python"

string_concatenada = string1 + string2
print(string_concatenada)

#repetir unas cadena
string1 = "Hola"
string2 = string1 * 3
print(string2)

#Longitud de cadena
longitud = len(string1)
print(longitud)
print(string1[2])

frase1 = string1[:4]
print(frase1)
frase2 = string1[::-1]
print("frase2", frase2)

#cadena miniscula
string5 = "Hola Python"
print(string5.lower())

#cadena mayuscula
print(string5.upper())

# primera mayuscula
print(string5.capitalize())

#validacion de cadena
string6 = "12345678"

print (string6.isdigit()) #Pregunta si la cadena 6 son digitos =>True

string7 = "abced"
print(string7.isalpha()) #Pregunta si la cadena 7 es alfabetica => True

string8 = "ced1234"
print(string8.isalnum()) #Pregunta si la cadena 8 es alfanumerica => True

string9 = "      "
print(string9.isspace()) #Pregunta si la cadena 9 son espacios => True


string10 = "Hola Python"
print(string10.replace("Hola", "Te quiero")) #Reemplaza la palabra Hola por Te quierpo

string11 = "busqueda"
print((string11.split("q"))) # division ['bus', 'ueda']




#Dificultad extra
def mostrar_menu():
    print("\nPrograma para analizar palabras")
    print("Palindromos : [P]")
    print("Anagramas : [A]")
    print("Isogramas: [I]")
    print("Salir del programa: [S]")
    opcion = input("Por favor indique su opcion:[P], [A], [I], [S]: ").upper()
    
    if opcion == "S":
        salir_programa()
    return opcion






def main():
       
    while True:
        opcion = mostrar_menu()
        
        string1 = input("Por favor escriba la primera palabra: ").lower()
        string2 = input("Por favor escriba la segunda palabra: ").lower()           
        
        if opcion == "P":
            is_palindromo(string1, string2)
        elif opcion == "A":
            is_anagrama(string1, string2)
        elif opcion =="I":
            is_isograma(string1,string2)
        
        else:
            print("Ha introdicido una opcion no valida")


def salir_programa(): 
    print("Salida del Programa")
    exit()

       
def is_palindromo(string1, string2):
    if string1 == string1[::-1]:
        print(f"{string1}  es palindromo")
    else: print(f"{string1} No es un paindromo")
    
    if string2 == string2[::-1]:
        print(f"{string2} es palindromo")
    else:
        print(f"{string2} No es un palindromo")

    

def is_anagrama(string1,string2):
    if sorted(string1) == sorted(string2):
        print(f"{string1} y {string2} son anagramas")


def is_isograma(string1,string2):
    if isograma(string1):
        print(f"{string1} es un isograma.")
    else:
        print(f"{string1} no es un isograma.")
    
    if isograma(string2):
        print(f"{string2} es un isograma.")
    else:
        print(f"{string2} no es un isograma.")


def isograma(string):
    
    letras = set()

    for char in string:
        if char in letras:
            return False
        letras.add(char)


    return True
    







if __name__ == "__main__":
    main()
