import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        wx.Frame.__init__(self, *args, **kwds)
        self.cb1 = wx.CheckBox(self, -1, "CheckBox 1")
        self.cb2 = wx.CheckBox(self, -1, "CheckBox 2")
        self.cb3 = wx.CheckBox(self, -1, "CheckBox 3")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.cb1, 0, wx.ADJUST_MINSIZE, 0)
        sizer.Add(self.cb2, 0, wx.ADJUST_MINSIZE, 0)
        sizer.Add(self.cb3, 0, wx.ADJUST_MINSIZE, 0)

        self.SetSizer(sizer)
        self.Layout()

        self.Bind(wx.EVT_CHECKBOX, self.OnCb1, self.cb1)
        self.Bind(wx.EVT_CHECKBOX, self.OnCb2, self.cb2)

    def OnCb1(self, evt):
        self.cb2.SetValue(evt.IsChecked())

    def OnCb2(self, evt):
        self.cb3.SetValue(evt.IsChecked())


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    frame = MyFrame(None, -1, "")
    app.SetTopWindow(frame)
    frame.Show()
    app.MainLoop()