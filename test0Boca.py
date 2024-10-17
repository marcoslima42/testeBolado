from collections import Counter

def sao_anagramas(str1, str2):
    # Remover espaços, converter para minúsculas e manter apenas caracteres alfanuméricos
    filtro_str1 = ''.join(c.lower() for c in str1 if c.isalnum())
    filtro_str2 = ''.join(c.lower() for c in str2 if c.isalnum())

    # Comparar a frequência de caracteres usando Counter
    return Counter(filtro_str1) == Counter(filtro_str2)

# Leitura das duas strings
str1 = input().strip()
str2 = input().strip()

# Verifica se são anagramas e imprime o resultado
if sao_anagramas(str1, str2):
    print("sim")
else:
    print("não")
