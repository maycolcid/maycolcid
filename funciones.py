from random import randrange
from numpy import sum
import csv

trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel
"Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]


def generar_sueldos(lista):
    for i in range(10):
        nom = 'Empleado '+str(i+1)
        sueldo = randrange(300000,2200000)
        d = {'nombre':nom,'sueldo':sueldo}
        lista.append(d)

def menu():
    m = """BIENVENIDO
**************
[1] Clasificar sueldos.
[2] Ver estadisticas de los sueldos
[3] Exportar reporte de sueldos
[4] Salir
--> """
    print(m,end="")

def validar_op():
    while True:
        try:
            op = int(input())
            if op>=1 and op<=4:
                return op
            else:
                raise ValueError
        except:
            print("Selecciona una opcion valida. --> ",end="")

def clasificar_empleados(lista):
    bajos = []
    medios = []
    altos = []

    for trabajador in lista:
        if trabajador["sueldo"]<=300000:
            bajos.append(trabajador)
        elif trabajador["sueldo"]<=2500000:
            medios.append(trabajador)
        else:
            altos.append(trabajador)

    print("EMPLEADOS CON SUELDO MENOR A $300000:")
    print()

    for e in bajos:
        print(f"{e["nombre"]} : ${e["sueldo"]:,.0f}")
    print("**************")

    print("EMPLEADOS CON SUELDO ENTRE $300000 Y $2.500.000")
    print()

    for e in medios:
        print(f"{e["nombre"]} : ${e["sueldo"]:,.0f}")
    print("**************")

    print("EMPLEADOS CON SUELDO MAYORES A $2.500.000:")
    print()

    for e in altos:
        print(f"{e["nombre"]} : ${e["sueldo"]:,.0f}")

def sueldo_bajo(lista):
    bajo = lista[0]
    for empleado in lista:
        if bajo["sueldo"]>empleado["sueldo"]:
            bajo = empleado
    return bajo

def sueldo_alto(lista):
    alto = lista[0]giy
    for empleado in lista:
        if alto["sueldo"]<empleado["sueldo"]:
            alto = empleado
    return alto

def imprimir_estadisticas(lista):
    print(f"Sueldo más bajo: {sueldo_bajo(lista)}")
    print(f"Sueldo más alto: {sueldo_alto(lista)}")
    listar_sueldos = [sueldo["sueldo"] for sueldo in lista]
    suma = sum(listar_sueldos)
    promedio = suma/10
    print(f"Sueldo promedio: {promedio:,.0f}")

def report_sueldos(lista):
    reporte = []
    for trabajador in lista:
        sueldo_bruto = trabajador["sueldo"]
        afp = int(sueldo_bruto * 0.12)
        salud = int(sueldo_bruto * 0.07)
        sueldo_liquido = sueldo_bruto - afp - salud
        a = {"nombre":trabajador["nombre"],"sueldo_bruto":sueldo_bruto,"afp":afp,"salud":salud,"sueldo_liquido":sueldo_liquido}
        reporte.append(a)
    
    nombre_campos = ["nombre","sueldo_bruto","afp","salud","sueldo_liquido"]
    with open('Reporte Sueldos.csv','w',newline="") as archivo:
        escritor = csv.DictWriter(archivo,fieldnames=nombre_campos)
        escritor.writeheader()
        escritor.writerows(reporte)