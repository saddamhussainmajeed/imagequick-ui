import wx 

ID_EXIT = 110

class MainPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.buttonRun = wx.Button(self, label="Run")
        self.buttonRun.Bind(wx.EVT_BUTTON, self.OnRun )
        self.buttonExit = wx.Button(self, label="Exit")
        self.buttonExit.Bind(wx.EVT_BUTTON, self.OnExit)

        self.labelChooseRoot = wx.StaticText(self, label ="Root catalog: ") 
        self.labelScratchWrk = wx.StaticText(self, label ="Scratch workspace: ")
        self.labelMergeFile = wx.StaticText(self, label ="Merge file: ")

        self.textChooseRoot = wx.TextCtrl(self, size=(210, -1))
        self.textChooseRoot.Bind(wx.EVT_LEFT_UP, self.OnChooseRoot)
        self.textScratchWrk = wx.TextCtrl(self, size=(210, -1))
        self.textMergeFile = wx.TextCtrl(self, size=(210, -1))
        self.textOutput = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY)

        self.sizerF = wx.FlexGridSizer(3, 2, 5, 5)
        self.sizerF.Add(self.labelChooseRoot)  #row 1, col 1
        self.sizerF.Add(self.textChooseRoot)   #row 1, col 2
        self.sizerF.Add(self.labelScratchWrk)  #row 2, col 1
        self.sizerF.Add(self.textScratchWrk)   #row 2, col 2
        self.sizerF.Add(self.labelMergeFile)   #row 3, col 1
        self.sizerF.Add(self.textMergeFile)    #row 3, col 2

        self.sizerB = wx.BoxSizer(wx.VERTICAL)
        self.sizerB.Add(self.buttonRun, 1, wx.ALIGN_RIGHT|wx.ALL, 5)
        self.sizerB.Add(self.buttonExit, 0, wx.ALIGN_RIGHT|wx.ALL, 5)

        self.sizer1 = wx.BoxSizer()
        self.sizer1.Add(self.sizerF, 0, wx.ALIGN_RIGHT | wx.EXPAND | wx.ALL, 10)
        self.sizer1.Add(self.sizerB, 0, wx.ALIGN_RIGHT | wx.EXPAND | wx.ALL)

        self.sizer2 = wx.BoxSizer()
        self.sizer2.Add(self.textOutput, 1, wx.EXPAND | wx.ALL, 5)

        self.sizerFinal = wx.BoxSizer(wx.VERTICAL)
        self.sizerFinal.Add(self.sizer1, 0, wx.ALIGN_RIGHT | wx.EXPAND | wx.ALL)
        self.sizerFinal.Add(self.sizer2, 1, wx.ALIGN_RIGHT | wx.EXPAND | wx.ALL)

        self.SetSizerAndFit(self.sizerFinal)


    def OnChooseRoot(self, event):
        dlg = wx.DirDialog(self, "Choose a directory:", style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            root_path = dlg.GetPath()
            self.textChooseRoot.SetValue(root_path)
        dlg.Destroy()

    def OnRun(self, event):
        #First check if any of the boxes is empty
        pass

    def OnExit(self, event):
        self.GetParent().Close()


class MainWindow(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="IndexGenerator", size=(430, 330), 
                          style=((wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE | 
                                  wx.STAY_ON_TOP) ^ wx.RESIZE_BORDER))
        self.CreateStatusBar() 

        self.fileMenu = wx.Menu()
        self.fileMenu.Append(ID_EXIT, "E&xit", "Exit the program")
        self.menuBar = wx.MenuBar()
        self.menuBar.Append(self.fileMenu, "&File")
        self.SetMenuBar(self.menuBar)
        wx.EVT_MENU(self, ID_EXIT, self.OnExit)                    

        self.Panel = MainPanel(self)

        self.CentreOnScreen()
        self.Show()

    def OnExit(self,  event):
        self.Close()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MainWindow()
    app.MainLoop()