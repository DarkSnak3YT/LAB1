def subtrair(x: float, y: float) -> float:
    return x - y

def somar (x: float, y: float) -> float:
    return x + y


def dividir(x: float, y: float) -> float:
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y


def multiplicar(x: float, y: float) -> float:
    return x * y

def raizquadrada( x: float) -> float:
    return x**0.5

def main():
    print("Preciso que introduza dois valores:")
    x: float = float(input("x="))
    y: float = float(input("y="))

    z: float = multiplicar(x, y)
    print("O resultado da multiplicação é:", z)

    try:
        z = dividir(x,y)
        print("O resultado da divisão é:", z)
    except ZeroDivisionError as e:
        print("Error:", e)

    m: float = somar(x, y)
    print("O resultado da soma é:", m)

    n: float = subtrair(x, y)
    print("O resultado da subtração é:", n)

    try:
        r: float = raizquadrada(x)
        print("O resultado da raiz quadrada é:", r)
    except ZeroDivisionError as e:
        print("Error:", e)



if __name__ == '__main__':
    main()
