from . import template

class handler(template.handler):
    def __init__(self, *args):
        self.NAME = "Update Tile Entity"
        self.HEADER = 0x84

    def receive(self, roboclass):
        roboclass.PACKETS.POINTER.read('int')
        roboclass.PACKETS.POINTER.read('short')
        roboclass.PACKETS.POINTER.read('int')
        roboclass.PACKETS.POINTER.read('byte')
        roboclass.PACKETS.POINTER.read('shortdata')
        return roboclass.PACKETS.POINTER.getposition()
