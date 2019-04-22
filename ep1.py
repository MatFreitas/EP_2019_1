# EP 2019-1: Escape Insper
#
# Alunos: 
#- Matheus Freitas Sant'Ana, matheusfs2@al.insper.edu.br
#- Gabriel Salvator Benatar, gabriel.benatar@beityaacov.com.br
import random
import time
inventario={}
usuario=input("Para começar a jogar digite seu nome: ")

def carregar_realidade3(escolha2):
    vida_usuario=220
    vida_agente=180
    tapa_intergaláctico=20
    combo_de_socos=80
    banho_de_ácido=50
    soco_agente=60
    chute_agente=50
    peteleco_agente=100
    
    
    print()
    time.sleep(0.2)
    print("Rick: Socorro! Agente Thompson nos encontrou! Ele é do governo, e está atrás de nós, pois o que estamos fazendo é ilegal! Ganhe dele na luta para que possamos continuar. (Dica: atente-se para a vida do oponente para verificar a eficiência de seus ataques!)")
    time.sleep(0.2)
    print("Vida de {0}: {1}".format(usuario,vida_usuario))
    time.sleep(0.2)
    print("Vida do Agente: {0}".format(vida_agente))
    while vida_agente>0 and vida_usuario>0:
        a=random.randint(1,20)
        print("Sua vez de atacar! Opções: tapa intergaláctico, combo de socos, banho de ácido.")
        ataque=input("Ataque escolhido: ")
        while ataque!="tapa intergaláctico" and ataque!="combo de socos" and ataque!="banho de ácido" and ataque!="arma intergaláctica":
            ataque=input("Ihhhh, não foi dessa vez. Tente outro ataque: ")
        if ataque=="arma intergaláctica":
            print("A-ha! Você lembrou-se da sua arma guardada em seu inventário!")
            vida_agente-=inventario["arma intergaláctica"]
        else:
            if ataque=="tapa intergaláctico":
                vida_agente-=tapa_intergaláctico
                print("Vida do agente: {0}".format(vida_agente))
            elif ataque=="combo_de_socos":
                vida_agente-=combo_de_socos
                print("Vida do agente: {0}".format(vida_agente))
            else:
                vida_agente-=banho_de_ácido
                print("Vida do agente: {0}".format(vida_agente))
            if 1<=a<=10 and vida_agente>0:
                vida_usuario-=soco_agente
                print()
                time.sleep(0.2)
                print("O oponente utilizou 'Soco agente'!")
                time.sleep(0.2)
                print("Vida de {0}: {1}".format(usuario,vida_usuario))
            elif 11<=a<18 and vida_agente>0:
                vida_usuario-=chute_agente
                print()
                time.sleep(0.2)
                print("O oponente utilizou 'Chute agente'!")
                time.sleep(0.2)
                print("Vida de {0}: {1}".format(usuario,vida_usuario))
            elif 18<=a<=20 and vida_agente>0:
                vida_usuario-=peteleco_agente
                print()
                time.sleep(0.2)
                print("O oponente utilizou o seu ataque especial! O peteleco agente!!")
                time.sleep(0.2)
                print("Vida de {0}: {1}".format(usuario,vida_usuario))
    if vida_usuario<=0:
        return("Você morreu!")
    else:
        inventario["troféu da realidade 3"]="Frasco de Magnésio"
        return("Agente derrotado! Agora, como recompensa, um frasco de magnésio que irá ajudar na constituição da arma foi adicionada ao seu inventário.")

def carregar_realidade2(escolha2):
    print()
    time.sleep(0.2)
    resolucao=input("Charada: a todas sas coisas e homens eu pertenço, mas ainda sou evitado com desdenho. Acaricie e cuide de mim até enlouquecer, mas nenhum golpe no fim pode me deter. Comigo crianças se deleitam, anciões me rejeitam e belas damas contemplam. Chore, e chorarei; boceje, e dormirei; sorria, e também sorrirei. Quem sou eu?  ")
    tentativas=10
    while tentativas>0 and resolucao!="reflexo":
        time.sleep(0.2)
        resolucao=input("Errado! Restam {0} tentativas! ".format(tentativas))
        tentativas-=1
    if tentativas>0:
        print()
        time.sleep(0.2)
        inventario["troféu da realidade 2"]="The Bowl"
        return ("Você decifrou a charada! Agora, o 'The Bowl', item que atua como transmissor de energia da arma, foi adicionado ao seu inventário.")
    else:
        print()
        return ("Fracassou! Você e Rick caem em no calabouço do rei onde estão destinados a permanecer até o fim de suas vidas!")

