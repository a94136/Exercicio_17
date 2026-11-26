"""Programa de demonstração das funções de geometria.

Pede quatro pontos e o nome de uma figura. Depois indica se o quarto
ponto pertence à figura definida pelos três primeiros.

:Autores: Pedro e Ana
:Versão: 0.1
"""
from figuras import pertence_figura
from pontos import le_ponto_2d
from retas import ordenada_na_reta, pontos_para_reta

def main():
    """Executa a demonstração no terminal."""
    p1 = le_ponto_2d("Ponto 1")
    p2 = le_ponto_2d("Ponto 2")
    p3 = le_ponto_2d("Ponto 3")
    p = le_ponto_2d("Ponto a testar")
    
    try:
        m, b = pontos_para_reta(*p1, *p2)
        print(f"Reta por P1 e P2: y = {m:g}x + {b:g}")
        y = ordenada_na_reta(m, b, p[0])
        print(f"Nessa reta, x = {p[0]:g} dá y = {y:g}")
    except ValueError as erro:
        print(f"Reta por P1 e P2: {erro}")
    figura = input("Figura (circulo ou triangulo): ")
    try:
        if pertence_figura(figura, p1, p2, p3, p):
            print("O ponto pertence à figura.")
        else:
            print("O ponto não pertence à figura.")
    except ValueError as erro:
        print(f"Erro: {erro}")


if __name__ == "__main__":
    main()