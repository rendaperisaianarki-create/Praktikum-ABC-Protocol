import importlib
import pkgutil


def muat_semua_plugin():

    for info in pkgutil.iter_modules(__path__):
        importlib.import_module(
            f"{__name__}.{info.name}"
        )