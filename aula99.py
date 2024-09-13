"""
#Introdução aos packages em python
from sys import path
import aula99_package.modulo
from aula99_package.modulo import soma, oi
from aula99_package import modulo

print(soma(1, 2)) #Com from
print(oi)
print(aula99_package.modulo.soma(1,3)) #Com import
print(modulo.soma(3,2)) #Import mod
#print(*path, sep='\n')
"""

"""
#O ponto de vista do __main__ pode te confundir em módulos e pacotes
from aula99_package.modulo import soma
print(soma(1,2))

"""

""""""
#__init__.py é um arquivo de inicialização dos packages
from aula99_package import falaOI
falaOI()