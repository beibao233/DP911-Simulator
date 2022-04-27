from DP911.Functions import describe
from DP911.Registers.Variables import Variable

"04 NN MMMM"
introduce = describe("04", 1, 2)


def main(var_name: str or int, data: str or int):
    Variable.save(var_name, data)
