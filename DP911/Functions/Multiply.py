from DP911.Functions import describe
from DP911.Registers.Variables import Variable


"25 NN MM"
introduce = describe("25", 1, 1)


def main(multiplicand: str or int, multiplier: str or int):
    multiplicand_data = Variable.read(multiplicand)
    multiplier_data = Variable.read(multiplier)

    Variable.save(multiplicand, int(multiplicand_data*multiplier_data))
