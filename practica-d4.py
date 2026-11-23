"""Gestor de la caja de un comercio con menú que permite: 
    - Registrar una venta (importe y forma de pago) 
    - Anular la última venta
    - Consultar el total del día
    - Consultar el número de operaciones
    - Consultar el importe medio
    - Consultar la venta mayor
    - Cerrar la caja mostrando un resumen

Módulo 0485 Programación · UD 3
Autor: Andrea Mira Hernández y Jose María Mas Chicharro
Fecha: 20/11/2026
"""

# Variables globales
ventas = []
operaciones = 0
total = 0


#Funciones
def leer_opcion():
    """Solicita una opción del menú y controla las entradas incorrectas."""
    while True:
        try:
            num_opcion = int(input("\nIntroduzca el número de la opción (1-7): "))

            if 1 <= num_opcion <= 7:
                return num_opcion
            else:
                print("Por favor, introduzca un número del 1 al 7.")

        except ValueError:
            print("Por favor introduzca un número entero.")


def leer_importe():
    """Solicita el importe y controla las entradas incorrectas."""
    while True:
        try:
            importe = float(input("\nIntroduce el importe: "))

            if importe > 0:
                return importe

            print("El importe introducido debe ser mayor a 0.")

        except ValueError:
            print("Por favor, introduzca un valor numérico como importe.")


def seleccionar_pago():
    """Solicita el método de pago y controla las entradas incorrectas."""
    while True:
        try:
            pago = input("Introduce el método de pago (efectivo o tarjeta): ")

            if pago.lower() == "tarjeta" or pago.lower() == "efectivo":
                return pago

            print("Por favor, introduzca una de los métodos de pago aceptado.")
        except ValueError:
            print("Método de pago no aceptado.")


def registrar_venta():
    """Registra una venta con su importe y forma de pago."""
    # Traemos las variables a la función
    global ventas, operaciones, total

    importe = leer_importe()
    pago = seleccionar_pago()

    # Guardamos la venta como una lista y creamos una lista de las ventas
    venta = [importe, pago]
    ventas += [venta]

    #Acumulamos el importe total y contamos la operación
    total += importe
    operaciones += 1

    print("Venta registrada correctamente.")


def anular_venta():
    """Anular la última venta registrada."""
    # Traemos las variables a la función
    global ventas, total, operaciones

    if operaciones == 0:
        print("No hay ninguna venta registrada.")
        return total, operaciones

    #Recuperamos la última venta y la eliminamos de la lista de ventas
    importe = ventas[-1][0]
    ventas = ventas[:-1]

    # Actualizamos el total y el número de operaciones
    operaciones -= 1
    total -= importe

    print("Venta anulada correctamente.")

    return total, operaciones


def importe_medio():
    """Calcular el importe medio de las operaciones."""
    if operaciones == 0:
        print("No hay ninguna venta registrada.")
        return 0

    return total / operaciones


def venta_mayor():
    """Buscar y devolver el importe de la venta mayor."""
    if operaciones == 0:
        print("No hay ninguna venta registrada.")
        return 0

    mayor = ventas[0][0]

    for venta in ventas:
        if venta[0] > mayor:
            mayor = venta[0]

    return mayor


def cerrar_caja():
    """Mostrar el resumen final y cerrar la caja."""
    print("\n----- RESUMEN DEL DÍA -----")
    print(f"Total del día: {total:.2f}€")
    print(f"Número de operaciones realizadas: {operaciones}")

    if operaciones == 0:
        print("Importe medio: 0.00€")
        print("Venta mayor: 0.00€")
    else:
        print(f"Importe medio: {importe_medio():.2f}€")
        print(f"Venta mayor: {venta_mayor():.2f}€")


#Programa principal
def main():
    """Controlar el menú principal mediante un bucle."""
    while True:
        print("\nOpciones de caja:")
        print("1. Registrar una venta")
        print("2. Anular última venta")
        print("3. Consultar el total del día")
        print("4. Consultar el número de operaciones")
        print("5. Consultar el importe medio")
        print("6. Consultar la venta mayor")
        print("7. Cerrar la caja")

        num_opcion = leer_opcion()

        match num_opcion:
            case 1:
                print("\n1. Registrar una venta")
                registrar_venta()

            case 2:
                print("\n2. Anular última venta")
                anular_venta()

            case 3:
                print("\n3. Consultar el total del día")
                print(f"El importe total del día es: {total:.2f}€")

            case 4:
                print("\n4. Consultar el número de operaciones")
                print(f"\nEl número de operaciones realizadas es: {operaciones}")

            case 5:
                print("\n5. Consultar el importe medio")
                media = importe_medio()
                print(f"\nEl importe medio de hoy es: {media:.2f}")

            case 6:
                print("\n6. Consultar la venta mayor")
                mayor = venta_mayor()
                print(f"\nLa venta mayor de hoy es: {mayor:.2f}")

            case 7:
                print("\n7. Cerrar la caja")
                cerrar_caja()
                break


if __name__ == "__main__":
    main()