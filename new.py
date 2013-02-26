from wx import *

ID_FILE_EXIT = wxNewId()
ID_FILE_ABOUT = wxNewId()
ID_CREATE_VOICE=1

class MainWindow(wx.Frame):

	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,'ImageQuick',size=(600,400))
		panel=wx.panel(self)
		wx.Frame.CentreOnScreen(self)

		status=self.CreateStatusBar()
		menubar=wx.MenuBar()
		file_menu=wx.Menu()
		create_menu=wx.Menu()
		file_menu.Append(ID_FILE_ABOUT, 'About')
		file_menu.AppendSeperator()
		file_menu.Append(ID_FILE_EXIT, 'Exit Program')
		create_menu.Append(ID_CREATE_VOICE, 'Create voice')

		menubar.Append(file_menu,"File")
		menubar.Append(create_menu,"Create")

		self.SetMenuBar(menubar)
		EVT_MENU(self, ID_FILE_EXIT, self.OnFileExit)
        
	def OnFileExit(self, evt):
		dlg = wxMessageDialog(self, 'Exit Program?', 'I Need To Know!',wxYES_NO | wxICON_QUESTION)
		if dlg.ShowModal() == wxID_YES:
			dlg.Destroy()
			self.Close(true)
		else:
			dlg.Destroy()

class myMenuApp(wxApp):
    def OnInit(self):
        frame = myFrame(NULL, -1, 'Menu Demo - Powered by wxPython')
        frame.Show(true)
        self.SetTopWindow(frame)
        return true
app=myMenuApp(0)
app.MainLoop()