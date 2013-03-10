import wx


class Example(wx.Frame):
           
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw) 
        
        self.InitUI()
        
    def InitUI(self):   

        pnl = wx.Panel(self)
        
        wx.StaticBox(pnl, label='Personal Info', pos=(5, 5), size=(240, 170))
        wx.CheckBox(pnl, label='Male', pos=(15, 30))
        wx.CheckBox(pnl, label='Married', pos=(15, 55))
        wx.StaticText(pnl, label='Age', pos=(15, 95))
        wx.SpinCtrl(pnl, value='1', pos=(55, 90), size=(60, -1), min=1, max=120)
        
        btn = wx.Button(pnl, label='Ok', pos=(90, 185), size=(60, -1))

        btn.Bind(wx.EVT_BUTTON, self.OnClose)

        self.SetSize((270, 250))
        self.SetTitle('Static box')
        self.Centre()
        self.Show(True)          
        
    def OnClose(self, e):
        
        self.Close(True)    
               
        
def main():
    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main()   
