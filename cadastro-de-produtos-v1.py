#!/usr/bin/env python3
"""Cadastro de Produto"""
__version__  = "0.1.0"

produto_nome = "caneta"
produto_cor1 = "azul"
produto_cor2 = "branco"
produto_preco = 3.23
produto_dimensao_altura = 12.1
produto_dimensao_largura = 0.8
produto_em_estoque = True
produto_codigo = 45678
produto_codebar = None

compra = ("Diago", produto_nome, 3)

print(
    f"O cliente {compra[0]} comprou {compra[1]}"
    f"e pagou o Total de {compra[2] * produto_preco}"
)
