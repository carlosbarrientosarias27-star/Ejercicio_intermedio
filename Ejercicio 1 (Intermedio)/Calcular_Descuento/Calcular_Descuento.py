def calcular_descuento(precio, porcentaje, tipo_cliente):
    """
    Calcula el precio final aplicando descuento.
    
    :param precio: Precio original (>=0)
    :param porcentaje: Descuento base entre 0 y 100
    :param tipo_cliente: 'premium' o 'regular'
    :return: Precio final redondeado a 2 decimales
    """

    # 🔎 Validación inmediato 

    if not isinstance(precio, (int, float)):
            raise TypeError("El precio debe ser numérico.")
    
    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")
    
    if porcentaje < 0 or porcentaje > 100:
        raise ValueError("El porcentaje debe estar entre 0 y 100.")
    

    descuento_total = porcentaje
    
    if tipo_cliente == 'premium':
        descuento_total += 5
    
    precio_final = precio * (1 - descuento_total / 100)
    
    return round(precio_final, 2) 

if __name__ == "__main__":
    try:
        resultado = calcular_descuento(50, 10, 'premium')
        print(resultado)

    except ValueError as e:
        print("Se produjo un error:", e)

