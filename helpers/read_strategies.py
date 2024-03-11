import importlib
import inspect
import os

from helpers.base_strategy import BaseStrategy

def read_strategies(path: str):
    strategies = []

    for file in os.listdir(path):
        if not file.endswith(".py"):
            continue

        module = importlib.import_module(f"{path}.{file[: -3]}")
        for _, obj in inspect.getmembers(module, inspect.isclass):
            if issubclass(obj, BaseStrategy) and obj != BaseStrategy:
                strategies.append(obj)
                
    return strategies
