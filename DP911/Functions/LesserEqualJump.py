from DP911.Tools import ishex, set_range
from DP911.Functions import describe
from DP911.Registers.Variables import Variable


"""1B NN,NN MM,MM"""
introduce = describe("1B", 2, 2)


def main(com_number: str or int, address: str or int):
    set_range(0x0, ishex(com_number), 0xFFFF)
    set_range(0x0, ishex(address), 0xFFFF)

    if ishex(com_number) <= Variable.read(Variable.temp_register):
        return ishex(address)
