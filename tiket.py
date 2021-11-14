from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

from PuntoVentasWhatsAPP.cliente import Carrito

RGB = 255
COLOR_ROSA = 1, 223/255, 213/255
COLOR_MARRON = 105/RGB, 68/RGB, 46/RGB
JOSEFINSANSB = "JosefinSansB"
JOSEFINSANSL = "JosefinSansL"


class Ticket:

    def __init__(self, carrito, empresa, numero, cliente):
        self.carrito = carrito
        self.empresa = empresa
        self.numero = numero
        self.cliente = cliente
        self.identificador = f"{self.numero}/:{self.cliente}"




    def _info_inicial(self, hoja, ancho):
        """Diseño de informacion en la primera pagina:
        datos generales de la empresa: nombre, rubro, direccion; 
        numero de factura y cliente;
        encabezado informativo de la compra, producto, precio, cant, subtotal"""
        mitad_ancho = ancho/2
        posicion_y = 260
        pos_cliente_x = 40
        pos_factura_x = 150
        pos_encabezado_x = [30, 100, 135, 170]
        titulo_factura = "FACTURA"
        palabras_encabezado = ["DESCRIPCION DEL PRODUCTO", "CANT", "PRECIO", "SUBTOTAL"]


        # Datos de la empresa
        hoja.setFont(JOSEFINSANSB, 48)
        hoja.setFillColorRGB(*COLOR_MARRON) #marronopaco
        hoja.drawCentredString(mitad_ancho*mm, posicion_y*mm, self.empresa.nombre)

        posicion_y -= 10
        hoja.setFont(JOSEFINSANSB, 15)
        hoja.drawCentredString(mitad_ancho*mm, posicion_y*mm, self.empresa.rubro)

        posicion_y -= 7
        hoja.setFont(JOSEFINSANSL, 10)
        hoja.drawCentredString(mitad_ancho*mm, posicion_y*mm, self.empresa.direccion)

        #Datos del cliente y numero de factura
        posicion_y -= 20
        hoja.setFont(JOSEFINSANSB, 14)
        hoja.drawCentredString(pos_cliente_x*mm, posicion_y*mm, self.cliente)
        hoja.drawCentredString(pos_factura_x*mm, posicion_y*mm, titulo_factura)
        posicion_y -= 4
        hoja.setFont(JOSEFINSANSB, 10)
        hoja.drawCentredString(pos_factura_x*mm, posicion_y*mm, self.numero)

        posicion_y -= 30
        hoja.setFillColorRGB(*COLOR_MARRON) #marronopaco
        hoja.Rect((pos_encabezado_x[0]-10)*mm, posicion_y*mm, width=500, height=30, fill=1)

        #Encabezado informativo de compra
        hoja.setFont(JOSEFINSANSB, 10)
        hoja.setFillColorRGB(*COLOR_ROSA) #rosa
        hoja.drawCentredString(pos_encabezado_x[0]*mm, (posicion_y+4)*mm, palabras_encabezado[0])
        hoja.drawCentredString(pos_encabezado_x[1]*mm, (posicion_y+4)*mm, palabras_encabezado[1])
        hoja.drawCentredString(pos_encabezado_x[2]*mm, (posicion_y+4)*mm, palabras_encabezado[2])
        hoja.drawCentredString(pos_encabezado_x[3]*mm, (posicion_y+4)*mm, palabras_encabezado[3])

        return posicion_y




    def _info_final(self, hoja, alto):
        """Diseño de señalizador de fin información de compra y total a pagar;
        Información de contacto de la empresa"""
        posicion_y = alto
        inicio_linea_x = 20
        inicio_cuad_x = 126
        pos_total = 135
        pos_contacto = 50
        pos_infopago = 125
        pos_montotal= 170
        titulo_total = "Total"
        titulo_contacto = ["CONTACTO", "INFORMACIÓN DE PAGO"]

        #Finalizador información de compra
        hoja.Rect(inicio_linea_x*mm, posicion_y*mm, width=500 ,height=3, fill=1)
        
        posicion_y -= 10
        hoja.Rect(inicio_cuad_x*mm, posicion_y*mm, width=200 ,height=30, fill=1)

        posicion_y -= 2

        #Total a pagar
        hoja.setFont(JOSEFINSANSB, 10)
        hoja.setFillColorRGB(*COLOR_ROSA) #rosa
        hoja.drawCentredString(pos_total*mm, (posicion_y+6)*mm, titulo_total)
        hoja.drawCentredString((pos_montotal)*mm, (posicion_y+6)*mm, self.carrito.monto)
        
        #Informacion de pago y contacto
        posicion_y -= 20
        hoja.setFont(JOSEFINSANSB, 13)
        hoja.setFillColorRGB(*COLOR_MARRON) #marronopaco
        hoja.drawCentredString(pos_contacto*mm, posicion_y*mm, titulo_contacto[0])
        hoja.drawCentredString(pos_infopago*mm, posicion_y*mm, titulo_contacto[1])

        posicion_y -= 8
        hoja.setFont(JOSEFINSANSL, 13)
        hoja.drawCentredString(pos_contacto*mm, posicion_y*mm, self.empresa.dueño)
        hoja.drawCentredString(pos_infopago*mm, posicion_y*mm, self.empresa.dueño)
        
        posicion_y -= 6
        hoja.draCentredwString(pos_contacto*mm, posicion_y*mm, self.empresa.numero)
        hoja.drawCentredString(pos_infopago*mm, posicion_y*mm, self.empresa.CBU)
        
        posicion_y -= 6
        hoja.drawCentredString(pos_contacto*mm, posicion_y*mm, self.empresa.email)
        hoja.save()




    def _info_compra(self, hoja, alto):
        """Presentación de la información de la compra, una fila por producto 
        y comienzo de hoja nueva y se acaba la actual"""
        posicion_y = alto
        pos_descripcion = 35
        pos_cantidad = 115
        pos_precio = 140
        pos_subtotal = 175
        posicion_y_nueva = 266
        espacio_min_hoja = 70
        salto_renglon = 6

        #Datos de la compra
        for item in self.carrito:
            hoja.drawCentredString(pos_descripcion*mm, posicion_y*mm, self.carrito[item].descripcion)
            hoja.drawCentredString(pos_cantidad*mm, posicion_y*mm, str(self.carrito[item].cant))
            hoja.drawCentredString(pos_precio*mm, posicion_y*mm, str(self.carrito[item].precio))
            hoja.drawCentredString(pos_subtotal*mm, posicion_y*mm, str(self.carrito[item].subtotal))

            # Condición para comenzar una nueva hoja
            if posicion_y < espacio_min_hoja:
                hoja.showPage()
                posicion_y = posicion_y_nueva
                
            posicion_y -= salto_renglon
         
        return posicion_y




    def generar(self):
        """Genera un ticket con el formato definido"""
        hoja = canvas.Canvas(f"{self.identificador}.pdf", pagesize= A4)
        ancho, alto = A4

        pdfmetrics.registerFont(TTFont('JosefinSansB',"JosefinSans-Bold.ttf"))
        pdfmetrics.registerFont(TTFont('JosefinSansL',"JosefinSans-light.ttf"))

        alto = self._info_inicial(hoja, ancho)
        alto = self._info_compra(hoja, alto)
        self._info_final(hoja, alto)