def carregar_realidade1(escolha2):
    vida_usuario=220
    vida_selvagem=180
    laser_blaster=20
    conjunto_com_rick=80
    espada_do_julgamento=50
    soco_selvagem=60
    chute_selvagem=50
    combo_selvagem=100
    print()
    time.sleep(0.2)
    print("Oh não! Um selvagem super forte surgiu no seu caminho! (Dica: atente-se para a vida do oponente para verificar a eficiência de seus ataques!)")
    time.sleep(0.2)
    print("Vida de {0}: {1}".format(usuario,vida_usuario))
    time.sleep(0.2)
    print("Vida de Selvagem: {0}".format(vida_selvagem))
    while vida_selvagem>0 and vida_usuario>0:
        a=random.randint(1,20)
        time.sleep(0.2)
        print("Sua vez de atacar! Opções: laser blaster, ataque em conjunto com rick, espada do julgamento")
        ataque=input("Ataque escolhido: ")
        while ataque!="laser blaster" and ataque!="ataque em conjunto com rick" and ataque!="espada do julgamento" and ataque!="arma intergaláctica":
            ataque=input("Ihhhh, não foi dessa vez. Tente outro ataque: ")
        if ataque=="arma intergaláctica":
            print("A-ha! Você lembrou-se da sua arma guardada em seu inventário!")
            vida_selvagem-=inventario["arma intergaláctica"]
        else:
            if ataque=="laser blaster":
                vida_selvagem-=laser_blaster
                time.sleep(0.9)
                print("Vida do selvagem: {0}".format(vida_selvagem))
            elif ataque=="ataque em conjunto com rick":
                vida_selvagem-=conjunto_com_rick
                time.sleep(0.9)
                print("Vida do selvagem: {0}".format(vida_selvagem))
            else:
                vida_selvagem-=espada_do_julgamento
                time.sleep(0.9)
                print("Vida do selvagem: {0}".format(vida_selvagem))
            if 1<=a<=10 and vida_selvagem>0:
                vida_usuario-=chute_selvagem
                print()
                time.sleep(0.2)
                print("O oponente utilizou 'chute selvagem'!")
                time.sleep(0.2)
                print("Vida de {0}: {1}".format(usuario,vida_usuario))
            elif 11<=a<18 and vida_selvagem>0:
                vida_usuario-=soco_selvagem
                print()
                time.sleep(0.2)
                print("O oponente utilizou 'soco selvagem'!")
                time.sleep(0.2)
                print("Vida de {0}: {1}".format(usuario,vida_usuario))
            elif 18<=a<=20 and vida_selvagem>0:
                vida_usuario-=combo_selvagem
                print()
                time.sleep(0.2)
                print("O oponente utilizou o seu ataque especial!")
                time.sleep(0.2)
                print("Vida de {0}: {1}".format(usuario,vida_usuario))
    if vida_usuario<=0:
        return("Você morreu!")
    else:
        inventario["troféu da realidade 1"]="Pedra de Urânio"
        return("Selvagem derrotado! Agora, como recompensa, uma pedra de urânio que irá servir como fonte da arma foi adicionada ao seu inventário.")
        
def carregar_realidades(escolha2):
    print()
    info=''
    realidades={"realidade 1": {"titulo":"Planeta Armaggedon","descricao":"Rick e {0} viajam para um mundo pós-apocalíptico, onde precisarão usar suas habilidades para lutar contra os selvagens nativos".format(usuario)},"realidade 2":{"titulo":"Castelo Medieval","descricao":"Rick e {0} viajam para um forte antigo em ruínas e o item necessário para sua jornada está do outro lado de uma ponte. O único obstáculo que os impede de obtê-lo é um portão que exige a resolução de uma charada para ser destrancado".format(usuario)},"realidade 3":{"titulo":"Caverna Obscura","descricao":"Rick e {0} viajam para uma caverna muito escura iluminada por um só feixe de luz que aponta para um altar sagrado. Curiosos, vocês vão ver o que tem nele".format(usuario)}}
    for e,v in realidades.items():
        if e==escolha2:
            for k in v.values():
                info+=k
                info+='. '
    print (info)
    if escolha2=="realidade 1":
        return carregar_realidade1(escolha2)
    elif escolha2=="realidade 2":
        return carregar_realidade2(escolha2)
    else:
        return carregar_realidade3(escolha2)
    
