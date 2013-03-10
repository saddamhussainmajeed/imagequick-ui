import time
import wx
import wx.gizmos as gizmos

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(450, 100))

        self.led = gizmos.LEDNumberCtrl(self, -1, wx.DefaultPosition, wx.DefaultSize, gizmos.LED_ALIGN_CENTER)
        self.OnTimer(None)
        self.timer = wx.Timer(self, -1)
        self.timer.Start(1000)
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        self.Centre()

    def OnTimer(self, event):
        t = time.localtime(time.time())
        st = time.strftime("%I:%M:%S", t)
        self.led.SetValue(st)

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, 'lednumber.py')
        frame.Show(True)
        self.SetTopWindow(frame)
        return True

app = MyApp(0)
app.MainLoop()