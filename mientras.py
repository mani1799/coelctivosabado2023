controladora=100
print("***empanadas el ***")
print("*******************")
print("1.agregar sabor de empanada")
print("2.mostrar sabor de empanada")
print("3.editar y cambiar sabor de empanada")
print("0.salir")

while(controladora!=0):
    empanada=None
    controladora=int(input("digita una opcion: "))
    if controladora==1:
        empanada=input ("cual es el sabor")
    elif controladora==2:
        print(f"El sabor es {empanada}")
    elif controladora==3:
        empanada=input("cual es el sabor: ")
    elif controladora==0:
        print("vuelve pronto")
        
    else:
        print("opcion invalida")