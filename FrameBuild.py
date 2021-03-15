# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Titip.in", pos = wx.DefaultPosition, size = wx.Size( 1280,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 213, 229, 249 ) )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_panel13 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel13.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		bSizer9.SetMinSize( wx.Size( -1,720 ) )
		self.m_button25 = wx.Button( self.m_panel13, wx.ID_ANY, u"Home", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button25, 0, wx.ALL, 5 )

		self.m_button56 = wx.Button( self.m_panel13, wx.ID_ANY, u"Lihat", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button56, 0, wx.ALL, 5 )

		self.m_button26 = wx.Button( self.m_panel13, wx.ID_ANY, u"Buat Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button26, 0, wx.ALL, 5 )

		self.m_button27 = wx.Button( self.m_panel13, wx.ID_ANY, u"Ubah Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button27, 0, wx.ALL, 5 )

		self.m_button28 = wx.Button( self.m_panel13, wx.ID_ANY, u"HapusData", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button28, 0, wx.ALL, 5 )


		self.m_panel13.SetSizer( bSizer9 )
		self.m_panel13.Layout()
		bSizer9.Fit( self.m_panel13 )
		fgSizer2.Add( self.m_panel13, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel14 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText5 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"Selamat datang, Jessica Maya Berlianasari!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		self.m_staticText5.SetFont( wx.Font( 32, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Raleway SemiBold" ) )
		self.m_staticText5.SetForegroundColour( wx.Colour( 0, 70, 215 ) )

		bSizer10.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.m_staticText51 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"NIM 192410101030", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		self.m_staticText51.SetFont( wx.Font( 24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Raleway Medium" ) )
		self.m_staticText51.SetForegroundColour( wx.Colour( 144, 144, 144 ) )

		bSizer10.Add( self.m_staticText51, 0, wx.ALL, 5 )

		self.m_staticText511 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"Hello, wx!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText511.Wrap( -1 )

		self.m_staticText511.SetFont( wx.Font( 22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Raleway" ) )
		self.m_staticText511.SetForegroundColour( wx.Colour( 80, 80, 80 ) )

		bSizer10.Add( self.m_staticText511, 0, wx.ALL, 5 )


		self.m_panel14.SetSizer( bSizer10 )
		self.m_panel14.Layout()
		bSizer10.Fit( self.m_panel14 )
		fgSizer2.Add( self.m_panel14, 1, wx.EXPAND |wx.ALL, 25 )


		self.SetSizer( fgSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


