from DP911.Registers import Code
from DP911.Interpreter import run

from tkinter import *
import tkinter.filedialog

import atexit
import loguru

root = Tk()
root.withdraw()
root.iconbitmap('./Resource/logo.ico')


filenames = tkinter.filedialog.askopenfilenames(title="请选择程序文件！")
if len(filenames) != 0:
    for filename in filenames:
        with open(filenames[0]) as code:
            run(Code.sim_storage_space(code.read()))
else:
    loguru.logger.warning("未选择文件！")


@atexit.register
def exit_msg():
    loguru.logger.info("程序正常结束！")
