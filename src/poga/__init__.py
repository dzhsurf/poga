from . import libpoga_capi
from .poga_layout import PogaLayout
from .poga_types import *
from .poga_view import PogaView


def get_include():
    import os

    def is_ok(path):
        return os.path.exists(path) and os.path.isdir(path)

    package_path = os.path.dirname(os.path.realpath(__file__))
    install_path = os.path.join(package_path, "include")

    # in case we are installed
    if is_ok(install_path):
        return install_path

    # in case we are running from source
    if is_ok(package_path):
        return package_path

    # in case we are in an .egg
    import pkg_resources

    return pkg_resources.resource_filename(__name__, "include")
