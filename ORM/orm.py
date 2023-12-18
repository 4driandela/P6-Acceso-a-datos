import tkinter as tk
import random
import math
import json

personas = []
numeroPersonas = 1

class Persona:
    def __init__(self):
        colores = ["blue","green","yellow","red","orange","pink","black","purple"]
        self.posx= random.randint(0,512)
        self.posy= random.randint(0,512)
        self.radio = 20
        self.direccion = random.randint(0,360)
        self.color = colores[random.randint(0,7)]
        print(self.color)
        self.entidad = ""
        self.numeroColisiones = 0
    def dibuja(self):
        self.entidad = lienzo.create_oval(
            self.posx-self.radio/2,
            self.posy-self.radio/2,
            self.posx+self.radio/2,
            self.posy+self.radio/2,
            fill=self.color
            )
    def mueve(self):
        self.colisiones()
        lienzo.move(self.entidad,math.cos(self.direccion),math.sin(self.direccion))
        self.posx += math.cos(self.direccion)
        self.posy += math.sin(self.direccion)
    def colisiones(self):
        if self.posx < 0 or self.posx >512 or self.posy < 0 or self.posy >512:
            self.direccion +=180
            self.numeroColisiones +=1
            print(self.numeroColisiones,self.color,self.entidad)
            if len(personas) < 10 and self.numeroColisiones>=20:
                self.numeroColisiones = 0
                persona = Persona()
                personas.append(persona)
                persona.dibuja()
            
def guardarPersonas():
    print("Guardado")
    cadena= json.dumps([vars(persona) for persona in personas])
    print(cadena)
    archivo = open("jugadores.json","w")
    archivo.write(cadena)
    archivo.close()
    
raiz = tk.Tk()
raiz.geometry("1024x512")
lienzo = tk.Canvas(raiz,width=512,height=512)
lienzo.pack()

try:
    carga = open("jugadores.json","r")
    cargado = carga.read()
    cargadolista = json.loads(cargado)

    for elemento in cargadolista:
        persona = Persona()
        persona.__dict__.update(elemento)
        personas.append(persona)
except FileNotFoundError:
    print ("No dispones de un archivo de guardado")
    
guardar =tk.Button(raiz,text="Guardar",command=guardarPersonas)
guardar.place(x=10,y=10)

modificarVelocidad = tk.Spinbox(raiz,from_=0,to=60,value=20)
modificarVelocidad.place(x=10,y=60)

if len(personas) == 0:
    numeropersonas = len(personas)
    for i in range(0,numeroPersonas):
        personas.append(Persona())
for persona in personas:
    persona.dibuja()
    
def bucle():
    for persona in personas:
        persona.mueve()
    raiz.after(modificarVelocidad.get(),bucle)
    
bucle()

raiz.mainloop()
