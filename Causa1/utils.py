# Causa1/utils.py
from django.db import connection

def verificar_y_actualizar_esquema():
    """
    Verifica si las columnas necesarias existen en la tabla 'notificacion' y las agrega si faltan.
    """
    columnas_requeridas = {
        "arancel_nombre": "VARCHAR(255) NULL"
    }
    
    with connection.cursor() as cursor:
        # Verifica las columnas existentes
        cursor.execute("SHOW COLUMNS FROM notificacion")
        columnas_actuales = [columna[0] for columna in cursor.fetchall()]

        # Revisa si las columnas requeridas están presentes
        for columna, tipo in columnas_requeridas.items():
            if columna not in columnas_actuales:
                # Agrega la columna si no existe
                cursor.execute(f"ALTER TABLE notificacion ADD COLUMN {columna} {tipo}")


