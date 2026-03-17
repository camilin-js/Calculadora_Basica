"""
Módulo: calculadora_basica.py
Propósito: Proveer funciones para operaciones aritméticas elementales.
Autor: Camilo Rodríguez
"""

# Definición de Constantes para evitar "Strings Mágicos" (PEP 8)
OP_SUMAR = "sumar"
OP_RESTAR = "restar"
OP_MULTIPLICAR = "multiplicar"
OP_DIVIDIR = "dividir"


def realizar_operacion(numero_a, numero_b, operacion):
    """
    Realiza una operación aritmética entre dos números.

    Args:
        numero_a (float): Primer operando.
        numero_b (float): Segundo operando.
        operacion (str): Tipo de operación.

    Returns:
        float: Resultado de la operación.
        str: Mensaje de error en caso de división por cero o falla lógica.
    """
    # Aplicación de Cláusulas de Guarda (Early Returns)
    if operacion == OP_SUMAR:
        return numero_a + numero_b

    if operacion == OP_RESTAR:
        return numero_a - numero_b

    if operacion == OP_MULTIPLICAR:
        return numero_a * numero_b

    if operacion == OP_DIVIDIR:
        if numero_b == 0:
            return "Error: No se puede dividir entre cero."
        return numero_a / numero_b

    return "Operación no reconocida."


def ejecutar_interfaz_calculadora():
    """
    Maneja la interacción con el usuario de forma robusta.
    Implementa validación de excepciones (ValueError).
    """
    print("--- Calculadora Aritmética Básica ---")
    print(f"Opciones: {OP_SUMAR}, {OP_RESTAR}, {OP_MULTIPLICAR}, {OP_DIVIDIR}")

    try:
        # Captura segura de datos con conversión a float
        num1 = float(input("\nIngresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        accion = input("Ingresa la operación a realizar: ").lower().strip()

        # Invocación de la lógica central
        resultado = realizar_operacion(num1, num2, accion)

        # Salida formateada respetando límites de línea (PEP 8)
        print(f"\n>>> Resultado final: {resultado}")

    except ValueError:
        # Manejo de excepciones para entradas no numéricas
        print("\nError de entrada: Por favor, ingresa solo valores numéricos válidos.")


# Bloque de Ejecución Principal (Pruebas e Interacción)
if __name__ == "__main__":
    ejecutar_interfaz_calculadora()
