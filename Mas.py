


def es_vocal_minuscula(vocal):
    # Verifica si es una vocal minúscula
    if vocal in 'aeiou':
        return True
    # Verifica si es una vocal mayúscula
    elif vocal in 'AEIOU':
        return False
    # Si no es una vocal, retorna None o lanza un error
    else:
        return None  # O podrías lanzar un ValueError si lo prefieres
        
print(es_vocal_minuscula('0'))  # True

