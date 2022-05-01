from DP911.Functions import describe
from DP911.Exceptions import OutOfRangeError

import re

"05 NN MM"
introduce = describe("05", 1, 1, True)


def main(var_name: str or int, base: str or int):
    if not re.match(r"^[0][1-4]$", str(base)):
        raise OutOfRangeError('01', '04')

    return (var_name, base), "Emit"
