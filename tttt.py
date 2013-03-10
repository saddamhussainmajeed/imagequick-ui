import wx

class MainWindow(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title,wx.DefaultPosition,
                            wx.Size(205,220),
                            wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER |
                            wx.RESIZE_BOX | wx.MAXIMIZE_BOX))
        
        # ------ Area for the text output of pressing button
        textarea = wx.TextCtrl(self, -1,
                                style=wx.TE_MULTILINE|wx.BORDER_SUNKEN|wx.TE_READONLY|
                                wx.TE_RICH2, size=(200,100))
        self.usertext = textarea
        
        # ------ Area for the user's controls
        userin = wx.Panel(self, -1, (0,100), (200,100))

        wx.StaticText(userin, -1, "Type\nHere", pos=(15,0))
        wx.TextCtrl(userin, -1, "", pos=(48,5))
        Press = wx.Button(userin, -1, "Press", (60,30))
        
        Press.Bind(wx.EVT_BUTTON, self.inserttext)
    
    def inserttext(self, event):
        self.usertext.write("hiya ")

class MainApp(wx.App):
    def OnInit(self):
        myWindow = MainWindow(None, -1, "Text to Textarea")
        myWindow.Show(True)
        self.SetTopWindow(myWindow)
        return(True)

AppStart = MainApp(0)
AppStart.MainLoop()  