from Operacoes import somar, multiplicar, subtrair, raizQuadrada, dividir


class Interacao:
    def __init__(self):
        self.res: int = 0
    def executar(self):
        print("Preciso que introduza dois valores:")
        x: float = float(input("x="))
        y: float = float(input("y="))
        s: object = somar.Somar(x, y)
        sub: object = subtrair.Subtrair(x, y)
        m: object = multiplicar.Multiplicar(x, y)
        d: object = dividir.Dividir(x, y)
        r: object = raizQuadrada.Quadrado(x)

        res = s.executar()
        print("O valor da operação somar é:", res)
        res = sub.executar()
        print("O valor da operação subtrair é:", res)
        res = d.executar()
        print("O valor da operação divisão é:", res)
        res = m.executar()
        print("O valor da operação divisão é:", res)
        res = r.executar()
        print("O valor da operação divisão é:", res)