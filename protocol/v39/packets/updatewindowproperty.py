from . import template

class handler(template.handler):
    def __init__(self, *args):
        self.NAME = "Update Window Property"
        self.HEADER = 0x69

    def receive(self, roboclass):
        return 5
