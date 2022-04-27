from DP911.Exceptions import WrongTypeArgument
from DP911.Tools.Hex import ishex


def __typecheck(para, want: type = None):
    """
    检查是否为想要的类型
    :param para: 参数
    :param want: 期望类型
    :return: 原参数参数或报错
    """

    if want is None:
        para = ishex(para)

    if para is None or isinstance(para, want):
        return para
    else:
        if want is None:
            WrongTypeArgument(type(para), "Hex str")
        WrongTypeArgument(type(para), want)
