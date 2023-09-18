verificare1 = 1
verificare2 = 1
verificare3 = 1

while verificare1 == 1:
    caracter_om = input("Alege caracterul cu care vrei sa joci. (x sau 0) \n")
    if caracter_om == "x":
        caracter_calculator = "0"
        verificare1 = 0
    elif caracter_om == "0":
        caracter_calculator = "x"
        verificare1= 0
    else:
        print("Alege x sau 0")
        verificare1 = 1

model_tabla_joc = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
tabla_joc = ["_", "_", "_", "_", "_", "_", "_", "_", "_", ]
tabla_joc_afisabila = f"Aceasta este tabla curenta a jocului: \n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
model_tabla_joc_afisabila =f"Aceasta este modelul tablei de joc : \n {model_tabla_joc[0]} {model_tabla_joc[1]} {model_tabla_joc[2]} \n {model_tabla_joc[3]} {model_tabla_joc[4]} {model_tabla_joc[5]} \n {model_tabla_joc[6]} {model_tabla_joc[7]} {model_tabla_joc[8]}"

while verificare2 == 1:
    primul_jucator = input("Daca doresti sa fii primul jucator, scrie 1, daca doresti ca PC-ul sa inceapa primul, scrie 2: \n")

    if primul_jucator == "1":  # Omul este primul jucator
        verificare2 = 0

        while verificare3 == 1:
            # Tura Om
            if tabla_joc[0] != "_" and tabla_joc[1] != "_" and tabla_joc[2] != "_" and tabla_joc[3] != "_" and tabla_joc[4] != "_" and tabla_joc[5] != "_" and tabla_joc[6] != "_" and tabla_joc[7] != "_" and tabla_joc[8] != "_":
                tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                print(tabla_joc_afisabila)
                print("Remiza!")
                break

            pozitie_aleasa_om=input(f"Alege pozitia pe care vrei sa inserezi simbolul {caracter_om} \n \n{model_tabla_joc_afisabila} \n \n{tabla_joc_afisabila} \n \n")
            while tabla_joc[int(pozitie_aleasa_om)-1] == "x" or tabla_joc[int(pozitie_aleasa_om)-1] == "0":
                pozitie_aleasa_om = input("Pozitia este deja ocupata. Alege o alta pozitie! \n")
            tabla_joc[int(pozitie_aleasa_om)-1] = caracter_om
            tabla_joc_afisabila = f"Aceasta este tabla curenta a jocului: \n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
            print(f"Ai introdus {caracter_om} pe pozitia {pozitie_aleasa_om}. \n{tabla_joc_afisabila}")

            # Verificarea castigului
            if tabla_joc[0] == tabla_joc[1] == tabla_joc[2] != "_":
                if tabla_joc[0] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
            elif tabla_joc[3] == tabla_joc[4] == tabla_joc[5] != "_":
                if tabla_joc[3] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
            elif tabla_joc[6] == tabla_joc[7] == tabla_joc[8] != "_":
                if tabla_joc[6] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
            elif tabla_joc[0] == tabla_joc[3] == tabla_joc[6] != "_":
                if tabla_joc[0] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
            elif tabla_joc[1] == tabla_joc[4] == tabla_joc[7] != "_":
                if tabla_joc[1] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
            elif tabla_joc[2] == tabla_joc[5] == tabla_joc[8] != "_":
                if tabla_joc[2] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
            elif tabla_joc[0] == tabla_joc[4] == tabla_joc[8] != "_":
                if tabla_joc[0] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
            elif tabla_joc[2] == tabla_joc[4] == tabla_joc[6] != "_":
                if tabla_joc[2] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
            else:
                verificare3 = 1
                # print("Este randul calculatorului.")

            # Tura Calculator
            # Abordare defensiva
            if tabla_joc[0] != "_" and tabla_joc[1] != "_" and tabla_joc[2] != "_" and tabla_joc[3] != "_" and tabla_joc[4] != "_" and tabla_joc[5] != "_" and tabla_joc[6] != "_" and tabla_joc[7] != "_" and tabla_joc[8] != "_":
                tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                print(tabla_joc_afisabila)
                print("Remiza!")
                break
            print("Urmeaza randul calculatorului.")
            if tabla_joc[0] == tabla_joc [1] and tabla_joc[0] == caracter_om and tabla_joc[2] == "_":  # Situatia 1
                tabla_joc[2] = caracter_calculator
            elif tabla_joc[3] == tabla_joc [4] and tabla_joc[3] == caracter_om and tabla_joc[5] == "_":
                tabla_joc[5] = caracter_calculator
            elif tabla_joc[6] == tabla_joc[7] and tabla_joc[6] == caracter_om and tabla_joc[8] == "_":
                tabla_joc[8] = caracter_calculator
            elif tabla_joc[0] == tabla_joc[3] and tabla_joc[0] == caracter_om and tabla_joc[6] == "_":
                tabla_joc[6] = caracter_calculator
            elif tabla_joc[1] == tabla_joc[4] and tabla_joc[1] == caracter_om and tabla_joc[7] == "_":
                tabla_joc[7] = caracter_calculator
            elif tabla_joc[2] == tabla_joc[5] and tabla_joc[2] == caracter_om and tabla_joc[8] == "_":
                tabla_joc[8] = caracter_calculator
            elif tabla_joc[0] == tabla_joc[4] and tabla_joc[0] == caracter_om and tabla_joc[8] == "_":
                tabla_joc[8] = caracter_calculator
            elif tabla_joc[2] == tabla_joc[4] and tabla_joc[2] == caracter_om and tabla_joc[6] == "_":
                tabla_joc[6] = caracter_calculator
            elif tabla_joc[2] == tabla_joc [1] and tabla_joc[2] == caracter_om and tabla_joc[0] == "_":  # Situatia 2
                tabla_joc[0] = caracter_calculator
            elif tabla_joc[5] == tabla_joc [4] and tabla_joc[5] == caracter_om and tabla_joc[3] == "_":
                tabla_joc[3] = caracter_calculator
            elif tabla_joc[8] == tabla_joc[7] and tabla_joc[8] == caracter_om and tabla_joc[6] == "_":
                tabla_joc[6] = caracter_calculator
            elif tabla_joc[6] == tabla_joc[3] and tabla_joc[6] == caracter_om and tabla_joc[0] == "_":
                tabla_joc[0] = caracter_calculator
            elif tabla_joc[7] == tabla_joc[4] and tabla_joc[7] == caracter_om and tabla_joc[1] == "_":
                tabla_joc[1] = caracter_calculator
            elif tabla_joc[8] == tabla_joc[5] and tabla_joc[8] == caracter_om and tabla_joc[2] == "_":
                tabla_joc[2] = caracter_calculator
            elif tabla_joc[8] == tabla_joc[4] and tabla_joc[8] == caracter_om and tabla_joc[0] == "_":
                tabla_joc[0] = caracter_calculator
            elif tabla_joc[6] == tabla_joc[4] and tabla_joc[6] == caracter_om and tabla_joc[2] == "_":
                tabla_joc[2] = caracter_calculator
            elif tabla_joc[0] == tabla_joc [2] and tabla_joc[0] == caracter_om and tabla_joc[1] == "_":  # Situatia 3
                tabla_joc[1] = caracter_calculator
            elif tabla_joc[3] == tabla_joc [5] and tabla_joc[3] == caracter_om and tabla_joc[4] == "_":
                tabla_joc[4] = caracter_calculator
            elif tabla_joc[6] == tabla_joc[8] and tabla_joc[6] == caracter_om and tabla_joc[7] == "_":
                tabla_joc[7] = caracter_calculator
            elif tabla_joc[0] == tabla_joc[6] and tabla_joc[0] == caracter_om and tabla_joc[3] == "_":
                tabla_joc[3] = caracter_calculator
            elif tabla_joc[1] == tabla_joc[7] and tabla_joc[1] == caracter_om and tabla_joc[4] == "_":
                tabla_joc[4] = caracter_calculator
            elif tabla_joc[2] == tabla_joc[8] and tabla_joc[2] == caracter_om and tabla_joc[5] == "_":
                tabla_joc[5] = caracter_calculator
            elif tabla_joc[0] == tabla_joc[8] and tabla_joc[0] == caracter_om and tabla_joc[4] == "_":
                tabla_joc[4] = caracter_calculator
            elif tabla_joc[2] == tabla_joc[6] and tabla_joc[2] == caracter_om and tabla_joc[4] == "_":
                tabla_joc[4] = caracter_calculator
            else:  # Abordarea ofensiva
                if tabla_joc[0] == tabla_joc[1] and tabla_joc[0] == caracter_calculator and tabla_joc[2] == "_":  # Situatia 1
                    tabla_joc[2] = caracter_calculator
                elif tabla_joc[3] == tabla_joc[4] and tabla_joc[3] == caracter_calculator and tabla_joc[5] == "_":
                    tabla_joc[5] = caracter_calculator
                elif tabla_joc[6] == tabla_joc[7] and tabla_joc[6] == caracter_calculator and tabla_joc[8] == "_":
                    tabla_joc[8] = caracter_calculator
                elif tabla_joc[0] == tabla_joc[3] and tabla_joc[0] == caracter_calculator and tabla_joc[6] == "_":
                    tabla_joc[6] = caracter_calculator
                elif tabla_joc[1] == tabla_joc[4] and tabla_joc[1] == caracter_calculator and tabla_joc[7] == "_":
                    tabla_joc[7] = caracter_calculator
                elif tabla_joc[2] == tabla_joc[5] and tabla_joc[2] == caracter_calculator and tabla_joc[8] == "_":
                    tabla_joc[8] = caracter_calculator
                elif tabla_joc[0] == tabla_joc[4] and tabla_joc[0] == caracter_calculator and tabla_joc[8] == "_":
                    tabla_joc[8] = caracter_calculator
                elif tabla_joc[2] == tabla_joc[4] and tabla_joc[2] == caracter_calculator and tabla_joc[6] == "_":
                    tabla_joc[6] = caracter_calculator
                elif tabla_joc[2] == tabla_joc[1] and tabla_joc[2] == caracter_calculator and tabla_joc[0] == "_":  # Situatia 2
                    tabla_joc[0] = caracter_calculator
                elif tabla_joc[5] == tabla_joc[4] and tabla_joc[5] == caracter_calculator and tabla_joc[3] == "_":
                    tabla_joc[3] = caracter_calculator
                elif tabla_joc[8] == tabla_joc[7] and tabla_joc[8] == caracter_calculator and tabla_joc[6] == "_":
                    tabla_joc[6] = caracter_calculator
                elif tabla_joc[6] == tabla_joc[3] and tabla_joc[6] == caracter_calculator and tabla_joc[0] == "_":
                    tabla_joc[0] = caracter_calculator
                elif tabla_joc[7] == tabla_joc[4] and tabla_joc[7] == caracter_calculator and tabla_joc[1] == "_":
                    tabla_joc[1] = caracter_calculator
                elif tabla_joc[8] == tabla_joc[5] and tabla_joc[8] == caracter_calculator and tabla_joc[2] == "_":
                    tabla_joc[2] = caracter_calculator
                elif tabla_joc[8] == tabla_joc[4] and tabla_joc[8] == caracter_calculator and tabla_joc[0] == "_":
                    tabla_joc[0] = caracter_calculator
                elif tabla_joc[6] == tabla_joc[4] and tabla_joc[6] == caracter_calculator and tabla_joc[2] == "_":
                    tabla_joc[2] = caracter_calculator
                elif tabla_joc[0] == tabla_joc[2] and tabla_joc[0] == caracter_calculator and tabla_joc[1] == "_":  # Situatia 3
                    tabla_joc[1] = caracter_calculator
                elif tabla_joc[3] == tabla_joc[5] and tabla_joc[3] == caracter_calculator and tabla_joc[4] == "_":
                    tabla_joc[4] = caracter_calculator
                elif tabla_joc[6] == tabla_joc[8] and tabla_joc[6] == caracter_calculator and tabla_joc[7] == "_":
                    tabla_joc[7] = caracter_calculator
                elif tabla_joc[0] == tabla_joc[6] and tabla_joc[0] == caracter_calculator and tabla_joc[3] == "_":
                    tabla_joc[3] = caracter_calculator
                elif tabla_joc[1] == tabla_joc[7] and tabla_joc[1] == caracter_calculator and tabla_joc[4] == "_":
                    tabla_joc[4] = caracter_calculator
                elif tabla_joc[2] == tabla_joc[8] and tabla_joc[2] == caracter_calculator and tabla_joc[5] == "_":
                    tabla_joc[5] = caracter_calculator
                elif tabla_joc[0] == tabla_joc[8] and tabla_joc[0] == caracter_calculator and tabla_joc[4] == "_":
                    tabla_joc[4] = caracter_calculator
                elif tabla_joc[2] == tabla_joc[6] and tabla_joc[2] == caracter_calculator and tabla_joc[4] == "_":
                    tabla_joc[4] = caracter_calculator
                else:  # Abordare neutra
                    if tabla_joc[4] == "_":
                        tabla_joc[4] = caracter_calculator
                    elif tabla_joc[0] == "_":
                        tabla_joc[0] = caracter_calculator
                    elif tabla_joc[2] == "_":
                        tabla_joc[2] = caracter_calculator
                    elif tabla_joc[6] == "_":
                        tabla_joc[6] = caracter_calculator
                    elif tabla_joc[8] == "_":
                        tabla_joc[8] = caracter_calculator
                    elif tabla_joc[1] == "_":
                        tabla_joc[1] = caracter_calculator
                    elif tabla_joc[3] == "_":
                        tabla_joc[3] = caracter_calculator
                    elif tabla_joc[5] == "_":
                        tabla_joc[5] = caracter_calculator
                    else:
                        tabla_joc[7] = caracter_calculator

            tabla_joc_afisabila = f"Aceasta este tabla curenta a jocului: \n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
            print(f"Calculatorul a facut mutarea! \n\n{tabla_joc_afisabila}")

            # Verificarea castigului
            if tabla_joc[0] == tabla_joc[1] == tabla_joc[2] != "_":
                if tabla_joc[0] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
            elif tabla_joc[3] == tabla_joc[4] == tabla_joc[5] != "_":
                if tabla_joc[3] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
            elif tabla_joc[6] == tabla_joc[7] == tabla_joc[8] != "_":
                if tabla_joc[6] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
            elif tabla_joc[0] == tabla_joc[3] == tabla_joc[6] != "_":
                if tabla_joc[0] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
            elif tabla_joc[1] == tabla_joc[4] == tabla_joc[7] != "_":
                if tabla_joc[1] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
            elif tabla_joc[2] == tabla_joc[5] == tabla_joc[8] != "_":
                if tabla_joc[2] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
            elif tabla_joc[0] == tabla_joc[4] == tabla_joc[8] != "_":
                if tabla_joc[0] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
            elif tabla_joc[2] == tabla_joc[4] == tabla_joc[6] != "_":
                if tabla_joc[2] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
            else:
                verificare3 = 1
                print("Este randul tau.")


    elif primul_jucator == "2":  # Calculatorul este primul jucator
        verificare2 = 0
        print("Calculatorul va fi primul jucator! Succes!")

        while verificare3 == 1:

            # Tura Calculator
            # Abordare defensiva
            if tabla_joc[0] != "_" and tabla_joc[1] != "_" and tabla_joc[2] != "_" and tabla_joc[3] != "_" and tabla_joc[4] != "_" and tabla_joc[5] != "_" and tabla_joc[6] != "_" and tabla_joc[7] != "_" and tabla_joc[8] != "_":
                tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                print(tabla_joc_afisabila)
                print("Remiza!")
                break

            if tabla_joc[0] == tabla_joc[1] and tabla_joc[0] == caracter_om and tabla_joc[2] == "_":  # Situatia 1
                tabla_joc[2] = caracter_calculator
            elif tabla_joc[3] == tabla_joc[4] and tabla_joc[3] == caracter_om and tabla_joc[5] == "_":
                tabla_joc[5] = caracter_calculator
            elif tabla_joc[6] == tabla_joc[7] and tabla_joc[6] == caracter_om and tabla_joc[8] == "_":
                tabla_joc[8] = caracter_calculator
            elif tabla_joc[0] == tabla_joc[3] and tabla_joc[0] == caracter_om and tabla_joc[6] == "_":
                tabla_joc[6] = caracter_calculator
            elif tabla_joc[1] == tabla_joc[4] and tabla_joc[1] == caracter_om and tabla_joc[7] == "_":
                tabla_joc[7] = caracter_calculator
            elif tabla_joc[2] == tabla_joc[5] and tabla_joc[2] == caracter_om and tabla_joc[8] == "_":
                tabla_joc[8] = caracter_calculator
            elif tabla_joc[0] == tabla_joc[4] and tabla_joc[0] == caracter_om and tabla_joc[8] == "_":
                tabla_joc[8] = caracter_calculator
            elif tabla_joc[2] == tabla_joc[4] and tabla_joc[2] == caracter_om and tabla_joc[6] == "_":
                tabla_joc[6] = caracter_calculator
            elif tabla_joc[2] == tabla_joc[1] and tabla_joc[2] == caracter_om and tabla_joc[0] == "_":  # Situatia 2
                tabla_joc[0] = caracter_calculator
            elif tabla_joc[5] == tabla_joc[4] and tabla_joc[5] == caracter_om and tabla_joc[3] == "_":
                tabla_joc[3] = caracter_calculator
            elif tabla_joc[8] == tabla_joc[7] and tabla_joc[8] == caracter_om and tabla_joc[6] == "_":
                tabla_joc[6] = caracter_calculator
            elif tabla_joc[6] == tabla_joc[3] and tabla_joc[6] == caracter_om and tabla_joc[0] == "_":
                tabla_joc[0] = caracter_calculator
            elif tabla_joc[7] == tabla_joc[4] and tabla_joc[7] == caracter_om and tabla_joc[1] == "_":
                tabla_joc[1] = caracter_calculator
            elif tabla_joc[8] == tabla_joc[5] and tabla_joc[8] == caracter_om and tabla_joc[2] == "_":
                tabla_joc[2] = caracter_calculator
            elif tabla_joc[8] == tabla_joc[4] and tabla_joc[8] == caracter_om and tabla_joc[0] == "_":
                tabla_joc[0] = caracter_calculator
            elif tabla_joc[6] == tabla_joc[4] and tabla_joc[6] == caracter_om and tabla_joc[2] == "_":
                tabla_joc[2] = caracter_calculator
            elif tabla_joc[0] == tabla_joc[2] and tabla_joc[0] == caracter_om and tabla_joc[1] == "_":  # Situatia 3
                tabla_joc[1] = caracter_calculator
            elif tabla_joc[3] == tabla_joc[5] and tabla_joc[3] == caracter_om and tabla_joc[4] == "_":
                tabla_joc[4] = caracter_calculator
            elif tabla_joc[6] == tabla_joc[8] and tabla_joc[6] == caracter_om and tabla_joc[7] == "_":
                tabla_joc[7] = caracter_calculator
            elif tabla_joc[0] == tabla_joc[6] and tabla_joc[0] == caracter_om and tabla_joc[3] == "_":
                tabla_joc[3] = caracter_calculator
            elif tabla_joc[1] == tabla_joc[7] and tabla_joc[1] == caracter_om and tabla_joc[4] == "_":
                tabla_joc[4] = caracter_calculator
            elif tabla_joc[2] == tabla_joc[8] and tabla_joc[2] == caracter_om and tabla_joc[5] == "_":
                tabla_joc[5] = caracter_calculator
            elif tabla_joc[0] == tabla_joc[8] and tabla_joc[0] == caracter_om and tabla_joc[4] == "_":
                tabla_joc[4] = caracter_calculator
            elif tabla_joc[2] == tabla_joc[6] and tabla_joc[2] == caracter_om and tabla_joc[4] == "_":
                tabla_joc[4] = caracter_calculator
            else:  # Abordarea ofensiva
                if tabla_joc[0] == tabla_joc[1] and tabla_joc[0] == caracter_calculator and tabla_joc[2] == "_":  # Situatia 1
                    tabla_joc[2] = caracter_calculator
                elif tabla_joc[3] == tabla_joc[4] and tabla_joc[3] == caracter_calculator and tabla_joc[5] == "_":
                    tabla_joc[5] = caracter_calculator
                elif tabla_joc[6] == tabla_joc[7] and tabla_joc[6] == caracter_calculator and tabla_joc[8] == "_":
                    tabla_joc[8] = caracter_calculator
                elif tabla_joc[0] == tabla_joc[3] and tabla_joc[0] == caracter_calculator and tabla_joc[6] == "_":
                    tabla_joc[6] = caracter_calculator
                elif tabla_joc[1] == tabla_joc[4] and tabla_joc[1] == caracter_calculator and tabla_joc[7] == "_":
                    tabla_joc[7] = caracter_calculator
                elif tabla_joc[2] == tabla_joc[5] and tabla_joc[2] == caracter_calculator and tabla_joc[8] == "_":
                    tabla_joc[8] = caracter_calculator
                elif tabla_joc[0] == tabla_joc[4] and tabla_joc[0] == caracter_calculator and tabla_joc[8] == "_":
                    tabla_joc[8] = caracter_calculator
                elif tabla_joc[2] == tabla_joc[4] and tabla_joc[2] == caracter_calculator and tabla_joc[6] == "_":
                    tabla_joc[6] = caracter_calculator
                elif tabla_joc[2] == tabla_joc[1] and tabla_joc[2] == caracter_calculator and tabla_joc[
                    0] == "_":  # Situatia 2
                    tabla_joc[0] = caracter_calculator
                elif tabla_joc[5] == tabla_joc[4] and tabla_joc[5] == caracter_calculator and tabla_joc[3] == "_":
                    tabla_joc[3] = caracter_calculator
                elif tabla_joc[8] == tabla_joc[7] and tabla_joc[8] == caracter_calculator and tabla_joc[6] == "_":
                    tabla_joc[6] = caracter_calculator
                elif tabla_joc[6] == tabla_joc[3] and tabla_joc[6] == caracter_calculator and tabla_joc[0] == "_":
                    tabla_joc[0] = caracter_calculator
                elif tabla_joc[7] == tabla_joc[4] and tabla_joc[7] == caracter_calculator and tabla_joc[1] == "_":
                    tabla_joc[1] = caracter_calculator
                elif tabla_joc[8] == tabla_joc[5] and tabla_joc[8] == caracter_calculator and tabla_joc[2] == "_":
                    tabla_joc[2] = caracter_calculator
                elif tabla_joc[8] == tabla_joc[4] and tabla_joc[8] == caracter_calculator and tabla_joc[0] == "_":
                    tabla_joc[0] = caracter_calculator
                elif tabla_joc[6] == tabla_joc[4] and tabla_joc[6] == caracter_calculator and tabla_joc[2] == "_":
                    tabla_joc[2] = caracter_calculator
                elif tabla_joc[0] == tabla_joc[2] and tabla_joc[0] == caracter_calculator and tabla_joc[1] == "_":  # Situatia 3
                    tabla_joc[1] = caracter_calculator
                elif tabla_joc[3] == tabla_joc[5] and tabla_joc[3] == caracter_calculator and tabla_joc[4] == "_":
                    tabla_joc[4] = caracter_calculator
                elif tabla_joc[6] == tabla_joc[8] and tabla_joc[6] == caracter_calculator and tabla_joc[7] == "_":
                    tabla_joc[7] = caracter_calculator
                elif tabla_joc[0] == tabla_joc[6] and tabla_joc[0] == caracter_calculator and tabla_joc[3] == "_":
                    tabla_joc[3] = caracter_calculator
                elif tabla_joc[1] == tabla_joc[7] and tabla_joc[1] == caracter_calculator and tabla_joc[4] == "_":
                    tabla_joc[4] = caracter_calculator
                elif tabla_joc[2] == tabla_joc[8] and tabla_joc[2] == caracter_calculator and tabla_joc[5] == "_":
                    tabla_joc[5] = caracter_calculator
                elif tabla_joc[0] == tabla_joc[8] and tabla_joc[0] == caracter_calculator and tabla_joc[4] == "_":
                    tabla_joc[4] = caracter_calculator
                elif tabla_joc[2] == tabla_joc[6] and tabla_joc[2] == caracter_calculator and tabla_joc[4] == "_":
                    tabla_joc[4] = caracter_calculator
                else:  # Abordare neutra
                    if tabla_joc[4] == "_":
                        tabla_joc[4] = caracter_calculator
                    elif tabla_joc[0] == "_":
                        tabla_joc[0] = caracter_calculator
                    elif tabla_joc[2] == "_":
                        tabla_joc[2] = caracter_calculator
                    elif tabla_joc[6] == "_":
                        tabla_joc[6] = caracter_calculator
                    elif tabla_joc[8] == "_":
                        tabla_joc[8] = caracter_calculator
                    elif tabla_joc[1] == "_":
                        tabla_joc[1] = caracter_calculator
                    elif tabla_joc[3] == "_":
                        tabla_joc[3] = caracter_calculator
                    elif tabla_joc[5] == "_":
                        tabla_joc[5] = caracter_calculator
                    else:
                        tabla_joc[7] = caracter_calculator

            tabla_joc_afisabila = f"Aceasta este tabla curenta a jocului: \n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
            print("Calculatorul a facut mutarea!")

            # Verificarea castigului
            if tabla_joc[0] == tabla_joc[1] == tabla_joc[2] != "_":
                if tabla_joc[0] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                    break
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
                    break
            elif tabla_joc[3] == tabla_joc[4] == tabla_joc[5] != "_":
                if tabla_joc[3] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                    break
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
                    break
            elif tabla_joc[6] == tabla_joc[7] == tabla_joc[8] != "_":
                if tabla_joc[6] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                    break
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
                    break
            elif tabla_joc[0] == tabla_joc[3] == tabla_joc[6] != "_":
                if tabla_joc[0] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                    break
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
                    break
            elif tabla_joc[1] == tabla_joc[4] == tabla_joc[7] != "_":
                if tabla_joc[1] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                    break
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
                    break
            elif tabla_joc[2] == tabla_joc[5] == tabla_joc[8] != "_":
                if tabla_joc[2] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                    break
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
            elif tabla_joc[0] == tabla_joc[4] == tabla_joc[8] != "_":
                if tabla_joc[0] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                    break
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
                    break
            elif tabla_joc[2] == tabla_joc[4] == tabla_joc[6] != "_":
                if tabla_joc[2] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                    break
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
                    break
            else:
                verificare3 = 1


            # Tura Om
            if tabla_joc[0] != "_" and tabla_joc[1] != "_" and tabla_joc[2] != "_" and tabla_joc[3] != "_" and tabla_joc[4] != "_" and tabla_joc[5] != "_" and tabla_joc[6] != "_" and tabla_joc[7] != "_" and tabla_joc[8] != "_":
                tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                print(tabla_joc_afisabila)
                print("Remiza!")
                break
            print("Este randul tau.")
            pozitie_aleasa_om = input(f"\n{model_tabla_joc_afisabila} \n \n{tabla_joc_afisabila} \n \nAlege pozitia pe care vrei sa inserezi simbolul {caracter_om} \n")
            while tabla_joc[int(pozitie_aleasa_om) - 1] == "x" or tabla_joc[int(pozitie_aleasa_om) - 1] == "0":
                pozitie_aleasa_om = input("Pozitia este deja ocupata. Alege o alta pozitie! \n")
            tabla_joc[int(pozitie_aleasa_om) - 1] = caracter_om
            tabla_joc_afisabila = f"Aceasta este tabla curenta a jocului: \n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
            print(f"Ai introdus {caracter_om} pe pozitia {pozitie_aleasa_om}. \n{tabla_joc_afisabila}")


            # Verificarea castigului
            if tabla_joc[0] == tabla_joc[1] == tabla_joc[2] != "_":
                if tabla_joc[0] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
            elif tabla_joc[3] == tabla_joc[4] == tabla_joc[5] != "_":
                if tabla_joc[3] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
            elif tabla_joc[6] == tabla_joc[7] == tabla_joc[8] != "_":
                if tabla_joc[6] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
            elif tabla_joc[0] == tabla_joc[3] == tabla_joc[6] != "_":
                if tabla_joc[0] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
            elif tabla_joc[1] == tabla_joc[4] == tabla_joc[7] != "_":
                if tabla_joc[1] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
            elif tabla_joc[2] == tabla_joc[5] == tabla_joc[8] != "_":
                if tabla_joc[2] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
            elif tabla_joc[0] == tabla_joc[4] == tabla_joc[8] != "_":
                if tabla_joc[0] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
            elif tabla_joc[2] == tabla_joc[4] == tabla_joc[6] != "_":
                if tabla_joc[2] == caracter_om:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Felicitari! Ai castigat!")
                    verificare3 = 0
                else:
                    tabla_joc_afisabila = f"\n {tabla_joc[0]} {tabla_joc[1]} {tabla_joc[2]} \n {tabla_joc[3]} {tabla_joc[4]} {tabla_joc[5]} \n {tabla_joc[6]} {tabla_joc[7]} {tabla_joc[8]}"
                    print(tabla_joc_afisabila)
                    print("Calculatorul a castigat! Mult succes data viitoare!")
                    verificare3 = 0
            else:
                verificare3 = 1
                # print("Este randul calculatorului.")

    else:
        verificare2 = 1
        print("Alege 1 sau 2!")


