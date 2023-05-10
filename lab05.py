def reverter(sequencia_original, i, j): 
    '''Reverte a parte do genoma que vai de i até j'''
    if i > len(sequencia_original):
        i = len(sequencia_original) - 1
    if j > len(sequencia_original):
        j = len(sequencia_original) - 1
    subseq1 = sequencia_original[:i]
    subseq2 = sequencia_original[i:j+1]
    subseq3 = sequencia_original[j+1:]
    return subseq1 + subseq2[::-1] + subseq3

def transpor(sequencia_original, i, j, k):
    '''separar a sequencia em subsequencias e reordenar elas'''
    sub_sequencia1 = sequencia_original[:i]  
    sub_sequencia2 = sequencia_original[i:j+1]  
    sub_sequencia3 = sequencia_original[j+1:k+1]  
    sub_sequencia4 = sequencia_original[k+1:]
    sequencia_final = sub_sequencia1 + sub_sequencia3 + sub_sequencia2 + sub_sequencia4 
    return sequencia_final

def combinar(sequencia, g, i):
    '''Combina o genoma inicial com outro genoma dado na posição i'''
    subseq1 = sequencia[:i]
    subseq2 = sequencia[i:]
    return subseq1 + g + subseq2

def concatenar(sequencia, g):
    '''Concatena o genoma inicial com outro genoma dado'''
    return sequencia + g

def remover(sequencia, i, j):
    '''Remove uma parte do genoma'''
    if i > len(sequencia):
        i = len(sequencia) - 1
    if j > len(sequencia):
        j = len(sequencia) - 1
    subseq1 = sequencia[:i]
    subseq2 = sequencia[j+1:]
    return subseq1 + subseq2

def transpor_e_reverter(sequencia, i, j, k):
    '''Transpõe e depois reverte parte do genoma'''
    sequencia = transpor(sequencia, i, j, k)
    sequencia = reverter(sequencia, i, k)
    return sequencia

def buscar(sequencia, g): 
    '''Busca por ocorrencias de um trecho especifico de genoma no genoma inicial'''
    ocorrencias = sequencia.count(g)
    return ocorrencias

def buscar_bidirecional(sequencia, g):
    '''Busca por ocorrencias de um trecho especifico de genoma no genoma inicial'''
    ocorrencias = 0
    ocorrencias += buscar(sequencia, g)
    g = g[::-1]
    ocorrencias += buscar(sequencia, g)
    print(ocorrencias)

def mostrar(sequencia):
    '''Mostra o genoma'''
    print(sequencia)


genoma = input()
entrada = ''
while entrada != 'sair':
    entrada = input()
    if entrada.split()[0] == 'reverter':
        genoma = reverter(genoma, int(entrada.split()[1]), int(entrada.split()[2]))

    elif entrada.split()[0] == 'transpor':
        genoma = transpor(genoma, int(entrada.split()[1]), int(entrada.split()[2]), int(entrada.split()[3]))
    
    elif entrada.split()[0] == 'combinar':
        genoma = combinar(genoma, entrada.split()[1], int(entrada.split()[2]))
    
    elif entrada.split()[0] == 'concatenar':
        genoma = concatenar(genoma, entrada.split()[1])
    
    elif entrada.split()[0] == 'remover':
        genoma = remover(genoma, int(entrada.split()[1]), int(entrada.split()[2]))

    elif entrada.split()[0] == 'transpor_e_reverter':
        genoma = transpor_e_reverter(genoma, (int(entrada.split()[1])), (int(entrada.split()[2])), (int(entrada.split()[3])))
    
    elif entrada.split()[0] == 'buscar':
        print(buscar(genoma, entrada.split()[1]))
    
    elif entrada.split()[0] == 'buscar_bidirecional':
        buscar_bidirecional(genoma, entrada.split()[1])
    
    elif entrada.split()[0] == 'mostrar':
        mostrar(genoma)
