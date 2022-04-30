from DP911.Functions import describe
from DP911.Exceptions import OutOfRangeError
import winsound
import loguru
import re

"03 NN MM"
introduce = describe("03", 1, 1)

pitches = {
    1: 261,
    2: 293,
    3: 329,
    4: 349,
    5: 391,
    6: 440,
    7: 493,
    8: 523,
    9: 587,
    10: 659,
    11: 698,
    12: 783,
    13: 880,
    14: 987,
    15: 1046,
    16: 1174,
    17: 1318,
    18: 1396,
    19: 1567,
    20: 1760,
    21: 1975
}

lengths = {
    0: 250,
    1: 500,
    2: 750,
    3: 1000,
    4: 1500,
    5: 2000,
    6: 3000,
    7: 4000,
    8: 3200,
    9: 6400,
}


def main(pitch: str or int, length: str or int):
    if int(pitch) >= 10:
        pitch = int(pitch)-10

    if not (0 <= pitch <= 21):
        raise OutOfRangeError('00-07 11', '18 21-27')

    if not re.match(r"^[0][1-9]$", str(length)):
        raise OutOfRangeError('01', '09')

    length = int(length)

    if not (pitch == "00"):
        try:
            winsound.Beep(pitches[pitch], lengths[length])
        except RuntimeError:
            loguru.logger.warning("系统无法播放声音，请检查扬声器")
