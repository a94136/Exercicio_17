"""Leitura de pontos do plano.

Este módulo reúne as funções que pedem coordenadas ao utilizador.
Um ponto é representado por um tuplo ``(x, y)`` com dois valores reais.

:Autores: Pedro e Ana
:Versão: 0.1
"""

def le_ponto_2d(mensagem="Ponto"):
    """Lê do teclado as coordenadas de um ponto do plano.
    
    A função pede primeiro a abcissa e depois a ordenada. Aceita a vírgula
    como separador decimal, por isso ``2,5`` e ``2.5`` dão o mesmo valor.
    Quando o texto escrito não é um número, a pergunta repete-se.
    
    :param mensagem: texto que identifica o ponto a pedir
    :type mensagem: str
    :return: as coordenadas do ponto, pela ordem ``(x, y)``
    :rtype: tuple[float, float]
    """
    x = _le_real(f"{mensagem}, x: ")
    y = _le_real(f"{mensagem}, y: ")
    return (x, y)

def _le_real(pergunta):
    """Pede um número real até o utilizador escrever um valor válido."""
    while True:
        texto = input(pergunta).strip().replace(",", ".")
        try:
            return float(texto)
        except ValueError:
            print("Valor inválido. Escreva um número, por exemplo 2.5")
            