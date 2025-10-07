from django.db import models
from django.utils import timezone

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.TextField(unique=True)
    contrasena = models.TextField(max_length=15)
    fecha_registro = models.DateTimeField(default=timezone.now)
    
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion_estimada = models.FloatField()
    fecha_inicio = models.DateTimeField(default=timezone.now)
    fecha_fin = models.DateTimeField()
    #Relaciones
    colaboradores = models.ManyToManyField(Usuario)
    creador = models.ForeignKey(Usuario, related_name='creador', on_delete=models.CASCADE, null=True)
      
class Tarea(models.Model):
    OPCIONES = [
        {"PENDIENTE","Pendiente"},
        {"PROGRESO","Progreso"},
        {"COMPLETADA","Completada"},
    ]
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    prioridad = models.IntegerField()
    estado = models.CharField(
        max_length=20,
        choices=OPCIONES,
        default="Pendiente",
    )
    completada = models.BooleanField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    hora_vencimiento = models.DateTimeField()
    #Relacion
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    usuarios_asignados = models.ManyToManyField(
        Usuario, 
        through="Asignacion_tarea",
        related_name='usuarios_asignados')
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=True)
    
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100,unique=True)
    tarea=models.ManyToManyField(Tarea)
        
  
class Asignacion_tarea(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE, null=True)
    tarea = models.ForeignKey(Tarea,on_delete=models.CASCADE, null=True)
    observaciones = models.TextField()
    fecha_asignacion = models.DateTimeField(default=timezone.now)

class Comentario(models.Model):
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(Usuario,on_delete=models.CASCADE, null=True)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, null=True)
    