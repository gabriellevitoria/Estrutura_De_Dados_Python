# -*- coding: utf-8 -*-
"""Revisao_Lists_06_Strings.ipynb

Automatically generated by Colaboratory.

# **Revisão de 'list' - Parte 6: Lista x String**
"""

# 06.1 - Uma string é implicitamente uma lista
print("06.1 - Uma string é implicitamente uma lista")
str_1 = 'Alô, Carlos !'
for c in str_1:
	print(c,' ',end='')
print('\n')

# 06.2 - Uma string pode ser explicitamente uma lista
print("06.2 - Uma string pode ser explicitamente uma lista")
str_2 = 'Alô, Carlos !'
lst_2 = list(str_2)
print(lst_2)
print('\n')

# 06.3 - Acesso a um caracter da string como um elemento de uma lista
print("06.3 - Acesso a um caracter da string como um elemento de uma lista")
str_3 = 'Alô, Carlos !'
c_ini = str_3[0]
c_fim = str_3[-1]
print("Sendo a string: '" + str_3 + "', o primeiro caracter é '" + c_ini + "' e o último é '" + c_fim + "'.")
print('\n')

# 06.4 - Acesso a um trecho da string ('substring') como um trecho de uma lista ('slice')
print("06.4 - Acesso a um trecho da string como um trecho de uma lista ('slice')")
str_4 = 'Alô, Carlos !'
t_ini = str_4[:4]
t_fim = str_4[-4:]
print("Sendo a string: '" + str_4 + "', o primeiro trecho é '" + t_ini + "' e o último é '" + t_fim + "'.")
print('\n')

# 06.5 - Identificação de presença de uma 'substring' na string por meio de operador de lista
print("06.5 - Identificação de presença de uma 'substring' na string por meio de operador de lista")
str_5 = 'O professor Carlos é professor de Estruturas de Dados e de Inteligência Artificial.'
encontrou     = 'professor'  in str_5
nao_encontrou = 'Tecnologia' in str_5
print("A string é: '" + str_5 + "'")
print("A busca por 'professor'  resultou",encontrou)
print("A busca por 'Tecnologia' resultou",nao_encontrou)
print('\n')

# 06.6 - Identificação de posição de uma 'substring' na string por meio de operador de lista
print("06.6 - Identificação de posição de uma 'substring' na string por meio de operador de lista")
str_6 = 'O professor Carlos é professor de Estruturas de Dados e de Inteligência Artificial.'
pos_primeira = 'professor'  in str_5
pos_ultima   = 'Tecnologia' in str_5
print("A string é: '" + str_6 + "'")
print("A primeira substring 'professor' começa na posição",str_6.find('professor'))
print("A ultima   substring 'professor' começa na posição",str_6.rfind('professor'))
print('\n')