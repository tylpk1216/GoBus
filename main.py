import ctypes
import json
import os
import requests
import wx

ERROR_STR = 'ERR'
CONFIG_FILE = 'GoBus.json'

def getConfigJSON(jsonFile):
    fd = open(jsonFile)
    jsonData = json.load(fd)
    fd.close()

    return jsonData

def getLeftMinute():
    if not os.path.isfile(CONFIG_FILE):
        return ERROR_STR

    jsonData = getConfigJSON(CONFIG_FILE)

    url = jsonData['url']
    pattern1 = str(jsonData['pattern1'])
    pattern2 = str(jsonData['pattern2'])

    r = requests.get(url)
    if r.status_code != 200:
        return ERROR_STR

    s1 = r.text
    try:
        index = s1.index(pattern1)
        s2 = s1[index:]

        index = s2.index(pattern2)
        s3 = s2[index + len(pattern2):]

        num = ''
        for c in s3:
            if not c.isdigit():
                break
            num += c

        return num

    except:
        return ERROR_STR

class MainFrame(wx.Frame):
    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(MainFrame, self).__init__(*args, **kw)

        # create a panel in the frame
        width = self.GetSize().GetWidth()
        height = self.GetSize().GetHeight()
        pnl = wx.Panel(self, size=wx.Size(width, height))

        # show min info
        x = (width - 65) / 2
        y = (height - 45) / 2

        min = getLeftMinute()

        self.st = wx.StaticText(pnl, label=min, pos=(x, y))
        font = self.st.GetFont()
        font.PointSize += 20
        font = font.Bold()

        self.st.SetForegroundColour(wx.Colour(128,0,0))
        self.st.SetFont(font)

        self.busTimer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.updateBusMinute, self.busTimer)
        self.busTimer.Start(60000, wx.TIMER_CONTINUOUS)

    def updateBusMinute(self, event):
        num = getLeftMinute()
        print(num)
        self.st.SetLabel(num)

def main():
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()

    frmWidth = 90
    frmHeight = 60

    user32 = ctypes.windll.user32
    screenWidth = user32.GetSystemMetrics(0)
    screenHeight = user32.GetSystemMetrics(1)

    size = wx.Size(frmWidth, frmHeight)
    style = wx.MAXIMIZE_BOX | wx.STAY_ON_TOP
    point = (screenWidth - frmWidth, screenHeight - frmHeight - 40)

    frm = MainFrame(None, title='GoBus', size=size, style=style, pos=point)
    frm.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()

