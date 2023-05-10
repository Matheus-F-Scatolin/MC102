opcoes = ''
print('Este é um sistema que irá te ajudar a escolher a sua próxima Distribuição Linux. Responda a algumas poucas perguntas para ter uma recomendação.')
resposta_1 = input('''Seu SO anterior era Linux?
(0) Não
(1) Sim
''')
caminho = 0
if resposta_1 == '0':
  resposta_2 = input('''Seu SO anterior era um MacOS?
(0) Não
(1) Sim
''')
  if resposta_2 == '0':
    opcoes = 'Ubuntu Mate, Ubuntu Mint, Kubuntu, Manjaro'
    caminho = 2
  elif resposta_2 == '1':
    opcoes = 'ElementaryOS, ApricityOS'
    caminho = 2
elif resposta_1 == '1':
  resposta_2 = input('''É programador/ desenvolvedor ou de áreas semelhantes?
(0) Não
(1) Sim
(2) Sim, realizo testes e invasão de sistemas
''')
  if resposta_2 == '0':
    opcoes = 'Ubuntu Mint, Fedora'
    caminho = 3
  elif resposta_2 == '1':
    resposta_3 = input('''Gostaria de algo pronto para uso ao invés de ficar configurando o SO?
(0) Não
(1) Sim
''')
    if resposta_3 == '0':
      resposta_4 = input('''Já utilizou Arch Linux?
(0) Não
(1) Sim
''')
      if resposta_4 == '0':
        opcoes = 'Antergos, Arch Linux'
        caminho = 3
      elif resposta_4 == '1':
        opcoes = 'Gentoo, CentOS, Slackware'
        caminho = 1
    elif resposta_3 == '1':
      resposta_5 = input('''Já utilizou Debian ou Ubuntu?
(0) Não
(1) Sim
''')
      if resposta_5 == '0':
        opcoes = 'OpenSuse, Ubuntu Mint, Ubuntu Mate, Ubuntu'
        caminho = 3
      elif resposta_5 == '1':
        opcoes = 'Manjaro, ApricityOS'
        caminho = 1
  elif resposta_2 == '2':
    opcoes = 'Kali Linux, Black Arch'
    caminho = 3

if opcoes != '':
  if caminho == 1:
    print('Suas escolhas te levaram a um caminho repleto de desafios, para você recomendamos as distribuições: ', end='')
  elif caminho == 2:
    print('Você passará pelo caminho daqueles que decidiram abandonar sua zona de conforto, as distribuições recomendadas são: ', end = '')
  elif caminho == 3:
    print('Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: ', end = '')

  print(opcoes, end='.')
else:
  print('Opção inválida, recomece o questionário.')