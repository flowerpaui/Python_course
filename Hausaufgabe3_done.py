
###Es gibt einen vierstelligen Code, an jeder Stelle können die Zahlen von 0-9 sein
def mastermind (guess):
    guess = str(guess)
    guess = guess.strip()
            #Zuerst denkt sich der Computer einen Code aus:
        #jede stelle einzeln und als string, damit auch Nullen am Anfang kommen können
    import random
    code = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
    if len(guess) == 4: #nur wenn person echt 4 stellen genommen hat
        while guess != code: #all das nur, wenn nicht eh schon erraten
            fastrichtig = 0
            reststellen=[]
            restzahlen=[]
            for stelle in range(0,4): #alle stellen durchgehen
                if guess[stelle] != code[stelle]: #wenn kein "perfekter guess" an dieser stelle..
                    reststellen.append(stelle) #Liste mit den "nicht perfekten" Stellen
                    restzahlen.append(code[stelle]) #Zahlen die nicht "perfekt erraten"
            for stelle in reststellen: #nur die Stellen, die nicht perfekte guesses sind
                if guess[stelle] in restzahlen: #wenn richtige zahl, aber falsche stelle...
                    fastrichtig=fastrichtig+1 #gezählt für den entspr. zähler
                    restzahlen.remove(guess[stelle]) #damit richtige zahl nur so oft zählt, wie sie auch in echtem code vorhanden ist, nicht so oft wie person sie rät 
                                    #(zB, "1" kommt einmal vor, person rät drei 1en, soll dafür ja nur einen Hit bekommen)
            ganzrichtig=4-len(reststellen)
            print('Richtige Zahl an der richtigen Stelle: {0} mal. \nRichtige Zahl, aber an der falschen Stelle: {1} mal'.format(ganzrichtig, fastrichtig))
            guess = input('Nächster Versuch:')
                
            #return ganzrichtig, fastrichtig #BRAUCHE ICH DAS?
        print("WOW!!! An genau diesen Code habe ich gedacht, woher wusstest du das?")
    else:
        print ("Der Code muss VIER Stellen haben und darf NUR aus ZAHLEN bestehen.")


##Bisher nur Funktion definiert, jetzt das "Drumherum"
print('Hallo! Schön dass du mit mir spielen willst! \nIch habe mir einen vierstelligen Code ausgedacht... Er besteht aus Zahlen zwischen 0 und 9. \nSchaffst du es, ihn zu erraten?')
guess = input('Na los, rate mal: ')
mastermind(guess)






