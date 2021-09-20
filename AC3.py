# -*- coding: utf-8 -*-
#Importação de modulos
import abc
from logging import raiseExceptions
from unittest import TestCase,main


#Criação de classes
class Calculadora(object):
    def calcular(self,arg1,arg2,operador):
        operacao = OperacaoFabrica().criar(operador)
        if(operacao == None):
            return 0
        else:
            resultado = operacao.executar(arg1,arg2)
            return resultado

class OperacaoFabrica(object):
    def criar(self, operador):
        if (operador == 'soma'):
            return soma()
        elif (operador == 'subtração'):
            return subtracao()
        elif (operador == 'divisão'):
            return divisao()
        elif (operador == 'multiplicação'):
            return multiplicacao()
        elif (operador == 'potenciação'):
            return potenciacao()
        elif (operador == 'resto'):
            return resto()

class Operacao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def executar(self,arg1,arg2):
        pass

#Classes de Operação
class soma(Operacao):
    def executar(self, arg1, arg2):
        resultado = arg1 + arg2
        return resultado
class subtracao(Operacao):
    def executar(self, arg1, arg2):
        resultado = arg1 - arg2
        return resultado
class divisao(Operacao):
    def executar(self, arg1, arg2):
        resultado = arg1 / arg2
        return resultado
class multiplicacao(Operacao):
    def executar(self, arg1, arg2):
        resultado = arg1 * arg2
        return resultado    
class resto(Operacao):
    def executar(self,arg1,arg2):
        resultado = arg1%arg2
        return resultado
class potenciacao(Operacao):
    def executar(self, arg1, arg2):
        resultado = arg1 ** arg2
        return resultado


#Testes
class Testes(TestCase):
    def teste_soma(self):
        calculo_soma = Calculadora()
        result = calculo_soma.calcular(2,3,'soma')
        self.assertEqual(result,5)
        
    def teste_multiplicacao(self):
        calculo_multiplicacao = Calculadora()
        result = calculo_multiplicacao.calcular(2,5,'multiplicação')
        self.assertEqual(result,10)

    def teste_divisao(self):
        calculo_divisao = Calculadora()
        result = calculo_divisao.calcular(2,4,'divisão')
        self.assertEqual(result,0.5)

    def teste_subtracao(self):
        calculo_subtracao = Calculadora()
        result = calculo_subtracao.calcular(10,50,'subtração')
        self.assertEqual(result, -40)

    def teste_potenciacao(self):
        calculo_potencia = Calculadora()
        result = calculo_potencia.calcular(4,4,'potenciação')
        self.assertEqual(result,256)
    def teste_resto(self):
        calculo_resto= Calculadora()
        result= calculo_resto.calcular(99,2,'resto')
        self.assertEqual(result,1)


banner = """CALCULADORA
Operações:\n
    Soma            +
    Subtracao       -
    Multiplicacao   x
    Divisao         /
    Potenciacao     n²
    Resto           %\n"""


def codigo():
    operacoes=['soma','subtração','multiplicação','divisão','potenciação','resto']
    operacao=input("Digite a operação desejada, de acordo com a lista acima, sem acentos e com a letra incial maiúscula:\n").lower()
    if operacao not in operacoes:
        print("Operação não reconhecida")
        codigo()
    arg1=float(input("Digite o primeiro valor:\n"))
    arg2=float(input("Digite o segundo valor:\n"))
    resultado = Calculadora().calcular(arg1,arg2,operacao)
    print ("Resultado = {0:g}".format(float(resultado)))


print(banner)
codigo()
main()
