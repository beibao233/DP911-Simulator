from DP911.Functions import describe
from DP911.Tools import ishex, x16n
from DP911.Registers.Variables import Variable


"27 NN MM"
introduce = describe("27", 1, 1)


def main(combine: str or int, reference: str or int):
    combine_data = Variable.read(combine)
    reference_data = Variable.read(reference)

    data = ''.join(list(x16n(x16n(combine_data)))[2:4] + list(x16n(x16n(reference_data))[2:4]))

    Variable.save(combine, ishex(data))
