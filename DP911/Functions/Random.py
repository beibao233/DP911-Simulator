from DP911.Functions import describe
from DP911.Registers.Variables import Variable
import random

"22 MM"
introduce = describe("22", 1)


def main(var_name: str or int):
    Variable.save(var_name, random.randint(0, 255))
