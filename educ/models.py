from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='nombre')
    baja = models.BooleanField(default='False')

    def __str__(self):
        return self.nombre


class Eje(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='nombreEje', default='eje1')
    descripcion = models.TextField(null=True, verbose_name='descripcion')
    categoria = models.ForeignKey(Categoria, default=1, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nombre} {self.descripcion}"
        
    class Meta():
        verbose_name_plural = 'Eje'
        
        
class Estudiante(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='nombre')
    apellido = models.CharField(max_length=50, verbose_name='apellido')
    email = models.EmailField(max_length=100, verbose_name='email')
    dni = models.IntegerField(verbose_name='dni')
    ejes = models.ManyToManyField(Eje, through='Inscripcion')
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
        
    class Meta():
        verbose_name_plural = 'Estudiante'

        
class Inscripcion(models.Model):
    
    ESTADOS = [
        (1,'Inscripto'),
        (2,'Cursando'),
        (3,'Egresado'),
    ]
    
    fecha = models.DateField(null=True, verbose_name='fecha_de_creacion')
    ejes = models.ForeignKey(Eje, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    estado = models.IntegerField(choices=ESTADOS, default=1)
    
    def __str__(self):
        return f"{self.estudiante.nombre} {self.estudiante.apellido}"

   
