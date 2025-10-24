#!/usr/bin/env python3
"""Cadastro de Produto"""
__version__  = "0.1.0"

###import pprint

produto = {
    "nome" : "caneta",
    "cores" : ["azul", "branco"],
    "preco": 3.23,
    "dimensao": {
        "altura" : 12.1,
        "largura": 0.8,
    },
    "em_estoque" : True,
    "codigo" : 45678,
    "codebar":  None,
}

###compra = ("Diago", produto["nome"], 3)

cliente = {
    "nome": "Diago"
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3

}

##print(compra)

###pprint.pprint(compra)

###total_compra = compra[2] * produto["preco"]
total_compra = compra["quantidade"] * compra["produto"]["preco"]

print(
     f"O cliente {compra['cliente'] ['nome']}"
     f" comprou {compra['produto']['nome']}"
     f" e pagou o Total de {total_compra}"
)
