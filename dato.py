#Alexander Nissen
#Importerer datetime bibli.
import datetime

#Oppretter en klasse Dato
class Dato():
    #Initierer konstruktoren med parametere ar,mnd og dag som er forventet a vare heltall
    def __init__(self, ar, mnd, dag):
        self._ar = ar
        self._mnd = mnd
        self._dag = dag
    #Definerer en metode som heter hentdato
    def hentDato(self):
        #Definerer en variabel dato som oppretter en dato
        dato = datetime.datetime(int(self._ar), int(self._mnd), int(self._dag))
        #Returnerer denne datoen
        return dato
    #Definerer en metode hentHelTall
    def hentHelTall(self):
        #Returnerer instansvariablene self.ar og self.dag
        return self._ar,self._mnd,self._dag
