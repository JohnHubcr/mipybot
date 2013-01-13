import internalib
import network
import pluginmanager

import threading
import time

class main():
    def __init__(self):
        self.HOST = '127.0.0.1'
        self.PORT = 25565
        self.USERNAME = 'MiPyBot'

        self.STOPPING = False

        self.INTERNALIB = internalib

        self.LOGGINGTOOLS = internalib.loggingtools()

        self.MAINSIGNALS = internalib.signalmanager()

        # Clock starts after robot logs in via 0x01
        self.MAINSIGNALS.newsignal("clockupdate")
        self.CLOCKTHREAD = threading.Thread(target=self.tickclock)

        self.MAINSIGNALS.newsignal("stop")
        self.MAINSIGNALS.getsignal("stop").addreceiver(self.stop)

        self.NETWORK = network.network()
        self.NETWORK.load(self)

        self.CHARACTER = character(self)

        self.WORLD = world(self)

        self.PLUGINMANAGER = pluginmanager.manager(self)
        self.PLUGINMANAGER.initPlugins()

    def tickclock(self):
        while not self.STOPPING:
            self.MAINSIGNALS.emit("clockupdate")
            time.sleep(0.05)

    def start(self):
        self.PLUGINMANAGER.startPlugins()
        self.NETWORK.start()

    def stop(self):
        self.PLUGINMANAGER.stopPlugins()
        self.STOPPING = True

class character():
    def __init__(self, roboclass):
        self.ROBOCLASS = roboclass
        self.ENTITYID = None
        self.GAMEMODE = None
        self.DIFFICULTY = None

        self.HEALTH = None
        self.FOOD = None
        self.FOODSATURATION = None

        self.X = None
        self.Y = None
        self.Z = None
        self.YAW = None
        self.PITCH = None
        self.ONGROUND = None
        self.STANCE = None

        self.XPBAR = None
        self.XPLEVEL = None
        self.XPTOTAL = None

class world():
    def __init__(self, roboclass):
        self.ROBOCLASS = roboclass
        self.LEVELTYPE = None
        self.DIMENSION = None
        self.MAXPLAYERS = None
        self.AGE = None
        self.TIME = None
        self.BUILDLIMIT = None