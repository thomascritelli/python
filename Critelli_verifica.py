#Dichiaro le variabili
scelta = 1
stab = {}
prezzo = 0
prezzoBase = 0
lun = 0

#Inserimento mese
def callMese():
  m = int(input("Inserisci il mese: "))
  while (m != 6 and m != 9 and m != 7 and m != 8):
    m = int(input("Inserisci il mese: "))
    return m

#Inserimento dati nelle variabili
def dati(i):

  #Codice prenotazione
  cod = i+1

  #Data prenotazione
  gg = int(input("Inserisci il giorno: "))
  mm = int(input("Inserisci il mese: "))
  """
  while(((mm != 6 and mm != 9) and (gg > 0 and gg < 31)) or ((mm == 7 or mm == 8) and (gg > 0 and gg < 32))):
  
  print("Input non valido!")
      gg = int(input("Inserisci il giorno: "))
      mm = int(input("Inserisci il mese: "))
  """
  aa = int(input("Inserisci l'anno: "))
  if mm == 6 or mm == 9:
    stagione = 1
    prezzoBase = 12
  elif mm == 7:
    stagione = 2
    prezzo = 25
  elif mm == 8:
    stagione = 2
    prezzoBase = 22
  else:
    stagione = 1
    prezzoBase = 9
  prezzo = prezzoBase

  data = [gg,mm,aa]

  #Giorni di prenotazione
  g = int(input("Inserisci per quanti giorni vuoi prenotare: "))

  #Opzioni
  sdraio = int(input("Inserisci il numero di sdraio: "))
  lettini = int(input("Inserisci il numero di lettini: "))
  prezzo += (((1/3)*sdraio)+((1/2)*lettini))
  opzione = [sdraio,lettini]

  print("--PRENOTAZIONE AGGIUNTA--")
  print()
  return [cod,prezzoBase,data,g,opzione,prezzo]
  
#Aggiunta Prenotazione
def aggiungiPrenotazione(i):
  stab[i] = dati(i)

#Visualizzazione prenotazioni n mesi
  


#1. Creazione Menu
#Menu
while(scelta !=0):
  print("--SELEZIONA L'OPZIONE--")
  print("0. Esci")
  print("1. Popola")
  print("2. Mostra le prenotazioni di un mese")
  print("3. Mostra tutte le prenotazioni")
  print("4. Riduzione prezzo percentuale")
  print("5. Calcola l'incasso totale di un mese")
  print("6. Visualizza le prenotazioni di n mesi")
  scelta = int(input("Cosa vuoi fare? "))
  while (scelta < 0 or scelta > 6):
    scelta = int(input("Input non valido! Cosa vuoi fare? "))
  print("Input accettato!")

  #Scelta 1: Popola
  if (scelta == 1):
    nP = int(input("Quante prenotazioni vuoi aggiungere? "))
    for i in range(nP):
      aggiungiPrenotazione(i)
      lun += 1
    
  elif (scelta == 2):
    for j in range (lun):
      print(stab[j][2][1][callMese()])
    print()
    
  elif (scelta == 3):
    print(stab)
    print()
  
  elif (scelta == 4):
    percent = int(input("Inserire la percentuale"))
    for x in range (lun):
      stab[x][5] = (stab[x][5]*percent)/100
    print("--OPERAZIONE ESEGUITA")
    print()
  elif (scelta == 0):
    break;
