/**
 * Valida si un número de teléfono español tiene el formato correcto.
 *
 * El formato válido debe:
 * - Comenzar con '+34'
 * - Estar seguido exactamente por 9 dígitos (0-9)
 * - No contener espacios ni caracteres adicionales
 *
 * Ejemplo válido:
 *   +34612345678
 *
 * @param numero - Número de teléfono a validar.
 * @returns true si el número cumple el formato, false en caso contrario.
 */
function validarTelefonoES(numero: string): boolean {
  const patron: RegExp = /^\+34\d{9}$/;
  return patron.test(numero);
}


// -------------------
// Casos de prueba
// -------------------

// 1. Caso válido
console.assert(validarTelefonoES("+34612345678") === true, "Debe ser válido");

// 2. Caso inválido: menos de 9 dígitos
console.assert(validarTelefonoES("+3461234567") === false, "Debe ser inválido");

// 3. Caso inválido: sin prefijo +34
console.assert(validarTelefonoES("612345678") === false, "Debe ser inválido");

console.log("Todos los casos de prueba ejecutados.");