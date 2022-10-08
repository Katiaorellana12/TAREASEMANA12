from ast import Delete
from ensurepip import bootstrap
from pydoc import text
from turtle import clear
from Source import email
from dotenv import load_dotenv
from os import environ
from tkinter import Button, Entry, Label  , Tk



load_dotenv()



mensaje_html="""

<!DOCYPE html>
<html>
<body>
<h1>LE SALUDAMOS DESDE PYTHON {}</h1>
<p>{}</p>
</body>
</html>
"""
def enviar():
   variable=destinatario.get()
   variabl2=escribir2.get()
   variable3=escribir3.get()
   Correo = email.Email()
   Correo.mandar_email([variable],"PYHTON", message_format=mensaje_html.format(variabl2,variable3), format="html")




ventana = Tk()
ventana.geometry("500x500")
ventana.title("CORREOS")


label1=Label(ventana, text="Enviar a(CORREO):"  ,bg="pink")
destinatario=Entry(ventana )
nombre=Label(ventana, text="Nombre:"  ,bg="pink")
escribir2=Entry(ventana)
escribir3=Entry(ventana)
mensaje=Label(ventana, text="Escribir mensaje:",bg="pink")
boton1=Button(ventana, text="Enviar",  bg="pink", command=enviar )

label1.place(x=40,y=40)
destinatario.place(x=200, y=40, width=200, height=20)
nombre.place(x=40,y=70)
escribir2.place(x=200, y=70 , width=200, height=20)
mensaje.place(x=40 , y=100)
escribir3.place(x=40, y=140 , width=400, height=100)
boton1.place(x=400, y=240)
ventana.mainloop()