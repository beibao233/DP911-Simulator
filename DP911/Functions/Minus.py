from DP911.Functions import describe
from DP911.Registers.Variables import Variable

"07 NN MMMM"
introduce = describe("07", 1, 2)


def main(var_name: str or int, data: str or int):
    Variable.minus(var_name, data)
