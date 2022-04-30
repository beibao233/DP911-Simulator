from DP911.Functions import describe
from DP911.Tools import set_range, ishex

import loguru

"19 NN"
introduce = describe("19", 1)


def main(number: str or int):
    set_range(0x0, ishex(number), 0xFF)

    loguru.logger.info("程序正常结束！（清程后无可执行代码）")
    exit()

