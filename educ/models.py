from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='nombre')
    baja = models.BooleanField(default=1)

    def __str__(self):
        return self.nombre


class Eje(models.Model):
    nombreEje = models.CharField(max_length=50, verbose_name='nombreEje', default='eje1')
    descripcion = models.TextField(null=True, verbose_name='descripcion')
    #categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombreEje

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='nombre')
    apellido = models.CharField(max_length=50, verbose_name='apellido')
    email = models.EmailField(max_length=100, verbose_name='email')
    dni = models.IntegerField(verbose_name='dni')
    ejes = models.ManyToManyField(Eje, through='Inscripcion')

        
        
    


class Inscripcion(models.Model):
    
    ESTADOS = [
        (1,'Inscripto'),
        (2,'Cursando'),
        (3,'Egresado'),
    ]
    
    fecha = models.DateField(verbose_name='fecha_de_creacion')
    ejes = models.ForeignKey(Eje, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    estado = models.IntegerField(choices=ESTADOS, default=1)
    
    def __str__(self):
        return self.estado


   
