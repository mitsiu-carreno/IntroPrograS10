# coding=utf-8  # Esta linea la agregue para que no marcara error entre tabulados y espacios
import sys;     # Esta linea es para usar la función input() y raw_input()

#Suma




#Resta
def resta_sofia (num1, num2):
    resta = num1 - num2
    if (resta <1000):
        return resta 
    else: "pon otros números"
        
numero1 = int(input("Ingresa número uno menor a 1000"))
numero2 = int(input("Ingresa otro número menor a 1000"))

resultado = resta_sofia (numero1, numero2)

print("El resultado es", resultado)



#Multiplicacion
def multiplica(a,b):
    return a*b


#Division

def division(num1, num2):
	return num1/num2;
resultadodiv= division(8,2)
print (resultadodiv)




#VerifSuma





# Englobe toda la lógica del menú en una función llamada main, es una convención que lo primero que se ejecuta en un programa es la función main()
def main():
    operation = None;   # Variable para guardar el número de operación (1 = Suma, 2 = Resta, 3 = Multip, 4 = División)
    operationText = ''; # Variable para guardar el caracter que representa la operación elegida (+, -, *, /)
    num1 = None;        # Variable para guardar el primer número de nuestra operación
    num2 = None;        # Variable para guardar el segundo número de nuestra operación 
    result = None;      # Variable para guardar el resutlado de nuestra operación

    print("\n\n") # El caracter \n es la representación de salto de linea (tecla enter) en este caso hago dos saltos de linea
    #Imprimimos el menu con las opciones de operación
    print("Choose an operation:"); 
    print("1) +")
    print("2) -")
    print("3) *")
    print("4) /")
    # La función raw_input() imprime el string dentro de los parentesis y espera a que el usuario escriba algo y dé enter
    # Lo que sea que haya escrito el usuario, en nuestro caso queremos que sean números, por ello el resultado de raw_input()
    # lo convertimos en un int -> integer
    # La mejor práctica sería colocar esta operacion en un try/except por si nuestra conversión a int, falle
    # (supongamos que ingresa una letra o simbolo en lugar de  un número), no falle todo el programa
    operation = int(raw_input("Option: "))

    #Realizamos la misma lógica que para la selección de operación, pero ahora convertimos a float (permite puntos decimales)
    num1 = float(raw_input("First number "))
    num2 = float(raw_input("Second number "))

    # Si la operación elegida fue 1 = Suma, se invoca la función *suma (que aun no existe)
    if operation == 1 :
        result = suma(num1, num2);
        operationText = '+';
    # Si la operación fue 2 = Resta se invoca la función resta_sofia
    elif operation == 2 :
        result = resta_sofia(num1, num2);
        operationText = '-';
    # Si la operación fue 3 = multip se invoca la función multiplica
    elif operation == 3 :
        result = multiplica(num1, num2);
        operationText = '*'
    # Si la operación fue 4 = división se invoca la función division
    elif operation == 4 :
        result = division(num1, num2);
        operationText = '/'
    # Si la operación no fue 1,2,3 ni 4, no es una opción valida 
    else:
        print("Not a valid operation, sorry")

    # Finalmente imprimimos el resultado de la operación 
    print num1, operationText, num2, " = ", result

# Cuando corremos nuestro programa, python por default genera algunas variables, una de ellas se llama __name__ y si su valor es __main__
# Significa que el usuario esta ejecutando directamente este programa desde su terminal con python calculadora.py 
# (por lo tanto no es otro programa el que esta invocando nuestro archivo)
if __name__ == '__main__':
    # Si la condición se cumple invocamos la función main definida más arriba (línea 46 aprox)
    main();
