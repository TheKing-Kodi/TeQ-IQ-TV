#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import xbmc,xbmcgui,xbmcaddon

while 1 :
	macadress = xbmc.getInfoLabel('Network.MacAddress')	
	if macadress != "Busy" and macadress != "" :
		break
xbmcgui.Dialog().ok("Mac Adress", "" + macadress.replace(":","-"))