"""Testes de pertença de um ponto a figuras definidas por três pontos.

Em todas as funções, cada ponto é um tuplo ``(x, y)``. Os três primeiros
pontos definem a figura e o quarto é o ponto a testar. A fronteira conta
como parte da figura.

:Autores: Pedro e Ana
:Versão: 0.1
"""
import math

TOLERANCIA = 1e-9
"""Margem usada nas comparações entre números reais."""

def pertence_circulo(p1, p2, p3, p):
    """Indica se um ponto pertence ao círculo definido por três pontos.
    O círculo é o que tem por fronteira a circunferência que passa por
    ``p1``, ``p2`` e ``p3``. O ponto pertence ao círculo quando a distância
    ao centro não ultrapassa o raio.
    :param p1: primeiro ponto da circunferência
    :type p1: tuple[float, float]
    :param p2: segundo ponto da circunferência
    :type p2: tuple[float, float]
    :param p3: terceiro ponto da circunferência
    :type p3: tuple[float, float]
    :param p: ponto a testar
    :type p: tuple[float, float]
    :return: ``True`` se ``p`` estiver no interior ou na fronteira
    :rtype: bool
    :raises ValueError: se os três pontos forem colineares, caso em que
    nenhuma circunferência passa por eles
    >>> pertence_circulo((0, 0), (2, 0), (0, 2), (1, 1))
    True
    >>> pertence_circulo((0, 0), (2, 0), (0, 2), (2, 2))
    True
    >>> pertence_circulo((0, 0), (2, 0), (0, 2), (3, 3))
    False
    """
    centro, raio = _circunferencia(p1, p2, p3)
    distancia = math.dist(centro, p)
    return distancia <= raio + TOLERANCIA

def pertence_triangulo(p1, p2, p3, p):
    """Indica se um ponto pertence ao triângulo definido por três pontos.
    
    O teste verifica de que lado de cada aresta fica o ponto. O ponto está
    no triângulo quando fica do mesmo lado das três arestas, ou sobre
    alguma delas.
    
    :param p1: primeiro vértice
    :type p1: tuple[float, float]
    :param p2: segundo vértice
    :type p2: tuple[float, float]
    :param p3: terceiro vértice
    :type p3: tuple[float, float]
    :param p: ponto a testar
    :type p: tuple[float, float]
    :return: ``True`` se ``p`` estiver no interior ou na fronteira
    :rtype: bool
    :raises ValueError: se os três vértices forem colineares, caso em que
        não existe triângulo
    
    >>> pertence_triangulo((0, 0), (4, 0), (0, 4), (1, 1))
    True
    >>> pertence_triangulo((0, 0), (4, 0), (0, 4), (2, 2))
    True
    >>> pertence_triangulo((0, 0), (4, 0), (0, 4), (3, 3))
    False
    """
    if abs(_produto_vetorial(p1, p2, p3)) <= TOLERANCIA:
        raise ValueError("Os três vértices são colineares: não há triângulo.")
    d1 = _produto_vetorial(p1, p2, p)
    d2 = _produto_vetorial(p2, p3, p)
    d3 = _produto_vetorial(p3, p1, p)
    ha_negativo = min(d1, d2, d3) < -TOLERANCIA
    ha_positivo = max(d1, d2, d3) > TOLERANCIA
    return not (ha_negativo and ha_positivo)

def pertence_figura(figura, p1, p2, p3, p):
    """Indica se um ponto pertence à figura definida por três pontos.
   
    O primeiro argumento escolhe a figura. A comparação ignora maiúsculas,
    espaços nas pontas e acentos, por isso ``"Círculo"`` e ``"circulo"``
    são equivalentes.
    
    :param figura: ``"circulo"`` ou ``"triangulo"``
    :type figura: str
    :param p1: primeiro ponto que define a figura
    :type p1: tuple[float, float]
    :param p2: segundo ponto que define a figura
    :type p2: tuple[float, float]
    :param p3: terceiro ponto que define a figura
    :type p3: tuple[float, float]
    :param p: ponto a testar
    :type p: tuple[float, float]
    :return: ``True`` se ``p`` pertencer à figura escolhida
    :rtype: bool
    :raises ValueError: se ``figura`` tiver outro valor, ou se os três
        pontos forem colineares
    >>> pertence_figura("circulo", (0, 0), (2, 0), (0, 2), (2, 2))
    True
    >>> pertence_figura("triangulo", (0, 0), (2, 0), (0, 2), (2, 2))
    False
    """
    nome = figura.strip().lower().replace("í", "i").replace("â", "a")
    if nome == "circulo":
        return pertence_circulo(p1, p2, p3, p)
    if nome == "triangulo":
        return pertence_triangulo(p1, p2, p3, p)
    raise ValueError(
        f"Figura desconhecida: {figura!r}. Use 'circulo' ou 'triangulo'."
    )

def _produto_vetorial(a, b, c):
    """Devolve o produto vetorial dos vetores ``ab`` e ``ac``.
    
    O sinal indica de que lado da reta ``ab`` fica o ponto ``c``. O valor
    zero indica que os três pontos são colineares.
    """
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def _circunferencia(p1, p2, p3):
    """Devolve o centro e o raio da circunferência por três pontos."""
    (ax, ay), (bx, by), (cx, cy) = p1, p2, p3
    d = 2 * _produto_vetorial(p1, p2, p3)
    if abs(d) <= TOLERANCIA:
        raise ValueError(
            "Os três pontos são colineares: não definem uma circunferência."
        )
    a2 = ax * ax + ay * ay
    b2 = bx * bx + by * by
    c2 = cx * cx + cy * cy
    ux = (a2 * (by - cy) + b2 * (cy - ay) + c2 * (ay - by)) / d
    uy = (a2 * (cx - bx) + b2 * (ax - cx) + c2 * (bx - ax)) / d
    centro = (ux, uy)
    return centro, math.dist(centro, p1)
