import wx

class MainWindow(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Python Test App',size=(600,400))
        panel=wx.Panel(self)
        wx.Frame.CenterOnScreen(self)

        status=self.CreateStatusBar()
        menubar=wx.MenuBar()
        file_menu=wx.Menu()
        edit_menu=wx.Menu()

        ID_FILE_NEW = 1
        ID_FILE_OPEN = 2

        ID_EDIT_UNDO = 3
        ID_EDIT_REDO = 4


        file_menu.Append(ID_FILE_NEW,"New Window","This is a new window")
        file_menu.Append(ID_FILE_OPEN,"Open...","This will open a new window")

        edit_menu.Append(ID_EDIT_UNDO,"Undo","This will undo your last action")
        edit_menu.Append(ID_EDIT_REDO,"Redo","This will redo your last undo")


        menubar.Append(file_menu,"File")
        menubar.Append(edit_menu,"Edit")
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.test, None, 1)

    def test(self, event):
        self.new = NewWindow(parent=None, id=-1)
        self.new.Show(True)


class NewWindow(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self, parent, id, 'New Window', size=(400,300))
        wx.Frame.CenterOnScreen(self)
        #self.new.Show(False)

if __name__=='__main__':
        app=wx.PySimpleApp()
        frame=MainWindow(parent=None,id=-1)
        frame.Show()
        app.MainLoop()