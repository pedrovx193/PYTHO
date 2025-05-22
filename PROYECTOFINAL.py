import math
from datetime import datetime

# ===================== CALCULADORA =====================
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division por cero"

def potencia(a,b):
        return a ** b

def raiz(a):
    return math.sqrt(a)

def mostrar_menu_calculadora():
    print("\n======================================================")
    print("             CALCULADORA CON FUNCIONALIDAD EXTRA              ")
    print("======================================================")
    print("[1]. Suma")
    print("[2]. Resta")
    print("[3]. Multiplicacion")
    print("[4]. Division")
    print("[5]. Potencia")
    print("[6]. Raiz cuadrada")
    print("[7]. Volver al menú principal")
    print("======================================================")

def ejecutar_calculadora():
    while True:
        mostrar_menu_calculadora()
        opcion = input("Elige una opción: ")
        if opcion == "7":
            break

        if opcion in ["1", "2", "3", "4", "5", "6"]:
            try:
                if opcion in ["1", "2", "3", "4", "5"]:
                    num1 = float(input("Ingresa el primer número: "))
                    num2 = float(input("Ingresa el segundo número: "))

                    if opcion == "1":
                        print(f"Resultado: {suma(num1, num2)}")
                    elif opcion == "2":
                        print(f"Resultado: {resta(num1, num2)}")
                    elif opcion == "3":
                        print(f"Resultado: {multiplicacion(num1, num2)}")
                    elif opcion == "4":
                        print(f"Resultado: {division(num1, num2)}")
                    elif opcion == "5":
                        print(f"Resultado: {potencia(num1, num2)}")
                elif opcion == "6":
                    num1 = float(input("Ingresa un número: "))  # Corregí la errata en el mensaje
                    print(f"Resultado: {raiz(num1)}")
            except ValueError:
                print("Error: Ingresa números válidos.")
            except Exception as e:
                print(f"Ocurrió un error: {e}")
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# ===================== GESTION DE CONTACTOS =====================
class Contacto:
    def __init__(self, nombre, telefono, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
def mostrar_menu_contactos():
    print("\n================= GESTION DE CONTACTOS =================")
    print("[1]. Agregar contacto")
    print("[2]. Mostrar contactos")
    print("[3]. Buscar contacto")
    print("[4]. Eliminar contacto")
    print("[5]. Volver al menú principal")
    print("======================================================")

def ejecutar_gestion_contactos():
    contactos = []
    while True:
        mostrar_menu_contactos()
        opcion = input("Elige una opción: ")

        if opcion == "5":
            break

        if opcion == "1":
            print("\n============== AGREGAR CONTACTO =================")
            nombre = input("Ingresa el nombre: ")
            telefono = input("Ingresa el teléfono: ")
            direccion = input("Ingresa la direccion: ")

            contacto = Contacto(nombre, telefono,direccion)
            contactos.append(contacto)
            print("Contacto agregado.")

        elif opcion == "2":
            print("\n============== MOSTRAR CONTACTOS =================")
            if contactos:
                for c in contactos:
                    print(f"Nombre: {c.nombre}, Teléfono: {c.telefono}, Direccion:{c.direccion}")
            else:
                print("No hay contactos guardados.")

        elif opcion == "3":
            print("\n============== BUSCAR CONTACTO =================")
            nombre_buscar = input("Ingresa el nombre a buscar: ")
            encontrado = False
            for c in contactos:
                if c.nombre.lower() == nombre_buscar.lower():
                    print(f"Nombre: {c.nombre}, Teléfono: {c.telefono}, Direccion:{c.direccion}")
                    encontrado = True
                    break
            if not encontrado:
                print("Contacto no encontrado.")

        elif opcion == "4":
            print("\n============== ELIMINAR CONTACTO =================")
            nombre_eliminar = input("Ingresa el nombre a eliminar: ")
            encontrado = False
            for i, c in enumerate(contactos):
                if c.nombre.lower() == nombre_eliminar.lower():
                    del contactos[i]
                    print("Contacto eliminado.")
                    encontrado = True
                    break
            if not encontrado:
                print("Contacto no encontrado.")
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# ===================== SISTEMA DE INVENTARIOS =====================
class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

def mostrar_menu_inventario():
    print("\n===================== SISTEMA DE INVENTARIOS ======================")
    print("                         MENU DE OPCIONES                           ")
    print("[1]. Agregar producto")
    print("[2]. Mostrar producto")
    print("[3]. Buscar producto")
    print("[4]. Actualizar producto")
    print("[5]. Eliminar producto")
    print("[6]. Volver al menú principal")
    print("===================================================================")

def ejecutar_inventario():
    inventario = []
    while True:
        mostrar_menu_inventario()
        opcion = input("Elige una opcion: ")

        if opcion == "6":
            break

        if opcion == "1":
            print("\n===================== INGRESAR PRODUCTO ========================")
            nombre = input("Ingresa el nombre del producto: ")
            try:
                cantidad = int(input("Ingresa la cantidad: "))
                precio = float(input("Ingresa el precio: "))
                producto = Producto(nombre, cantidad, precio)
                inventario.append(producto)
                print("Producto agregado.")
            except ValueError:
                print("Error, entrada no valida.")
        elif opcion == "2":
            print("\n===================== MOSTRAR PRODUCTO ========================")
            if inventario:
                for p in inventario:
                    print(f"Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")
                print("===========================================================")
            else:
                print("No hay productos en el inventario.")
        elif opcion == "3":
            print("\n===================== BUSCAR PRODUCTO ========================")
            nombre_buscar = input("Ingresa el nombre del producto a buscar: ")
            encontrado = False
            for p in inventario:
                if p.nombre.lower() == nombre_buscar.lower():
                    print(f"Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")
                    encontrado = True
                    break
            if not encontrado:
                print("Producto no encontrado.")
                print("=============================================")
        elif opcion == "4":
            print("\n===================== ACTUALIZAR PRODUCTO ========================")
            nombre_actualizar = input("Ingresa el nombre del producto a actualizar: ")
            try:
                nueva_cantidad = int(input("Ingresa la nueva cantidad: "))
                for p in inventario:
                    if p.nombre.lower() == nombre_actualizar.lower():
                        p.cantidad = nueva_cantidad
                        print("Cantidad actualizada.")
                        break
                else:
                    print("Producto no encontrado.")
            except ValueError:
                print("Error, entrada no valida.")
        elif opcion == "5":
            print("\n===================== ELIMINAR PRODUCTO ========================")
            nombre_eliminar = input("Ingresa el nombre del producto a eliminar: ")
            for p in inventario:
                if p.nombre.lower() == nombre_eliminar.lower():
                    inventario.remove(p)
                    print("Producto eliminado.")
                    break
            else:
                print("Producto no encontrado.")
        else:
            print("Opcion no valida, intentalo de nuevo")

# ===================== GESTION DE ACTIVIDADES =====================
class Tarea:
    def __init__(self, nombre, descripcion, estado):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado

def mostrar_menu_tareas():
    print("\n================= SISTEMA DE GESTION DE ACTIVIDADES ==================")
    print("                               MENU DE OPCIONES                           ")
    print("[1]. Agregar actividad")
    print("[2]. Mostrar actividad")
    print("[3]. Buscar actividad")
    print("[4]. Actualizar actividad")
    print("[5]. Eliminar actividad")
    print("[6]. Volver al menú principal")
    print("=======================================================================")

def ejecutar_tareas():
    actividad = []
    while True:
        mostrar_menu_tareas()
        opcion = input("Elige una opcion: ")

        if opcion == "6":
            break

        if opcion == "1":
            print("\n============= INGRESAR TAREA ======================")
            nombre = input("Ingresa el nombre de la tarea: ")
            descripcion = input("Ingresa una descripcion de la tarea: ")
            estado = input("Ingresa el estado de la tarea: ")
            tarea = Tarea(nombre, descripcion, estado)
            actividad.append(tarea)
            print("Tarea agregada.")
            print("===================================")

        elif opcion == "2":
            print("\n==================== MOSTRAR TAREAS ======================================")
            if actividad:
                for tarea in actividad:
                    print(f"Tarea: {tarea.nombre}, Descripción: {tarea.descripcion}, Estado: {tarea.estado}")
                print("===========================================================")
            else:
                print("No hay tareas registradas.")

        elif opcion == "3":
            print("\n==================== BUSCAR TAREA ======================================")
            nombre_buscar = input("Ingresa el nombre de la tarea: ")
            encontrado = False
            for tarea in actividad:
                if tarea.nombre.lower() == nombre_buscar.lower():
                    print(f"Nombre: {tarea.nombre}, Descripción: {tarea.descripcion}, Estado: {tarea.estado}")
                    encontrado = True
                    break
            if not encontrado:
                print("Tarea no encontrada.")
                print("=============================================")

        elif opcion == "4":
            print("\n==================== ACTUALIZAR TAREA ======================================")
            nombre_actualizar = input("Ingresa el nombre de la tarea a actualizar: ")
            nuevo_status = input("Ingresa el nuevo estado: ")
            actualizado = False
            for tarea in actividad:
                if tarea.nombre.lower() == nombre_actualizar.lower():
                    tarea.estado = nuevo_status
                    print("Estado actualizado.")
                    print("=============================================")
                    actualizado = True
                    break
            if not actualizado:
                print("Tarea no encontrada.")

        elif opcion == "5":
            print("\n==================== ELIMINAR TAREA ======================================")
            nombre_eliminar = input("Ingresa el nombre de la tarea a eliminar: ")
            eliminado = False
            for i, tarea in enumerate(actividad):
                if tarea.nombre.lower() == nombre_eliminar.lower():
                    del actividad[i]
                    print("Tarea eliminada.")
                    print("=============================================")
                    eliminado = True
                    break
            if not eliminado:
                print("Tarea no encontrada.")
        else:
            print("Opcion no valida, intentalo de nuevo")

# ===================== GESTION DE NOTAS =====================
tipodearchivo = "notas.txt"

class Notas:
    def __init__(self, titulo, descripcion, categoria, fechadecreacion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.categoria = categoria
        self.fechadecreacion = fechadecreacion

def mostrar_menu_notas():
    print("\n===================== SISTEMA DE GESTION DE NOTAS =====================")
    print("                               MENU DE OPCIONES                           ")
    print("[1]. Agregar Nota")
    print("[2]. Mostrar Notas")
    print("[3]. Buscar Nota")
    print("[4]. Modificar Nota")
    print("[5]. Eliminar Nota")
    print("[6]. Volver al menú principal")
    print("========================================================================")

usuarios = []

def registrar_usuario():
    nombre_usuario = input("Ingresa un nombre de usuario: ")
    contrasena = input("Ingresa una contraseña: ")
    usuarios.append({"usuario": nombre_usuario, "contrasena": contrasena})
    print(f"Usuario {nombre_usuario} ahora esta registrado.")
    print("================================================================")

def iniciar_sesion():
    nombre_usuario = input("Accede al programa escribiendo tu nombre de usuario: ")
    contrasena = input("Escribe tu contraseña: ")
    for usuario in usuarios:
        if usuario["usuario"] == nombre_usuario and usuario["contrasena"] == contrasena:
            print(f"Bienvenido, {nombre_usuario}!")
            return True
    print("login incorrecto.")
    return False

lista = []

def cargar_notas():
    try:
        with open(tipodearchivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
            bloques_lista = contenido.split("\n\n")
            for bloque in bloques_lista:
                if bloque.strip():
                    lineas = bloque.strip().split('\n')
                    titulo = lineas[0].split(': ')[1]
                    categoria = lineas[1].split(': ')[1]
                    fechadecreacion = lineas[2].split(': ')[1]
                    descripcion = '\n'.join(lineas[3:])
                    lista.append(Notas(titulo, descripcion, categoria, fechadecreacion))
    except FileNotFoundError:
        print(f"Archivo {tipodearchivo} no encontrado. Se creará uno nuevo.")
    return lista

def guardar_notas(lista):
    with open(tipodearchivo, 'w', encoding='utf-8') as f:
        for nota in lista:
            f.write(f"Título: {nota.titulo}\n")
            f.write(f"Categoría: {nota.categoria}\n")
            f.write(f"Fecha de Creación: {nota.fechadecreacion}\n")
            f.write(f"{nota.descripcion}\n\n")

lista = cargar_notas()

def ejecutar_notas():
    while True:
        mostrar_menu_notas()
        opcion = input("Elige una opcion: ")

        if opcion == "6":
            guardar_notas(lista)
            break

        elif opcion == "1":
            print("\n============= INGRESAR NOTA ======================")
            titulo = input("Ingresa el titulo de la nota: ")
            descripcion = input("Ingresa una descripcion de la nota: ")
            categoria = input("Ingresa la categoria de la nota: ")
            fechadecreacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            nota = Notas(titulo, descripcion, categoria, fechadecreacion)
            lista.append(nota)
            guardar_notas(lista)
            print("Nota agregada exitosamente.")
            print("===================================")

        elif opcion == "2":
            if not lista:
                print("No hay notas para mostrar.")
                print("===========================")
            else:
                for nota in lista:
                    print("==================== MOSTRAR NOTA ======================================")
                    print(f"Título: {nota.titulo}")
                    print(f"Descripción: {nota.descripcion}")
                    print(f"Categoría: {nota.categoria}")
                    print(f"Fecha de Creación: {nota.fechadecreacion}")
                    print("===========================================================")

        elif opcion == "3":
            print("\n==================== BUSCAR NOTA ======================================")
            palabra_clave = input("Ingrese la palabra clave a buscar: ").lower()
            resultados = []
            for nota in lista:
                if palabra_clave in nota.titulo.lower() or palabra_clave in nota.descripcion.lower():
                    resultados.append(nota)

            if resultados:
                print("\n--- Resultados de la Búsqueda ---")
                for i, nota in enumerate(resultados):
                    print(f"{i + 1}. Título: {nota.titulo}")
                    print(f"   Categoría: {nota.categoria}")
                    print(f"   Descripcion: {nota.descripcion}")
                    print(f"   Fecha de Creación: {nota.fechadecreacion}")
                    print("-------------------------------")
            else:
                print("No se encontraron notas con la palabra clave ingresada.")
                print("=============================================")

        elif opcion == "4":
            print("==================== MODIFICAR NOTA ======================================")
            if not lista:
                print("No hay notas para modificar.")
                print("=============================================")
            else:
                for i, nota in enumerate(lista):  # itera sobre cada elemento de la lista y a su vez obtengo  el indice de cada elemento
                    print(f"Nota {i + 1}: {nota.titulo}")
                try:
                    indice_a_modificar = int(input("Ingrese el número de la nota a modificar: ")) - 1
                    if 0 <= indice_a_modificar < len(lista):
                        nota_a_modificar = lista[indice_a_modificar]
                        nuevo_titulo = input(f"Nuevo título ({nota_a_modificar.titulo}): ") or nota_a_modificar.titulo
                        nueva_descripcion = input(
                            f"Nueva descripción ({nota_a_modificar.descripcion}): ") or nota_a_modificar.descripcion
                        nueva_categoria = input(
                            f"Nueva categoría ({nota_a_modificar.categoria}): ") or nota_a_modificar.categoria

                        nota_a_modificar.titulo = nuevo_titulo
                        nota_a_modificar.descripcion = nueva_descripcion
                        nota_a_modificar.categoria = nueva_categoria
                        guardar_notas(lista)
                        print("Nota modificada exitosamente.")
                        print("=============================================")
                    else:
                        print("Número de nota inválido.")
                        print("=============================================")
                except ValueError:
                    print("Por favor, ingrese un número.")
                    print("=============================================")

        elif opcion == "5":
            print("==================== ELIMINAR NOTA ======================================")
            if not lista:
                print("No hay notas para eliminar.")
                print("=============================================")
            else:
                for i, nota in enumerate(lista):  # itera sobre cada nota de la lista, obtengo su posicion e imprimo el numero de la nota
                    print(f"{i + 1}. Título: {nota.titulo}")
                try:
                    indice_a_eliminar = int(input("Ingrese el número de la nota a eliminar: ")) - 1
                    if 0 <= indice_a_eliminar < len(lista):#elimino la nota de la lista de acuerdo al indice que el usuario elija
                        del lista[indice_a_eliminar]  # Uso del para eliminar por índice
                        guardar_notas(lista)
                        print("Nota eliminada.")
                        print("=============================================")
                    else:
                        print("Número de nota inválido.")
                        print("=============================================")
                except ValueError:
                    print("Por favor, ingrese un número.")
                    print("=============================================")
        else:
            print("Opcion no valida, intentalo de nuevo")

def mostrar_menu_principal():
                print("     ============================================================================================")
                print("     PROYECTO FINAL PHYTON 1. Estudiante:PEDRO ALEXANDER SOLARTE. Docente: Ing.JOSE AGUSTIN CACAIS")
                print("     ============================================================================================")
                print("\n===================== MENU PRINCIPAL =====================")
                print("1. Calculadora con nueva funcionalidad")
                print("2. Gestión de Contactos")
                print("3. Sistema de Inventarios")
                print("4. Gestión de Actividades")
                print("5. Gestión de Notas")
                print("6. Salir")
                print("=========================================================")
def menu_principal():
    while True:
        mostrar_menu_principal()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            ejecutar_calculadora()
        elif opcion == "2":
            ejecutar_gestion_contactos()
        elif opcion == "3":
            ejecutar_inventario()
        elif opcion == "4":
            ejecutar_tareas()
        elif opcion == "5":
            ejecutar_notas()
        elif opcion == "6":
            print("Gracias por usar nuestro sistema")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# ================== ACCEDER CON REGISTRO DE USUARIO Y CONTRASEÑA ==================

if __name__ == "__main__":
    print("========= BIENVENIDO AL SISTEMA DE REGISTRO E INGRESO A LA APLICACION =========")

    if not usuarios:
        print("Por favor registre su nombre de usuario.")
        registrar_usuario()

    while not iniciar_sesion():
        print("Intenta de nuevo.\n")

menu_principal() #Me muestra las opciones del menu
