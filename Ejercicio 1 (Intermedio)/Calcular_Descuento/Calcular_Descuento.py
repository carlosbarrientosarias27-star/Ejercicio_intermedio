def calcular_descuento(precio, porcentaje, tipo_cliente):
    # 🔎 Validación inmediata
    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")
    
    if porcentaje < 0 or porcentaje > 100:
        raise ValueError("El porcentaje debe estar entre 0 y 100.")
    

    descuento_total = porcentaje
    
    if tipo_cliente == 'premium':
        descuento_total += 5
    
    precio_final = precio * (1 - descuento_total / 100)
    
    return round(precio_final, 2) 

try:
    resultado = calcular_descuento(-50, 10, 'premium')
    print(resultado)
except ValueError as e:
    print("Se produjo un error:", e)

