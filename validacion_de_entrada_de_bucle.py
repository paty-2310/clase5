print("validacion de entrada de bucle")

while True : 

    numero = 6

    print("\nADIVINE UN NUMERO DEL 1 AL 10\n") 
    ingrese = int(input("ingrese el numero: ")) 
    if ingrese == 6 :
        print("numero correcto") 
        break
    elif ingrese >= 1 and ingrese <= 4 : 
        print("intentalo de nuevo")
    elif ingrese > 5 and ingrese < 10 : 
        print("estas muy cerca pero debes volver a intentarlo") 
    else : 
        print("debes elegir un numero en el rango de 1 al 10") 
  
