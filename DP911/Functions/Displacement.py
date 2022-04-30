from DP911.Functions import describe
from DP911.Registers.Variables import Variable
from DP911.Exceptions import OutOfRangeError
import re


"14 NN MM"
introduce = describe("14", 1, 1)


def main(save_address: str or int, mode: str or int):
    if not re.match(r"^[0][0-1]$", str(mode)):
        raise OutOfRangeError('00', '01')

    unprocessed = list(bin(Variable.read(save_address)).replace('0b', ''))

    for _ in range(16-len(unprocessed)):
        unprocessed.insert(0, '0')

    if int(mode) == 1:
        unprocessed.insert(0, unprocessed.pop())
    else:
        unprocessed.insert(len(unprocessed), unprocessed[0])
        unprocessed.remove(unprocessed[0])

    Variable.save(save_address, int(''.join(unprocessed), 2))
