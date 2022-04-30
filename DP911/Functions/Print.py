from DP911.Functions import describe
from DP911.Exceptions import OutOfRangeError
from DP911.Registers.Variables import Variable

import re

"05 NN MM"
introduce = describe("05", 1, 1)

bases = {
    '01': ("hex", "0x", 4, 4),
    '02': ("", "", 5, 3),
    '03': ("oct", "0o", 6, 3),
    '04': ("bin", "0b", 16, 4)
}


def main(var_name: str or int, base: str or int):
    if not re.match(r"^[0][1-4]$", str(base)):
        raise OutOfRangeError('01', '04')

    unprocessed = list(eval(f"str({bases[base][0]}({Variable.read(var_name)})).replace('{bases[base][1]}', '', 1)"))

    for _ in range(bases[base][2]-len(unprocessed)):
        unprocessed.insert(0, '0')

    for i in range(int(bases[base][2]/bases[base][3])):
        unprocessed.insert((i*bases[base][3])+i, ' ')

    if unprocessed[0] == ' ':
        unprocessed.pop(0)

    processed = ''.join(unprocessed)

    print(processed)
