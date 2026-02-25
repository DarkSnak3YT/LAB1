class Quadrado:
    def __init__(self, x:float):
        self.x = x
        self.res = 0


    def executar(self)->float:
        self.res = self.x ** 0.5
        return self.res