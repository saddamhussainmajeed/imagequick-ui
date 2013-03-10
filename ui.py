import wx
import ui_core

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
        voice = { 
            'name':self.av.GetValue(),
            'description':self.de.GetValue()
        }
        print voice
        self.Close()


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
        style = {'name':self.av.GetValue() }
        print style
        self.Close()

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
        frequency = {
            'frequency':self.fr.GetValue(),
            'filename':self.fn.GetValue()
        }
        print frequency
        self.Close()

class AddSta(wx.Frame):
    def __init__(self,parent,id):
        self.format_list = []
        wx.Frame.__init__(self,parent,id,'Stations',size=(400,300))
        wx.Frame.CentreOnScreen(self)
        userin=wx.Panel(self,-1,(-1,-1),(-1,-1))
        wx.StaticText(userin,-1,"Station Name",pos=(100,80))
        self.av=wx.TextCtrl(userin,-1,"",pos=(225,75),size=(100,30))
        '''
        self.cb1 = wx.CheckBox(userin, -1, "HAC",pos=(100,110))
        self.cb2 = wx.CheckBox(userin, -1, "CTY",pos=(100,130))
        self.cb3 = wx.CheckBox(userin, -1, "RCK",pos=(100,150))
        self.cb4 = wx.CheckBox(userin, -1, "ALT",pos=(100,170))
        self.cb5 = wx.CheckBox(userin, -1, "VAR",pos=(100,190))'''
        x=100
        y=110
        for format in ui_core.get_format_list():
            wx.CheckBox(userin,-1,format,pos=(x,y)).Bind(wx.EVT_CHECKBOX, self.check_event)
            y +=20

        userbut=wx.Button(userin,label='Add',pos=(180,210),size=(60,-1))
        userbut.Bind(wx.EVT_BUTTON,self.butact)

    def check_event(self,e):
        sender = e.GetEventObject()
        if sender.GetValue() == True:
            self.format_list.append(sender.Label)
        else:
            self.format_list.remove(sender.Label)

    def butact(self,event):
        station = {
            'name':self.av.GetValue(),
            'formatids':ui_core.get_format_ids(self.format_list)
        }
        print station
        self.Close()

class AddPos(wx.Frame):
    def __init__(self,parent,id):
        self.format_list = []
        wx.Frame.__init__(self,parent,id,'Positioning Statements',size=(400,300))
        wx.Frame.CentreOnScreen(self)
        userin=wx.Panel(self,-1,(-1,-1),(-1,-1))
        wx.StaticText(userin,-1,"Format Name",pos=(100,80))
        self.av=wx.TextCtrl(userin,-1,"",pos=(225,75),size=(100,30))
        # Code for Dynamic Buttons 
        x=100
        y=110
        for format in ui_core.get_format_list():
            wx.CheckBox(userin,-1,format,pos=(x,y)).Bind(wx.EVT_CHECKBOX, self.check_event)
            y +=20

        userbut=wx.Button(userin,label='Add',pos=(180,210),size=(60,-1))
        userbut.Bind(wx.EVT_BUTTON,self.butact,userbut)
        

    def check_event(self,e):
        sender = e.GetEventObject()
        if sender.GetValue() == True:
            self.format_list.append(sender.Label)
        else:
            self.format_list.remove(sender.Label)

    def butact(self,event):
        position = {
            'name':self.av.GetValue(),
            'formatids':ui_core.get_format_ids(self.format_list)
        }
        print position
        self.Close()

class AddFor(wx.Frame):
    def __init__(self,parent,id):
        self.voice_list = []
        wx.Frame.__init__(self,parent,id,'Add Format',size=(400,300))
        wx.Frame.CentreOnScreen(self)
        userin=wx.Panel(self,-1,(-1,-1),(-1,-1))
        wx.StaticText(userin,-1,"Industry Name",pos=(100,50))
        self.av=wx.TextCtrl(userin,-1,"",pos=(215,45),size=(100,30))
        wx.StaticText(userin,-1,"Real Name",pos=(100,90))
        self.de=wx.TextCtrl(userin,-1,"",pos=(215,85),size=(100,30))
        # Code for Dynamic Buttons 
        x=120
        y=140
        for voice in ui_core.get_voice_list():
            wx.CheckBox(userin,-1,voice,pos=(x,y)).Bind(wx.EVT_CHECKBOX, self.check_event)
            y +=20

        userbut=wx.Button(userin,label='Add',pos=(250,y),size=(60,-1))
        userbut.Bind(wx.EVT_BUTTON,self.butact,userbut)

    def check_event(self,e):
        sender = e.GetEventObject()
        if sender.GetValue() == True:
            self.voice_list.append(sender.Label)
        else:
            self.voice_list.remove(sender.Label)

    def butact(self,event):
        format = {
            'name':self.av.GetValue(),
            'realName':self.de.GetValue(),
            'voiceIds':ui_core.get_voice_ids(self.voice_list)
        }
        print format
        self.Close()

app = MyApp(0)
app.MainLoop()







##################################################################
############### CODE BY SADDAM HUSSAIN MAJEED ####################
###############     QUADLOOPS TECHNOLOGIES    ####################
##################################################################