"""
Tarea:    Siguiente día
Autor:  Mariana Izquierdo Preciado
Expediente: 756355
Carrera: Ingeniería y Ciencia de Datos 

Materia: Algoritmos y Programación
Profesor: Jorge A. Zaldívar Carrillo
Grupo:    ESI232B2

Fecha:    2/nov/2024
Tiempo aproxumado de elaboración: 1 hora
"""
#importar
from dia_siguiente import dias_del_mes

# Programa principal
def main():
    #Entradas
    dia = int(input("Día: "))
    mes = int(input("Mes: "))
    anho = int(input("Año: "))

    #Proceso
    dia -=1
    if dia == 0:
        mes -=1
        if mes == 0:
            mes=12
            anho-=1
        dia=dias_del_mes(mes,anho)

    #Salidas
    print()
    print("Dia: ", dia)
    print("Mes: ", mes)
    print("Año: ", anho)

if __name__== "__main__":
    main()
