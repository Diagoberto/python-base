#!/usr/bin/env python3
""" Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente.

Como usar:

Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_BR

Execucao:

    pytho3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.2"
__author__  = "Diago"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US" )[:5] 

# sets (Hash Table) - 0(1) - constante
# dict (Hash Table) 

msg = { 
    "en_US": "Hello,World!",
    "pt_BR": "Ola,Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

print(msg[current_language]) 
