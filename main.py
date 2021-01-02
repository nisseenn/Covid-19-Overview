#Alexander Nissen
#Importerer biblioteker
from datetime import datetime, timedelta
import re
import random
import glob, os
import matplotlib.pyplot as plt
import numpy as np
#Importerer de ulike klassene
from dato import Dato
from land import Land
from smitte import Smitte
from region import Region
#Definerer en ordbok som holder regioner
region = {}
#Definerer en funksjon hovedprogram
def hovedprogram():
    #Pa grunn av usikkerhet om det fungerer pa deres maskiner kommenterer jeg det som er under ut!
    #Gjerne prov a uncomment det, da det skal finne tilgjengelige txt filer i dir deres

    #Finner pathen til dir som man er i
    # path = os.getcwd()
    # #Setter os til den directorien
    # os.chdir(path)
    # #Printer menneskesetning og space
    # print("\n")
    # print("Du har folgende txt filer i mappen: ")
    # #Sjekker hvilke filer som finnes i dir som er txt filer
    # for file in glob.glob("*.txt"):
    #     #Printer alle filene med txt filending
    #     print(file)
    #
    # print("\n")

    #Printer menneskesetning med input for a gi bruker muligheten til a velge fil
    print("Oppgi navnet paa filen med smittedata som du vil lese inn i programmet")
    fileToRead = input()
    #Apner denne filen som bruker velger
    f = open(fileToRead, "r")

    land = {}
    datoer = []
    #Gar gjennom listen
    for x in f:
        #lager et nytt element i array for hvert komma
        infoDeltOpp = x.split(",")
        #Gar gjennom listen
        for index,t in enumerate(infoDeltOpp):
            #Sjekker om anforselstegn finnes i elementet i listen
            if '"' in t:
                #Fjerner anforselstegn
                infoDeltOpp[index] = t.replace('"', '')
        #Slettes siste element i listen
        del infoDeltOpp[-1]

        #Lager dato som er forstaelig for klassen
        midl = re.compile("([a-zA-Z]+)([0-9]+)")
        mnd = midl.match(infoDeltOpp[2]).group(1)
        dag = midl.match(infoDeltOpp[2]).group(2)
        ar = int(infoDeltOpp[3])

        #Konverterer mnd til int format ved a sjekke hva de de er i tekstformat
        if mnd == "Jan":
            mnd = 1
        if mnd == "Feb":
            mnd = 2
        if mnd == "Mar":
            mnd = 3
        if mnd == "Apr":
            mnd = 4
        if mnd == "May":
            mnd = 5
        if mnd == "Jun":
            mnd = 6
        if mnd == "Jul":
            mnd = 7
        if mnd == "Aug":
            mnd = 8
        if mnd == "Sep":
            mnd = 9
        if mnd == "Oct":
            mnd = 10
        if mnd == "Nov":
            mnd = 11
        if mnd == "Dec":
            mnd = 12

        #Definerer en dato
        dato = datetime(ar, int(mnd), int(dag))

        #Sjekker om datoen finnes i listen over unike datoer
        if dato in datoer:
            #Hvis den finnes der, skal den ikke legges til i listen
            pass
        #Hvis den ikke finnes blir den lagt til i listen over unike datoer
        else:
            datoer.append(dato)

        #Henter ut koden for landet
        id = infoDeltOpp[1]
        #Sjekker om koden finnes i ordboken land
        if id in land:
            #Dersom den gjor det legges ny info om land og antall smittede til
            land[id].append([infoDeltOpp[0], infoDeltOpp[4], dato])
        else:
            #Hvis den ikke er i listen legges det til et nytt key value par med key=landskoden og value til navnet pa landet og antall smittede
            land[infoDeltOpp[1]] = [[infoDeltOpp[0], infoDeltOpp[4], dato]]

    #Gar gjennom datoer i datoer listen
    for index,datoz in enumerate(datoer):
        #Setter variabelen ar lik det man far fra a datetime konvertert
        ar = datoz.strftime("%Y")
        #Setter variabelen mnd lik det man far fra mnd datetime konvertert
        mnd = datoz.strftime("%m")
        #Setter dag lik det datetime konvertert
        dag = datoz.strftime("%d")
        #Lager datoobjekt pa datoer
        nyDato = Dato(ar,mnd,dag)
        #Setter key i datoer ordboken lik den nye datoen som er et objekt
        datoer[index] = nyDato

    #Leser fra land ordboken
    for key,value in land.items():
        #Setter navn lik obj i value
        navn = value[0][0]
        #Lager et landobjekt med key og navnet til landet
        landObj = Land(key,navn)
        #Gar gjennom elementene i value
        for elements in value:
            #Gar gjennom datoene i datoer
            for dates in datoer:
                #Sjekker om datoen i ordboken er lik som datoen til objektet
                if elements[2] == dates.hentDato():
                    #Hvis den er lik settes den lik datoobjektet
                    elements[2] = dates
            #Lager et smitteobjekt med dato og smittetall
            smittede = Smitte(elements[2],int(elements[1]))
            #Henter ut info om objektet
            datoSmittede,antallSmittede = smittede.hentInfo()
            #Legger til info om smitte i landobjektet
            landObj.addSmittede(antallSmittede)
            #Setter elementet lik objektet smitte
            elements[1] = smittede
            #Setter landinfo lik landobjektet
            elements[0] = landObj
    #Printer menyvalgene
    #Den ene funksjonen er ikke utarbeidet og derfor ikke aktiv i koden
    print("Trykk c for a skrive ut data for et land du velger")
    print("Trykk d for a skrive ut smittedata for alle land pa en gitt dato")
    print("Trykk g for a opprette en region med smittedata for en gruppe land")
    print("Trykk m for a finne hvilken dato smitten okte mest for en region")
    # print("Trykk n for a legge til ny info i databasen")
    print("Trykk p for a plotte smittegrafene for et gitt land")
    print("Trykk q for a avslutte")
    print("Trykk r for a fjerne alle smitteobjekter med smittetall 0 som kommer tidligere enn forste dag med smitte")
    print("Trykk w for a skrive ut data pa fil som kan brukes som input til programmet")
    #Lager en var som holder den brukeren skriver inn
    userChoice = input()
    #Dersom userChoice ikke er q gar vi inn i whileloopen
    while userChoice != "q":
        #Sjekker om userChoice er d
        if userChoice == "d":
            #Dersom den er d printer vi brukerinput for a fa aar,mnd og dag
            print("Skriv inn aar i tall: ")
            userAr = input()
            print("Skriv inn mnd i tall: ")
            userMnd = input()
            print("Skriv inn dag i tall: ")
            userDag = input()
            #Kaller funksjonen hentSmittedeDato og gir den landordboken og brukerinput
            hentSmittedeDato(land, userAr, userMnd, userDag)
        #Sjekker om userChoice er r
        if userChoice == "r":
            #Kaller funksjonen fjernSmitteTall
            fjernSmitteTall(land)
        #Sjekker om userChoice er g
        if userChoice == "g":
            #Dersom den er g, printer vi input til brukeren
            print("Skriv inn navn paa regionen: ")
            userRegion = input()
            print("Skriv inn kode for regionen: ")
            userKode = input()
            print("Skriv inn antall land du vil legge til: ")
            numOfLand = input()

            #Definerer en liste som skal holde landene som skal legges til i regionen
            landListe = []
            #Printer menneskesetning som forteller hvordan de skal legges inn
            print("Skriv inn navn: ")
            print("VIKITG: SKRIV LANDET PA ENGELSK")
            #Lager for loop som kjorer x antall basert pa brukerinput
            for index,x in enumerate(range(0,int(numOfLand))):
                #Lager input for hvilke land som skal legges til
                print("Land #" + repr(index + 1) + ":")
                landInput = input()
                #Legger til stringen i listen landListe
                landListe.append(landInput)
            #Kaller funksjonen opprettRegion som far landordboken og userinput
            opprettRegion(land, userRegion, userKode, landListe)
        #Sjekker om userChoice er m
        if userChoice == "m":
            #Printer space
            print("\n")
            #Printer menneskesetning
            print("Her er listen over regioner")
            #Gar gjennom regionordboken
            for key,value in region.items():
                #Printer liste over regioner
                print(" - " + value.hentRegionKode())
            #Printer space
            print("\n")
            #Printer userinput for a velge regionskode
            print("Skriv inn kode pa regionen du vil se statistikk om")
            userKode = input()
            #Kaller findHighest funksjonen og gir den regionskoden som bruker oppgir
            findHighest(userKode)
        #Sjekker om userChoice er w
        if userChoice == "w":
            #Kaller funksjonen skrivTilFil
            skrivTilFil(land)
        #Sjekker om userChoice er c
        if userChoice == "c":
            #Printer menneskesetning som gir info om hvordan soke pa land
            print("Skriv inn landet du vil hente data om: ")
            print("VIKITG: SKRIV LANDET PA ENGELSK")
            userLand = input()
            #Kaller funksjonen skrivUtLand og gir ordboken land og userinput som argument
            skrivUtLand(land, userLand)
        #Sjekker om userChoice er p
        if userChoice == "p":
            #Printer menneskesetning om hvordan land som skal plottes
            print("Skriv inn landet du vil plotte")
            print("VIKITG: SKRIV LANDET PA ENGELSK")
            userLand = input()
            #Kaller pa funksjonen plotLand og gir userinput og ordboken
            plotLand(land,userLand)
        #Printer menyvalgene
        #Den ene funksjonen er ikke utarbeidet og derfor ikke aktiv i koden
        print("Trykk c for a skrive ut data for et land du velger")
        print("Trykk d for a skrive ut smittedata for alle land pa en gitt dato")
        print("Trykk g for a opprette en region med smittedata for en gruppe land")
        print("Trykk m for a finne hvilken dato smitten okte mest for en region")
        # print("Trykk n for a legge til ny info i databasen")
        print("Trykk p for a plotte smittegrafene for et gitt land")
        print("Trykk q for a avslutte")
        print("Trykk r for a fjerne alle smitteobjekter med smittetall 0 som kommer tidligere enn forste dag med smitte")
        print("Trykk w for a skrive ut data pa fil som kan brukes som input til programmet")
        #Oppdaterer userChoice med det nye valget til brukeren
        userChoice = input()

