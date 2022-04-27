from DP911.Functions import describe
from DP911.Registers.Variables import Variable


"0C NN"
introduce = describe("0C", 1, 0)


def main(var_name: str or int):
    number = list(bin(Variable.read(var_name)))

    for bit in range(2, len(number)):
        if (not int(number[bit])) is True:
            number[bit] = '1'
        else:
            number[bit] = '0'

    Variable.save(var_name, int(''.join(number), 2))
