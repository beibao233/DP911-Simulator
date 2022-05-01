from DP911.Functions import describe
from DP911.Exceptions import OutOfRangeError
import re

"03 NN MM"
introduce = describe("03", 1, 1, True)


def main(pitch: str or int, length: str or int):
    if int(pitch) >= 10:
        pitch = int(pitch)-10
    else:
        pitch = int(pitch)

    if not (0 <= pitch <= 21):
        raise OutOfRangeError('00-07 11', '18 21-27')

    if not re.match(r"^[0][1-9]$", str(length)):
        raise OutOfRangeError('01', '09')

    length = int(length)

    return (pitch, length), "Speaker"
