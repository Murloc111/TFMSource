# coding: utf-8
import struct

def sendMBox(self, text, x, y, width, height, alpha, bgcolor, bordercolor, boxid):
        text = str(text)
        x, y, width, height = int(x), int(y), int(width), int(height)

        alpha = str(alpha).split("%")[0]
        alpha = int(alpha)

        if "#" in str(bgcolor):
                bgcolor = str(bgcolor[1:])
        else:
                pass
        if "#" in str(bordercolor):
                bordercolor = str(bordercolor[1:])
        else:
                pass
        bgcolor, bordercolor = int(bgcolor, 16), int(bordercolor, 16)

        data = struct.pack("!ih", int(boxid), len(text)) + str(text) + struct.pack("!hhhhiib", int(x), int(y), int(width), int(height), int(bgcolor), int(bordercolor), int(alpha))
        self.sendData("\x1d\x14", data+"\x00", True)

        # sendMBox(self, "ARTMICE", 730, 335, 65, 55, "50%", "#000000", "#C00000", 0)

def sendAllMBox(self, text, x, y, width, height, alpha, bgcolor, bordercolor, boxid):
        text = str(text)
        x, y, width, height = int(x), int(y), int(width), int(height)

        alpha = str(alpha).split("%")[0]
        alpha = int(alpha)

        if "#" in str(bgcolor):
                bgcolor = str(bgcolor[1:])
        else:
                pass
        if "#" in str(bordercolor):
                bordercolor = str(bordercolor[1:])
        else:
                pass
        bgcolor, bordercolor = int(bgcolor, 16), int(bordercolor, 16)

        data = struct.pack("!ih", int(boxid), len(text)) + str(text) + struct.pack("!hhhhiib", int(x), int(y), int(width), int(height), int(bgcolor), int(bordercolor), int(alpha))
        self.room.sendAllBin("\x1d\x14", data+"\x00")

        # sendMBox(self, "ARTMICE", 730, 335, 65, 55, "50%", "#000000", "#C00000", 0)

def editMBox(self, boxid, newtext):
        data = struct.pack("!ih", int(boxid), len(newtext)) + str(newtext)
        self.room.sendAllBin("\x1d\x15", data)

        # editMBox(self, 0, "ARTMICE")

def removeMBox(self, boxid):
        data = struct.pack("!i", int(boxid))
        self.room.sendAllBin("\x1d\x16", data)

        # removeMBox(self, 0)
        
def setUIShamanName(self, name):
    name = name.replace("&#","&amp;#").replace('&lt;','<')
    data = struct.pack("!h", len(name))
    data = data + name
    for room in self.server.rooms.values():
        if room.name == self.room.name:
           for playerCode, client in room.clients.items():
               client.sendData("\x1d\x1a" + data, [], True)

    # setUIShamanName(self, "шаман")
               
def setUIMapName(self, name):
    name = name.replace("&#","&amp;#").replace('&lt;','<')
    data = struct.pack("!h", len(name))
    data = data + name
    for room in self.server.rooms.values():
        if room.name == self.room.name:
           for playerCode, client in room.clients.items():
               client.sendData("\x1d\x19" + data, [], True)

    # setUIMapName(self, "карта")