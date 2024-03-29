# -*- coding: utf-8 -*-
"""Lab_ArranjosDinamicos_ANTES_AULA.ipynb

Automatically generated by Colaboratory.

# **Lab. *Arrays* dinâmicos em Python**

### Objetivo específico desta aula prática
Apresentar o objeto **`list`** da linguagem Python.

##**Suporte Teórico: Estruturas de Dados Lineares**##
 
###**1.**###
"""
# IDENTIFICAÇÃO
# -------------
nome = 'Gabrielle Vitória'
print("Meu nome é:",nome)

"""## Atividade 1
Escreva um programa Python que cria um arranjo dinâmico (lista) chamado `nomes`, inicialmente vazio. Em seguida, implemente as ações:


1.   Preencher o arranjo `nomes` com 10 nomes de pessoas em qualquer ordem, utilizando quaisquer das maneiras de inserção de elementos acima apresentadas.
2.   Exibir os nomes armazenados no arranjo.
1.   Ordenar fisicamente os nomes armazenados no arranjo e exibi-los depois disso.
2.   Colocar os nomes armazenados na ordem física exatamente contrária e exibi-los depois disso.

"""

# ATIVIDADE 1
print(40*'-') 
print('Atividade 1')
print(40*'-') 

nomes = []
print('1.Preencher a lista com 10 nomes em ordem aleatória')
nomes.extend(['Gabrielle', 'Victor', 'Isis', 'Felipe', 'Maria', 'Eva', 'Kauan' , 'Mario' , 'Manoel', 'Ana'])
print('\n')

print('2.Exibir os nomes armazenados na lista: ')
print(nomes)
print('\n')


print('3.Ordenar fisicamente os nomes da lista e exibi-los: ')

print('Lista Original: ', nomes)
nomes.sort()
print( 'Lista Ordenada: ', nomes)
print('\n')


print('4.Colocar os nomes ordenados anteriormente em uma ordem física contrária')

print('Lista em Ordem alfabetica: ', nomes)
nomes.sort(reverse=True)
print('Lista em ordem contrária: ', nomes)
print('\n')







"""## Atividade 2
Mestre Yoda é célebre por organizar as palavras de suas frases em sentido geralmente diferente daquele que entendemos como ‘direto’.
Considere a frase: *“A vida é bela, porém precisa ser plenamente vivida.”*

Escreva um programa Python que:

1.   monta uma lista com as palavras originais;
2.   modifica suas posições nessa lista (ou em uma lista nova) para que elas fiquem no estilo Mestre Yoda; e
2.   imprime a lista para mostrar a frase modificada.

"""

# ATIVIDADE 2
print(40*'-')  
print('Atividade 2')
print(40*'-') 

print('1. Montar uma lista com as palavras originais')

frase_Original = "A vida é bela, porém precisa ser plenamente vivida." #variavel com a frase original
palavras = frase_Original.split() #lista que armazena as palavras da frase

print(palavras)
print('\n')

print('2. Modificar suas posições para que fiquem no estilo Mestre Yoda e imprimir para mostrar a frase modificada')

palavras_mestre = [] #lista para armazenar as palavras

for i in range(len(palavras) -1, -1, -1): #for para que armazene as letras na ordem contrária
    palavras_mestre.append(palavras[i])

print(palavras_mestre) #print da frase modificada 
print('\n')

print('3. Mostrar a frase modificada')
7
frase_modificada = ' '.join(palavras_mestre) #transformando a lista em uma string

print(frase_modificada)

print('\n')




"""## Atividade 3
Um exemplo de uma cadeia (*string*) de DNA de tamanho 21 que contém os símbolos `‘A’`, `‘C’`, `‘G’` e `‘T’` é:

`“ATGCTTCAGAAAGGTCTTACG”`.

Escreva um programa Python que, a partir de uma cadeia `str_DNA` de comprimento máximo 1000, monta uma lista com 4 números inteiros, 
indicando respectivamente as quantidades de ocorrências dos símbolos `‘A’`, `‘C’`, `‘G’` e `‘T’` em `str_DNA`.

Por exemplo, sendo `str_DNA`:
`“AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC”`,

a lista montada para este exemplo será: `[20,12,17,21]`.
"""

# ATIVIDADE 3
print(40*'-') 
print('Atividade 3')
print(40*'-') 

import random #importando biblioteca

#criar uma string aleatória com os caracteres A C G T
caracteres = ['A' , 'C' , 'G' , 'T']
str_DNA = ' '.join(random.choice(caracteres) for i in range(1000))

#mostrar quantas vezes cada elemento foi repetido dentro da string

a = 0
c = 0
g = 0
t = 0

for caracteres in str_DNA:
    if caracteres == 'A':
        a = a+1

    elif caracteres == 'C':
        c = c+1
    elif caracteres == 'G':
        g = g+1
    elif caracteres == 'T':
        t = t+1

contagem = [ a , c , g , t ]

print(contagem)


"""## Desafio (não será avaliado)
Escreva um programa Python que imprime todos os números primos menores que 1000.

Sugestão:
1.	Crie uma lista de números primos, inicialmente vazia.
2.	Utilize dois comandos for aninhados (“um dentro do outro”). O *loop* externo percorre os números entre 2 e 999. O *loop* interno percorre a lista atual de números primos.
3.	Se o número do *loop* externo não é divisível por nenhum dos números primos já encontrados, então ele (o externo) é primo e deve ser impresso e adicionado à lista de números primos (por meio de `append`).

"""

# DESAFIO
print(40*'-') 
print('Desafio -> Tentativa 01')
print(40*'-') 

#objetivo : mostrar todos os números primos menores que 1000

numeros_primos = [] #lista de números primos

for n in range (2,1000): #loop que faz a leitura de 2 até 999

    for primo in numeros_primos: #loop que percorre a lista atual de números primos
        if n % primo == 0: #se não for divisivel por nenhum dos números primos identificamos que não é primo
            break
        else: #caso seja primo será adicionado a lista e mostrado na tela
            numeros_primos.append(n)
            print(n)

print(numeros_primos)


print(40*'-') 
print('Desafio -> Tentativa 02')
print(40*'-') 


primos = [] #lista vazia de números primos 

for n in range(2,1000): #loop que percorre do número 2 até o 999

    is_primo = True #variável que verifica se o numero testado é primo ou nãp

    for primo in primos: #loop que verifica se é divisivel por algum número primo já encontrado

        if n %primo == 0:
            is_primo = False
            break

    if is_primo: #se for primo é adicionado a lista
        primos.append(n)

print(primos)