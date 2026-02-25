import soma
import subtracao
import multiplicacao
import divisao
import raizQuadrada


def main():
    print("Preciso que introduza dois valores:")
    x: float = float(input("x="))
    y: float = float(input("y="))

    z: float = multiplicacao.multiplicar(x, y)
    print("O resultado da multiplicação é:", z)

    try:
        z = divisao.dividir(x,y)
        print("O resultado da divisão é:", z)
    except ZeroDivisionError as e:
        print("Error:", e)

    m: float = soma.somar(x, y)
    print("O resultado da soma é:", m)

    n: float = subtracao.subtracao(x, y)
    print("O resultado da subtração é:", n)

    try:
        r: float = raizQuadrada.raizquadrada(x)
        print("O resultado da raiz quadrada é:", r)
    except ZeroDivisionError as e:
        print("Error:", e)



if __name__ == '__main__':
    main()
