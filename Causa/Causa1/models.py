from django.db import models

# Create your models here.



class Notificacion(models.Model):
    fechaNotificacion = models.DateTimeField()  # Correspondiente a `fechaNotificacion DATETIME`
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
    arancel = models.IntegerField()  # Correspondiente a `arancel INT`
    estadoNoti = models.IntegerField()  # Correspondiente a `estadoNoti INT`
    estadoCausa = models.IntegerField()  # Correspondiente a `estadoCausa INT`
    actu = models.CharField(max_length=255)

    class Meta:
        managed = False  # Esto indica que Django no gestionará la creación de la tabla
        db_table = 'notificacion'  # Asegura que se apunte a la tabla correcta en la base de datos



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
    
    
class Estampado(models.Model):
    fechaNotificacion = models.DateField()
    numjui = models.CharField(max_length=50)
    nomb_tribunal = models.CharField(max_length=100)
    demandante = models.CharField(max_length=100)
    demandado = models.CharField(max_length=100)
    repre = models.CharField(max_length=100)
    mandante = models.CharField(max_length=100)
    domicilio = models.CharField(max_length=200)
    comuna = models.CharField(max_length=100)
    encargo = models.CharField(max_length=100)
    soli = models.TextField()
    arancel = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.numjui} - {self.demandante} CON {self.demandado}"