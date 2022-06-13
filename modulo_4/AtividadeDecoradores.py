'''
Uma pessoa do seu time de desenvolvimento está escrevendo várias funções que calculam diferentes formas
de gerar juros.
Ela pediu para você escrever um decorator chamado decorator_imprimir, que será usado para a função
chamada imprima os parâmetros: capital, taxa e tempo, além do resultado da função.

Com isso, será criada uma função decoradora (decorator) chamada decorator_imprimir que, ao ser usada com
qualquer função parecida com a juros_simples (isto é, uma função que receba 3 parâmetros – capital, taxa, tempo),
seja retornado um valor numérico correspondente ao juros.

'''

def decorador_imprimir(funcao):
    def imprima(capital,taxa,tempo):
        r = funcao(capital,taxa,tempo)
        print (f'Capital: {capital} Taxa: {taxa} Tempo: {tempo}\n'
               f'Resultato: {r}'.upper())
    return imprima

@decorador_imprimir
def juros_simples(capital, taxa, tempo):
    return capital * (taxa/100) * tempo

#Programa Principal - chamando a função juros_simples:

juros_simples(1000,5,6)



