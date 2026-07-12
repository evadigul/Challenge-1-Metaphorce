
"""
Punto de entrada de la aplicación.
Coordina el ciclo principal y redirige las opciones a la interfaz.
"""
import interfaz

def main():
    while True:
        interfaz.mostrar_menu()
        opcion = input("\nElige una opción: ").strip()

        if opcion == "1":
            interfaz.ui_agregar_tarea()
        elif opcion == "2":
            interfaz.ui_ver_tareas()
        elif opcion == "3":
            interfaz.ui_completar_tarea()
        elif opcion == "4":
            interfaz.ui_eliminar_tarea()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("⚠ Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()