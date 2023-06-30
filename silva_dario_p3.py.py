import os
import time
import numpy

lista_ruts = []
lista_nombres = []
lista_mascotas = []
lista_columnas = []
lista_filas = []
lista_totales = []
lista_correos = []
lista_ruts = []
lista_cantidad_de_dias = []

print("""MENÚ GUARDERIA MASCOTAS
1. Ingrese su rut (Dueño de la mascota)
2. Nombre del dueño 
3. Identificador Unico
4. Nombre de la mascota
5. Cantidad de dias permaneciendo en la guarderia """)

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese su RUT sin puntos ni dígito verificador: "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("¡ERROR! ¡INGRESE UN RUT VÁLIDO!")
        except:
            print("¡ERROR! ¡DEBE INGRESAR UN NÚMERO ENTERO!")
def validar_nombre():
    while True:
        nombre = input("Ingrese su nombre: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha() and not nombre.isspace():
            return nombre
        else:
            print("El Nombre ingresado es muy corto (minimo debe tener 3 letras) o contiene caracteres no validos!")
def validar_nombre_mascotas():
    while True:
        nombre = input("Ingrese nombre de su mascota: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha() and not nombre.isspace():
            return nombre
        else:
            print("El Nombre ingresado es muy corto (minimo debe tener 3 letras) o contiene caracteres no validos!")            

def validar_efectivo(total:int):
    while True:
        try:
            efectivo = int(input(f"El total es: ${total} \nIngrese efectivo para pagar: "))
            if efectivo < total:
                print("El dinero ingresado es insuficiente, intente nuevamente!")
            else:
                print("Gracias por pagar!")
                return efectivo
        except:
            print("Ingrese un monto valido!")
def validar_fila(min:int,max:int):
    while True:
        try:
            fila = int(input(f"Ingrese número de fila ({min},{max}):"))
            if fila >= min and fila <= max:
                return fila
            else:
                print("ERROR! FILA INCORRECTA")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO POSITIVO!")
def validar_columna(min:int,max:int):
    while True:
        try:
            columna = int(input(f"Ingrese número de columna ({min},{max}):"))
            if columna >= min and columna <= max:
                return columna
            else:
                print("ERROR! COLUMNA INCORRECTA")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO POSITIVO!")
def validar_opcion(min:int,max:int):
        while True:
            try:
                opcion = int(input("Ingrese opción: "))
                if opcion >= min and opcion <= max:
                    return opcion
                else:
                    print("¡ERROR! ¡OPCIÓN INCORRECTA!")
def validar_telefono():
    while True:
        try:
            telefono = int(input("Ingrese su número de teléfono: "))
            if len(str(telefono)) == 9 and '9' == str(telefono)[0]:
                return telefono
            else:
                print("FORMATO DE TELÉFONO INCORRECTO!")
                
        except:
            print("ERROR! Debe ingresar un número de 9 digitos")
def validar_codigo(cod):
    while True:
            codigo = input("Ingrese su codigo: ")
            if codigo == cod:
                return True
            else:
                print("ERROR! El codigo ingresado no existe o ya no es valido!")
                return
def validar_comunaderegion():
    region = validar_region()
    while True:
        comuna = input("Ingrese su comuna: ")
        comunas_por_region = {
            "arica y parinacota": ["arica", "putre"],
            "tarapacá": ["iquique", "pozo almonte"],
            "antofagasta": ["antofagasta", "calama"],
            "atacama": ["copiapó", "vallenar"],
            "coquimbo": ["la serena", "coquimbo"],
            "valparaíso": ["valparaíso", "viña del mar"],
            "metropolitana de santiago": ["santiago", "puente alto"],
            "o'higgins": ["rancagua", "san fernando"],
            "maule": ["talca", "curicó"],
            "ñuble": ["chillán", "bulnes"],
            "biobío": ["concepción", "talcahuano"],
            "la araucanía": ["temuco", "padre las casas"],
            "los ríos": ["valdivia", "la unión"],
            "los lagos": ["puerto montt", "osorno"],
            "aysén": ["coyhaique", "puerto aysén"],
            "magallanes": ["punta arenas", "puerto natales"]
        }
        if comuna.lower() in comunas_por_region.get(region.lower(), []):
            return comuna
        else:
            print("La comuna no existe!")
def validar_direccion(longitud_min):
    while True:
        direccion = input("Ingrese su dirección: ")
        if direccion >= longitud_min:
            return direccion
        else:
            print("La dirección especificada no tiene el minimo de longitud requerida.")
            