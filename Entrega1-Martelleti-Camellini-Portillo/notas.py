'''django-admin startproject coder31105
se crea el paquete y manage.py
cd /coder31105
adentro creamos app con  estudiantes profosres cursop

python manage.py startapp AppCoder#esto crea un paquete nuevo con apps.py y app modularizada


con models y distinto paquetes
vamos a models.py

class Curso(models.Model): #esta linea models.Model esta herendando de models, curso es un modelo
    nombre=models.CharField(max_length=50)
    comision=models.IntegerField()
    
crear views model en app.
en el proyecto urls.py poner     path("/", include(".urls")),
con import path, include

https://startbootstrap.com/previews/landing-page
    
    
    
'''