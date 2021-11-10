from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, mm
from reportlab.lib.utils import ImageReader


class Tiket:

    def __init__(self, compra) -> None: 
        self.productos = compra

    def generar(self):
        lienzo = canvas.Canvas("tiketTest.pdf", pagesize=A4)

        
        lienzo.setFillColor("black")
        lienzo.setFont('Courier',30)
        lienzo.drawString(20*mm, 270 *mm, "Lista de productos")
        lienzo.setFont('Courier',18)
        
        step = 0
        total = 0
        for item in self.productos:
            linea = "{} ${}x{} subtotal ${}".format(self.productos[item].descripcion, self.productos[item].precio, self.productos[item].cant, self.productos[item].subtotal)
            lienzo.drawString(50*mm, (230-step)*mm, linea)
            step -= 10
            total += self.productos[item].subtotal

        #total
        footer = ImageReader("footer.png")
        lienzo.drawImage(footer,0,0,height=100)
        lienzo.setFillColor("white")
        lienzo.setFont('Courier',50)
        lienzo.drawString(30,35,"TOTAL : {}".format(total))

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