#Definerer en funksjon som tar ordboken og userinput som parameter
def hentSmittedeDato(ordbok, userAr, userMnd, userDag):
    #Gjor om datoen til bruker til en dato som kan sammenlignes med objektene lagret som dato
    userDato = datetime(int(userAr), int(userMnd), int(userDag))
    #Printer space
    for x in range(0,3):
        print("\n")
    #Printer ut menneskesetning for dato valgt
    print("Dato valgt: " + str(userDato))
    #Gar gjennom ordboken
    for key,value in ordbok.items():
        #Gar gjennom listene i de gitte key/value parene
        for elements in value:
            #Sjekker om brukerdatoen oppgitt er lik noen i ordboken
            if userDato == elements[2].hentDato():
                #Hvis den matcher en dato, hentes info om dato og smittetall ut og printes til terminal
                dato, smittetall = elements[1].hentInfo()
                print(elements[0].hentLandNavn() + ": " + repr(smittetall))
    #Printer space
    for x in range(0,3):
        print("\n")
#Definerer en funksjon fjernSmitteTall
def fjernSmitteTall(ordbok):
    #Gar gjennom ordboken
    for key,value in ordbok.items():
        #Lager en liste som skal holde alle elementene med smittetall = 0
        elementsNull = []
        #Lager en liste som skal holde elementene med smittetall som ikke er 0
        elementsNotNull = []
        #Lager liste som skal holde elementene som skal slettes
        elementsToDelete = []
        #Gar gjennom elementene i ordboken i det gitte key/value paret
        for elements in value:
            #Sjekker om antallSmittede er storre enn 0
            if elements[1].hentSmittede() > 0:
                #Hvis det er sant legges elementet til i listen med elementer som har smittetall storre enn null
                elementsNotNull.append(elements)
            #Hvis den ikke er storre enn null, kan vi anta at den er 0
            else:
                #Legger den da til i listen med elementer med smittetall 0
                elementsNull.append(elements)

        #Lager en variabel som skal holde laveste dato av de elementene med smittetall storre enn null
        #Setter den forste datoen som verdi forst, bare for a ha et utgangspunkt
        lavesteDatoMedSmitte = elementsNotNull[0][2].hentDato()
        #Gar gjennom elementene i listen
        for obj in elementsNotNull:
            #Sjekker om datoen til elementet er mindre enn lavesteDatoMedSmitte variabelen
            if obj[2].hentDato() < lavesteDatoMedSmitte:
                #Dersom den er det settes denne til laveste dato
                lavesteDatoMedSmitte = obj[2].hentDato()
        #Gar gjennom listen med elementer
        for objects in elementsNull:
            #Sjekker om datoen er lavere enn laveste dato med smittetall som er storre enn 0
            if objects[2].hentDato() < lavesteDatoMedSmitte:
                #Hvis den er det legges disse elementene inn i listen som holder elementer som skal slettes fra ordboken
                elementsToDelete.append(objects)

        #Printer et par spaces
        for x in range(0,3):
            print("\n")
        print("Fjernet " + repr(len(elementsToDelete)) + " objekter fra land: " + str(key))
        #Printer et par spaces
        for x in range(0,3):
            print("\n")

        #Gar gjennom listen
        for objectDel in elementsToDelete:
            #Henter ut datoen til objektet
            objDelDato = objectDel[2].hentDato()
            #Gar gjennom value i key/value paret, legger til index, slik at vi kan slette elementet ved a bruke hvor det er i arrayet
            for index,element in enumerate(value):
                #Sjekker om datoen til objektet er likt som det i ordboken
                if element[2].hentDato() == objDelDato:
                    #Sletter dette elementet i ordboken dersom den matcher
                    del value[index]

