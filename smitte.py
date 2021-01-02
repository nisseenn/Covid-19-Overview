#Alexander Nissen

#Definerer en klasse Smitte
class Smitte():
    #Lager konstroktoren, den tar i mor dato og smittede
    def __init__(self, dato, smittede):
        #Lager instansvariabelen som holder dato
        self._dato = dato
        #instansvariabel for smittede
        self._smittede = smittede
        #Lager de ulike instansvariabelene som kan brukes dersom flere funksjoner skal implementeres
        self._antallTestet = None
        self._antallInnlagt = None
        self._antallResp = None
        self._antallDod = None
    #Definerer en metode som returnerer dato og smittede
    def hentInfo(self):
        return self._dato,self._smittede
    #Definerer en metode som henter smittede (vet det er duplikat)
    def hentSmittede(self):
        return self._smittede
