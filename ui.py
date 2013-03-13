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
        analt=wx.Menu()
        
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
        
                        
        sub=wx.Menu()
        sub.Append(310,'SFP',kind=wx.ITEM_NORMAL)
        sub.Append(311,'SF',kind=wx.ITEM_NORMAL)
        sub.Append(312,'Station',kind=wx.ITEM_NORMAL)
        sub.Append(313,'Frequency',kind=wx.ITEM_NORMAL)
        sub.Append(314,'Position',kind=wx.ITEM_NORMAL)
        
        batch.AppendMenu(302,'Voice to Template',sub)

        
        menuhelp.Append(501, 'About')

        sm1=wx.Menu()
        sm2=wx.Menu()
        sm1.Append(701,'Format',kind=wx.ITEM_NORMAL)
        sm1.Append(702,'Voice',kind=wx.ITEM_NORMAL)
        sm1.Append(703,'Template',kind=wx.ITEM_NORMAL)
        sm1.Append(704,'Producer',kind=wx.ITEM_NORMAL)
        sm2.Append(607,'Voice',kind=wx.ITEM_NORMAL)
        sm2.Append(607,'Producer',kind=wx.ITEM_NORMAL)

        analt.Append(601, 'Format')
        analt.Append(602, 'Voice')
        analt.Append(603, 'Template')
        analt.Append(604, 'Producer')
        analt.Append(605, 'Voice Format')
        analt.AppendMenu(606, 'Monthly Sheets',sm1)
        analt.AppendMenu(607, 'Monthly PayBills',sm2)
        
        menubar.Append(menufile, '&File')
        menubar.Append(create, '&Create')
        menubar.Append(batch, '&Batch')
        menubar.Append(analt, '&Analytics')
        menubar.Append(menuhelp, '&Help')
        self.SetMenuBar(menubar)
        self.Centre()
        self.Bind(wx.EVT_MENU,self.OnQuit, id=105)
        self.Bind(wx.EVT_MENU,self.actconnect,id=101)
        self.Bind(wx.EVT_MENU,self.actvoice,id=201)
        self.Bind(wx.EVT_MENU,self.acttemp,id=202)
        self.Bind(wx.EVT_MENU,self.acthook,id=203)
        self.Bind(wx.EVT_MENU,self.actfor,id=204)
        self.Bind(wx.EVT_MENU,self.actpos,id=205)
        self.Bind(wx.EVT_MENU,self.actsta,id=206)
        self.Bind(wx.EVT_MENU,self.actfre,id=207)
        self.Bind(wx.EVT_MENU,self.actdel,id=208)
        self.Bind(wx.EVT_MENU,self.OnAbout,id=501)
        #self.Bind(wx.EVT_MENU,self.OnAbout,id=701)
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

    def acthook(self,event):
        self.new=AddHook()
        self.new.Show(True)

    def acttemp(self,event):
        self.new=AddTemp()
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
        wx.StaticText(userin,-1,"Station Name",pos=(80,60))
        self.av=wx.TextCtrl(userin,-1,"",pos=(210,55),size=(100,30))
        wx.StaticText(userin,-1,"Associated Formats",pos=(80,90))

        x=100
        y=110
        for format in ui_core.get_format_list():
            wx.CheckBox(userin,-1,format,pos=(x,y)).Bind(wx.EVT_CHECKBOX, self.check_event)
            y +=20

        userbut=wx.Button(userin,label='Add',pos=(200,200),size=(60,-1))
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
        wx.StaticText(userin,-1,"Format Name",pos=(80,60))
        self.av=wx.TextCtrl(userin,-1,"",pos=(200,55),size=(100,30))
        wx.StaticText(userin,-1,"Associated Formats",pos=(80,90))
        # Code for Dynamic Buttons 
        x=100
        y=110
        for format in ui_core.get_format_list():
            wx.CheckBox(userin,-1,format,pos=(x,y)).Bind(wx.EVT_CHECKBOX, self.check_event)
            y +=20

        userbut=wx.Button(userin,label='Add',pos=(200,200),size=(60,-1))
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
        wx.StaticText(userin,-1,"Industry Name",pos=(80,30))
        self.av=wx.TextCtrl(userin,-1,"",pos=(210,25),size=(120,30))
        wx.StaticText(userin,-1,"Real Name",pos=(80,70))
        self.de=wx.TextCtrl(userin,-1,"",pos=(210,65),size=(120,30))
        wx.StaticText(userin,-1,"Associated Voices",pos=(80,110))

        # Code for Dynamic Buttons 
        x=120
        y=140
        for voice in ui_core.get_voice_list():
            wx.CheckBox(userin,-1,voice,pos=(x,y)).Bind(wx.EVT_CHECKBOX, self.check_event)
            y +=20

        userbut=wx.Button(userin,label='Add',pos=(250,160),size=(60,-1))
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

