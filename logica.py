# logica.py
"""
Módulo con la lógica de negocio.
Se comunica con los datos, pero no interactúa con el usuario.
"""
import datos

def obtener_tareas():
    """Devuelve la lista actual de tareas."""
    return datos.tareas

def agregar_tarea(descripcion):
    """Crea un diccionario de tarea y lo añade a la lista."""
    tarea = {"descripcion": descripcion, "completada": False}
    datos.tareas.append(tarea)
    return tarea

def completar_tarea(indice):
    """Marca una tarea como completada si el índice es válido."""
    tareas = obtener_tareas()
    if 0 <= indice < len(tareas):
        tareas[indice]["completada"] = True
        return True, tareas[indice]
    return False, None

def eliminar_tarea(indice):
    """Elimina una tarea si el índice es válido."""
    tareas = obtener_tareas()
    if 0 <= indice < len(tareas):
        tarea_eliminada = tareas.pop(indice)
        return True, tarea_eliminada
    return False, None