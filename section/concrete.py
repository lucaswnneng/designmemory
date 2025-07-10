class RuptureException(ValueError):
    pass

class Concrete:
    def __init__(self, fck, gammac):
        self.fck = fck
        self.gammac = gammac
        self.fcd = fck / gammac
        self.fc = self.fcd * 0.85

    def getStress(self, ec):
        ecu = (
            3.5 / 1000
            if self.fck <= 50
            else (2.6 + 35 * ((90 - self.fck) / 100) ** 4) / 1000
        )
        if ec > ecu:
            raise RuptureException("Deformação ultrapassa limite de ruptura")

        nc = 1 if self.fck <= 40 else (40 / self.fck) ** (1 / 3)
        n = 2 if self.fck <= 50 else 1.4 + 23.4 * ((90 - self.fck) / 100) ** 4
        ec2 = (
            2 / 1000 if self.fck <= 50 else (2 + 0.085 * (self.fck - 50) ** 0.53) / 1000
        )

        return self.fc * nc * (1 - (1 - ec / ec2) ** n)
