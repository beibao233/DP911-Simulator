from DP911.Exceptions.Errors import OutOfRangeError
from DP911.Tools import ishex, set_range
from DP911.Functions import describe
import re

"02 NN,NN MM"
introduce = describe("02", 2, 1)


def main(long: str or int, unit: str or int):
    if not re.match(r"^[0][0-4]$", str(unit)):
        raise OutOfRangeError('00', '04')

    set_range(0x0, ishex(long), 0xFFFF)

    return (long, unit), 'Sleep'
