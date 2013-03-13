#!/usr/bin/python

import wx

class FicheFrame( wx.Frame ) :

    def __init__( self ) :

        wx.Frame.__init__( self, None,-1, "FicheFrame", size=(300, 400) )

        scrollWin = wx.PyScrolledWindow( self, -1 )

        x = 20       # Magic numbers !?
        y = 20
        for i in range( 50 ) :

            txtStr = " Text %02d  : " % (i+1)
            stTxt = wx.StaticText( scrollWin, -1, txtStr, pos=(x, y) )
            
            w, h = stTxt.GetSize()
            txtCtrl = wx.TextCtrl( scrollWin, -1, pos=(x+w+5, y) )
            
            dy = h + 10     # calculate for next loop
            y += dy

        #end for

        scrollWin.SetScrollbars( 0, dy,  0, y/dy+1 )
        scrollWin.SetScrollRate( 1, 1 )      # Pixels per scroll increment

    #end __init__ def

#end class

if __name__ == '__main__' :

    myapp = wx.App( redirect=False )

    myAppFrame = FicheFrame()
    myAppFrame.Show()

    myapp.MainLoop()