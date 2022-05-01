from DP911.Tools import ishex
import time

convents = {
    '00': 100,
    '01': 10,
    '02': 1,
    '03': 60,
    '04': 360
}


def main(data: tuple, web_mode: bool = False):
    long = ishex(data[0]) / convents[data[1]]

    if not web_mode:
        time.sleep(long)

    return f"睡眠时间(秒): {str(long)}"
