from DP911.Interpreter.Core import initialize, core
import importlib


def run(codes: list, web_mode: bool = False):
    results = core(initialize(codes, web_mode=web_mode))
    if not (results is None):
        return results
