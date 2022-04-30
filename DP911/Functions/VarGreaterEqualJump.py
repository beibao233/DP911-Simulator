from DP911.Tools import ishex, set_range
from DP911.Functions import describe
from DP911.Registers.Variables import Variable


"23 NN MM,MM"
introduce = describe("23", 1, 2)


def main(var_name: str or int, address: str or int):
    set_range(0x0, ishex(address), 0xFFFF)

    if ishex(Variable.read(var_name)) >= Variable.read(Variable.temp_register):
        return ishex(address)
