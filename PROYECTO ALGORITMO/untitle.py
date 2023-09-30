import os
import json
from datetime import datetime

# Nombres de archivos para guardar las tareas
tareas_pendientes_file = "tareas_pendientes.json"
tareas_completadas_file = "tareas_completadas.json"

def cargar_tareas_desde_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def guardar_tareas_en_archivo(nombre_archivo, tareas):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(tareas, archivo, indent=4)

def agregar_tarea():
    titulo = input("Ingrese el título de la tarea: ")
    descripcion = input("Ingrese la descripción de la tarea: ")
    fecha_vencimiento = input("Ingrese la fecha de vencimiento (opcional, formato: YYYY-MM-DD): ")

    tarea = {
        "titulo": titulo,
        "descripcion": descripcion,
        "completada": False,
        "fecha_vencimiento": fecha_vencimiento if fecha_vencimiento else None
    }

    tareas_pendientes.append(tarea)
    guardar_tareas_en_archivo(tareas_pendientes_file, tareas_pendientes)
    print("Tarea agregada con éxito!")

def listar_tareas(tareas):
    for idx, tarea in enumerate(tareas, start=1):
        print(f"Tarea {idx}:")
        print(f"Título: {tarea['titulo']}")
        print(f"Descripción: {tarea['descripcion']}")
        if tarea['fecha_vencimiento']:
            print(f"Fecha de vencimiento: {tarea['fecha_vencimiento']}")
        if tarea['completada']:
            print("Estado: Completada")
        else:
            print("Estado: Pendiente")
        print("-" * 20)

def marcar_completada():
    listar_tareas(tareas_pendientes)
    try:
        tarea_idx = int(input("Ingrese el número de la tarea que desea marcar como completada: ")) - 1
        if 0 <= tarea_idx < len(tareas_pendientes):
            tareas_pendientes[tarea_idx]['completada'] = True
            tarea_completada = tareas_pendientes.pop(tarea_idx)
            tareas_completadas.append(tarea_completada)
            guardar_tareas_en_archivo(tareas_pendientes_file, tareas_pendientes)
            guardar_tareas_en_archivo(tareas_completadas_file, tareas_completadas)
            print("Tarea marcada como completada.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Entrada inválida. Debe ingresar un número.")

def main():
    global tareas_pendientes, tareas_completadas
    tareas_pendientes = cargar_tareas_desde_archivo(tareas_pendientes_file)
    tareas_completadas = cargar_tareas_desde_archivo(tareas_completadas_file)

    while True:
        print("\nMenu:")
        print("1. Agregar tarea")
        print("2. Listar tareas pendientes")
        print("3. Marcar tarea como completada")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            print("\nTareas Pendientes:")
            listar_tareas(tareas_pendientes)
        elif opcion == "3":
            marcar_completada()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()

