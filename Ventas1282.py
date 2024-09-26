print("Ever Pereyra 22308051281282")
print("-------------------------------")
class ventas1282:
    ID_venta1282 = 0
    Cantidad1282 = 0
    precio1282 = 0.0
    vendedor1282 = ""
    Impuestos1282 = 0
    Comprador1282 = 0
    Fecha1282 = ""

    def mostrardatos(self):
        print("Estos son los datos de una venta:")
        print(f"Fué la venta número {datos.Cantidad1282}")
        print(f"El cliente {datos.Comprador1282} compró una cantidad de {datos.Cantidad1282}kg de frutas y verduras,")
        print(f"lo que sumó un total de ${datos.precio1282} más ${datos.Impuestos1282} en impuestos")
        print(f"Fué atendido por {datos.vendedor1282} el día  {datos.Fecha1282}")

    def Listafrutas(self):
        print("Lista de frutas más vendidas:")
        flist=["Mango","Platano","Manzana","pera","piña","sandía","melon"]
        for x in flist:
            print(x)

    def Tuplaverduras(self):
        print("Tupla de verduras más vendidas:")
        vtupla=("Pepino","Zanahoria","calabaza","Rabano","lechuga","Chile jalapeño","Apio")
        for a in vtupla:
            print(a)

    def Diccionarioempleados(self):
        print("Diccionario con los empleados con más ventas:")
        ediccionario={
            "Mauricio": 132,
            "Pablo": 112,
            "Luis": 100,
            "Uriel": 89,
            "Alexis": 80,
            "Marco": 76,
            "Diego": 68
        }
        for d,c in ediccionario.items():
            print(d,c)

    def alta(self):
        print("Alta y baja:")
        print("La venta se ha subido a la Base de Datos")

    def baja(self):
        print("La venta se ha dado de baja correctamente")        

datos = ventas1282()
datos.ID_venta1282=139
datos.Cantidad1282=43
datos.precio1282=334.49
datos.vendedor1282="carlos"
datos.Impuestos1282=27.00
datos.Comprador1282="Joel"
datos.Fecha1282="26 de septiembre del 2024"


datos.mostrardatos()

datos.Listafrutas()

datos.Tuplaverduras()

datos.Diccionarioempleados()

datos.alta()

datos.baja()


