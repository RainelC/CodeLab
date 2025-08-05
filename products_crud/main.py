# CRUD de productos, guardar en un txt y que persistencia.
# Productos:
# Nombre   
# Descripción
# Precio
# Si el usuario pasa más de un minuto con 20 segundos y no ha agregado nada a la canasta se cierra el programa con un mensaje que diga 
# "Has excedido el tiempo inactividad"
# Tres puntos extras si tiene ASCII y dos extras más si tiene colores
# Tiempo es: 3 horas

from manage_product import *
import database.data  as db

print(db.getData())

# add_product("Laptop", "Buena", 1500.00)
delete_product("id")
