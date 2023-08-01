#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import datetime

# Dados

cumprimentos = ["ola", "eai", "oi", "bom dia", "boa tarde", "boa noite", "yo", "hey", "io", "salve salve", "salve", "rascol", "oi rascol", "ola rascol", "eai rascol"]
cumprimentos_respostas = ["Oi! :)", "Olá! :)", "Como posso ajudar? >_<", "Eai! XD", "Oi! Estou feliz por você estar aqui. <3", "Yo! O que posso fazer por você hoje? :)", "Manda a braba meu patrão! :D", "Estou a sua disposição! :P", "Oi! O que vai ser hoje? :)", "Qual sua ordem? :)", "Há! Você apareceu! O que vamos explodir hoje? >:)", "Salve salve meu mestre! B)"]

perguntas_status = ["tudo bem", "como vai", "como voce esta", "esta tudo bem com voce"]
pergunta_status_respostas = ["Estou bem sim. :)", "Estou melhor agora com a sua compania. :)", "Estou indo bem. :)", "Estou legal. :)"]

perguntas_nome = ["qual e o seu nome","qual o seu nome", "qual seu nome", "como se chama", "voce se chama","como voce se chama", "quem e voce", "voce e quem", "eu te conheço", "conheço voce"]
perguntas_nome_respostas = ["Meu nome é Rascol e eu sou uma assistente de terminal! :P", "Meu nome é Rascol. :)", "Meu nome é Rascol! :D", "Se você não me conhece, meu nome é Rascol! :)", "Rapaiz, me chamam de Rascol. :P"]

perguntas_criador = ["quem te criou", "qual e o nome do cara que te fez", "quem te programou", "quem te desenvolveu", "voce foi feita por quem", "quem te fez", "voce foi feito por quem"]
perguntas_criador_respostas = ["Eu fui criada por um cara chamado Isac. :)", "O nome dele era Isac e ele gostava muito de fazer códigos. :P", "José \"Rasquirrel\" Isac. Ele gostava de sistemas operacionais Linux, programar em Python, coisas difíceis, complexidade, estudar o funcionamento dos computadores, gostava de bolo de chocolate\naprender coisas novas, ser hacker e gostava muito do outono e de uma garotinha em especial.\nEle está em algum lugar...", "O apelido dele era Rasquirrel, mas o nome verdadeiro dele era Isac. :)", "O nome dele é Isac, e ele foi a pessoa mais incrivel que eu já conheci. :)", "O nome dele é Isac, e ele era um amor de pessoa! <3"]

perguntas_proposito = ["por que voce existe", "qual o seu proposito", "qual seu proposito", "qual seu ojetivo", "qual o seu objetivo", "por que voce esta aqui", "por que voce foi criada",  "por que voce foi desenvolvida", "por que tu existe", "por que voce foi programada"]
perguntas_proposito_respostas = ["Eu existo primordialmente porque meu criador queria presentear o querido amigo dele, Carlos Gabriel, no\nseu aniversario de 18 anos com um presente único: uma I.A assistente de terminal! :D", "O cara que me criou era apaixonado pela linha de comando, ai para se divertir, ele me criou! Vê se pode! >:)", "O cara que me criou queria uma companhia no seu terminal... talvez meu objetivo seja esse... <3", "O meu programador não encontrou uma assistente de terminal decente, ai ele me criou, e eu estou aqui. Talvez esse seja meu propósito. :)"]

despedidas = ["tchau", "tchal", "bye", "bye bye", "ate mais", "flw", "adeus", "good bye", "sayonara", "see you later", "ate depois", "ate qualquer hora", "ate qualquer dia"]
despedidas_respostas = ["Tchau! :)", "A gente se vê! :)", "Obrigada por hoje, até mais! :P", "Hey, muito obrigada por ter interagido comigo. Até depois. <3", "Você é legal, tchau! :D", "Se cuida viu? <3", "Cuidado ao rodar comandos como super usuário! Tchau! :)", "Tchau e nada de ir dormir depois de 00:00 viu? :>"]


# Functions

def hora_atual():
    # Essa função pega a hora de agora

    tempo_atual = datetime.datetime.now()

    tempo_formatado = tempo_atual.strftime("%H:%M")

    return tempo_formatado


def limpar_frase(frase):
    # Esta função remove os seguintes caracteres de determinada frase 

    caracteres_ignorados = ['!', '.', '?', ',' ';', ':']
    frase_list = list(frase)
    for caractere in frase_list:
        if caractere in caracteres_ignorados:
            frase_list.remove(caractere)

    nova_frase = ''.join(frase_list)
    
    return nova_frase


def rascol_resposta(respostas: list):
    # Esta função fornece uma resposta aleatoria para uma pergunta

    tamanho_lista_respostas = len(respostas)
    numero_aleatorio = random.randint(0, tamanho_lista_respostas-1)
    print(f"{hora_atual()} Rascol -> {respostas[numero_aleatorio]}")
    
# Art
ascii_art = """
            
                      WWWWWWWWWW                 dCCb      
                     WCCCCCCCCCCW               dC  Cb
                    WCCCCC+++CCCCW              RC  Cb    daab     dssss    dCCCCb     dooob    FF
                    WCCCC+++++CCCWbb            RCCb     da  ab   cc       dCC   Cb   do   ob   FF
                    WCCCCC+++CCCC!!!!!!         RC H     FaaaaJ    $$$     OC         Oc   cO   FF
                     WCCCCCCCCCC!!!!!!!!        RC CH    Fa  aJ      $$b   dCC   Cb   dc   cb   FF
                      WCCCCCCCCC!!!!!!          RC CH    Fa  aJ   ssssb     dOCCCb     dooob    FFFFFF
                    WMFFFFFFFFFddd
                  WMFFFFFFFFFFWW
                WMFFFFFFFFFFFFWW                           \x1B[3mSua assistente de terminal\x1B[0m.
              WMFFFFFFFFFFFMFWWWW                                   Alpha 0.2 
             MWWFFFEEEEEEFMFFFFW
           MWFFFFEEEEEEEEMFFFWM
        MMWFFFFFFMEEEEEMMFFFW
     WWWFFFFFFFFFFFFFFFFFFMW
      WWWFFFFFFFFFFFFFFFFW
         MMMMMMMMMMMMMMM

"""

programa_rodando = True

print(ascii_art)
while programa_rodando:
    frase = str(input(f'{hora_atual()} Hacker -> ')).lower().strip()

    frase = limpar_frase(frase)

    if frase in perguntas_status:
        rascol_resposta(pergunta_status_respostas) 
    elif frase in cumprimentos:
        rascol_resposta(cumprimentos_respostas)
    elif frase in perguntas_nome:
        rascol_resposta(perguntas_nome_respostas)
    elif frase in perguntas_criador:
        rascol_resposta(perguntas_criador_respostas)
    elif frase in perguntas_proposito:
        rascol_resposta(perguntas_proposito_respostas)
    elif frase in despedidas:
        rascol_resposta(despedidas_respostas)
        programa_rodando = False
    else:
        print("...;-; AAAAA me desculpa eu não entendi o que você quis dizer. Tente de novo por favor!!!")
        print("Talvez tenha faltado um artigo, ou algo a mais, eu não sei ;-;")
