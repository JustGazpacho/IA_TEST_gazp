import random

segni = [
    "Ariete", "Toro", "Gemelli", "Cancro", "Leone", "Vergine",
    "Bilancia", "Scorpione", "Sagittario", "Capricorno", "Acquario", "Pesci"
]

frasi = [
    "Oggi è una giornata perfetta per iniziare qualcosa di nuovo.",
    "Attenzione alle emozioni: parlano più di quanto pensi.",
    "La tua energia attirerà l’attenzione di chi ti circonda.",
    "Una sorpresa potrebbe cambiarti la giornata.",
    "Ascolta il tuo istinto: sarà la tua guida migliore.",
    "Prenditi del tempo per riflettere su ciò che davvero conta.",
    "Una nuova opportunità potrebbe bussare alla tua porta.",
    "Non lasciare che piccoli ostacoli frenino il tuo entusiasmo."
]
#auguri 
def genera_oroscopo():
    oroscopo = {}
    for segno in segni:
        oroscopo[segno] = random.choice(frasi)
    return oroscopo

# Esempio di utilizzo
oroscopi_del_giorno = genera_oroscopo()
for segno, messaggio in oroscopi_del_giorno.items():
    print(f"{segno}: {messaggio}")