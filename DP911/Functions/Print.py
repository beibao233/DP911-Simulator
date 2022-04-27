from DP911.Functions import describe
from DP911.Exceptions import OutOfRangeError
from DP911.Registers.Variables import Variable

import re

"""05 NN MM"""
introduce = describe("05", 1, 1)

bases = {
    '01': ("hex", "0x"),
    '02': ("", ""),
    '03': ("oct", "0o"),
    '04': ("bin", "0b")
}


def main(var_name: str or int, base: str or int):
    if not re.match(r"^[0][1-4]$", str(base)):
        raise OutOfRangeError('01', '04')

    exec(f"print(str({bases[base][0]}({Variable.read(var_name)})).replace('{bases[base][1]}', '', 1))")

