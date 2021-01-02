#Alexander Nissen

#Definerer en klasse Land
class Land():
    #Definerer en konstroktor som far parameterene id og navn
    def __init__(self, id, navn):
        #Definerer instansvariablene id,navn og antallSmittede
        self._id = id
        self._navn = navn
        self._antallSmittede = 0
    #Definerer en metode som tar i mot objektet og antall smittede som skal legges til
    def addSmittede(self, antall):
        #Legger til antallet til tallet som er i antallSmittede
        self._antallSmittede += antall
    #Definerer en metode hentAntallSmittede
    def hentAntallSmittede(self):
        #Returnerer antallSmittede
        return self._antallSmittede
    #Definerer en metode hentLandId som returnerer id-en til landet
    def hentLandId(self):
        return self._id
    #Definerer en metode hentLandNavn som returnerer navnet til objektet.
    def hentLandNavn(self):
        return self._navn
