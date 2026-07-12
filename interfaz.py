# interfaz.py
"""
Módulo encargado de la interacción con el usuario (I/O).
Muestra menús, recibe inputs y maneja errores de entrada.
"""
import logica

def mostrar_menu():
    print("\n===== SISTEMA DE TAREAS =====")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")

def ui_agregar_tarea():
    descripcion = input("Escribe la descripción de la tarea: ").strip()
    if not descripcion:
        print("⚠ Error: La descripción no puede estar vacía.")
        return
    
    logica.agregar_tarea(descripcion)
    print(f"✔ Tarea '{descripcion}' agregada correctamente.")

def ui_ver_tareas():
    tareas = logica.obtener_tareas()
    if not tareas:
        print("ℹ No hay tareas registradas.")
        return False # Retornamos False para saber si hay tareas disponibles

    print("\n--- Lista de tareas ---")
    for i, tarea in enumerate(tareas):
        estado = "✔ Completada" if tarea["completada"] else "✘ Pendiente"
        print(f"{i + 1}. {tarea['descripcion']} - {estado}")
    return True

def ui_completar_tarea():
    # Si no hay tareas, no tiene sentido pedir un número
    if not ui_ver_tareas():
        return
    
    try:
        numero = int(input("\nIngresa el número de la tarea a completar: "))
        exito, tarea = logica.completar_tarea(numero - 1)
        
        if exito:
            print(f"✔ Tarea '{tarea['descripcion']}' marcada como completada.")
        else:
            print("⚠ Error: El número de tarea no existe.")
            
    except ValueError:
        print("⚠ Error: Entrada inválida. Por favor, ingresa un número entero.")

def ui_eliminar_tarea():
    if not ui_ver_tareas():
        return
    
    try:
        numero = int(input("\nIngresa el número de la tarea a eliminar: "))
        exito, tarea = logica.eliminar_tarea(numero - 1)
        
        if exito:
            print(f"✔ Tarea '{tarea['descripcion']}' eliminada.")
        else:
            print("⚠ Error: El número de tarea no existe.")
            
    except ValueError:
        print("⚠ Error: Entrada inválida. Por favor, ingresa un número entero.")