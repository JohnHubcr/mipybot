from . import template

class handler(template.handler):
    def __init__(self, *args):
        self.NAME = "Entity Equipment"
        self.HEADER = 0x05

    def getlength(self, roboclass, data):
        print("Data", data)
        Length = roboclass.CONVERTER.INTEGER_LENGTH + roboclass.CONVERTER.SHORT_LENGTH
        # Reading the slot
        slotid = roboclass.CONVERTER.getshort(data, Length)
        Length += roboclass.CONVERTER.SHORT_LENGTH
        if slotid == -1:
            print("Slot ID is -1")
            return Length
        Length += roboclass.CONVERTER.BYTE_LENGTH
        slotdatalength = roboclass.CONVERTER.getshort(data, Length)
        Length += roboclass.CONVERTER.SHORT_LENGTH
        if slotdatalength == -1:
            print("Slot Data length is -1")
            return Length
        Length += slotdatalength
        return Length
