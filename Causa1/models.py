from django.db import models
from django.contrib.auth.models import User


        
   



class Usuario(models.Model):
    id = models.AutoField(primary_key=True)  # Campo de clave primaria autoincremental
    username = models.CharField(max_length=225)  # Nombre de usuario
    nombreusuario = models.CharField(max_length=255)  # Nombre del usuario
    apellidousuario = models.CharField(max_length=255)  # Apellido del usuario
    password = models.CharField(max_length=255)  # Contraseña del usuario

    class Meta:
        managed = False  # No permitir que Django gestione esta tabla
        db_table = 'usuarios'  # Nombre exacto de la tabla en la base de datos

    def __str__(self):
        return self.username  # Representación en cadena del objeto
    
    


class Demanda(models.Model):
    numjui = models.CharField(max_length=255)
    nombTribunal = models.CharField(max_length=255)
    demandante = models.CharField(max_length=255)
    demandado = models.CharField(max_length=255)
    repre = models.CharField(max_length=255)
    mandante = models.CharField(max_length=255)
    domicilio = models.CharField(max_length=255)
    comuna = models.CharField(max_length=255)
    encargo = models.CharField(max_length=255)
    soli = models.CharField(max_length=255)
    arancel = models.IntegerField()
    arancel_nombre = models.CharField(max_length=255, null=True, blank=True)  # Nuevo campo
    actu = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'demanda'

        unique_together = ('numjui', 'nombTribunal')

    def __str__(self):
        return f"{self.numjui} - {self.nombTribunal} - {self.demandante} vs {self.demandado}"
class AUD_notificacion(models.Model):
    fechaNotificacion = models.DateTimeField()
    numjui = models.CharField(max_length=255)
    nombTribunal = models.CharField(max_length=255)
    demandante = models.CharField(max_length=255)
    demandado = models.CharField(max_length=255)
    repre = models.CharField(max_length=255)
    mandante = models.CharField(max_length=255)
    domicilio = models.CharField(max_length=255)
    comuna = models.CharField(max_length=255)
    encargo = models.CharField(max_length=255)
    soli = models.CharField(max_length=255)
    arancel = models.IntegerField()
    arancel_nombre = models.CharField(max_length=255, null=True, blank=True)  # Nuevo campo
    estadoNoti = models.IntegerField()
    estadoCausa = models.IntegerField()
    actu = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'aud_notificacion'

    
    def __str__(self):
        return f'{self.numjui} - {self.demandante} vs {self.demandado}'
    
class Historial(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario
    accion = models.CharField(max_length=255)                    # Acción realizada
    fecha_hora = models.DateTimeField(auto_now_add=True)         # Fecha y hora de la acción, se establece automáticamente

    def __str__(self):
        return f"{self.usuario.username} - {self.accion} - {self.fecha_hora}"

    class Meta:
        db_table = 'Historial'  # Nombre de la tabla en la base de datos
        managed = False
        



class Notificacion(models.Model):
    fechaNotificacion = models.DateTimeField()
    numjui = models.CharField(max_length=255)
    nombTribunal = models.CharField(max_length=255)
    demandante = models.CharField(max_length=255)
    demandado = models.CharField(max_length=255)
    repre = models.CharField(max_length=255)
    mandante = models.CharField(max_length=255)
    domicilio = models.CharField(max_length=255)
    comuna = models.CharField(max_length=255)
    encargo = models.CharField(max_length=255)
    soli = models.CharField(max_length=255)
    arancel = models.IntegerField()
    arancel_nombre = models.CharField(max_length=255, null=True, blank=True)  # Nuevo campo
    estadoNoti = models.IntegerField()
    estadoCausa = models.IntegerField()
    actu = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'notificacion'