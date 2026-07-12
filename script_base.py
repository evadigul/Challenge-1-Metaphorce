"""
Sistema de Gestión de Tareas (To-Do List) - CONSOLA
----------------------------------------------------
Este script funciona correctamente, PERO mezcla a propósito:
- Los datos (la lista de tareas)
- La lógica de negocio (agregar, completar, eliminar)
- La interfaz con el usuario (print, input, menús)

Tu trabajo en el Skill Challenge 1 es reorganizar este código en módulos
separados (datos.py, logica.py, interfaz.py, main.py), sin cambiar
el comportamiento que ve el usuario final.

NOTA: este script tampoco maneja errores (por ejemplo, si el usuario
escribe texto en vez de un número, el programa se cae). Parte de tu
reto también es corregir eso.
"""

tareas = []


def mostrar_menu():
    print("\n===== SISTEMA DE TAREAS =====")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")


def agregar_tarea():
    descripcion = input("Escribe la descripción de la tarea: ")
    tarea = {"descripcion": descripcion, "completada": False}
    tareas.append(tarea)
    print(f"Tarea '{descripcion}' agregada correctamente.")


def ver_tareas():
    if len(tareas) == 0:
        print("No hay tareas registradas.")
        return

    print("\n--- Lista de tareas ---")
    for i in range(len(tareas)):
        estado = "✔ Completada" if tareas[i]["completada"] else "✘ Pendiente"
        print(f"{i + 1}. {tareas[i]['descripcion']} - {estado}")


def completar_tarea():
    ver_tareas()
    numero = int(input("\nIngresa el número de la tarea a completar: "))
    indice = numero - 1
    tareas[indice]["completada"] = True
    print(f"Tarea '{tareas[indice]['descripcion']}' marcada como completada.")


def eliminar_tarea():
    ver_tareas()
    numero = int(input("\nIngresa el número de la tarea a eliminar: "))
    indice = numero - 1
    tarea_eliminada = tareas.pop(indice)
    print(f"Tarea '{tarea_eliminada['descripcion']}' eliminada.")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            ver_tareas()
        elif opcion == "3":
            completar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
