import sys
import inspect
import pkgutil
from pathlib import Path
from importlib import import_module


def dynamic_import(abs_module_path, target_name):
  module_object = import_module(abs_module_path)
  target = getattr(module_object, target_name)
  return target