print()
print()
time.sleep(0.4)
print("Sala 405- Aula de Design de Software")
time.sleep(0.4)
print('-'*37)
time.sleep(0.4)
print('É Quarta-Feira à tarde, você está no Insper na Aula de Design de Software e decide ir ao banheiro, pois precisa de um lugar sossegado para pensar em uma maneira de como adiar o EP, já que você nem começou a fazer. De repente seu avô Rick que estava desaparecido há anos surge e te convida para uma aventura diferenciada, sobre realidades alternativas, mudar o futuro, etc. Você não entende muito bem o que ele quer dizer, mas vê isso como uma possibilidade de adiar o EP.')
print()
time.sleep(0.4)
print("Rick: Rápido! Preciso de sua ajuda, minha arma de teletransporte, a Teriathlon Plasmium 26 quebrou! Se você me ajudar, te retribuo com um favor!")
escolha1=input("aceitar ou recusar? ")
if escolha1!="aceitar" and escolha1!="recusar":
    while escolha1!="aceitar" and escolha1!="recusar":
        print()
        escolha1=input("Rick: 'Fala que nem gente!' (digite uma resposta válida): ")       
if escolha1=="aceitar":
    print()
    time.sleep(0.2)
    print("Rick: Obrigado por aceitar! Agora vou te explicar o que precisa ser feito para consertar minha arma. Para isso será necessário visitar 3 realidades diferentes, em cada uma você encontrará um componete para a contrução da arma. Os componentes necessários para a contrução são: uma pedra de urânio, um frasco de magnésio e o 'Bowl'") 
else:
    print()
    time.sleep(0.2)
    print("Rick insiste que você deve ajudá-lo  dizendo que se for com ele, além de te ajudar com a data, também te ajudará a tirar um 10 no EP.")
    escolha1=input("aceitar ou recusar? ")
    if escolha1!="aceitar" and escolha1!="recusar":
        while escolha1!="aceitar" and escolha1!="recusar":
            print()
            escolha1=input("Rick: 'Fala que nem gente!' (digite uma resposta válida: )") 
    if escolha1=="aceitar":
        print()
        time.sleep(0.2)
        print("Que a aventura começe! Rick começa a te explicar que precisa consertar sua arma. Para isso, é necessário que vocês visitem 3 realidades diferentes para conseguir os componentes que constituem sua arma: o 'Bowl', uma pedra de urânio e um frasco de magnésio.")
    else:
        print()
        time.sleep(0.2)
        print("Easter egg descoberto! {0} é teletransportado para a garagem de seu avô e uma arma intergaláctica é adicionada ao seu inventário para ser usada no futuro. Rick começa a te explicar que precisa consertar sua arma. Para isso, é necessário que vocês visitem 3 realidades diferentes para conseguir os componentes que constituem sua arma: o 'Bowl', uma pedra de urânio e um frasco de magnésio.".format(usuario))
        inventario["arma intergaláctica"]=1000
print()
escolha2=input("Agora, Rick pede para você segui-lo até a câmara quântica de teleporte que está no porão da garagem. Para usá-la, basta digitar o lugar a que deseja ir (suas opções são realidade 1, realidade 2 ou realidade 3): ")
if escolha2!="realidade 1" and escolha2!="realidade 2" and escolha2!="realidade 3":
    while escolha2!="realidade 1" and escolha2!="realidade 2" and escolha2!="realidade 3":
        escolha2=input("Uma mensagem aparece dizendo 'Não Disponível. Tente novamente: ")
print(carregar_realidades(escolha2))
escolha2=input("De volta a garagem, Rick te diz que ainda há muito trabalho a ser feito e pede para você digitar a realidade a que deseja ir: ")
if escolha2!="realidade 1" and escolha2!="realidade 2" and escolha2!="realidade 3":
    while escolha2!="realidade 1" and escolha2!="realidade 2" and escolha2!="realidade 3":
        escolha2=input("Uma mensagem aparece dizendo 'Não Disponível. Tente novamente: ")
print(carregar_realidades(escolha2))
escolha2=input("De volta a garagem, Rick te diz que a aventura está quase acabando e pede para você digitar a realidade a que deseja ir: ")
if escolha2!="realidade 1" and escolha2!="realidade 2" and escolha2!="realidade 3":
    while escolha2!="realidade 1" and escolha2!="realidade 2" and escolha2!="realidade 3":
        escolha2=input("Uma mensagem aparece dizendo 'Não Disponível. Tente novamente: ")
print(carregar_realidades(escolha2))






        