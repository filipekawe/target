def verificar_a(texto):
    texto = texto.lower()
    #conta quantas vezes a letra A aparece
    contagem = texto.count('a')

    #verifica se existe letra A no texto
    if contagem > 0:
        return f"A letra 'a' aparece: {contagem} vezes"
    else:
        return f"A letra 'a' nao foi encontrada"
    
texto = "teste"
resultado = verificar_a(texto)
print(resultado)


    