from typing import List

from DP911.Functions import functions as function_list
from DP911.Exceptions import FunctionNotFindError, JumpedWrongAddressError
import importlib
import sys


class initialize:
    def __init__(self, codes: list, functions: dict = function_list()):
        self.codes = codes
        self.address_count = len(codes)
        self.functions = functions


def import_module(data: initialize, address: int, skip_address: list):
    try:
        if address in skip_address:
            JumpedWrongAddressError(address, data.codes[address])
        else:
            function = data.functions[data.codes[address]]
            return function
    except KeyError:
        raise FunctionNotFindError(data.codes[address])


def format_para(data: initialize, datas_address: list, frpara: int, separa: int):
    frpara_data, separa_data = "", ""

    for r in range(frpara):
        frpara_data += data.codes[datas_address[r]]

    for r in range(separa):
        try:
            if frpara >= 2:
                separa_data += data.codes[datas_address[r + 2]]
            else:
                separa_data += data.codes[datas_address[r + 1]]
        except IndexError:
            separa_data += data.codes[datas_address[r + 1]]

    return frpara_data, separa_data


def run_module(code, frpara_data: str, separa_data: str):
    try:
        jump_address = code.main(frpara_data, separa_data)
    except TypeError:
        try:
            jump_address = code.main(frpara_data)
        except TypeError:
            jump_address = code.main()

    return jump_address


def jump(data: initialize, address: int):
    skip_address = []

    for address in range(address, data.address_count):
        if address in skip_address:  # 如果地址在跳过地址中则跳过
            continue
        else:
            function = import_module(data, address, skip_address)

            frpara, separa, name = function[0][0], function[0][1], function[1]

            datas_address = []

            for data_address in range(frpara + separa):  # 需要跳过的地址
                temp_address = data_address + address

                skip_address.append(temp_address + 1)
                datas_address.append(temp_address + 1)

            code = importlib.import_module(f"DP911.Functions.{name}")

            frpara_data, separa_data = format_para(data=data,
                                                   datas_address=datas_address,
                                                   frpara=frpara,
                                                   separa=separa
                                                   )

            jump_address = run_module(code, frpara_data, separa_data)

            if isinstance(jump_address, int):
                try:
                    jump(data=data, address=jump_address)
                except RecursionError:
                    sys.setrecursionlimit(sys.getrecursionlimit() + 1)
                    jump(data=data, address=jump_address)


def core(data: initialize):
    skip_address: List[int] = []

    for address in range(data.address_count):  # 获取所有地址
        if address in skip_address:  # 如果地址在跳过地址中则跳过
            continue
        else:
            function = import_module(data, address, skip_address)

            frpara, separa, name = function[0][0], function[0][1], function[1]

            datas_address = []

            for data_address in range(frpara + separa):  # 需要跳过的地址
                temp_address = data_address + address

                skip_address.append(temp_address + 1)
                datas_address.append(temp_address + 1)

            code = importlib.import_module(f"DP911.Functions.{name}")

            frpara_data, separa_data = format_para(data=data,
                                                   datas_address=datas_address,
                                                   frpara=frpara,
                                                   separa=separa
                                                   )

            jump_address = run_module(code, frpara_data, separa_data)

            if isinstance(jump_address, int):
                try:
                    jump(data=data, address=jump_address)
                except RecursionError:
                    sys.setrecursionlimit(sys.getrecursionlimit()+1)
                    jump(data=data, address=jump_address)
