import funciones as ff
from os import system as ss

op = 0

empleados = []
ff.generar_sueldos(empleados)

while op !=4:
    ss("cls")
    ff.menu()
    op = ff.validar_op()
    if op==1:
        ss("cls")
        ff.clasificar_empleados(empleados)
        ss("pause")
    elif op==2:
        ss("cls")
        ff.imprimir_estadisticas(empleados)
        ss("pause")
    elif op==3:
        ss("cls")
        ff.report_sueldos(empleados)
        ss("pause")

ss("cls")
print("Finalizando programa")
print("Creado por Maycol Cid, rut 20.951.737-k")