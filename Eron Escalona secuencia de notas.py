def main():
    #Definir variables globales
    n:int
    sumap:int
    sumre:int
    cont:int
    x:int
    promap:float
    promre:float
    contap:int
    contre:int

    #Entrada de datos
    print("UCAB Elaborado por: Eron Escalona")
    print("Indique un numero entero positivo entre 1 y 20 de la secuencia de notas de los estudiantes")
    n=int(input())
    
    # Inicializacion contadores
    sumap = 0
    sumre = 0
    cont = 0
    x = n
    promap = 0
    promre = 0
    contap = 0
    contre = 0

    #Procesamiento de datos
    #Comprobación si el usuario coloco un datos permitidos dentro del rango
    if(x>20) or (x<1):
        print("ERROR, el numero que indico es: " ,x)
        print("Debe indicar las notas del 1 al 20")
        print("Por favor intente nuevamente")
    else:
        print("La secuencia de notas es: ")
        #Ciclo para procesar exactamente 6 notas
        while(cont<6):

            #No se permiten valores mayores a 20 en la secuencia de notas
            if(x>=20):
                x=20
                
            #Contador de estudiantes aprobados y reprobados
            #Suma de notas de los estudiantes aprobados y reprobados
            if(x>=10):
                contap=(contap + 1)
                sumap=(sumap + x)
            else:
                contre=(contre + 1)
                sumre=(sumre + x)

            #Impresion de las notas en una misma linea en pantalla
            if(cont<5):
                print(x,end=", ")
            else:
                print(x,end=". ")

            x=(x+2)

            #Incremento del contador de notas en la secuencia
            cont=(cont+1)

        #Calculo dinamico de promedio de notas dependiendo de la cantidad de estudiantes aprobados y reprobados
        if(sumap>0) and (contap>0):
            promap=(sumap/contap)

        if(sumre>0) and (contre>0):
            promre=(sumre/contre)

            #Salida de datos
        print()

        print("La cantidad de estudiantes reprobados es: " ,contre)
        print("La suma de las notas de los estudiantes reprobados es: " ,sumre)
        print("El promedio de notas de los estudiantes reprobados es: " ,promre)

        print()

        print("La cantidad de estudiantes aprobados es: " ,contap)
        print("La suma de las notas de los estudiantes aprobados es " ,sumap)
        print("El promedio de notas de los estudiantes aprobados es: " ,promap)
main()