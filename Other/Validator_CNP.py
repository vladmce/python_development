"""
0 1 2 3 4 5 6 7 8 9 0 1 2
1 9 9 0 6 2 2 2 9 7 2 5 2
S A A L L Z Z J J N N N C

- S intre 1 si 9
- A A intre 00 si 99
- L L intre 01 si 12
- Z Z intre:
    - (01 si 31) pentru lunile cu 31 de zile (01, 03, 05, 07, 08, 10, 12)
    - (01 si 30) pentru lunile cu 30 de zile (04, 06, 09, 11)
    - (01 si 29) pentru luna 02 si an bisect
    - (01 si 28) pentru luna 02 si an nebisect
- J J intre (01 si 46) sau 51, sau 52
- N N N intre (000 si 999)
- Cifra de cotrol:
    lista_verificare = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
    - Se inmulteste fiecare cifra din cnp cu cifra de pe aceeasi pozitie din lista de verificare
    - Se aduna produsele intre ele
    - se imparte rezultatul la 11
    - cifra de control restul impartirii
    - daca restul este 10, restul devine 1
"""


while True:
    cnp = input("Introdu CNP-ul: ")
    if cnp.isdigit() and len(cnp) == 13:
        cnp = list(cnp)
        break
    else:
        print("Format invalid.")

sex = int(cnp[0])
anul_nasterii = int(cnp[1] + cnp[2])
luna_nasterii = int(cnp[3] + cnp[4])
ziua_nasterii = int(cnp[5] + cnp[6])
judet = int(cnp[7] + cnp[8])
numar = int(cnp[9] + cnp[10] + cnp[11])
control = int(cnp[12])

cnp_de_control=[]
for i in range(0,12):
    cnp_de_control.append(int(cnp[i]))

# cnp_de_control = [1, 9, 9, 0, 6, 2, 2, 2, 9, 7, 2, 5]
lista_verificare = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]

suma = 0
for i in range(len(lista_verificare)):
    produs = lista_verificare[i] * cnp_de_control[i]
    suma = suma + produs

cif = suma % 11
if cif == 10:
    cif = 1

if sex in range(1, 10):
    if luna_nasterii in range(1, 13):
        if (luna_nasterii in [1, 3, 5, 7, 8, 10, 12] and ziua_nasterii in range(1,32)) or \
                (luna_nasterii in [4, 6, 9, 11] and ziua_nasterii in range(1,31)) or \
                (luna_nasterii == 2 and anul_nasterii % 4 == 0 and ziua_nasterii in range(1,30)) or \
                (luna_nasterii == 2 and anul_nasterii %4 != 0 and ziua_nasterii in range(1,29)):
            if judet in range(1, 47) or judet in [51, 52]:
                if cif == control:
                    print("CNP Valid")
                else:
                    print("Eroare cifra control")
            else:
                print("Eroare judet")
        else:
            print("Eroare ziua nasterii")
    else:
        print("Eroare luna nasterii")
else:
    print("Eroare sex")


