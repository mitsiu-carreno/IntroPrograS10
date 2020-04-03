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
resultadodiv= división(8,2)
print (resultadodiv)




#VerifSuma






def main():
    operation = None;
    num1 = None;
    num2 = None;

    Print(Operation:);
    Print(1 +)
    Print(2 -)
    Print(3 *)
    Print(4 /)
    operation = int(raw_input("Option:"))

    num1 = float(raw_input("First number"))
    num2 = float(raw_input("Second number"))


    if operation == 1 :
        suma(num1, num2);
    elif operation == 2 :
        resta(num1, num2);
    elif operation == 3 :
        multip(num1, num2);
    elif operation == 4 :
        division(num1, num2);
    else
        print("bye")

if __name__ == '__main__':
    main();
