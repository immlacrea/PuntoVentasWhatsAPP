from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, mm
from reportlab.lib.utils import ImageReader
import os

class Tiket:

    def __init__(self, compra) -> None: 
        self.productos = compra

    def generar(self):
        lienzo = canvas.Canvas("tiketTest.pdf", pagesize=A4)
        logo = ImageReader("templatetiket.png")
        lienzo.drawImage(logo,0,0,600,900)

        pdfmetrics.registerFont(TTFont('JosefinSansB',"JosefinSans-Bold.ttf"))
        lienzo.setFont("JosefinSansB",48)
        lienzo.setFillColorRGB(105/255, 68/255, 46/255) #marronopaco

        #HEADER LOGO
        lienzo.drawString(75*mm,260*mm,"El Carlo´")
        lienzo.setFont("JosefinSansB",15)
        lienzo.drawString(95*mm,250*mm,"Almacen")
        lienzo.setFont("JosefinSansB",10)
        lienzo.drawString(85*mm,243*mm,"Punta Lara 565, Villa Celina")
        
        #header GRID
        lienzo.setStrokeColorRGB(105/255, 68/255, 46/255)
        lienzo.roundRect(20*mm, 210*mm, width=500 ,height=30, radius=0 , stroke=1, fill=1)

        #content grid
        lienzo.setFillColorRGB(1, 223/255, 213/255)
        lienzo.drawString(30*mm,214*mm,"DESCRIPCION DEL PRODUCTO")
        lienzo.drawString(100*mm,214*mm,"CANT")
        lienzo.drawString(135*mm,214*mm,"PRECIO")
        lienzo.drawString(170*mm,214*mm,"SUBTOTAL")

        #value grid
        lienzo.setFillColorRGB(105/255, 68/255, 46/255) #marronopaco

        step = 0
        total = 0
        for item in self.productos:
            lienzo.drawString(30*mm,(205-step)*mm,self.productos[item].descripcion)
            lienzo.drawString(103*mm,(205-step)*mm,str(self.productos[item].cant))
            lienzo.drawString(138*mm,(205-step)*mm,str(self.productos[item].precio))
            lienzo.drawString(173*mm,(205-step)*mm,str(self.productos[item].subtotal))
        
            step += 4
            total += self.productos[item].subtotal

        lienzo.save()
    

    

    def enviar(self, plataforma):
        if plataforma == "whatsapp":
            self._enviar_wp()
        
        elif plataforma == "gmail":
            self._enviar_gmail()
    
    #funcion privada de la clase
    def _enviar_wp(self):
        pass
    
    #idem
    def _enviar_gmail(self):
        pass
