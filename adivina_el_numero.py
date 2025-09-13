print("\n\n-----------ADIVINA EL NUMERO---------\n\n") 

while True : 

    numero = 8 

    print("\nADIVINE UN NUMERO DEL 1 AL 10\n") 
    ingrese = int(input("ingrese el numero: ")) 
    if ingrese == 8 : 
        print("\nusted ha elegido el numero correcto\n") 
    elif ingrese >= 1 or ingrese <= 5 : 
        print("estas muy abajo del numero")
    elif ingrese > 6 or ingrese < 10 : 
        print("estas muy cerca del numero") 
    else : 
        print("debes elegir un numero en el rango drl 1 al 10")
    
    


    
