import wx
import random

class Example(wx.Dialog):
    
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)
        
        self.InitUI()
        
    def InitUI(self):
        
        images = ['sid1.png', 'sid2.png', 'sid3.png', 'sid4.png', 
                'sid5.png', 'sid6.png', 'sid7.png', 'sid8.png']

        self.pos = [ [0, 1, 2], [3, 4, 5], [6, 7, 8] ]

        self.sizer = wx.GridSizer(3, 3, 0, 0)

        numbers = [0, 1, 2, 3, 4, 5, 6, 7]
        random.shuffle(numbers)

        for i in numbers:
            
                btn = wx.BitmapButton(self, i, wx.Bitmap(images[i]))
                btn.Bind(wx.EVT_BUTTON, self.OnPressButton, btn)
                self.sizer.Add(btn)

        self.empty = wx.BitmapButton(self, bitmap=wx.Bitmap('1.png'))
        self.empty.Bind(wx.EVT_BUTTON, self.OnPressButton, self.empty)
        self.sizer.Add(self.empty)

        self.SetSizerAndFit(self.sizer)
        self.SetTitle('Puzzle')
        self.Centre()
        self.ShowModal()
        self.Destroy()

    def OnPressButton(self, e):
        
        btn = e.GetEventObject()
        
        width = self.empty.GetSize().x
        height = self.empty.GetSize().y

        btnX = btn.GetPosition().x
        btnY = btn.GetPosition().y
        emptyX = self.empty.GetPosition().x
        emptyY = self.empty.GetPosition().y
    
        
        if (((btnX == emptyX) and (emptyY - btnY) == height)
          or ((btnX == emptyX) and (emptyY - btnY) == -height)
          or ((btnY == emptyY) and (emptyX - btnX) == width)
          or ((btnY == emptyY) and (emptyX - btnX) == -width)):
                 
            self.ExchangeImages(btn)

            
    def ExchangeImages(self, btn):
        
        bmp1 = self.empty.GetBitmapLabel()
        bmp2 = btn.GetBitmapLabel()
        
        self.empty.SetBitmapLabel(bmp2)
        btn.SetBitmapLabel(bmp1)
        
        self.empty = btn        


def main():
    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main()  