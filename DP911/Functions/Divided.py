from DP911.Functions import describe
from DP911.Registers.Variables import Variable


"26 NN MM"
introduce = describe("26", 1, 1)


def main(dividend: str or int, divisor: str or int):
    dividend_data = Variable.read(dividend)
    divisor_data = Variable.read(divisor)

    Variable.save(dividend, dividend_data//divisor_data)
    Variable.save(divisor, dividend_data % divisor_data)
