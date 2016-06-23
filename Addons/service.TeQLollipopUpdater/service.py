import xbmc, xbmcaddon, xbmcgui, xbmcplugin, os, sys
import urllib2, urllib

path = xbmc.translatePath('special://home/addons/service.TeQWinUpdater')

installed = xbmc.translatePath("special://home/addons/service.TeQLollipopUpdater/installed_version.txt")
latest = xbmc.translatePath("special://home/addons/service.TeQLollipopUpdater/latest_version.txt")

def path():
	if not os.path.exists(path):
		os.mkdir(path)

url = 'http://teqiqtv.us/Teqiq/TeQ%20IQ%20Update/Lollipop/latest_version.txt'
urllib.urlretrieve(url, latest)


file_i = open(installed)
file_i.close()

file_l = open(latest, 'r')
checksum_latest = file_l.read()
file_l.close()

def check(checksum):
	datafile = file(installed)
	updated = False
	for line in datafile:
		if checksum in line:
			updated = True
			break
	return updated

def wizard():
	choice = xbmcgui.Dialog().yesno('Updater for TeQ I.Q. TV', 'Update available for TeQ I.Q. TV', 'Select OK to start updating', nolabel='Cancel',yeslabel='OK')
	if choice == 0:
		return
	elif choice == 1:
		#xbmc.executebuiltin("RunAddon(plugin.video.teqiqwizard)")
		xbmc.executebuiltin('ActivateWindow(10025,plugin://plugin.program.teqiqwizard/?url=http://teqiqtv.us/Teqiq/TeQ%20IQ%20Update/Lollipop/Lollipop.zip&mode=1&name=UPDATE&iconimage=http://teqiqtv.us/Teqiq/Repo/fanart.jpg)')
		file_i = open(installed, "w")
		file_i.write(checksum_latest)
		file_i.close()
		file_i = open(installed)
		checksum_updated = file_i.read()
		file_i.close()

if check(checksum_latest):
	xbmc.sleep(1000)
else:
	wizard()
