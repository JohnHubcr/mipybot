from . import template

class handler(template.handler):
    def __init__(self, *args):
        self.NAME = "Enchant Item"
        self.HEADER = 0x6C

    def receive(self, roboclass):
        roboclass.PACKETS.POINTER.read(2)
        return roboclass.PACKETS.POINTER.getposition()
