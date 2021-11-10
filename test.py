from cliente import Producto, Carrito, BotVentas
from tiket import Tiket

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

def test_bot():
    bot = BotVentas()
    bot.inicializar()

