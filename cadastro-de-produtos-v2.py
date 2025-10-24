#!/usr/bin/env python3
"""Cadastro de Produto"""
__version__  = "0.1.0"

produto = {
    "nome" : "caneta",
    "cor1" : "azul",
    "cor2" : "branco",
    "preco": 3.23,
    "dimensao_altura" : 12.1,
    "dimensao_largura": 0.8,
    "em_estoque" : True,
    "codigo" : 45678,
    "codebar":  None,
}

compra = ("Diago", produto["nome"], 3)
total_compra = compra[2] * produto["preco"]
print(
    f"O cliente {compra[0]} comprou {compra[1]}"
    f"e pagou o Total de {total_compra}"
)
