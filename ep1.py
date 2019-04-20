# EP 2019-1: Escape Insper
#
# Alunos: 
#- Matheus Freitas Sant'Ana, matheusfs2@al.insper.edu.br
#- Gabriel Salvator Benatar, gabriel.benatar@beityaacov.com.br
inventario={}
vida=200
usuario=input("Para começar a jogar digite seu nome: ")
print()
print()
print("Sala 405- Aula de Design de Software")
print('-'*37)
print('É Quarta-Feira à tarde, você está no Insper na Aula de Design de Software e decide ir ao banheiro, pois precisa de um lugar sossegado para pensar em uma maneira de como adiar o EP, já que você nem começou a fazer. De repente seu avô Rick que estava desaparecido há anos surge e te convida para uma aventura diferenciada, sobre realidades alternativas, mudar o futuro, etc. Você não entende muito bem o que ele quer dizer, mas vê isso como uma possibilidade de adiar o EP.')
print()
print("Rick: Rápido! Preciso de sua ajuda, a Teriathlon Plasmium 26 quebrou! Se você me ajudar, te retribuo com um favor!")
print()
escolha1=input("aceitar ou recusar? ")
if escolha1!="aceitar" and escolha1!="recusar":
    while escolha1!="aceitar" and escolha1!="recusar":
        print()
        escolha1=input("Rick: 'Fala que nem gente!' (digite uma resposta válida)")       
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
            escolha1=input("Rick: 'Fala que nem gente!' (digite uma resposta válida)") 
    if escolha1=="aceitar":
        print()
        print("Que a aventura começe!")
    else:
        print("{0} é teletransportado para a garagem de seu avô e uma arma intergaláctica é adicionada ao seu inventário para ser usada no futuro.".format(usuario))
        inventario["arma intergaláctica"]=50

        