from os import TMP_MAX
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, mm
from reportlab.lib.utils import ImageReader

RGB = 255
COLOR_ROSA = 1, 223/255, 213/255
COLOR_MARRON = 105/RGB, 68/RGB, 46/RGB

class Tiket():

    def __init__(self, compra) -> None: 
        self.productos = compra

    def generar(self):
        lienzo = canvas.Canvas("tiketTest.pdf", pagesize=A4)
        logo = ImageReader("templatetiket.png")
        lienzo.drawImage(logo,0,0,600,900)
        ALTO = 260

        pdfmetrics.registerFont(TTFont('JosefinSansB',"JosefinSans-Bold.ttf"))
        pdfmetrics.registerFont(TTFont('JosefinSansL',"JosefinSans-light.ttf"))
        

        #HEADER
        ##EMPRESA
        
        lienzo.setFont("JosefinSansB",48)
        lienzo.setFillColorRGB(*COLOR_MARRON) #marronopaco
        lienzo.drawString(75*mm,ALTO*mm,"El Carlo´")
        

        ##RUBRO
        ALTO -= 10
        lienzo.setFont("JosefinSansB",15)
        lienzo.drawString(95*mm,ALTO*mm,"Almacen")

        ##DIRECCION
        ALTO -= 7
        lienzo.setFont("JosefinSansL",10)
        lienzo.drawString(85*mm,ALTO*mm,"Punta Lara 565, Villa Celina")

        #Cliente
        ALTO -= 20
        lienzo.setFont("JosefinSansB",14)
        lienzo.drawString(40*mm,ALTO*mm,"MATIAS REA")
        lienzo.drawString(150*mm,ALTO*mm,"FACTURA")
        ALTO -= 4
        lienzo.setFont("JosefinSansB",10)
        lienzo.drawString(147*mm,ALTO*mm,"Número 760 312 11")
        
        #header GRID
        ALTO -= 30
        lienzo.setStrokeColorRGB(*COLOR_MARRON)
        lienzo.setFillColorRGB(*COLOR_MARRON) #marronopaco
        lienzo.roundRect(20*mm, ALTO*mm, width=500 ,height=30, radius=0 , stroke=1, fill=1)

        #content grid
        lienzo.setFont("JosefinSansB",10)
        lienzo.setFillColorRGB(*COLOR_ROSA) #rosa
        lienzo.drawString(30*mm,(ALTO+4)*mm,"DESCRIPCION DEL PRODUCTO")
        lienzo.drawString(100*mm,(ALTO+4)*mm,"CANT")
        lienzo.drawString(135*mm,(ALTO+4)*mm,"PRECIO")
        lienzo.drawString(170*mm,(ALTO+4)*mm,"SUBTOTAL")

        #value grid
        lienzo.setFillColorRGB(*COLOR_MARRON) #marronopaco
        ALTO -= 8
        total = 0
        for item in self.productos:
            lienzo.drawString(30*mm,ALTO*mm,self.productos[item].descripcion)
            lienzo.drawString(103*mm,ALTO*mm,str(self.productos[item].cant))
            lienzo.drawString(138*mm,ALTO*mm,str(self.productos[item].precio))
            lienzo.drawString(173*mm,ALTO*mm,str(self.productos[item].subtotal))
        
            ALTO -= 4
            total += self.productos[item].subtotal
        
        #total
        ALTO -= 4
        lienzo.roundRect(20*mm, ALTO*mm, width=500 ,height=3, radius=0 , stroke=1, fill=1)
        
        ALTO -= 10
        lienzo.roundRect(126*mm, ALTO*mm, width=200 ,height=30, radius=0 , stroke=1, fill=1)
        
        ALTO -= 2

        lienzo.setFont("JosefinSansB",10)
        lienzo.setFillColorRGB(*COLOR_ROSA) #rosa
        lienzo.drawString(130*mm,(ALTO+6)*mm,"Total")
        lienzo.drawString(140*mm,(ALTO+6)*mm, str(total))
        
        #Informacion de pago
        ALTO -= 20
        lienzo.setFont("JosefinSansB",13)
        lienzo.setFillColorRGB(*COLOR_MARRON) #marronopaco
        lienzo.drawString(50*mm,ALTO*mm,"INFORMACION DE PAGO")
        lienzo.drawString(125*mm,ALTO*mm,"INFO. BANCARIA")
        ALTO -= 8
        lienzo.setFont("JosefinSansL",13)
        lienzo.drawString(51*mm,ALTO*mm,"Carlos Rolon")
        lienzo.drawString(126*mm,ALTO*mm,"Carlos Rolon")
        ALTO -= 6
        lienzo.drawString(51*mm,ALTO*mm,"(011) 15-1234-5678")
        lienzo.drawString(126*mm,ALTO*mm,"Cuenta: 1234 2341 1234 1410")
        ALTO -= 6
        lienzo.drawString(51*mm,ALTO*mm,"elCarlo@gmail.com")
        lienzo.save()
    

    