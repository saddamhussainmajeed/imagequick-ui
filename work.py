import wx

class MainFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(600,400))
        menubar = wx.MenuBar()
        
        menufile = wx.Menu()
        create = wx.Menu()
        batch=wx.Menu()
        menuhelp=wx.Menu()
        
        menufile.Append(101, '&Connect')
        menufile.AppendSeparator()
        quit = wx.MenuItem(menufile, 105, '&Quit\tCtrl+Q')
        menufile.AppendItem(quit)
        
        create.Append(201, 'Voice Talent')
        create.Append(202, 'Template')
        create.Append(203, 'Hook Template')
        create.Append(204, 'Format')
        create.Append(205, 'Positioning Statement')
        create.Append(206, 'Station')
        create.Append(207, 'Frequency')
        create.Append(208, 'Delivery Style')
        
                        
        submenu=wx.Menu()
        submenu.Append(302,'Station',kind=wx.ITEM_NORMAL)
        batch.AppendMenu(302,'Voice to Template',submenu)
        
        menuhelp.Append(501, 'About')
        
        menubar.Append(menufile, '&File')
        menubar.Append(create, '&Create')
        menubar.Append(batch, '&Batch')
        menubar.Append(menuhelp, '&Help')
        
        self.SetMenuBar(menubar)
        self.Centre()
        self.Bind(wx.EVT_MENU,self.OnQuit, id=105)
        self.Bind(wx.EVT_MENU,self.actconnect,id=101)
        self.Bind(wx.EVT_MENU,self.actvoice,id=201)
        #self.Bind(wx.EVT_MENU,self.acttemp,id=202)
        #self.Bind(wx.EVT_MENU,self.test,id=203)
        self.Bind(wx.EVT_MENU,self.actfor,id=204)
        self.Bind(wx.EVT_MENU,self.actpos,id=205)
        self.Bind(wx.EVT_MENU,self.actsta,id=206)
        self.Bind(wx.EVT_MENU,self.actfre,id=207)
        self.Bind(wx.EVT_MENU,self.actdel,id=208)
        self.Bind(wx.EVT_MENU,self.OnAbout,id=501)
    def actconnect(self,event):
        self.new=IpConnect(parent=None,id=-1)
        self.new.Show(True)
    
    def actvoice(self,event):
        self.new=AddVoice(parent=None,id=-1)
        self.new.Show(True)

    def actdel(self,event):
        self.new=AddDel(parent=None,id=-1)
        self.new.Show(True)
    
    def actfre(self,event):
        self.new=AddFre(parent=None,id=-1)
        self.new.Show(True)

    def actsta(self,event):
        self.new=AddSta(parent=None,id=-1)
        self.new.Show(True)
    
    def actpos(self,event):
        self.new=AddPos(parent=None,id=-1)
        self.new.Show(True)

    def actfor(self,event):
        self.new=AddFor(parent=None,id=-1)
        self.new.Show(True)

    def OnQuit(self, event):
        self.Close()

    def OnAbout(self,event):
        dlg = wx.MessageDialog( self, "Developed By SHM\n Version 1.1", "ImageQuick", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

class MyApp(wx.App):
    def OnInit(self):
        frame = MainFrame(None, -1, 'ImageQuick')
        frame.Show(True)
        #self.SetTopWindow(frame)
        return True

class IpConnect(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Connect to Server',size=(400,300))
        wx.Frame.CentreOnScreen(self)
        inp=wx.Panel(self,-1,(-1,-1),(-1,-1))
        wx.StaticText(inp,-1,"Server IP",pos=(100,80))
        self.s=wx.TextCtrl(inp,-1,"",pos=(225,75),size=(150,30))
        wx.StaticText(inp,-1,"PORT",pos=(100,120))
        self.p=wx.TextCtrl(inp,-1,"27017",pos=(225,115),size=(100,30))
        self.p.SetInsertionPoint(0)
        but=wx.Button(inp,label='Connect',pos=(150,150),size=(65,-1))
        but2=wx.Button(inp,label='Cancel',pos=(250,150),size=(65,-1))
        but.Bind(wx.EVT_BUTTON,self.butact,but)
        but2.Bind(wx.EVT_BUTTON,self.quitwin)

    def butact(self,event):
        print self.s.GetValue() + ':' + self.p.GetValue()
        
    def quitwin(self,event):
        self.Close()

class AddVoice(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Add Voice',size=(400,300))
        wx.Frame.CentreOnScreen(self)
        #self.Bind(wx.EVT_CLOSE, self.on_close)
        userin=wx.Panel(self,-1,(-1,-1),(-1,-1))
        wx.StaticText(userin,-1,"Add Voice",pos=(100,80))
        self.av=wx.TextCtrl(userin,-1,"",pos=(225,75),size=(100,30))
        wx.StaticText(userin,-1,"Description",pos=(100,120))
        self.de=wx.TextCtrl(userin,-1,"",pos=(225,115),size=(150,30))
        userbut=wx.Button(userin,label='Add',pos=(150,150),size=(60,-1))
        userbut.Bind(wx.EVT_BUTTON,self.butact,userbut)

    def butact(self,event):
        print self.av.GetValue() + ':' + self.de.GetValue()


class AddDel(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Delivery',size=(400,300))
        wx.Frame.CentreOnScreen(self)
        userin=wx.Panel(self,-1,(-1,-1),(-1,-1))
        wx.StaticText(userin,-1,"Delivery Style",pos=(100,80))
        self.av=wx.TextCtrl(userin,-1,"",pos=(225,75),size=(100,30))
        userbut=wx.Button(userin,label='Add',pos=(150,150),size=(60,-1))
        userbut.Bind(wx.EVT_BUTTON,self.butact,userbut)

    def butact(self,event):
        print self.av.GetValue()

class AddFre(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Add a Frequency',size=(400,300))
        wx.Frame.CentreOnScreen(self)
        #self.Bind(wx.EVT_CLOSE, self.on_close)
        userin=wx.Panel(self,-1,(-1,-1),(-1,-1))
        wx.StaticText(userin,-1,"Frequency",pos=(100,80))
        self.fr=wx.TextCtrl(userin,-1,"",pos=(225,75),size=(100,30))
        wx.StaticText(userin,-1,"FileName",pos=(100,120))
        self.fn=wx.TextCtrl(userin,-1,"",pos=(225,115),size=(150,30))
        userbut=wx.Button(userin,label='Add',pos=(150,150),size=(60,-1))
        userbut.Bind(wx.EVT_BUTTON,self.butact,userbut)

    def butact(self,event):
        print self.fr.GetValue() + ':' + self.fn.GetValue()

class AddSta(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Stations',size=(400,300))
        wx.Frame.CentreOnScreen(self)
        userin=wx.Panel(self,-1,(-1,-1),(-1,-1))
        wx.StaticText(userin,-1,"Format Name",pos=(100,80))
        self.av=wx.TextCtrl(userin,-1,"",pos=(225,75),size=(100,30))
        self.cb1 = wx.CheckBox(userin, -1, "HAC",pos=(100,110))
        self.cb2 = wx.CheckBox(userin, -1, "CTY",pos=(100,130))
        self.cb3 = wx.CheckBox(userin, -1, "RCK",pos=(100,150))
        self.cb4 = wx.CheckBox(userin, -1, "ALT",pos=(100,170))
        self.cb5 = wx.CheckBox(userin, -1, "VAR",pos=(100,190))
        #self.Bind(wx.EVT_CHECKBOX, self.OnCb, self.cb1)
        """self.Bind(wx.EVT_CHECKBOX, self.OnCb, self.cb2)
        self.Bind(wx.EVT_CHECKBOX, self.OnCb, self.cb3)
        self.Bind(wx.EVT_CHECKBOX, self.OnCb, self.cb4)
        self.Bind(wx.EVT_CHECKBOX, self.OnCb, self.cb5)"""
        userbut=wx.Button(userin,label='Add',pos=(180,210),size=(60,-1))
        userbut.Bind(wx.EVT_BUTTON,self.butact,userbut)
        #if self.cb1.GetValue() == True:
            #setattr(newAttr, comp, 'Y')
        #else:
            #setattr(newAttr, comp, 'N') 

    def butact(self,event):
        print self.av.GetValue()

class AddPos(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Positioning Statements',size=(400,300))
        wx.Frame.CentreOnScreen(self)
        userin=wx.Panel(self,-1,(-1,-1),(-1,-1))
        wx.StaticText(userin,-1,"Format Name",pos=(100,80))
        self.av=wx.TextCtrl(userin,-1,"",pos=(225,75),size=(100,30))
        self.cb1 = wx.CheckBox(userin, -1, "HAC",pos=(100,110))
        self.cb2 = wx.CheckBox(userin, -1, "CTY",pos=(100,130))
        self.cb3 = wx.CheckBox(userin, -1, "RCK",pos=(100,150))
        self.cb4 = wx.CheckBox(userin, -1, "ALT",pos=(100,170))
        self.cb5 = wx.CheckBox(userin, -1, "VAR",pos=(100,190))
        #self.Bind(wx.EVT_CHECKBOX, self.OnCb, self.cb1)
        """self.Bind(wx.EVT_CHECKBOX, self.OnCb, self.cb2)
        self.Bind(wx.EVT_CHECKBOX, self.OnCb, self.cb3)
        self.Bind(wx.EVT_CHECKBOX, self.OnCb, self.cb4)
        self.Bind(wx.EVT_CHECKBOX, self.OnCb, self.cb5)"""
        userbut=wx.Button(userin,label='Add',pos=(180,210),size=(60,-1))
        userbut.Bind(wx.EVT_BUTTON,self.butact,userbut)

    def butact(self,event):
        print self.av.GetValue()

class AddFor(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Add Format',size=(400,300))
        wx.Frame.CentreOnScreen(self)
        userin=wx.Panel(self,-1,(-1,-1),(-1,-1))
        wx.StaticText(userin,-1,"Industry Name",pos=(100,50))
        self.av=wx.TextCtrl(userin,-1,"",pos=(215,45),size=(100,30))
        wx.StaticText(userin,-1,"Real Name",pos=(100,90))
        self.de=wx.TextCtrl(userin,-1,"",pos=(215,85),size=(100,30))
        self.cb1 = wx.CheckBox(userin, -1, "Sam",pos=(120,120))
        self.cb2 = wx.CheckBox(userin, -1, "Gary",pos=(120,140))
        self.cb3 = wx.CheckBox(userin, -1, "Lisa",pos=(120,160))
        self.cb4 = wx.CheckBox(userin, -1, "Steve",pos=(120,180))
        self.cb5 = wx.CheckBox(userin, -1, "Mike",pos=(120,200))
        self.cb6 = wx.CheckBox(userin, -1, "Alexa",pos=(120,220))
        self.cb7 = wx.CheckBox(userin, -1, "Sassy",pos=(120,240))
        #self.Bind(wx.EVT_CHECKBOX, self.OnCb, self.cb1)
        """self.Bind(wx.EVT_CHECKBOX, self.OnCb, self.cb2)
        self.Bind(wx.EVT_CHECKBOX, self.OnCb, self.cb3)
        self.Bind(wx.EVT_CHECKBOX, self.OnCb, self.cb4)
        self.Bind(wx.EVT_CHECKBOX, self.OnCb, self.cb5)"""
        userbut=wx.Button(userin,label='Add',pos=(250,150),size=(60,-1))
        userbut.Bind(wx.EVT_BUTTON,self.butact,userbut)

    def butact(self,event):
        print self.av.GetValue()+':'+self.de.GetValue()

app = MyApp(0)
app.MainLoop()







##################################################################
############### CODE BY SADDAM HUSSAIN MAJEED ####################
###############     QUADLOOPS TECHNOLOGIES    ####################
##################################################################