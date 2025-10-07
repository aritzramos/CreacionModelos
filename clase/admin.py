from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Usuario),
admin.site.register(Tarea),
admin.site.register(Proyecto),
admin.site.register(Etiqueta),
admin.site.register(Asignacion_tarea),
admin.site.register(Comentario)