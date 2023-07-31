def analisar_brigas(animal_procedimento, brigas):
    numero_brigas = 0
    for animal in animal_procedimento:
        animal = animal.split()[0]
        for briga in brigas:
            if animal in briga: #se um animal que briga tiver sido atendido
                #briga ex: 'bete ricardo'
                if animal == briga.split()[0]: #se for a bete
                    #procurar o ricardo
                    for elemento in animal_procedimento:
                        if briga.split()[1] == elemento.split()[0]:
                            numero_brigas += 1
                if animal == briga.split()[1]:  #se for o ricardo
                    #procurar a bete
                    for elemento in animal_procedimento:
                        if briga.split()[0] == elemento.split()[0]:
                            numero_brigas +=1
    numero_brigas = numero_brigas//2
    return numero_brigas
def lista_para_string(que_deseja_tranformar):
    string = ''
    for c in range(len(que_deseja_tranformar)):
        if c<len(que_deseja_tranformar)-1:
            string += que_deseja_tranformar[c] + ', '
        else:
            string += que_deseja_tranformar[c]
    return string

dias = int(input())
resultados = []
for dia in range(dias):
    quantidade_de_briguentos = int(input()) #quantidades de duplas de animais que brigam
    brigas = []
    for c in range(0,quantidade_de_briguentos):
        brigas.append(input())
    #brigas ex: ['bete ricardo', 'carla mila']
    procedimentos = input().split()
    #procedimentos ex: ['vacina', '1', 'tosa', '3', 'banho', '5']
    numero_animais = int(input())
    animal_procedimento = []
    for c in range(numero_animais):
        animal_procedimento.append(input())
    #animal_procedimento ex: ['mila banho', 'shiva exame', 'lola hotel']
    procedimentos_disponiveis = []
    animais_atendidos = []
    animais_nao_atendidos = []
    pedidos_indisponiveis = []
    for c in range(0, len(procedimentos), 2):
        for x in range(0, int(procedimentos[c+1])):
            procedimentos_disponiveis.append(procedimentos[c])
    #procedimentos_disponiveis ex: ['vacina', 'tosa', 'tosa', 'tosa', 'banho', 'banho', 'banho', 'banho', 'banho']

    #TESTAR ANIMAIS QUE FORAM ATENDIDOS
    for animal in animal_procedimento:
        if animal.split()[1] in procedimentos_disponiveis: # se o procedimento estiver disponivel
            procedimentos_disponiveis.remove(animal.split()[1])
            animais_atendidos.append(animal.split()[0])
        else:
            if animal.split()[1] in procedimentos:
                animais_nao_atendidos.append(animal.split()[0])
            else:
                pedidos_indisponiveis.append(animal.split()[0])
    
    str_atendidos = lista_para_string(animais_atendidos)
    str_nao_atendidos = lista_para_string(animais_nao_atendidos)
    
    # criando uma string com cada resultado

    resultado = ''
    resultado+=(f'Dia: {dia+1}')
    resultado+=(f'\nBrigas: {analisar_brigas(animal_procedimento, brigas)}')
    if len(animais_atendidos) != 0:
        resultado+=(f'\nAnimais atendidos: {str_atendidos}')
    if len(animais_nao_atendidos) != 0:
        resultado+=(f'\nAnimais não atendidos: {str_nao_atendidos}')
    for c in range(len(pedidos_indisponiveis)):
        resultado+=(f'\nAnimal {pedidos_indisponiveis[c]} solicitou procedimento não disponível.')
    resultados.append(resultado)

for c in range(len(resultados)):
    if c>0:
        print('')
    print(resultados[c])