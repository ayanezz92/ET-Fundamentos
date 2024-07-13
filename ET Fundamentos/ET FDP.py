import random
import math
import csv
#Lista de Trabajadores 
trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
def asignar_sueldos():
    sueldos = {}
    for trabajador in trabajadores:
        sueldo =random.randint(300000,2500000)
        sueldos[trabajador] = sueldo
        return sueldos
    
def clasificar_sueldos(sueldos):
    sueldos_800 = {}
    sueldos_1500000 = {}
    sueldos_2000000 = {}
    for trabajador, sueldo in sueldos.items():
        if sueldo <= 800000:
            sueldos_800[trabajador] = sueldo
        elif 800000<= sueldo <= 2000000:
            sueldos_1500000[trabajador] = sueldo
        else:
            sueldos_2000000[trabajador] = sueldo

    print("/n Sueldos menores a $800.000: ", sueldos_800)
    print("Sueldos entre $800.000 y $2.000.000: ", sueldos_1500000)
    print("Sueldos superiores a $2.000.000:", sueldos_2000000)
    print("El total de sueldos es:", sum(sueldos.values()))

def mostrar_estadisticas(sueldos):
    lista_sueldos = list(sueldos.values())
    sueldo_maximo = max(lista_sueldos)
    sueldo_minimo = min(lista_sueldos)
    sueldo_promedio = sum(lista_sueldos) / len(lista_sueldos)
    media_geometrica = math.exp(sum(math.log(s)for s in lista_sueldos)/ len(lista_sueldos))

    print("/nEstadisticas de sueldo: ")
    print(f"Sueldo más alto: {sueldo_maximo}")
    print(f"Sueldo más bajo: {sueldo_minimo}")
    print(f"Promedio de sueldos: {sueldo_promedio}")
    print(f"Media geometrica : {media_geometrica}")


def reporte_sueldos(sueldos):
    reporte = []
    for trabajador, sueldo in sueldos.items():
        descuento_salud = sueldo * 0.07
        descuento_afp = sueldo * 0.12
        sueldo_liquido = sueldo - descuento_salud - descuento_afp
        reporte.append([trabajador, sueldo, descuento_salud, descuento_afp, sueldo_liquido])

    print("/nReporte de sueldos:")
    for r in reporte:
        print(f"{r[0]}, Sueldo Base: {r[1]}, Descuento Salud: {r[2]}, Descuento AFP: {r[3]}, Sueldo Líquido: {r[4]} ")
        return reporte
    
def exportar_archivo():
    with open("Reporte de sueldos.csv", "w", newline= "") as file:
        writer = csv.writer(file)
        writer.writerow(["nombre :", "Sueldo Base:", "Descuento Salud:", "Descuento AFP:", "Sueldo líquido:"])
        writer.writerows(reporte_sueldos)


def aplicacion():
        sueldos = {}
        while True:
            print("/n=========================================")
            print(" 1.- Asignar Sueldos")
            print(" 2.- Clasificar Sueldos")
            print(" 3.- Ver estadisticas")
            print(" 4.- Reporte de sueldos")
            print(" 5.- Salir del programa")
            opcion = ("Selecciona una opción: ")

            if opcion == "1":
                sueldos = asignar_sueldos()
                print("Sueldos asignados con exito")
            elif opcion == "2":
                if sueldos:
                    clasificar_sueldos()
                else : print("Primero debes asignar los sueldos")
            elif opcion == "3":
                if sueldos:
                    mostrar_estadisticas()
                else : print("Primero debes asignar los sueldos")
            elif opcion == "4":
                if sueldos:
                    reporte = reporte_sueldos(sueldos)
                    exportar_archivo(reporte)
            elif opcion == "5":
                print("/nFinalizando programa....")
                print("Desarollado por Agustin Yañez Barria")
                print("RUT 21.865.003-1")

                break

            else:
                print("Opción invalida, intentalo nuevamente")


aplicacion()
        

