"""Retas do plano na forma reduzida ``y = mx + b``.

O declive ``m`` e a ordenada na origem ``b`` identificam qualquer reta
que não seja vertical.

:Autores: Pedro e Ana
:Versão: 0.1
"""

def pontos_para_reta(x1, y1, x2, y2):
    """Calcula a reta que passa por dois pontos.
    A reta fica escrita na forma ``y = mx + b``. Uma reta vertical não tem
    declive, por isso não se consegue escrever nesta forma.
    
    :param x1: abcissa do primeiro ponto
    :type x1: float
    :param y1: ordenada do primeiro ponto
    :type y1: float
    :param x2: abcissa do segundo ponto
    :type x2: float
    :param y2: ordenada do segundo ponto
    :type y2: float
    :return: o declive e a ordenada na origem, pela ordem ``(m, b)``
    :rtype: tuple[float, float]
    :raises ValueError: se os dois pontos tiverem a mesma abcissa, caso em
        que a reta é vertical ou os pontos coincidem
    
    >>> pontos_para_reta(0, 1, 2, 5)
    (2.0, 1.0)
    >>> pontos_para_reta(1, 3, 4, 3)
    (0.0, 3.0)
    """
    if x1 == x2:
        raise ValueError(
            "Os pontos têm a mesma abcissa: a reta é vertical "
            "ou os pontos coincidem."
    )
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    return (m, b)

def ordenada_na_reta(m, b, x):
    """Calcula a ordenada do ponto da reta ``y = mx + b`` com abcissa ``x``.
    
    :param m: declive da reta
    :type m: float
    :param b: ordenada na origem
    :type b: float
    :param x: abcissa do ponto pretendido
    :type x: float
    :return: a ordenada ``y`` que corresponde à abcissa ``x``
    :rtype: float
    
    >>> ordenada_na_reta(2, 1, 3)
    7
    >>> ordenada_na_reta(0.5, -1, 4)
    1.0
    """
    return m * x + b
