from . import template

class handler(template.handler):
    def __init__(self, *args):
        self.NAME = "Increment Statistic"
        self.HEADER = 0xC8

    def receive(self, roboclass):
        return 5
