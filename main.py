# ------ NO BORRAR -----
from funciones import *
from herramientas import *
# ------ NO BORRAR -----

user = {}
menu = []

carrito=[]

print(test()) #-> para verificar si el archivo funciona.




def listar_menu():
    print("Listado del menú")
    for i in menu:
        print(f'\nla lista del menu es:{i}\n')
    
    agregar_carrito=input("Agregar comida al carrito")
    if agregar_carrito in menu:
        carrito.append(agregar_carrito)
        print(carrito)
    
def revisar_carrito():
    if carrito==None:
        print("no hay items en el carrito")
    print(carrito)

def quitar_item_carrito(nombre):
    for index, carrito in menu
    if menu['nombre']==menu:
        del carrito[index]
        print(f'el producto {nombre} fue eliminado del carrito')
    print(f'el producto {nombre} no fue encontrado')


def modificar_item():




if __name__ == '__main__':
    test()

#menu principal
while (True):
    print("Bienvenido al menú")
    print("Para acceder a las funciones debe elegir una opción del 1 al 4")
    opcion=int(input("Que opción quiere elegir"))
    print("opcion 1")
    print("opcion 2")
    print("opcion 3")
    print("opcion 4->salir")
    if opcion==1:
        listar_menu
    if opcion==2:
        revisar_carrito
    if opcion==3:
        quitar_item_carrito
    if opcion==4:
        break
    
    
    ...
    #escribir menu con funciones aqui