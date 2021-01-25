# encoding: utf-8
import datetime
from ClassPerson import Persona as P
from ClassArticle import Articulo as A
from ClassLoan import Prestamo as L

p = P()
a = A()
l = L()
menu = True

def Prestamos(miembro,articulo,cantidad):
    datosValidados = l.ValidarDatosPrestamo(miembro,articulo,cantidad)
    if datosValidados:
        fecha = str(datetime.datetime.now())
        prestamo = l.RegistroPrestamo(miembro, articulo, cantidad, fecha)
        print("Se registrado exitosamente con el Id: "+str(prestamo.folio)+"\n")
    else: print(datosValidados)

def Devoluciones(folio):
    devolucion = l.RegistroDevolucion(folio)
    if devolucion:
      print('Devolucion Exitosa')
    else: print('Fevolucion Fallida, por favor verifique el folio que ingresó')

def RegistrarMiembro():
    persona = p.RegistroPersona(nombre, correo, cel)
    print("Miembro Registrado Exitosamente")
    print("Bienvenido " + persona.name)
    print("Su ID es: "+str(persona.Id))

def RegistrarArticulo():
    a.RegistroArticulo(articulo, inventario)

def VerInventario():
    print("ID - ARTICULO - INVENTARIO")
    listaA= a.VerArticulos()
    for articulo in listaA:
        print(str(articulo.Id)+" - "+articulo.articulo+" - "+str(articulo.inventario))
    
def VerMiembros():
    print("ID - NOMBRE - CORREO - CELULAR - CTD. PRESTAMOS DISPONIBLES")
    ListaP = p.VerPersonas()
    for miembro in ListaP:
        print(str(miembro.Id)+" - "+miembro.name+" - "+miembro.email+" - "+miembro.cel+" - "+str(miembro.prestamos))

def VerPrestamos():
    print("FOLIO - MIEMBRO - ARTICULO - CANTIDAD - FO.PRESTAMO - DEVUELTO - FO.DEVOL")
    ListaL = l.VerPrestamos()
    for pres in ListaL:
        print(str(pres.folio)+" - "+str(pres.miembro)+" - "+str(pres.articulo)+" - "+str(pres.cantidad)+" - "+pres.fPrestamo+" - "+str(pres.devuelto)+" - "+pres.fDevolucion)
 

while menu == True:
    print("1) Prestamo Nuevo")
    print("2) Devolución")
    print("3) Nuevo Miembro")
    print("4) Nuevo Articulo")
    print("5) Ver Inventario")
    print("0) Salir")

    accion = input("Seleccione una opción:\n"); print()
    if accion in ("1","2","3","4","5","6","7","0"):
        accion = int(accion)
        if accion == 1:
            print("REGISTRAR PRESTAMO")
            miembro  = int(input("Id del miembro: "))
            articulo = int(input("Articulo: "))
            cantidad = int(input("Cantidad: "))
            Prestamos(miembro,articulo,cantidad)
            print("")
        
        elif accion == 2:
            print("========== DEVOLUCIONES ==========")
            folio = int(input("Numero f. del Prestamo: "))
            Devoluciones(folio)
            print("")

        elif accion == 3:
            print("========== REGISTRA MIEMBRO ==========")
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            cel    = input("Celular: ")
            RegistrarMiembro()
            print("")  

        elif accion == 4:
            print("========== REGISTRA ARTICULO ==========")
            articulo   = input("Articulo: ")
            inventario = int(input("Cantidad: "))
            RegistrarArticulo()
            print("")

        elif accion == 5:
            print("========== INVENTARIO ==========")
            VerInventario()
            print("")

        elif accion == 6:
            print("========== VER MIEMBRO ==========")
            VerMiembros()
            print("")

        elif accion == 7:
            print("========== VER PRESTAMOS ==========")
            VerPrestamos()
            print("")

        else:
            print("Ahí nos vidrios xd\n")
            menu = False
                
    else: print("La opcion que selecciono no existe\n")
else: print("Fin")