#Oppretter en funksjon som tar i mot brukerinput om region og liste over land som er med i regionen
def opprettRegion(ordbok, userRegion, userKode, landListe):
    #Definerer en liste som skal holde landene som skal utgjore regionen
    listOfLand = []
    #Gar gjennom listen fra brukeren
    for userLand in landListe:
        #Gar gjennom ordboken
        for key,value in ordbok.items():
            #Gar gjennom listene i de gitte key/value parene
            for elements in value:
                #Lager en variabel som holder verdien til navnet paa landet i ordboken
                landNavn = elements[0].hentLandNavn()
                #Sjekker om landet oppgitt av brukeren finnes i ordboken
                if userLand == landNavn:
                    #Legger til elementet med land,smitte og dato i listen
                    listOfLand.append(elements)

    #Lager et regionobjekt som far parameterene som brukeren tastet inn, samt listen over land som er med, denne gangen med objekter
    regionObj = Region(userRegion, userKode, listOfLand)
    #Henter land som er i regionen
    hentAlleLand = regionObj.hentLand()

    #Gar gjennom listen med land
    for alleLand in hentAlleLand:
        #Henter antall smittede i landet totalt
        antallPrLand = alleLand.hentAntallSmittede()
        #Kaller pa metoden som legger sammen landenes totale smittetall
        regionObj.addSmitte(antallPrLand)

    #Printer et par linjer for space
    for x in range(0,2):
        print("\n")

    # #Printer menneskesetning som forteller hvilken region som er opprettet
    print("Region: " + userRegion + ", opprettet! " + " Land som er med i regionen: ")
    #Gar gjennom listen, med index, for a fa iterasjonstall
    for index,x in enumerate(hentAlleLand):
        #Printer hvilke land som er med i regionen i en numerert liste
        print("#" + repr(index +1 ) + " " + x.hentLandNavn())
    #Printer menneskesetning som forteller antall smittede i regionen
    print("Antall smittede i regionen: " + str(regionObj.hentAntallRegion()))
    #Lager et key/value par i ordboken region som holder regionkoden og regiondataen

    #Printer et par spaces
    for x in range(0,3):
        print("\n")

    #Legger til regionobjektet i regionordboken som er global
    region[userKode] = regionObj

