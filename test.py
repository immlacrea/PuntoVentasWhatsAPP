from cliente import Producto, Carrito

def test_producto():
    carrito = Carrito()
    with open("data.csv","r") as F:
        for linea in F:
            cod, desc, precio = linea.rstrip().split(",")
            precio = float(precio)
            producto = Producto(cod,desc,precio)
            carrito.agregar(producto)
    
    carrito.mostrarCarrito()
    carrito.mostrarTotal()

