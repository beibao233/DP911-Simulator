from DP911.Functions import describe
from DP911.Registers.Variables import Variable

"06 NN MMMM"
introduce = describe("06", 1, 2)


def main(var_name: str or int, data: str or int):
    Variable.add(var_name, data)
