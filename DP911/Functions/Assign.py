from DP911.Functions import describe
from DP911.Registers.Variables import Variable


"1C NN MM"
introduce = describe("1C", 1, 1)


def main(save_address: str or int, read_address: str or int):
    save_address(save_address, Variable.read(read_address))
