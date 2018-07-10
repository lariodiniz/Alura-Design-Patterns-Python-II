# -*- coding: utf-8 -*-

class Impressao(object):

    def visita_soma(self, soma):
        print ('(', end="")
        print (soma.expressao_esquerda.aceita(self), end="")
        print ('+', end="")
        print (soma.expressao_direita.aceita(self), end="")
        print (')', end="")

    def visita_subtracao(self, subtracao):
        print ('(', end="")
        print (subtracao.expressao_esquerda.aceita(self), end="")
        print ('-', end="")
        print (subtracao.expressao_direita.aceita(self), end="")
        print (')', end="")
    
    def visita_numero(self, numero):

        print(numero.avalia(), end="")
    