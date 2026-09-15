


# GLOBÁLIS VÁLTOZÓK
pin_kod = 1234
egyenleg = 0
hasznalati_dij = 1000
adatfajl = "szamla.txt"
jogosult = False
tranzakciok = []


#######################################
# FUNKCIÓK
#######################################
def adatbeolvasas(fajl):
    try:
        with open(fajl, "r", encoding="UTF-8") as f:
            global tranzakciok
            tranzakciok = f.readlines()
    except IOError as e:
        print(f"Fájl művelet hiba: {e}")

        
def mentes(fajl):
    try:
        with open(fajl, "w", encoding="UTF-8") as f:
            f.writelines(tranzakciok)
    except IOError as e:
        print(f"Fájl művelet hiba: {e}")


def egyenleg():
    szamla_egyenleg = 0
    
    for sz in tranzakciok:
        szamla_egyenleg += int(sz)
    
    print(f"Az egyenleged: {szamla_egyenleg} Ft")


def utalas(osszeg):
    print("Utalás: ")

def penzbetet(osszeg):
    print("Betét: ")

# darab = 0 -> összes tranzakció
# darab !=0 -> utolsó darab tranzakcio
def tortenet(darab):
    print("Tranzakciók: ")



#######################################
# A PROGRAM
#######################################

# BEJELENTKEZÉS
hibas_belepesszam = 3

pk = int(input("Add meg a PIN kódodat!: "))

if pk == pin_kod:
        jogosult = True
        print("Sikeres belépés!")

while(not jogosult and hibas_belepesszam > 1):
    print(f"Hibás PIN kód!")
    pk = int(input("Add meg a PIN kódodat!: "))
    hibas_belepesszam -= 1
  
    if pk == pin_kod:
        jogosult = True
        print("Sikeres belépés!")

if not jogosult:
    print(f"Hibás PIN kód!")

adatbeolvasas(adatfajl)

# Beolvasás teszt (kiírás)
# print(f"{tranzakciok}")


# FUNKCIÓVÁLASZTÓ MENÜ
cim = "\nSZÁMLAKEZELŐ PROGRAM\n====================\n"
menu = [
    "1. Egyenleg lekérdezés",
    "2. Pénz kivétel/átutalás",
    "3. Pénz betét",
    "--------------",
    "4. Tranzakciótörténet",
    "9. Kilépés"
]

menupontok = [1, 2, 3, 4, 9]

while True:
    print(cim)
    for me in menu:
        print(f"{me}")

    valasztas = int(input("Válassz tevékenységet: "))

    while valasztas not in menupontok:
        print("Nincs ilyen menüpont!\n")
        
        print(cim)    
        for me in menu:
            print(f"{me}")

        valasztas = int(input("Válassz tevékenységet: "))

    # "Képernyő törlése"
    print(f"{'\n' * 20}")

    if valasztas == 1:
        egyenleg()
    elif valasztas == 2:
        utalas(123)
    elif valasztas == 3:
        penzbetet(10000)
    elif valasztas == 4:
        tortenet(0)
    elif valasztas == 9:
        # mentes(adatfajl)
        exit()



