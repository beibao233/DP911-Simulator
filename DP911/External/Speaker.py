import loguru
import winsound

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


def main(data: tuple, web_mode: bool = False):
    if not web_mode:
        if not (data[0] == "00"):
            try:
                winsound.Beep(pitches[data[0]], lengths[data[1]])
            except RuntimeError:
                loguru.logger.warning("系统无法播放声音，请检查扬声器")

    return f"播放时间为{lengths[data[1]]}的{pitches[data[0]]}Hz声音"
