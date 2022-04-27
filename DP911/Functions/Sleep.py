from DP911.Exceptions.Errors import OutOfRangeError
from DP911.Tools import ishex, set_range
from DP911.Functions import describe
import time
import re

"""02 NN,NN MM"""
introduce = describe("02", 2, 1)


convents = {
    '00': 100,
    '01': 10,
    '02': 1,
    '03': 60,
    '04': 360
}


def main(long: str or int, unit: str or int):
    if not re.match(r"^[0][0-4]$", str(unit)):
        raise OutOfRangeError('00', '04')

    set_range(0x0, ishex(long), 0xFFFF)

    time.sleep(ishex(long)/convents[unit])

    return None