#Definerer en funksjon for a finne mest okning i smitte i en region
def findHighest(userKode):
    #Lager en ordbok som skal holde datoer
    sjekkDatoer = {}
    #Lager en liste som skal holde datoer og smittetall
    container = []
    #Lager en variabel som holder hoyeste differanse
    highestDiff = 0
    #Lager en liste som holder dato og tall pa datoer med storst differanse
    highestContainer = []
    #Sjekker om brukerinput finnes i regionordboken
    if userKode in region:
        #Dersom den finnes, gar vi gjennom verdiene til regionen
        allElements = region[userKode].hentAllInfo()
        #Gar gjennom alle elementene i listen
        for elements in allElements:
            #Lager en variabel som holder datoen til eldste dato
            dato = elements[2]
            #Kaller metoden til dato for a fa ut lesbar dato, ikke objekt
            baseDato = dato.hentDato()
            #Lager en variabel som er datoen som er en dag for
            relativeDato = baseDato - timedelta(days=1)
            #Sjekker om datoen allerede er i ordboken sjekkdatoer
            if dato in sjekkDatoer:
                #Dersom det er sant, appender vi smittedata og datoen som er en dag for
                sjekkDatoer[dato].append([elements[1], relativeDato])
            #Dersom den ikke er det lager vi et nytt key/value par der datoen er key og value er smittedata og datoen som er en dag for denne dataen
            else:
                sjekkDatoer[dato] = [[elements[1], relativeDato]]

        #Gar gjennom sjekkDatoer ordboken
        for key,value in sjekkDatoer.items():
            #Definerer en dato relativ som skal holde dato en dag for
            datoRelativ = None
            #Definerer en variabel som skal vare smittetall for dag nr 2
            firstNum = 0
            #Definerer en variabel so skal holde smittetall for dag nr 1 (dagen for dag nr2)
            secondNum = 0

            #Gar gjennom listen i key/value paret
            for data in value:
                #Setter dato en dag for til det som er i value
                datoRelativ = data[1]
                #Setter smitteAbsolutt lik objektet som er i value
                smitteAbsolutt = data[0]
                #Legger dette tallet til firstnum
                firstNum += smitteAbsolutt.hentSmittede()

            #Gar gjennom sjekkDatoer ordboken
            for nokkel,verdi in sjekkDatoer.items():
                #Sjekker om datoen som er en dag for finnes i ordboken
                if datoRelativ == nokkel.hentDato():
                    #Dersom den er der, gar vi inn i elementene i verdi i ordboken
                    for info in verdi:
                        #Henter ut objektet om smittetall
                        smitteRelativ = info[0]
                        #Setter secondNum lik og plusser pa tallet fra det vi henter ut av smittetall
                        secondNum += smitteRelativ.hentSmittede()
            #Legger deretter all dataen inn i en liste som holder de ulike datoene som er for / etter hverandre. Med tilhorende smittetall
            container.append([key.hentDato(),firstNum,datoRelativ,secondNum])

        #Gar gjennom container
        for allData in container:
            #Lager en variabel som holder differansen til de forskjellige datoene
            differanse = allData[1] - allData[3]
            #Sjekker om differansen er storre enn variabelen som er definert
            if differanse > highestDiff:
                #Dersom den er hoyere, er dette den nye differansen som er storst
                highestDiff = differanse
                #Legger deretter dataen om denne datoen inn i en liste som skal holde den endelige datoen og smittetall
                highestContainer.append(allData)
        #Definerer to variabler som holder datoene som er de med mest okning
        winningDate1 = None
        winningDate2 = None
        #Gar gjennom listen med info om hvilke datoer som har mest okning
        for theWinningDates in highestContainer:
            #Setter variablene til de to datoene
            winningDate1 = theWinningDates[2]
            winningDate2 = theWinningDates[0]

        #Printer litt space
        for x in range(0,2):
            print("\n")

        #Printer menneskesetning som gir info om dato og region
        print("Datoen der smitte okte mest i " + str(userKode) + " er: " + "fra: " + str(winningDate1) + " til: " + str(winningDate2))
        #Printer menneskesetning som forteller om antall okning
        print("I denne perioden oke antall smittede med " + repr(highestDiff))
        #Printer litt space
        for x in range(0,3):
            print("\n")
    #Dersom regionkoden finnes i ordboken printes menneskesetning som forteller at regionen ikke finnes
    else:
        print("Ingen regioner med den koden er definert, trykk g for a opprette en!")
        #Printer space
        for x in range(0,3):
            print("\n")

