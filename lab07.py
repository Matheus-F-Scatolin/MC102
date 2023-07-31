def decodificar(operacao: str, operando1: str, operando2: str,
                frases_codificadas: str) -> str:
    '''
    Função que decodifica uma frase mediante o cálculo de uma chave, a qual é
    imprimida durante o processo.

    Parâmetros:
        operacao (str): operacao a ser realizada com a posicao dos operandos.
        operando1 (str): variável que indica a primeira parte da frase a ser
        buscada.
        operando2 (str): variável que indica a segunda parte da frase a ser
        procurada.
        frases_codificadas (str): string com todas as frases que devem ser
        decodificadas concatenadas.

    Retorna:
        str: uma string com as frases decodificadas concatenadas.
    '''
    vogais = 'aeiouAEIOU'
    consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    numeros = '0123456789'
    # achar a posicao do operando1
    if operando1 == 'vogal':
        for caractere in frases_codificadas:
            if caractere in vogais:
                posicao_operando1 = frases_codificadas.index(caractere)
                break
    elif operando1 == 'consoante':
        for caractere in frases_codificadas:
            if caractere in consoantes:
                posicao_operando1 = frases_codificadas.index(caractere)
                break
    elif operando1 == 'numero':
        for caractere in frases_codificadas:
            if caractere in numeros:
                posicao_operando1 = frases_codificadas.index(caractere)
                break
    else:
        posicao_operando1 = frases_codificadas.index(operando1)

    # achar a posicao do operando2
    if operando2 == 'vogal':
        for caractere in frases_codificadas[posicao_operando1:]:
            if caractere in vogais:
                posicao_operando2 = frases_codificadas.index(caractere,
                                                             posicao_operando1)
                break
    elif operando2 == 'consoante':
        for caractere in frases_codificadas[posicao_operando1:]:
            if caractere in consoantes:
                posicao_operando2 = frases_codificadas.index(caractere,
                                                             posicao_operando1)
                break
    elif operando2 == 'numero':
        for caractere in frases_codificadas[posicao_operando1:]:
            if caractere in numeros:
                posicao_operando2 = frases_codificadas.index(caractere,
                                                             posicao_operando1)
                break
    else:
        posicao_operando2 = frases_codificadas.index(operando2,
                                                     posicao_operando1)

    if operacao == '*':
        chave = posicao_operando1 * posicao_operando2
    elif operacao == '+':
        chave = posicao_operando1 + posicao_operando2
    else:
        chave = posicao_operando1 - posicao_operando2
    print(chave)

    # somar a chave no valor inicial de cada caractere
    frases_decodificadas = ''
    for caractere in frases_codificadas:
        decimal_original = ord(caractere)
        decimal_decriptografado = decimal_original + chave
        # se passar de 126, voltar a contar do 32, e vice versa
        while decimal_decriptografado > 126:
            decimal_decriptografado -= 95
        while decimal_decriptografado < 32:
            decimal_decriptografado += 95
        frases_decodificadas += chr(decimal_decriptografado)

    return frases_decodificadas


def main() -> None:
    operacao = input()
    operando1 = input()
    operando2 = input()
    n_de_linhas = int(input())
    # frases codificadas é uma string que contém todas as frases codificadas
    frases_codificadas = ''
    quebras_de_linha = []
    for c in range(n_de_linhas):
        linha = input()
        frases_codificadas += linha
        quebras_de_linha.append(len(frases_codificadas))
    frases_decodificadas = decodificar(operacao, operando1, operando2,
                                       frases_codificadas)
    if len(quebras_de_linha) < 2:
        print(frases_decodificadas)
    else:
        resultado = [frases_decodificadas[:quebras_de_linha[0]]]
        inicio = 0
        fim = quebras_de_linha[0]
        for c in range(1, len(quebras_de_linha)):
            inicio = fim
            fim = quebras_de_linha[c]
            resultado.append(frases_decodificadas[inicio:fim])
        for elemento in resultado:
            print(elemento)


if __name__ == '__main__':
    main()
