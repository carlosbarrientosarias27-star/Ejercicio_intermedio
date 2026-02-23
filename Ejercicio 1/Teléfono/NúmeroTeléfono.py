import re

def validar_telefono_es(numero: str) -> bool:
    """
    Valida si un número de teléfono español tiene el formato correcto.

    El formato válido debe:
    - Comenzar con '+34'
    - Estar seguido exactamente por 9 dígitos (0-9)
    - No contener espacios ni caracteres adicionales

    Ejemplo válido:
        +34612345678

    :param numero: Número de teléfono a validar.
    :type numero: str
    :return: True si el número cumple el formato, False en caso contrario.
    :rtype: bool
    """
    patron: str = r'^\+34\d{9}$'
    return bool(re.fullmatch(patron, numero))


# -------------------
# Casos de prueba
# -------------------
if __name__ == "__main__":
    # 1. Caso válido
    assert validar_telefono_es("+34612345678") is True

    # 2. Caso inválido: menos de 9 dígitos
    assert validar_telefono_es("+3461234567") is False

    # 3. Caso inválido: sin prefijo +34
    assert validar_telefono_es("612345678") is False

    print("Todos los casos de prueba pasaron correctamente.")