#Definerer en funksjon skrivTilFil som tar ordbok som parameter
def skrivTilFil(ordbok):
    #Lager en liste som skal holde de ulike setningene
    container = []
    #Gar gjennom ordboken
    for key,value in ordbok.items():
        #Gar gjennom elementene i ordboken
        for lists in value:
            #Definerer en variabel som skal holde navnet pa landet
            landNavn = lists[0].hentLandNavn()
            #Definerer en var som skal holde koden til landet
            landsKode = lists[0].hentLandId()
            #Definerer en var som skal holde smittetall
            smittetall = lists[1].hentSmittede()
            #Definerer ar,mnd og dag var
            ar,mnd,dag = lists[2].hentHelTall()

            #sjekker om dag var starter med 0
            if str(dag).startswith("0"):
                #Dersom den gjor det fjernes den 0en
                dag = dag.replace("0", '')
            #Sjekker om mnd starter med 0
            if str(mnd).startswith("0"):
                #Dersom den gjor det fjernes den
                mnd = mnd.replace("0", '')

            #Gjor om alle mnd fra tall (well not really, but sort of) til tekst, for a fa det likt som i filen som leses inn i programmet
            if mnd == "1":
                mnd = "Jan"
            if mnd == "2":
                mnd = "Feb"
            if mnd == "3":
                mnd = "Mar"
            if mnd == "4":
                mnd = "Apr"
            if mnd == "5":
                mnd = "May"
            if mnd == "6":
                mnd = "Jun"
            if mnd == "7":
                mnd = "Jul"
            if mnd == "8":
                mnd = "Aug"
            if mnd == "9":
                mnd = "Sep"
            if mnd == "10":
                mnd = "Oct"
            if mnd == "11":
                mnd = "Nov"
            if mnd == "12":
                mnd = "Dec"

            #Lager et random nummer som skal vare det siste i tekststrengen
            endNum = random.randint(1,99)

            #Legger til de ulike variablene i listen container
            container.append([str(landNavn),str(landsKode),mnd,dag,str(ar),str(smittetall),str(endNum)])
    #Gar gjennom listen med info
    for lines in container:
        #Apner en tom fil som kan skrives til
        f = open("writefile.txt", "a")
        #Skriver til filen der alle variablene og tegn legges til identisk som i filen som leses inn i programmet orginalt
        f.write(lines[0] + "," + lines[1] + "," + '"' + lines[2] + lines[3] + ", " + lines[4] + '"' + "," + lines[5] + "," + lines[6] + "\n")
    #Printer space
    for x in range(0,3):
        print("\n")

    print("Skrev " + repr(len(container)) + " linjer til " + "filen writefile.txt")

    for x in range(0,3):
        print("\n")
