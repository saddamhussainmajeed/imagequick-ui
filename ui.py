import wx
import xlrd
import common.xlsgrid as XG
from common import ui_core
from common import database
from batch import voicetotemplate
from analytics import analytics
from crud import create


class MainFrame(wx.Frame):
    def __init__(self,parent,id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(600,400))
        menubar = wx.MenuBar()
        
        menufile = wx.Menu()
        createmenu = wx.Menu()
        batch=wx.Menu()
        menuhelp=wx.Menu()
        analt=wx.Menu()
        
        menufile.Append(101, '&Connect')
        menufile.AppendSeparator()
        quit = wx.MenuItem(menufile, 105, '&Quit\tCtrl+Q')
        menufile.AppendItem(quit)
        

        
        createmenu.Append(201, 'Voice Talent')
        createmenu.Append(204, 'Format')
        createmenu.Append(206, 'Station')
        createmenu.Append(207, 'Frequency')
        createmenu.Append(208, 'Delivery Style')
        createmenu.Append(205, 'Positioning Statement')
        createmenu.Append(202, 'Template')
        createmenu.AppendSeparator()
        createmenu.Append(209, 'Hook')
        createmenu.Append(203, 'Hook Template')
        createmenu.Append(210, 'Slogan Length')
        
                        
        sub=wx.Menu()
        sub.Append(310,'SFP',kind=wx.ITEM_NORMAL)
        sub.Append(311,'SF',kind=wx.ITEM_NORMAL)
        sub.Append(312,'Station',kind=wx.ITEM_NORMAL)
        sub.Append(313,'Frequency',kind=wx.ITEM_NORMAL)
        sub.Append(314,'Position',kind=wx.ITEM_NORMAL)
        batch.AppendMenu(302,'Voice to Template',sub)
        self.Bind(wx.EVT_MENU,self.batch_sfp,id=310)
        self.Bind(wx.EVT_MENU,self.batch_sf,id=311)
        self.Bind(wx.EVT_MENU,self.batch_s,id=312)
        self.Bind(wx.EVT_MENU,self.batch_f,id=313)
        self.Bind(wx.EVT_MENU,self.batch_p,id=314)
        
        menuhelp.Append(501, 'About')

        sm1=wx.Menu()
        sm2=wx.Menu()
        sm1.Append(701,'Format',kind=wx.ITEM_NORMAL)
        sm1.Append(702,'Voice',kind=wx.ITEM_NORMAL)
        sm1.Append(703,'Template',kind=wx.ITEM_NORMAL)
        sm1.Append(704,'Producer',kind=wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU,self.monthly_format,id=701)
        self.Bind(wx.EVT_MENU,self.monthly_voice,id=702)
        self.Bind(wx.EVT_MENU,self.monthly_template,id=703)
        self.Bind(wx.EVT_MENU,self.monthly_producer,id=704)
        sm2.Append(705,'Voice',kind=wx.ITEM_NORMAL)
        sm2.Append(706,'Producer',kind=wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU,self.pay_producer,id=706)
        self.Bind(wx.EVT_MENU,self.pay_voice,id=705)
        analt.Append(601, 'Format')
        analt.Append(602, 'Voice')
        analt.Append(603, 'Template')
        analt.Append(604, 'Producer')
        analt.Append(605, 'Voice Format')

        self.Bind(wx.EVT_MENU,self.analt_format,id=601)
        self.Bind(wx.EVT_MENU,self.analt_voice,id=602)
        self.Bind(wx.EVT_MENU,self.analt_template,id=603)
        self.Bind(wx.EVT_MENU,self.analt_producer,id=604)
        self.Bind(wx.EVT_MENU,self.analt_voice_format,id=605)

        analt.AppendMenu(606, 'Monthly Sheets',sm1)
        analt.AppendMenu(607, 'Monthly PayBills',sm2)
        
        menubar.Append(menufile, '&File')
        menubar.Append(createmenu, '&Create')
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
        self.Bind(wx.EVT_MENU,self.adhook,id=209)
        self.Bind(wx.EVT_MENU,self.actslo,id=210)

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

    def adhook(self,event):
        self.new=NewHook(parent=None,id=-1)
        self.new.Show(True)

    def acttemp(self,event):
        self.new=AddTemp()
        self.new.Show(True)

    def actslo(self,event):
        self.new=AddSlo(parent=None,id=-1)
        self.new.Show(True)
    

    def OnQuit(self, event):
        self.Close()

    def OnAbout(self,event):
        dlg = wx.MessageDialog( self, "Developed By SHM\n Version 0.1", "ImageQuick", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    ''' Actions for Batch Operations '''
    def batch_sfp(self,event):
        self.new = Batch_Box(parent=None,id=-1,selector='SFP')
        self.new.Show()

    def batch_sf(self,event):
        self.new = Batch_Box(parent=None,id=-1,selector='SF')
        self.new.Show()

    def batch_s(self,event):
        self.new = Batch_Box(parent=None,id=-1,selector='S')
        self.new.Show()

    def batch_f(self,event):
        self.new = Batch_Box(parent=None,id=-1,selector='F')
        self.new.Show()

    def batch_p(self,event):
        self.new = Batch_Box(parent=None,id=-1,selector='P')
        self.new.Show()
    '''Actions for Analytics'''
    def analt_voice(self,event):
        self.timer=Timer()
        self.timer.Show()
        analytics.chart_voices()
        self.timer.Close()
        self.new = LoadXLS(filelocation='files/voice_analysis.xls',title='Voice Analytics')
        self.new.Show()

    def analt_format(self,event):
        self.timer=Timer()
        self.timer.Show()
        analytics.chart_formats()
        self.timer.Close()
        self.new = LoadXLS(filelocation='files/format_analysis.xls',title='Fomat Analytics')
        self.new.Show()

    def analt_template(self,event):
        self.timer=Timer()
        self.timer.Show()
        analytics.chart_templates()
        self.timer.Close()
        self.new = LoadXLS(filelocation='files/templates_analysis.xls',title='Template Analytics')
        self.new.Show()

    def analt_producer(self,event):
        self.timer=Timer()
        self.timer.Show()
        analytics.chart_producers()
        self.timer.Close()
        self.new = LoadXLS(filelocation='files/producer_analysis.xls',title='Producer Analytics')
        self.new.Show()

    def analt_voice_format(self,event):
        self.timer=Timer()
        self.timer.Show()
        analytics.chart_voice_format()
        self.timer.Close()
        self.new = LoadXLS(filelocation='files/voice_format_analysis.xls',title='Voice-Format Analytics')
        self.new.Show()

    def monthly_voice(self,event):
        self.new = Monthly_Analytics(parent=None,id=-1,selector='voice')
        self.new.Show()

    def monthly_format(self,event):
        self.new = Monthly_Analytics(parent=None,id=-1,selector='format')
        self.new.Show()

    def monthly_producer(self,event):
        self.new = Monthly_Analytics(parent=None,id=-1,selector='producer')
        self.new.Show()

    def monthly_template(self,event):
        self.new = Monthly_Analytics(parent=None,id=-1,selector='template')
        self.new.Show()

    def pay_producer(self,event):
        self.new = Monthly_Analytics(parent=None,id=-1,selector='pay_producer')
        self.new.Show()

    def pay_voice(self,event):
        self.new = Monthly_Analytics(parent=None,id=-1,selector='pay_voice')
        self.new.Show()

'''Batch Opertation Class '''
class Batch_Box(wx.Frame):
    def __init__(self,parent,id,selector):
        self.selector = selector
        wx.Frame.__init__(self,parent,id,'Batch Operation',size=(210,180))
        wx.Frame.CentreOnScreen(self)
        inp=wx.Panel(self,-1,(-1,-1),(-1,-1))
        formats = ui_core.get_format_list()
        voices = ui_core.get_voice_list()
        wx.StaticText(inp,-1,"Select Format",pos=(10,20))
        self.cb = wx.ComboBox(inp, pos=(10, 40), choices=formats,style=wx.CB_READONLY)
        wx.StaticText(inp,-1,"Select Voice",pos=(10,70))
        self.cb2 = wx.ComboBox(inp, pos=(10, 90), choices=voices,style=wx.CB_READONLY)
        but=wx.Button(inp,label='Update',pos=(30,140),size=(65,-1))
        but2=wx.Button(inp,label='Cancel',pos=(110,140),size=(65,-1))
        but.Bind(wx.EVT_BUTTON,self.butact,but)
        but2.Bind(wx.EVT_BUTTON,self.quitwin)


    def butact(self,event):
        format = self.cb.GetValue()
        voice = self.cb2.GetValue()
        selector = self.selector
        self.timer=Timer()
        self.timer.Show()
        if selector == 'SFP':
            voicetotemplate.station_frequency_position(format,voice)
        elif selector == 'SF':
            voicetotemplate.station_frequency(format,voice)
        elif selector == 'S':
            voicetotemplate.station(format,voice)
        elif selector == 'F':
            voicetotemplate.frequency(format,voice)
        elif selector == 'P':
            voicetotemplate.position(format,voice)
        self.timer.Close()
        self.Close()

    def quitwin(self,event):
        self.Close()

class Monthly_Analytics(wx.Frame):
    ''' The Frame for Month and Year Selection'''

    def __init__(self,parent,id,selector):
        self.selector = selector
        wx.Frame.__init__(self,parent,id,'Monthly Analytics',size=(210,220))
        wx.Frame.CentreOnScreen(self)
        inp=wx.Panel(self,-1,(-1,-1),(-1,-1))
        years = ['2013']
        months = ui_core.get_months()
        wx.StaticText(inp,-1,"Select Month",pos=(10,20))
        self.cb = wx.ComboBox(inp, pos=(10, 40), choices=months,style=wx.CB_READONLY)
        wx.StaticText(inp,-1,"Select Year",pos=(10,70))
        self.cb2 = wx.ComboBox(inp, pos=(10, 90), choices=years,style=wx.CB_READONLY)
        but=wx.Button(inp,label='View',pos=(30,140),size=(65,-1))
        but2=wx.Button(inp,label='Cancel',pos=(110,140),size=(65,-1))
        but.Bind(wx.EVT_BUTTON,self.butact,but)
        but2.Bind(wx.EVT_BUTTON,self.quitwin)


    def butact(self,event):
        month = ui_core.get_month_number(str(self.cb.GetValue()))
        year = str(self.cb2.GetValue())
        selector = self.selector
        self.timer=Timer()
        self.timer.Show()
        if selector == 'voice':
            analytics.monthly_voice(month,year)
            self.xl = LoadXLS(filelocation='files/monthly_voices.xls',title="Monthly Voice Analytics")
            self.xl.Show()
        elif selector == 'producer':
            analytics.monthly_producer(month,year)
            self.xl = LoadXLS(filelocation='files/monthly_producers.xls',title="Monthly Producer Analytics")
            self.xl.Show()

        elif selector == 'template':
            analytics.monthly_templates(month,year)
            self.xl = LoadXLS(filelocation='files/monthly_templates.xls',title="Monthly Template Analytics")
            self.xl.Show()

        elif selector == 'format':
            analytics.monthly_format(month,year)
            self.xl = LoadXLS(filelocation='files/monthly_formats.xls',title="Monthly Format Analytics")
            self.xl.Show()

        elif selector == 'pay_producer':
            analytics.pay_producer(month,year)
            self.xl = LoadXLS(filelocation='files/pay_producers.xls',title="")
            self.xl.Show()

        elif selector == 'pay_voice':
            analytics.pay_voice(month,year)
            self.xl = LoadXLS(filelocation='files/pay_voices.xls',title="")
            self.xl.Show()

        self.timer.Close()
        self.Close()


    def quitwin(self,event):
        self.Close()

class MyApp(wx.App):
    def OnInit(self):
        frame = MainFrame(None, -1, 'ImageQuick')
        frame.Show(True)
        #self.SetTopWindow(frame)
        return True

class AddSlo(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Add Slogan Length',size=(400,300))
        wx.Frame.CentreOnScreen(self)
        inp=wx.Panel(self,-1,(-1,-1),(-1,-1))
        wx.StaticText(inp,-1,"Slogan",pos=(40,40))
        self.sl=wx.TextCtrl(inp,-1,"",pos=(120,35),size=(200,30))
        wx.StaticText(inp,-1,"Length",pos=(40,80))
        self.le=wx.TextCtrl(inp,-1,"",pos=(120,75),size=(200,30))
        but=wx.Button(inp,label='Add',pos=(150,130),size=(65,-1)).Bind(wx.EVT_BUTTON,self.butact)

    def butact(self,event):
        slog = {
                'slogan':self.sl.GetValue(),
                'length':self.le.GetValue(),
        }
        print slog

class NewHook(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Add Hooks',size=(400,300))
        wx.Frame.CentreOnScreen(self)
        inp=wx.Panel(self,-1,(-1,-1),(-1,-1))
        formats = ui_core.get_format_list()
        categories = ui_core.get_category_list()
        wx.StaticText(inp,-1,"Hook",pos=(40,40))
        self.hk=wx.TextCtrl(inp,-1,"",pos=(180,35),size=(200,30))
        wx.StaticText(inp,-1,"Select Format",pos=(40,80))
        self.cb = wx.ComboBox(inp, pos=(180, 75), choices=formats,style=wx.CB_READONLY)
        wx.StaticText(inp,-1,"Select Category",pos=(40,120))
        self.cb2 = wx.ComboBox(inp, pos=(180, 115), choices=categories,style=wx.CB_READONLY)
        wx.StaticText(inp,-1,"Normal Length",pos=(40,160))
        self.nl=wx.TextCtrl(inp,-1,"",pos=(180,155),size=(200,30))
        wx.StaticText(inp,-1,"VoiceOver Length",pos=(40,200))
        self.vl=wx.TextCtrl(inp,-1,"",pos=(180,195),size=(200,30))
        but=wx.Button(inp,label='Add',pos=(170,250),size=(65,-1)).Bind(wx.EVT_BUTTON,self.butact)

    def butact(self,event):
        hook = {
                'name':self.hk.GetValue(),
                'format':self.cb.GetValue(),
                'category':self.cb2.GetValue(),
                'vo_length':self.vl.GetValue(),
                'length':self.nl.GetValue(),
                'vo_hook':self.hk.GetValue()+'_VO'
        }
        print hook
        


class IpConnect(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Connect to Server',size=(400,300))
        wx.Frame.CentreOnScreen(self)
        inp=wx.Panel(self,-1,(-1,-1),(-1,-1))
        wx.StaticText(inp,-1,"Server IP",pos=(100,80))
        self.s=wx.TextCtrl(inp,-1,pos=(225,75),size=(150,30))
        wx.StaticText(inp,-1,"PORT",pos=(100,120))
        self.p=wx.TextCtrl(inp,-1,"27017",pos=(225,115),size=(100,30))
        self.p.SetInsertionPoint(0)
        but=wx.Button(inp,label='Connect',pos=(150,150),size=(65,-1))
        but2=wx.Button(inp,label='Cancel',pos=(250,150),size=(65,-1))
        but.Bind(wx.EVT_BUTTON,self.butact,but)
        but2.Bind(wx.EVT_BUTTON,self.quitwin)

    def butact(self,event):
        self.timer=Timer()
        self.timer.Show()
        database.connect(self.s.GetValue(),int(self.p.GetValue()))
        print database.db
        self.timer.Close()
        self.Close()

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
        create.voice(voice) 
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
        create.style(style)
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
        create.frequency(frequency)
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
        create.station(station)
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
        create.position(position)
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
        create.format(format)
        self.Close()

class AddHook( wx.Frame ): 
    def __init__( self ):
        wx.Frame.__init__( self, None,-1, "Add Hook Template", size=(350, 400) )
        scrollWin = wx.PyScrolledWindow( self, -1 )
# Add Code Below
        self.form_list= []
        self.posvoice_list= []
        self.posstyle_list= []
        self.stavoice_list= []
        self.stastyle_list= []
        self.frevoice_list= []
        self.frestyle_list= []
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
            wx.CheckBox(scrollWin,-1,format,pos=(x,y)).Bind(wx.EVT_CHECKBOX, self.check_for)
            y +=20
        wx.StaticText(scrollWin,-1,"SLOGAN DETAILS",pos=(40,y))
        y+=30
        wx.StaticText(scrollWin,-1,"Associated Voices",pos=(40,y))
        u=180
        y+=30
        for voice in ui_core.get_voice_list():
            wx.CheckBox(scrollWin,-1,voice,pos=(u,y)).Bind(wx.EVT_CHECKBOX, self.check_posv)
            y+=20
        y+=30
        wx.StaticText(scrollWin,-1,"Delay/Cue",pos=(40,y))
        y-=5
        self.dq=wx.TextCtrl(scrollWin,-1,"",pos=(180,y),size=(120,30))
        y+=30
        wx.StaticText(scrollWin,-1,"Associated Styles",pos=(40,y))
        ff=180
        y+=30
        for style in ui_core.get_style_list():
            wx.CheckBox(scrollWin,-1,style,pos=(ff,y)).Bind(wx.EVT_CHECKBOX, self.check_poss)
            y+=20
        wx.StaticText(scrollWin,-1,"STATION DETAILS",pos=(40,y))
        y+=30
        wx.StaticText(scrollWin,-1,"Associated Voices",pos=(40,y))
        ss=180
        y+=30
        for voice in ui_core.get_voice_list():
            wx.CheckBox(scrollWin,-1,voice,pos=(ss,y)).Bind(wx.EVT_CHECKBOX, self.check_stav)
            y+=20
        y+=30
        wx.StaticText(scrollWin,-1,"No: of Words",pos=(40,y))
        y-=5
        self.nw=wx.TextCtrl(scrollWin,-1,"",pos=(180,y),size=(120,30))
        y+=40
        wx.StaticText(scrollWin,-1,"Delay/Cue",pos=(40,y))
        y-=5
        self.dc=wx.TextCtrl(scrollWin,-1,"",pos=(180,y),size=(120,30))
        y+=40
        wx.StaticText(scrollWin,-1,"Associated Styles",pos=(40,y))
        cc=180
        y+=30
        for style in ui_core.get_style_list():
            wx.CheckBox(scrollWin,-1,style,pos=(cc,y)).Bind(wx.EVT_CHECKBOX, self.check_stas)
            y+=20
        y+=30
        wx.StaticText(scrollWin,-1,"FREQUENCY DETAILS",pos=(40,y))
        y+=30
        wx.StaticText(scrollWin,-1,"Associated Voices",pos=(40,y))
        ab=180
        y+=30
        for voice in ui_core.get_voice_list():
            wx.CheckBox(scrollWin,-1,voice,pos=(ab,y)).Bind(wx.EVT_CHECKBOX, self.check_frev)
            y+=20
        y+=40
        wx.StaticText(scrollWin,-1,"Delay/Cue",pos=(40,y))
        y-=5
        self.dcc=wx.TextCtrl(scrollWin,-1,"",pos=(180,y),size=(120,30))
        y+=30
        wx.StaticText(scrollWin,-1,"Associated Styles",pos=(40,y))
        xx=180
        y+=30
        for style in ui_core.get_style_list():
            wx.CheckBox(scrollWin,-1,style,pos=(xx,y)).Bind(wx.EVT_CHECKBOX, self.check_fres)
            y+=20
        y=y+20
        wx.StaticText(scrollWin,-1,"POST HOOK Details",pos=(40,y))
        y+=30
        wx.StaticText(scrollWin,-1,"File Name",pos=(40,y))
        y-=5
        self.f1=wx.TextCtrl(scrollWin,-1,"",pos=(180,y),size=(120,30))
        y+=40
        wx.StaticText(scrollWin,-1,"Station Details- Post Hooks",pos=(40,y))
        y+=30
        wx.StaticText(scrollWin,-1,"Delay/Cue",pos=(40,y))
        y=y-5
        self.d1=wx.TextCtrl(scrollWin,-1,"",pos=(180,y),size=(120,30))
        y+=40
        wx.StaticText(scrollWin,-1,"Frequency Details- Post Hooks",pos=(40,y))
        y+=30
        wx.StaticText(scrollWin,-1,"Delay/Cue",pos=(40,y))
        y-=5
        self.d2=wx.TextCtrl(scrollWin,-1,"",pos=(180,y),size=(120,30))
        y+=50
        userbut=wx.Button(scrollWin,label='Add',pos=(120,y),size=(100,-1))
        userbut.Bind(wx.EVT_BUTTON,self.butact,userbut)
        scrollWin.SetScrollbars(1,20,1,140)
        scrollWin.SetScrollRate( 1,5 )

    def check_for(self,e):
        sender = e.GetEventObject()
        if sender.GetValue() == True:
            self.form_list.append(sender.Label)
        else:
            self.form_list.remove(sender.Label)

    def check_posv(self,e):
        sender = e.GetEventObject()
        if sender.GetValue() == True:
            self.posvoice_list.append(sender.Label)
        else:
            self.posvoice_list.remove(sender.Label)

    def check_poss(self,e):
        sender = e.GetEventObject()
        if sender.GetValue() == True:
            self.posstyle_list.append(sender.Label)
        else:
            self.posstyle_list.remove(sender.Label)

    def check_stav(self,e):
        sender = e.GetEventObject()
        if sender.GetValue() == True:
            self.stavoice_list.append(sender.Label)
        else:
            self.stavoice_list.remove(sender.Label)

    def check_stas(self,e):
        sender = e.GetEventObject()
        if sender.GetValue() == True:
            self.stastyle_list.append(sender.Label)
        else:
            self.stastyle_list.remove(sender.Label)

    def check_frev(self,e):
        sender = e.GetEventObject()
        if sender.GetValue() == True:
            self.frevoice_list.append(sender.Label)
        else:
            self.frevoice_list.remove(sender.Label)

    def check_fres(self,e):
        sender = e.GetEventObject()
        if sender.GetValue() == True:
            self.frestyle_list.append(sender.Label)
        else:
            self.frestyle_list.remove(sender.Label)

    def butact(self,event):
        format = {
            'name':self.tn.GetValue(),
            'filename1':self.fn.GetValue(),
            'filename2':self.f1.GetValue(),
            'producer':self.po.GetValue(),
            'formatids':ui_core.get_format_ids(self.form_list),
            'posCue':self.dq.GetValue(),
            'posVoiceids':ui_core.get_voice_ids(self.posvoice_list),
            'posStyleids':ui_core.get_style_ids(self.posstyle_list),
            'statWords':self.nw.GetValue(),
            'statCue1':self.dc.GetValue(),
            'statCue2':self.d1.GetValue(),
            'statVoiceids':ui_core.get_voice_ids(self.stavoice_list),
            'statStyleids':ui_core.get_style_ids(self.stastyle_list),
            'freCue1':self.dcc.GetValue(),
            'freCue2':self.d2.GetValue(),
            'freVoiceids':ui_core.get_voice_ids(self.frevoice_list),
            'freStyleids':ui_core.get_style_ids(self.frestyle_list),
            'price':self.pr.GetValue()
        }
        print format
        #create.format(format)
        self.Close()
#end for

 
#Till Here
        

class AddTemp( wx.Frame ): 
    def __init__( self ):
        wx.Frame.__init__( self, None,-1, "Add a new Template piece", size=(350, 400) )
        scrollWin = wx.PyScrolledWindow( self, -1 )
# Add Code Below
        self.form_list= []
        self.posvoice_list= []
        self.posstyle_list= []
        self.stavoice_list= []
        self.stastyle_list= []
        self.frevoice_list= []
        self.frestyle_list= []
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
            wx.CheckBox(scrollWin,-1,format,pos=(x,y)).Bind(wx.EVT_CHECKBOX, self.check_for)
            y +=20
        wx.StaticText(scrollWin,-1,"SLOGAN DETAILS",pos=(40,y))
        y+=30
        wx.StaticText(scrollWin,-1,"Associated Voices",pos=(40,y))
        u=180
        y+=30
        for voice in ui_core.get_voice_list():
            wx.CheckBox(scrollWin,-1,voice,pos=(u,y)).Bind(wx.EVT_CHECKBOX, self.check_posv)
            y +=20
        y+=20
        wx.StaticText(scrollWin,-1,"No: of Words",pos=(40,y))
        y-=5
        self.nw=wx.TextCtrl(scrollWin,-1,"",pos=(180,y),size=(120,30))
        y+=40
        wx.StaticText(scrollWin,-1,"Delay/Cue",pos=(40,y))
        y-=5
        self.dq=wx.TextCtrl(scrollWin,-1,"",pos=(180,y),size=(120,30))
        y+=40
        wx.StaticText(scrollWin,-1,"Associated Styles",pos=(40,y))
        ff=180
        y+=30
        for style in ui_core.get_style_list():
            wx.CheckBox(scrollWin,-1,style,pos=(ff,y)).Bind(wx.EVT_CHECKBOX, self.check_poss)
            y+=20
        y+=20
        wx.StaticText(scrollWin,-1,"STATION DETAILS",pos=(40,y))
        y+=30
        wx.StaticText(scrollWin,-1,"Associated Voices",pos=(40,y))
        ss=180
        y+=30
        for voice in ui_core.get_voice_list():
            wx.CheckBox(scrollWin,-1,voice,pos=(ss,y)).Bind(wx.EVT_CHECKBOX, self.check_stav)
            y +=20
        y+=30
        wx.StaticText(scrollWin,-1,"No: of Words",pos=(40,y))
        y-=5
        self.nw1=wx.TextCtrl(scrollWin,-1,"",pos=(180,y),size=(120,30))
        y+=40
        wx.StaticText(scrollWin,-1,"Delay/Cue",pos=(40,y))
        self.dc=wx.TextCtrl(scrollWin,-1,"",pos=(180,y),size=(120,30))
        y+=30
        wx.StaticText(scrollWin,-1,"Associated Styles",pos=(40,y))
        cc=180
        y+=30
        for style in ui_core.get_style_list():
            wx.CheckBox(scrollWin,-1,style,pos=(cc,y)).Bind(wx.EVT_CHECKBOX, self.check_stas)
            y +=20
        y+=10
        wx.StaticText(scrollWin,-1,"FREQUENCY DETAILS",pos=(40,y))
        y+=20
        wx.StaticText(scrollWin,-1,"Associated Voices",pos=(40,y))
        ab=180
        y+=20
        for voice in ui_core.get_voice_list():
            wx.CheckBox(scrollWin,-1,voice,pos=(ab,y)).Bind(wx.EVT_CHECKBOX, self.check_frev)
            y +=20
        y+=20
        wx.StaticText(scrollWin,-1,"Delay/Cue",pos=(40,y))
        y=y-5
        self.dcc=wx.TextCtrl(scrollWin,-1,"",pos=(180,y),size=(120,30))
        y+=30
        wx.StaticText(scrollWin,-1,"Associated Styles",pos=(40,y))
        xx=180
        y+=30
        for style in ui_core.get_style_list():
            wx.CheckBox(scrollWin,-1,style,pos=(xx,y)).Bind(wx.EVT_CHECKBOX, self.check_fres)
            y +=20
        y+=30
        userbut=wx.Button(scrollWin,label='Add',pos=(130,y),size=(100,-1))
        userbut.Bind(wx.EVT_BUTTON,self.butact,userbut)
        scrollWin.SetScrollbars(1,20,1,120)
        scrollWin.SetScrollRate( 1, 1 )        

    def check_for(self,e):
        sender = e.GetEventObject()
        if sender.GetValue() == True:
            self.form_list.append(sender.Label)
        else:
            self.form_list.remove(sender.Label)

    def check_posv(self,e):
        sender = e.GetEventObject()
        if sender.GetValue() == True:
            self.posvoice_list.append(sender.Label)
        else:
            self.posvoice_list.remove(sender.Label)

    def check_poss(self,e):
        sender = e.GetEventObject()
        if sender.GetValue() == True:
            self.posstyle_list.append(sender.Label)
        else:
            self.posstyle_list.remove(sender.Label)

    def check_stav(self,e):
        sender = e.GetEventObject()
        if sender.GetValue() == True:
            self.stavoice_list.append(sender.Label)
        else:
            self.stavoice_list.remove(sender.Label)

    def check_stas(self,e):
        sender = e.GetEventObject()
        if sender.GetValue() == True:
            self.stastyle_list.append(sender.Label)
        else:
            self.stastyle_list.remove(sender.Label)

    def check_frev(self,e):
        sender = e.GetEventObject()
        if sender.GetValue() == True:
            self.frevoice_list.append(sender.Label)
        else:
            self.frevoice_list.remove(sender.Label)

    def check_fres(self,e):
        sender = e.GetEventObject()
        if sender.GetValue() == True:
            self.frestyle_list.append(sender.Label)
        else:
            self.frestyle_list.remove(sender.Label)

    def butact(self,event):
        format = {
            'statCue':self.dc.GetValue(),
            'name':self.tn.GetValue(),
            'producer':self.po.GetValue(),
            'posCue':self.dq.GetValue(),
            'price':self.pr.GetValue(),
            'statWords':self.nw1.GetValue(),
            'filename':self.fn.GetValue(),
            'freCue':self.dcc.GetValue(),
            'length':self.le.GetValue(),
            'formatids':ui_core.get_format_ids(self.form_list),
            'freStyleids':ui_core.get_style_ids(self.frestyle_list),
            'freVoiceids':ui_core.get_voice_ids(self.frevoice_list),
            'statStyleids':ui_core.get_style_ids(self.stastyle_list),
            'posVoiceids':ui_core.get_voice_ids(self.posvoice_list),
            'posStyleids':ui_core.get_style_ids(self.posstyle_list),
            'statVoiceids':ui_core.get_voice_ids(self.stavoice_list),
            'posWords':self.nw.GetValue(),
        }
        print format
        #create.format(format)
        self.Close()

#end for

 
#Till Here


class LoadXLS(wx.Frame):
 
    #----------------------------------------------------------------------
    def __init__(self,filelocation,title):
        wx.Frame.__init__(self, None, wx.ID_ANY, title,size=(500,400))
        wx.Frame.CentreOnScreen(self)
        panel = wx.Panel(self, wx.ID_ANY)
 
        filename = filelocation
        book = xlrd.open_workbook(filename, formatting_info=1)
        sheetname = "sheet1"
        sheet = book.sheet_by_name(sheetname)
        rows, cols = sheet.nrows, sheet.ncols
        comments, texts = XG.ReadExcelCOM(filename, sheetname, rows, cols)
 
        xlsGrid = XG.XLSGrid(panel)
        xlsGrid.PopulateGrid(book, sheet, texts, comments)
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(xlsGrid, 1, wx.EXPAND, 5)
        panel.SetSizer(sizer)

class Timer(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Please Wait...', size=(250, 100))
        wx.Frame.CentreOnScreen(self)
        panel = wx.Panel(self, -1)
        wx.StaticText(panel, -1, " Please Wait...")
        self.count = 0
        self.gauge = wx.Gauge(panel, -1,100,(25,35), (200, 25))
        self.gauge.SetBezelFace(3)
        self.gauge.SetShadowWidth(3)
        self.Bind(wx.EVT_IDLE, self.OnIdle)


    def OnIdle(self, event):
        print "*"
        self.gauge.Pulse()

app = MyApp(0)
app.MainLoop()





##################################################################
############### CODE BY SADDAM HUSSAIN MAJEED ####################
###############     QUADLOOPS TECHNOLOGIES    ####################
##################################################################