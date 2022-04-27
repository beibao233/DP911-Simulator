import re


def ishex(number: str or int):
    """
    检查是否是hex str / 将 int hex 转换成 int
    :param number: 以0x开头的hex str/hex str | int hex
    :return: 0x返回True, 仅hex开头增加0x。不是hex则返回False。 | 返回 int
    """
    if isinstance(number, int):
        return int(number)

    if isinstance(number, str):
        if re.match(r"^[0-9A-Fa-f]+$", number):
            number = int("0x"+number, 16)
            return number
        if re.match(r"^0x[0-9A-Fa-f]+$", number):
            return True

    return False


def x16n(number: int or str):
    """
    格式化hex str
    :param number: hex str / int
    :return: int转为hex str, 0x开头去掉0x转为大写hex str。仅hex str增加0x
    """

    if isinstance(number, str):
        result = ishex(number)

        if result:
            number = number.upper().replace("0X", "", 1)
            return number
        elif isinstance(result, str):
            number = "0x"+number
            return number

    if isinstance(number, int):
        number = hex(number)
        return number