class AddHook( wx.Frame ): 
    def __init__( self ):
        wx.Frame.__init__( self, None,-1, "Add Hook Template", size=(350, 400) )
        scrollWin = wx.PyScrolledWindow( self, -1 )
# Add Code Below
        
        wx.StaticText(scrollWin,-1,"Template Name",pos=(40,30))
        self.tn=wx.TextCtrl(scrollWin,-1,"",pos=(180,25),size=(120,30))
        wx.StaticText(scrollWin,-1,"File Name",pos=(40,70))
        self.fn=wx.TextCtrl(scrollWin,-1,"",pos=(180,65),size=(120,30))
        wx.StaticText(scrollWin,-1,"Producer",pos=(40,110))
        self.po=wx.TextCtrl(scrollWin,-1,"",pos=(180,105),size=(120,30))
        wx.StaticText(scrollWin,-1,"Price",pos=(40,150))
        self.pr=wx.TextCtrl(scrollWin,-1,"",pos=(180,145),size=(120,30))
        wx.StaticText(scrollWin,-1,"Available Formats",pos=(40,190))
        x = 180 # Magic numbers !?
        y = 200
        for format in ui_core.get_format_list():
            wx.CheckBox(scrollWin,-1,format,pos=(x,y))#.Bind(wx.EVT_CHECKBOX, self.check_event)
            y +=20
        wx.StaticText(scrollWin,-1,"SLOGAN DETAILS",pos=(40,300))
        wx.StaticText(scrollWin,-1,"Associated Voices",pos=(40,320))
        u=180
        v=340
        for voice in ui_core.get_voice_list():
            wx.CheckBox(scrollWin,-1,voice,pos=(u,v))#.Bind(wx.EVT_CHECKBOX, self.check_event)
            v +=20
        wx.StaticText(scrollWin,-1,"Delay/Cue",pos=(40,490))
        self.dq=wx.TextCtrl(scrollWin,-1,"",pos=(180,485),size=(120,30))
        wx.StaticText(scrollWin,-1,"Associated Styles",pos=(40,515))
        ff=180
        fg=530
        for style in ui_core.get_style_list():
            wx.CheckBox(scrollWin,-1,style,pos=(ff,fg))#.Bind(wx.EVT_CHECKBOX, self.check_event)
            fg +=20
        wx.StaticText(scrollWin,-1,"STATION DETAILS",pos=(40,780))
        wx.StaticText(scrollWin,-1,"Associated Voices",pos=(40,800))
        ss=180
        st=815
        for voice in ui_core.get_voice_list():
            wx.CheckBox(scrollWin,-1,voice,pos=(ss,st))#.Bind(wx.EVT_CHECKBOX, self.check_event)
            st +=20
        wx.StaticText(scrollWin,-1,"No: of Words",pos=(40,970))
        self.nw=wx.TextCtrl(scrollWin,-1,"",pos=(180,965),size=(120,30))
        wx.StaticText(scrollWin,-1,"Delay/Cue",pos=(40,1010))
        self.dc=wx.TextCtrl(scrollWin,-1,"",pos=(180,1005),size=(120,30))
        wx.StaticText(scrollWin,-1,"Associated Styles",pos=(40,1035))
        cc=180
        cd=1050
        for style in ui_core.get_style_list():
            wx.CheckBox(scrollWin,-1,style,pos=(cc,cd))#.Bind(wx.EVT_CHECKBOX, self.check_event)
            cd +=20
        wx.StaticText(scrollWin,-1,"FREQUENCY DETAILS",pos=(40,1300))
        wx.StaticText(scrollWin,-1,"Associated Voices",pos=(40,1320))
        ab=180
        ac=1335
        for voice in ui_core.get_voice_list():
            wx.CheckBox(scrollWin,-1,voice,pos=(ab,ac))#.Bind(wx.EVT_CHECKBOX, self.check_event)
            ac +=20
        wx.StaticText(scrollWin,-1,"Delay/Cue",pos=(40,1485))
        self.dcc=wx.TextCtrl(scrollWin,-1,"",pos=(180,1480),size=(120,30))
        wx.StaticText(scrollWin,-1,"Associated Styles",pos=(40,1510))
        xx=180
        xy=1525
        for style in ui_core.get_style_list():
            wx.CheckBox(scrollWin,-1,style,pos=(xx,xy))#.Bind(wx.EVT_CHECKBOX, self.check_event)
            xy +=20
        wx.StaticText(scrollWin,-1,"POST HOOK Details",pos=(40,1775))
        wx.StaticText(scrollWin,-1,"File Name",pos=(40,1805))
        self.f1=wx.TextCtrl(scrollWin,-1,"",pos=(180,1800),size=(120,30))
        wx.StaticText(scrollWin,-1,"Station Details- Post Hooks",pos=(40,1840))
        wx.StaticText(scrollWin,-1,"Delay/Cue",pos=(40,1880))
        self.d1=wx.TextCtrl(scrollWin,-1,"",pos=(180,1875),size=(120,30))
        wx.StaticText(scrollWin,-1,"Frequency Details- Post Hooks",pos=(40,1915))
        wx.StaticText(scrollWin,-1,"Delay/Cue",pos=(40,1955))
        self.d2=wx.TextCtrl(scrollWin,-1,"",pos=(180,1950),size=(120,30))
        userbut=wx.Button(scrollWin,label='Add',pos=(120,2000),size=(100,-1))

