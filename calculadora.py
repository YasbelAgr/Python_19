
opcion = int(input("""Ingrese una opcion:
                   1. SUMAR
                   2. DIVIDIR
                   3. MULTIPLICAR
                   4. RESTAR: """))
numero_01 = int(input("Ingresa un numero: "))
numero_02 = int(input("Ingresa un numero: "))
if opcion == 1:
    print("Resultado: ",(numero_01 + numero_02))
elif opcion == 2:
    if numero_02 == 0:
        print("No se puede dividir por 0.")
    else:
        print("Resultado: ",(numero_01 / numero_02))
elif opcion == 3:
    print("Resultado: ",(numero_01 * numero_02))
elif opcion == 4:
    print("Resultado: ",(numero_01 - numero_02))
else:
    print("Ingrese una opcion valida.")
    