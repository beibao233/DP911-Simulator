from DP911.Tools import ishex
from DP911.Exceptions import WrongTypeArgument
import importlib
import os


class describe:
    """
    描述自己的调用方式以及所需参数
    key: 方法键
    frpara: 第一参数所占寄存器数量 (可选)
    separa: 第二参数所占寄存器数量 (可选)
    """
    def __init__(self, key: str, frpara: int = 0, separa: int = 0):
        self.key = key
        self.frpara = frpara
        self.separa = separa


def real_functions():
    """
    Return plugins are load
    :return: list of plugins are load
    """

    real = []  # 新建现实插件名称数据

    for module in os.listdir(os.path.dirname(os.path.abspath(__file__))):  # 获取现实存在的插件名称
        if module in ["__init__.py", "__pycache__"]:
            continue

        if os.path.isdir(module):
            real.append(module)
        else:
            real.append(module.split('.')[0])

    return real


def functions():
    function_list = {}

    for function in real_functions():

        try:
            function_object = importlib.import_module(f"DP911.Functions.{function}")
        except ModuleNotFoundError:
            continue

        function_object = function_object.introduce
        function_list[function_object.key] = ((function_object.frpara, function_object.separa), function)

    return function_list
