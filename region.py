#Alexander Nissen

#Definerer en klasse Region
class Region():
    #Definerer kontroktoren som tar i mot regionNavn, regionKode og en liste over landene som skal i regionen
    def __init__(self, regionNavn, regionKode, landList):
        #Definerer instansvariabelen antallSmittede som holder antall smittede i regionen
        self._antallSmittede = 0
        #Definerer en instansvariabel som holder navnet pa regionen
        self._regionNavn = regionNavn
        #Definerer en var som holder regionkoden
        self._regionKode = regionKode
        #Definerer en var som skal holde listen med land
        self._landList = landList
        #Definerer en liste som skal holde unike landskoder
        self._updatedLandList = []
        #Gar gjennom listen med land
        for land in self._landList:
            #Lager en var som holder landskoden
            landId = land[0]
            #Sjekker om koden er i unik listen
            if landId in self._updatedLandList:
                #Dersom den finnes der passer vi bare
                pass
            else:
                #Dersom den ikke finnes i listen, legges landskoden til der
                self._updatedLandList.append(landId)
    #Definerer en metode som tar i mot antall og legger det til antallSmittede i regionen
    def addSmitte(self, antall):
        self._antallSmittede += antall
    #Definerer en metode som returnerer antallSmittede
    def hentAntallRegion(self):
        return self._antallSmittede
    #Definerer en metode som returnerer regionskoden
    def hentRegionKode(self):
        return self._regionKode
    #Definerer en metode som returnerer listen over unike landskoder
    def hentLand(self):
        return self._updatedLandList
    #Definerer en metode som returnerer listen med objektene
    def hentAllInfo(self):
        return self._landList
