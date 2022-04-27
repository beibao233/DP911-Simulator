class OutOfRangeError(SyntaxError):
    """
    当超出设定的界线时抛出
    rmin: 最小值
    rmax: 最大值
    """
    def __init__(self, rmin: str or int, rmax: str or int):
        self.message = f"Out of range of define. The range:{rmin}-{rmax}."
        super().__init__(self.message)


class WrongTypeArgument(TypeError):
    """
    当输入参数错误时抛出
    now: 当前类型
    want: 期望类型
    """
    def __init__(self, now: type, want: str or type):
        self.message = f"Wrong Argument! Currently type is {str(now)}. Except {str(want)}"
        super().__init__(self.message)


class FunctionNotFindError(ImportError):
    """
    当输入参数错误时抛出
    now: 当前类型
    want: 期望类型
    """
    def __init__(self, function_key: str):
        self.message = f"Can't find {function_key}! Be sure it's exist or didn't miss spell!"
        super().__init__(self.message)


class JumpedWrongAddressError(ImportError):
    """
    当跳转到非方法调用代码寄存器丢出
    address: 代码寄存器号
    data: 代码寄存器存储数据
    """

    def __init__(self, address: int, data: str):
        self.message = f"Code Address {address} include with {data} was not a function address."
        super().__init__(self.message)
