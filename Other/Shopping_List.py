"""
SHOPPING LIST EXTENDED (LISTA DE CUMPARATURI - FUNCTIONALA)
Creati un program care are ca scop un meniu. Meniul se va selecta prin introducerea
de la tastaura a unui numar intre 1 si 5 captat intr-o variabila. Prezentati prin afisare
acest sir de caractere:
1 – Afisare lista de cumparaturi
2 – Adaugare element
3 – Stergere element
4 – Sterere lista de cumparaturi
5 - Cautare in lista de cumparaturi
Apoi folosindu-va de o constructie if-elif-else afisati:
- daca utilizatorul scrie de la tastaura 1 procesati “Afisare lista de cumparaturi”;
- daca utilizatorul scrie de la tastaura 2 procesati “Adugare element”;
- daca utilizatorul scrie de la tastaura 3 procesati “Stergere element”;
- daca utilizatorul scrie de la tastaura 4 procesati “Sterere lista de cumparaturit";
- daca utilizatorul scrie de la tastaura 5 procesati “Adaugare element”;
- daca utilizatorul scrie de la tastatura 6, procesati trimiterea unui email cu lista de cumparaturi;
- daca utilizatorul scrie altceva de la tastaura afisati “Alegerea nu exista. Reincercati”.

Completati pe linia 121 si linia 122 cu adresa de gmail a sender-ului si cu app password-ul din gmail
"""
from email.message import EmailMessage
import ssl
import smtplib

# Se creaza o lista care sa descrie elementele meniului.
optiuni_meniu = ["1 - Afisare lista de cumparaturi", "2 - Adaugare element",  "3 - Stergere element", "4 - Stergere lista de cumparaturi", "5 - Cautare in lista de cumparaturi", "6 - Trimite lista pe email"]



# Se creaza o variabila tip lista "lista_de_cumparaturi" care va deservi ca mediul in care vom stoca elementele listei.
lista_de_cumparaturi = []

# Instructiunea while True ruleaza programul la infinit.
while True:

    # Se printeaza lista iterand cu functi "print()" prin fiecare element al listei.
    for i in range(len(optiuni_meniu)):
        print(optiuni_meniu[i])

    # Se cere alegerea unei optiuni din lista ca input de la tastatura.
    alegere_utilizator = input("\nAlege o optiune: ")

    # In cazul in care stringul contine altceva in afara de cifre de la 1 la 5, se va cere imput pana cand acesta devine valid.
    while alegere_utilizator.isdigit() is False or alegere_utilizator not in ["1", "2", "3", "4", "5", "6"]:
        alegere_utilizator = input("Ai ales o optiune invalida. Alege din nou: ")

    # Se transforma numarul din string in integer ca sa in putem compara cu date de tip int.
    # Transformarea nu este obligatorie, puteam lasa variabila de tip string atat timp cat comparam tot cu viriabile de tip string.
    alegere_utilizator=int(alegere_utilizator)


    # Se verifica ce optiune a fost aleasa.
    # Se afiseaza diferite mesaje in terminal.
    if alegere_utilizator == 1:
        if len(lista_de_cumparaturi) != 0:
            print(f"\nLista de cumparaturi contine {len(lista_de_cumparaturi)} elemente si este urmatoarea: ")
            for i in range(len(lista_de_cumparaturi)):
                print(f"{i+1}. {lista_de_cumparaturi[i]}")
        else:
            print("\nLista de cumparaturi este goala.")
        print("")
    elif alegere_utilizator == 2:
        element_lista = ''
        while element_lista != 'x':
            element_lista = input("\nIntrodu elementul. Pentru intoarcere la meniul anterior, scrie 'x': ")
            lista_de_cumparaturi.append(element_lista)
            if element_lista == 'x':
                lista_de_cumparaturi.remove(element_lista)
            print("\n Lista actuala este:")
            for i in range(len(lista_de_cumparaturi)):
                print(f"{i + 1}. {lista_de_cumparaturi[i]}")
        print("")
    elif alegere_utilizator == 3:
        element_lista = ''
        while element_lista != 'x':
            print("\n Lista actuala este:")
            for i in range(len(lista_de_cumparaturi)):
                print(f"{i + 1}. {lista_de_cumparaturi[i]}")
            element_lista = input("\nIntrodu pozitia elementului pe care doresti sa il stergi. Pentru intoarcere la meniul anterior, scrie 'x': ")
            if element_lista.isdigit():
                lista_de_cumparaturi.remove(lista_de_cumparaturi[int(element_lista)-1])
        print("")
    elif alegere_utilizator == 4:
        alegere_4 = input("Doriti sa stergeti toata lista de cumparaturi? da/nu: ")
        while alegere_4 != "da" and alegere_4 != "nu":
            alegere_4 = input("Optiune gresita. Doriti sa stergeti toata lista de cumparaturi? da/nu: ")
        if alegere_4 == "da":
            lista_de_cumparaturi = []
            print("\nLista de cumparaturi este acum goala.\n")
    elif alegere_utilizator == 5:
        element_de_cautat = ""
        while element_de_cautat != "x":
            element_de_cautat = input("Scrie ce element vrei sa cauti in lista. Pentru intoarcere la meniul anterior, scrie 'x':  \n").lower()
            if element_de_cautat == "x":
                break
            elif element_de_cautat in lista_de_cumparaturi:
                print(f"Elementul {element_de_cautat} exista in lista, pe pozitia {lista_de_cumparaturi.index(element_de_cautat)+1}")
            else:
                alegere_5 = input(f"Elementul {element_de_cautat} nu exista in lista. Doresti sa il adaugi? da/nu: ")
                while alegere_5 != "da" and alegere_5 != "nu":
                    alegere_5 = input(f"Optiune gresita. Doresti sa adaugi {element_de_cautat} in lista? da/nu: ")
                if alegere_5 == "da":
                    lista_de_cumparaturi.append(element_de_cautat)
                    print(f"\nAm adaugat {element_de_cautat} listei tale.\n")
    elif alegere_utilizator == 6:
        lista_finala_titlu = 'Lista de cumparaturi: \n'
        lista_finala = ""
        for i in range(len(lista_de_cumparaturi)):
            lista_finala += (f"{i + 1}. {lista_de_cumparaturi[i]}\n")

        lista = lista_finala_titlu + lista_finala
        print(f"Lista finala este:")
        print(lista_finala)
        decizie = input("Doresti sa trimiti pe email lista finala? d/n: ")
        if decizie == 'd':
            email_sender = ""
            email_password = ""  # From Gmail settings -> two-factor auth -> app passwords

            email_receiver = input("Adauga adresa de email la care doresti sa trimiti lista: ")

            subject = 'Lista Cumparaturi'
            body = lista


            # Create the instance of the email
            em = EmailMessage()
            em["From"] = email_sender
            em["To"] = email_receiver
            em["subject"] = subject
            em.set_content(body)

            # Disable SSL certificate verification
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE

            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())
            print("\nLista a fost trimisa!\n")



    else:
        print("Alegerea nu exista. Reincercati: ")


