from pygame import mixer
class player:
    #atributo
    archivo = None
    #constructor
    def __init__(self, archivo):
        self.archivo = archivo
        mixer.init()
        mixer.music.load(archivo)
    def play(self):
        mixer.music.play()
        return "Reproduciendo música..."
    def pause(self):
        mixer.music.pause()
        return "La mùsica se ha pausado."
    def stop(self):
        mixer.music.stop()
        return "La música se detuvo."
    def volume(self, v):
        mixer.music.set_volume(v)
        return "Definiendo el volùmen a {}".format(v)

