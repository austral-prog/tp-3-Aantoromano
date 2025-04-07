def check_vowels():
    # Código a implementar utilizando input.
    nombre= input()
    nombre= nombre.lower() #Escribe todo en minúscula
    #Antonella

    #Imprime en pantalla
    print("Contiene a:", 'a' in nombre)
    print("Contiene e:", 'e' in nombre)
    print("Contiene i:", 'i' in nombre)
    print("Contiene o:", 'o' in nombre)
    print("Contiene u:", 'u' in nombre)


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
