#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 19:49:12 2019

@author: gabrielsalvatorbenatar
"""
print('Você escolheu fugir, digite aonde quer ir.(Frase no parenteses)')
print('Você está fugindo e têm duas opções: Beco escuro a sua esquerda.(beco) ou Pular portão a sua direita (pular)')
escolha=input('Para onde voê quer ir? ')
if escolha!="beco" and escolha!="pular":
    while escolha!="beco" and escolha!="pular":
        escolha=input("Operação Inválida, digite novamente: ")
if escolha=='beco':
    print('Você estava correndo e escorregou em uma poça ácida')
    #game over
else:
    print('Você pulou o portão e se depara novamente com duas opções: entrar em uma porta misteriosa (porta), ou se esconder em um arbusto (arbusto)')
    if escolha!="porta" and escolha!="arbusto":
        while escolha!="porta" and escolha!="arbusto":
            escolha=input("Operação Inválida, digite novamente: ")
    if escolha == 'arbusto':
        print('Os arbustos eram venenosos!')
        #game over
    else:
        print('Você entrou em uma sala escura após passar pela porta, mas o agente continua te seguindo. Você tem dua opções: seguir em linha reta até a luz no final do corredor (luz), ou pular da janela (janela)')
        if escolha!="luz" and escolha!="janela":
            while escolha!="luz" and escolha!="janela":
                escolha=input("Operação Inválida, digite novamente: ")
        if escolha == 'luz':
            print('O prédio em que você estava desabou!')
            #game over
        else:
            print('O predio desabou, mas você conseguiu fugir a tempo, está quase lá, mas Thompson ainda está atrás de você. Novamente se depara com duas opções: Roubar um carrinho de golf (carrinho), ou pular em um bueiro e fugir pelo esgoto (esgoto)')
            if escolha == 'carrinho':
                print('Ao girar a chave, o carrinho entrou em curto circuito e explodiu!!!')
                #game over
            else: 
                print('Parabéns você seguiu o esgoto ate o final até encontrar uma saída e fugiu do agente Thompson! Agora está livre para continuar sua busca!')
         

