import os

def downAudio(self):
		extension = '%(title)s.%(ext)s'
		url = str(self.url.get())
		ini = str(self.ini.get())
		fin = str(self.fin.get())
		ruta = str(self.ruta.get())+"/"
		if ruta == "/":
			os.system('youtube-dl -i --extract-audio --audio-format mp3 -o "'+extension+'" --playlist-start '+ini+' --playlist-end '+fin+' "'+url+'"')
		else:
			os.system('youtube-dl -i --extract-audio --audio-format mp3 -o "'+ruta+extension+'" --playlist-start '+ini+' --playlist-end '+fin+' "'+url+'"')

def instalar(self):
    	so = sys.platform
        if so == 'linux2':
            os.system('sudo apt-get install youtube-dl')
        elif so == 'darwin':
            os.system('sudo easy-install install youtube-dl')
