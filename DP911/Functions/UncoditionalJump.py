from DP911.Tools import ishex, set_range
from DP911.Functions import describe

"""10 MM,MM"""
introduce = describe("10", 2)


def main(address: str or int):
    set_range(0x0, ishex(address), 0xFFFF)

    return ishex(address)
