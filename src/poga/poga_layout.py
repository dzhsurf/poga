from .libpoga_capi import *

class PogaLayout(object):
    __node: YGNodeRef = None
    def __init__(self):
        self.__node = YGNodeNew()

    def __del__(self):
        YGNodeFree(self.__node)