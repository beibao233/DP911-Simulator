from DP911.Tools import x16n, ishex, set_range


def hex_format_fixer(register_name: int or str, data: int or str):
    if isinstance(register_name, str) and ishex(register_name):
        register_name = x16n(register_name)

    if isinstance(data, str):
        data = x16n(data)

    return register_name, data


class Variables:
    """
    数字寄存器，模拟DP911 00-0F
    默认临时寄存器设定为 00
    """

    def __init__(self):
        self.temp_register: int = 0x0
        for number in range(16):
            exec(f"self._{hex(number)} = 0x0")

    def __temp_register(self, register_name: str):
        if set_range(0x0, ishex(register_name), 0xF):
            self.temp_register = ishex(register_name)
            return True

    def save(self, register_name: int or str, data: int or str):
        """
        保存hex str/int 到寄存器内
        :param register_name: hex str：00-0F / int：0-15
        :param data: hex str: 0000 - FFFF
        :return:
        """
        register_name, data = hex_format_fixer(register_name, data)

        set_range(0x0, ishex(data), 0xFFFF)

        data = ishex(data)

        if data is False:
            data = 0

        if self.__temp_register(register_name=register_name):
            exec(f"self._{x16n(self.temp_register)} = {data}")

    def add(self, register_name: int or str, data: int or str):
        """
            在寄存器原有基础上增加（若结果大于255 = 结果 - 65535）
            :param register_name: hex str：00-0F / int：0-15
            :param data: hex str: 0000 - FFFF
            :return:
        """
        register_name, data = hex_format_fixer(register_name, data)

        set_range(0x0, ishex(data), 0xFFFF)

        if self.__temp_register(register_name=register_name):
            exec(f"self._{x16n(self.temp_register)} = self._{x16n(self.temp_register)} + {ishex(data)} - 65535 if "
                 f"self._{x16n(self.temp_register)} + {ishex(data)} > 65535 else "
                 f"self._{x16n(self.temp_register)} + {ishex(data)}")

    def minus(self, register_name: int or str, data: int or str):
        """
            在寄存器原有基础上减去（若结果小于0 = 65535 - abs(结果)）
            :param register_name: hex str：00-0F / int：0-15
            :param data: hex str: 0000 - FFFF
            :return:
        """
        register_name, data = hex_format_fixer(register_name, data)

        set_range(0x0, ishex(data), 0xFFFF)

        if self.__temp_register(register_name=register_name):
            exec(f"self._{x16n(self.temp_register)} = 65535 - abs(self._{x16n(self.temp_register)} - {ishex(data)}) if "
                 f"self._{x16n(self.temp_register)} - {ishex(data)} < 0 else "
                 f"self._{x16n(self.temp_register)} - {ishex(data)}")

    def read(self, register_name: int or str):
        """
        保存hex str/int 到寄存器内
        :param register_name: hex str：00-0F / int：0-15
        :return:
        """
        if isinstance(register_name, str) and ishex(register_name):
            register_name = x16n(register_name)

        if self.__temp_register(register_name=register_name):
            return eval(f"self._{x16n(self.temp_register)}")


Variable = Variables()
