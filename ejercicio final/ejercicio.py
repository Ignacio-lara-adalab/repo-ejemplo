print("""
      Bienvenidos a la calculadora de nacho
      Para salir escribe salir
      Las operaciones son: suma, resta, multi, div
      """)


while True:
    numero = input("ingrese numero:")
    if numero.lower()=="salir":
        break
    numero=int(numero)
    op = input("seleccione operacion:")
    if op.lower()=="salir":
        break
    if op == "suma":
        numero2=input("ingrese valor a sumar:")
        if numero2.lower()=="salir":
            break
        numero2=int(numero2)
        numero+=numero2
        print(f"el nuevo numero es {numero}")
    elif op == "resta":
        numero2=input("ingrese valor a restar:")
        if numero2.lower()=="salir":
            break
        numero2=int(numero2)
        numero-=numero2
        print(f"el nuevo numero es {numero}")
    elif op == "multi":
        numero2=input("ingrese valor a multiplicar:")
        if numero2.lower()=="salir":
            break
        numero2=int(numero2)
        numero*=numero2
        print(f"el nuevo numero es {numero}")
    elif op == "div":
        numero2=input("ingrese valor a dividir:")
        if numero2.lower()=="salir":
            break
        numero2=int(numero2)
        numero/=numero2
        print(f"el nuevo numero es {numero}")