#Definerer en funksjon som tar userinput og ordboken som parameter
def skrivUtLand(ordbok, userLand):
    #Setter landskode lik none
    userLandKode = None
    #Gar gjennom ordboken
    for key,value in ordbok.items():
        #Gar gjennom hvert element i key/value paret
        for elements in value:
            #Sjekker om landsnavnet er lik et objekt i ordboken
            if userLand == elements[0].hentLandNavn():
                #Dersom det matcher, vet vi hvilken landskode det er og setter den lik det i objektet
                userLandKode = elements[0].hentLandId()
        #Finner deretter alle value elementene i ordboken basert pa den nye landskoden vi fant
        if userLandKode == key:
            #Printer menneskesetning med hvilket land som ble valgt
            print("\n")
            print("Landet du valgte: " + str(ordbok[key][0][0].hentLandNavn()))
            #Gar gjennom hvert element i key/value paret til landet
            for element in ordbok[key]:
                #Printer dato og antall smittede knyttet til denne datoen
                print("Dato: " + str(element[2].hentDato()))
                print("Smittede: " + str(element[1].hentSmittede()))
    #Printer space
    for x in range(0,3):
        print("\n")

#Definerer en funksjon som tar ordboken og userinput som parameter
def plotLand(ordbok,userLand):
    #Definerer en variabel som skal holde landskoden
    userKode = None
    #Lager to lister som skal holde verdiene til punktene pa aksene
    xAxis = []
    yAxis = []
    #Gar gjennom ordboken
    for key,value in ordbok.items():
        #Gar gjennom hvert element i key/value paret
        for elements in value:
            #Sjekker om landet som bruker oppga finnes i ordboken
            if userLand == elements[0].hentLandNavn():
                #Dersom den finnes, settes userkode / landskoden til verdien som er unik for et land
                userKode = elements[0].hentLandId()
        #Finner landskoden i ordboken
        if userKode == key:
            #Gar gjennom hvert element i dette key/value paret
            for element in value:
                #Legger alle datoene til i listen for x akse
                xAxis.append(element[2].hentDato())
    #Sorterer datoene slik at de er tidligst forst, deretter stigende rekkefolge
    #Dette gjores dersom datoene i tekstfilen ikke kommer med stigende datoer
    xAxis.sort()

    #Gar deretter gjennom den sorterte listen
    for dates in xAxis:
        #Gar gjennom ordboken
        for key,value in ordbok.items():
            #Finner key/value paret til brukeren
            if userKode == key:
                #Gar gjennom elementene i dette key/value paret
                for smittetall in value:
                    #Finner datoen som tilhorer den sorterte listen
                    if dates == smittetall[2].hentDato():
                        #Legger smittetallet til denne datoen inn i yakse listen
                        yAxis.append(smittetall[1].hentSmittede())
    #Plotter listene
    plt.plot(xAxis, yAxis)
    #Gir navn til yakse
    plt.ylabel('Smittetall')
    #Viser figuren
    plt.show()

#Kaller hovedfunksjonen
hovedprogram()
