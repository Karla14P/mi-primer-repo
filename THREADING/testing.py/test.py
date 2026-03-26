import re

def evaluar_password(password):
    score = 0
    recomendaciones = []

    # Reglas de validación
    if len(password) >= 12:
        score += 1
    else:
        recomendaciones.append("- Debe tener al menos 12 caracteres.")

    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
    else:
        recomendaciones.append("- Mezcla mayúsculas y minúsculas.")

    if re.search(r"\d", password):
        score += 1
    else:
        recomendaciones.append("- Incluye al menos un número.")

    if re.search(r"[ !@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        recomendaciones.append("- Usa caracteres especiales (ej. @, #, $).")

    return score, recomendaciones

def main():
    print("--- Analizador de Contraseñas ---")
    pswd = input("Introduce una contraseña para probar: ")
    
    puntos, sugerencias = evaluar_password(pswd)
    
    print(f"\nFortaleza: {puntos}/4")
    if puntos == 4:
        print("¡Resultado: Muy segura!")
    else:
        print("Resultado: Débil. Sugerencias:")
        for s in sugerencias:
            print(s)

if __name__ == "__main__":
    main()
    