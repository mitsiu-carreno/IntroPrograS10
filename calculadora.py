#Suma




#Resta



#Multiplicacion



#Division





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
