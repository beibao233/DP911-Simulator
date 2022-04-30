from DP911.Functions import describe
from DP911.Registers.Variables import Variable

"21 NN MM"
introduce = describe("21", 1, 1)


def main(save_address: str or int, com_address: str or int):
    s, c \
        = \
        list(bin(Variable.read(save_address)).replace('0b', '')), \
        list(bin(Variable.read(com_address)).replace('0b', ''))

    for i in range((len(s) + len(c)) / 2):
        if s[i] + c[i] == 1:
            s[i] = 1
        else:
            s[i] = 0

    Variable.save(save_address, int(''.join(s), 2))
