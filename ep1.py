# EP 2019-1: Escape Insper
#
# Alunos: 
#- Matheus Freitas Sant'Ana, matheusfs2@al.insper.edu.br
#- Gabriel Salvator Benatar, gabriel.benatar@beityaacov.com.br
inventario={}
vida=200
usuario=input("Para começar a jogar digite seu nome: ")
def carregar_relidades(escolha2):
    info=''
    realidades={"realidade 1": {"titulo":"Planeta Armaggedon","descricao":"Rick e {0} viajam para um mundo pós-apocalíptico, onde precisarão usar suas habilidades para lutar contra os selvagens nativos".format(usuario)},"realidade 2":{"titulo":"Castelo Medieval","descricao":"Rick e {0} viajam para um forte antigo em ruínas e o item necessário para sua jornada está do outro lado de uma ponte. O único obstáculo que os impede de obtê-lo é um portão que exige a resolução de uma charada para sr destrancado".format(usuario)},"realidade 3":{"titulo":"Caverna Obscura","descricao":"Rick e {0} viajam para uma caverna muito escura iluminada por um só feixe de luz que aponta para um altar sagrado. Curiosos, vocês vão ver o que tem nele".format(usuario)}}
    for e,v in realidades.items():
        if e==escolha2:
            for k in v.values():
                info+='. '
                info+=k
    return info
print()
print()
print("Sala 405- Aula de Design de Software")
print('-'*37)
print('É Quarta-Feira à tarde, você está no Insper na Aula de Design de Software e decide ir ao banheiro, pois precisa de um lugar sossegado para pensar em uma maneira de como adiar o EP, já que você nem começou a fazer. De repente seu avô Rick que estava desaparecido há anos surge e te convida para uma aventura diferenciada, sobre realidades alternativas, mudar o futuro, etc. Você não entende muito bem o que ele quer dizer, mas vê isso como uma possibilidade de adiar o EP.')
print()
print("Rick: Rápido! Preciso de sua ajuda, a Teriathlon Plasmium 26 quebrou! Se você me ajudar, te retribuo com um favor!")
escolha1=input("aceitar ou recusar? ")
if escolha1!="aceitar" and escolha1!="recusar":
    while escolha1!="aceitar" and escolha1!="recusar":
        print()
        escolha1=input("Rick: 'Fala que nem gente!' (digite uma resposta válida): ")       
if escolha1=="aceitar":
    print()
    print("Rick começa a te explicar que precisa consertar sua arma. Para isso, é necessário que vocês visitem 3 realidades diferentes para conseguir os componentes que constituem sua arma: o 'Bowl', uma pedra de urânio e um frasco de magnésio.")
else:
    print()
    print("Rick insiste que você deve ajudá-lo  dizendo que se for com ele, além de te ajudar com a data, também te ajudará a tirar um 10 no EP.")
    escolha1=input("aceitar ou recusar? ")
    if escolha1!="aceitar" and escolha1!="recusar":
        while escolha1!="aceitar" and escolha1!="recusar":
            print()
            escolha1=input("Rick: 'Fala que nem gente!' (digite uma resposta válida: )") 
    if escolha1=="aceitar":
        print()
        print("Que a aventura começe!")
    else:
        print()
        print("Easter egg descoberto! {0} é teletransportado para a garagem de seu avô e uma arma intergaláctica é adicionada ao seu inventário para ser usada no futuro.".format(usuario))
        inventario["arma intergaláctica"]=50


        