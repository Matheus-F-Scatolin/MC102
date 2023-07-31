def encontrar_soma_medias(categorias_simples: dict[str, dict[str, list[int]]]) -> dict[str, int]:
    '''
    Função que, dado um dicionario com as categorias e os filmes com suas
    respectivas avaliações, devolve a soma das médias de categorias para
    cada filme.

    Parâmetros:
        categorias_simples (dict[str, dict[str, list[int]]]): dicionario
    com as categorias e os filmes com suas respectivas avaliações

    Retorna:
        dict[str, int]: dicionário com as somas das médias de categorias para
    cada filme.
    '''
    soma_medias = {}
    for categoria in categorias_simples:
        # iterando por cada categoria
        for filme in categorias_simples[categoria]:
            # iterando por cada filme dentro de determinada categoria
            # ex: categorias_simples[categoria][filme]  ---> [8, 5]
            if len(categorias_simples[categoria][filme]) != 0:
                if filme in soma_medias:
                    soma_medias[filme] += sum(categorias_simples[categoria][filme])/len(categorias_simples[categoria][filme])
                else:
                    soma_medias[filme] = sum(categorias_simples[categoria][filme])/len(categorias_simples[categoria][filme])
    return soma_medias


def encontrar_vencedor_simples(categoria_avaliada: dict[str, list[int]]) -> list[str]:
    '''
    Função que, dado um dicionario com os filmes e suas respectivas avaliações,
    devolve o vencedor da categoria.

    Parâmetros:
        categorias_avaliada (dict[str, list[int]]]): dicionario os filmes e
    suas respectivas avaliações

    Retorna:
        list[str]: lista com os vencedores da categoria
    '''
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


def encontrar_pior_filme(vencedores_individuais: list[str], soma_medias: dict[str, int]) -> str:
    '''
    Função que, dado uma lista com os vencedores de cada categoria,
    retorna o vencedor da categoria pior filme

    Parâmetros:
        vencedores_individuais (list[str]): lista com os vencedores
    de cada categoria simples
         soma_medias (dict[str, int]): dicionário com a soma das médias
    de cada filme

    Retorna:
        str: vencedor da categoria pior filme.
    '''
    maiores_vencedores = []
    n_max_de_vitorias = 0
    for filme in vencedores_individuais:
        if vencedores_individuais.count(filme) >= n_max_de_vitorias and filme not in maiores_vencedores:
            if vencedores_individuais.count(filme) > n_max_de_vitorias:
                maiores_vencedores.clear()
            maiores_vencedores.append(filme)
            n_max_de_vitorias = vencedores_individuais.count(filme)
    if len(maiores_vencedores) == 1:
        return maiores_vencedores[0]
    else:
        # Testar o critério de desempate
        maior_soma_medias = 0
        vencedor = ''
        for filme in vencedores_individuais:
            if soma_medias[filme] > maior_soma_medias:
                maior_soma_medias = soma_medias[filme]
                vencedor = filme
        return vencedor


categorias_simples = {"filme que causou mais bocejos": {},
                      "filme que foi mais pausado": {},
                      "filme que mais revirou olhos": {},
                      "filme que não gerou discussão nas redes sociais": {},
                      "enredo mais sem noção": {}}
f = int(input())
filmes = []
for c in range(f):
    filmes.append(input())
for categoria in categorias_simples:
    for c in range(len(filmes)):
        categorias_simples[categoria][filmes[c]] = []

q = int(input())  # quantidade de avaliadores
for c in range(q):
    # “avaliador, nome da categoria, nome do filme, nota“.
    avaliacao = input().split(", ")
    categorias_simples[avaliacao[1]][avaliacao[2]].append(int(avaliacao[3]))

# Criar um dicionario com os vencedores de cada categoria simples
vencedores_individuais = []
for categoria in categorias_simples:
    vencedores_individuais.append(encontrar_vencedor_simples
                                  (categorias_simples[categoria]))

# Achar o vencedor de pior filme do ano
pior_filme = encontrar_pior_filme(vencedores_individuais,
                                  encontrar_soma_medias(categorias_simples))

# Achar o vencedor da categoria não merecia estar aqui
# Testar os filmes que não aparecem em soma_medias
soma_medias = encontrar_soma_medias(categorias_simples)
nao_merecia = []
for filme in categorias_simples["filme que causou mais bocejos"]:
    if filme not in soma_medias:
        nao_merecia.append(filme)

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
- {pior_filme}
prêmio não merecia estar aqui
- {", ".join(nao_merecia) if len(nao_merecia) != 0 else "sem ganhadores"}''')