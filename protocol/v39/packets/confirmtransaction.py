from . import template

class handler(template.handler):
    def __init__(self, *args):
        self.NAME = "Confirm Transaction"
        self.HEADER = 0x6A

    def getlength(self, roboclass, data):
        return 4