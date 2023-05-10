def encontrar_vencedor_simples(categoria_avaliada: dict):
    # {'a força da amizade': [8,8], 'elas por elas': [9], 'ninguém é de ninguém': [10,8], 'o portal secreto': [9,9]}
    vencedores_da_categoria = []
    maior_pontuacao = -1
    for chave in categoria_avaliada:
        if len(categoria_avaliada[chave]) != 0:
            pontuacao = sum(categoria_avaliada[chave])/len(categoria_avaliada[chave])
            if pontuacao >= maior_pontuacao:
                if pontuacao > maior_pontuacao:
                    vencedores_da_categoria.clear()
                vencedores_da_categoria.append(chave)
                maior_pontuacao = pontuacao


    if len(vencedores_da_categoria) > 1:
        n_votos = []
        for vencedor in vencedores_da_categoria:
            n_votos.append(len(categoria_avaliada[vencedor]))
        return vencedores_da_categoria[n_votos.index(max(n_votos))]
    else:
        return vencedores_da_categoria[0]


categorias_simples: dict[str, dict[str, list[int]]] = {"filme que causou mais bocejos": {},
                      "filme que foi mais pausado": {},
                      "filme que mais revirou olhos": {},
                      "filme que não gerou discussão nas redes sociais": {},
                      "enredo mais sem noção": {}}
f = int(input())
filmes = []
for c in range(f):
    # filmes[input()] = []
    filmes.append(input())
# {'a força da amizade': [], 'elas por elas': [], 'ninguém é de ninguém': [], 'o portal secreto': []}
for categoria in categorias_simples:
    for c in range(len(filmes)):
        categorias_simples[categoria][filmes[c]] = []

q = int(input())  # quantidade de avaliadores
for c in range(q):
    # “avaliador, nome da categoria, nome do filme, nota“.
    avaliacao = input().split(", ")  #['avaliador 1', 'filme que causou mais bocejos', 'besouro azul', '7']
    categorias_simples[avaliacao[1]][avaliacao[2]].append(int(avaliacao[3]))

# Criar um dicionario com os vencedores de cada categoria simples
vencedores_individuais = []
for categoria in categorias_simples:
    vencedores_individuais.append(encontrar_vencedor_simples(categorias_simples[categoria]))

# Achar o vencedor de pior filme do ano
categorias = ['']


print(f'''#### abacaxi de ouro ####

categorias simples
categoria: filme que causou mais bocejos
- {vencedores_individuais[0]}
categoria: filme que foi mais pausado
- {vencedores_individuais[1]}
categoria: filme que mais revirou olhos
- {vencedores_individuais[2]}
categoria: filme que não gerou discussão nas redes sociais
- {vencedores_individuais[3]}
categoria: enredo mais sem noção
- {vencedores_individuais[4]}
categorias especiais
prêmio pior filme do ano
- o portal secreto
prêmio não merecia estar aqui
- sem ganhadores''')


#ACHAR O VENCEDOR DAS DUAS CATEGORIAS ESPECIAIS