#end for

 
#Till Here
        scrollWin.SetScrollbars(1,20,1,105)
        scrollWin.SetScrollRate( 1, 1 )

class AddTemp( wx.Frame ): 
    def __init__( self ):
        wx.Frame.__init__( self, None,-1, "Add a new Template piece", size=(350, 400) )
        scrollWin = wx.PyScrolledWindow( self, -1 )
# Add Code Below
        
        wx.StaticText(scrollWin,-1,"Template Name",pos=(40,30))
        self.tn=wx.TextCtrl(scrollWin,-1,"",pos=(180,25),size=(120,30))
        wx.StaticText(scrollWin,-1,"File Name",pos=(40,70))
        self.fn=wx.TextCtrl(scrollWin,-1,"",pos=(180,65),size=(120,30))
        wx.StaticText(scrollWin,-1,"Length",pos=(40,110))
        self.le=wx.TextCtrl(scrollWin,-1,"",pos=(180,105),size=(120,30))
        wx.StaticText(scrollWin,-1,"Producer",pos=(40,150))
        self.po=wx.TextCtrl(scrollWin,-1,"",pos=(180,145),size=(120,30))
        wx.StaticText(scrollWin,-1,"Price",pos=(40,190))
        self.pr=wx.TextCtrl(scrollWin,-1,"",pos=(180,185),size=(120,30))
        wx.StaticText(scrollWin,-1,"Available Formats",pos=(40,225))
        x = 180 # Magic numbers !?
        y = 235
        for format in ui_core.get_format_list():
            wx.CheckBox(scrollWin,-1,format,pos=(x,y))#.Bind(wx.EVT_CHECKBOX, self.check_event)
            y +=20
        wx.StaticText(scrollWin,-1,"SLOGAN DETAILS",pos=(40,335))
        wx.StaticText(scrollWin,-1,"Associated Voices",pos=(40,355))
        u=180
        v=375
        for voice in ui_core.get_voice_list():
            wx.CheckBox(scrollWin,-1,voice,pos=(u,v))#.Bind(wx.EVT_CHECKBOX, self.check_event)
            v +=20
        wx.StaticText(scrollWin,-1,"No: of Words",pos=(40,525))
        self.dq=wx.TextCtrl(scrollWin,-1,"",pos=(180,520),size=(120,30))
        wx.StaticText(scrollWin,-1,"Delay/Cue",pos=(40,565))
        self.dq=wx.TextCtrl(scrollWin,-1,"",pos=(180,560),size=(120,30))
        wx.StaticText(scrollWin,-1,"Associated Styles",pos=(40,580))
        ff=180
        fg=600
        for style in ui_core.get_style_list():
            wx.CheckBox(scrollWin,-1,style,pos=(ff,fg))#.Bind(wx.EVT_CHECKBOX, self.check_event)
            fg +=20
        wx.StaticText(scrollWin,-1,"STATION DETAILS",pos=(40,850))
        wx.StaticText(scrollWin,-1,"Associated Voices",pos=(40,870))
        ss=180
        st=890
        for voice in ui_core.get_voice_list():
            wx.CheckBox(scrollWin,-1,voice,pos=(ss,st))#.Bind(wx.EVT_CHECKBOX, self.check_event)
            st +=20
        wx.StaticText(scrollWin,-1,"No: of Words",pos=(40,1045))
        self.nw=wx.TextCtrl(scrollWin,-1,"",pos=(180,1040),size=(120,30))
        wx.StaticText(scrollWin,-1,"Delay/Cue",pos=(40,1085))
        self.dc=wx.TextCtrl(scrollWin,-1,"",pos=(180,1080),size=(120,30))
        wx.StaticText(scrollWin,-1,"Associated Styles",pos=(40,1110))
        cc=180
        cd=1130
        for style in ui_core.get_style_list():
            wx.CheckBox(scrollWin,-1,style,pos=(cc,cd))#.Bind(wx.EVT_CHECKBOX, self.check_event)
            cd +=20
        wx.StaticText(scrollWin,-1,"FREQUENCY DETAILS",pos=(40,1380))
        wx.StaticText(scrollWin,-1,"Associated Voices",pos=(40,1400))
        ab=180
        ac=1420
        for voice in ui_core.get_voice_list():
            wx.CheckBox(scrollWin,-1,voice,pos=(ab,ac))#.Bind(wx.EVT_CHECKBOX, self.check_event)
            ac +=20
        wx.StaticText(scrollWin,-1,"Delay/Cue",pos=(40,1570))
        self.dcc=wx.TextCtrl(scrollWin,-1,"",pos=(180,1565),size=(120,30))
        wx.StaticText(scrollWin,-1,"Associated Styles",pos=(40,1590))
        xx=180
        xy=1610
        for style in ui_core.get_style_list():
            wx.CheckBox(scrollWin,-1,style,pos=(xx,xy))#.Bind(wx.EVT_CHECKBOX, self.check_event)
            xy +=20
        userbut=wx.Button(scrollWin,label='Add',pos=(130,1870),size=(100,-1))

#end for

 
#Till Here
        scrollWin.SetScrollbars(1,20,1,100)
        scrollWin.SetScrollRate( 1, 1 )        


app = MyApp(0)
app.MainLoop()







##################################################################
############### CODE BY SADDAM HUSSAIN MAJEED ####################
###############     QUADLOOPS TECHNOLOGIES    ####################
##################################################################