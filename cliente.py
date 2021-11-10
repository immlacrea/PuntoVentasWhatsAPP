import os 

def clear():
    os.system("cls")

class Producto:
    def __init__(self, cod, descripcion, precio):
        self.cod = cod
        self.descripcion = descripcion
        self.precio = precio
        self.subtotal = precio
        self.cant = 1

class Carrito:
    def __init__(self) :
        self.carrito = {}
        self.monto = 0
        self.cant = 0
    
    def agregar(self, producto):
        if producto.cod not in self.carrito:
            self.carrito[producto.cod] = producto
        else:
            self.carrito[producto.cod].cant +=1
            self.carrito[producto.cod].subtotal += self.carrito[producto.cod].precio

        self.cant += 1
        self.monto += self.carrito[producto.cod].precio 

    def mostrarCarrito(self):
        for item in self.carrito:
            print("Producto {}, precio {}, cant {}, subtotal {}".format(self.carrito[item].descripcion, self.carrito[item].precio, self.carrito[item].cant, self.carrito[item].subtotal))

    def mostrarTotal(self):
        print("total ", self.total())

    def total(self):
        return self.monto


class BotVentas:
    def __init__(self) -> None:
        self.productos = {}
        self.estado = True
    
    def cargarProductos(self):
        with open("data.csv","r") as F:
            for linea in F:
                cod, desc, precio = linea.rstrip().split(",")
                precio = float(precio)
                producto = Producto(cod,desc,precio)
                self.productos[cod] = producto
        print("Productos fueron cargados en el Bot correctamente")
    
    def mostrarOpciones(self):
        listaP = [
            "1 - Leche",
            "2 - Fideo",
            "3 - Pan",
            "c - Muestra Carrito",
            "s - Salir"
        ]

        for item in listaP:
            print(item)


    def inicializar(self):
        self.cargarProductos()
        carrito = Carrito()
        while self.estado:
            clear()
            self.mostrarOpciones()
            op = input("opcion: ")
            clear()
            if op == "c":
                carrito.mostrarCarrito()
                carrito.mostrarTotal()
                input("tocar enter..")
                clear()
            elif op in "123":
                carrito.agregar(self.productos[op])
            elif op == "s":
                self.estado = False
        

    


class Cliente:
    def __init__(self, nombre, apellido, listaProductos):
        self.nombre = nombre
        self.apellido = apellido
        self.listaP = listaProductos
    
