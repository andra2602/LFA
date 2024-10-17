def citire_dpda(filename):
    with open(filename, "r") as f:
        # Citim nr de stari
        nr_stari = int(f.readline().strip())
        nr_litere_alfabet = int(f.readline().strip())

        alfabet = []
        # Literele din alfabet
        for _ in range(nr_litere_alfabet):
            litera = f.readline().strip()
            alfabet.append(litera)

        stare_init = int(f.readline().strip())
        simbol_stiva = f.readline().strip()
        stiva = [simbol_stiva]

        nr_stari_finale = int(f.readline().strip())
        stari_finale = []
        # Starile finale
        for _ in range(nr_stari_finale):
            stare = int(f.readline().strip())
            stari_finale.append(stare)

        nr_tranzitii = int(f.readline().strip())
        tranzitii = {}
        # Citesc tranzitiile = dictionar de dictionare
        for _ in range(nr_tranzitii):
            aux = f.readline().split()
            stare = int(aux[0].strip())
            litera = aux[1].strip()
            este_deja_pe_stiva = aux[2].strip()
            vreau_sa_pun_pe_stiva = aux[3].strip()
            stare_urm = int(aux[4].strip())
            if stare not in tranzitii:
                tranzitii[stare] = {}
            if litera not in tranzitii[stare]:
                tranzitii[stare][litera] = []
            tranzitii[stare][litera].append((este_deja_pe_stiva, vreau_sa_pun_pe_stiva, stare_urm))

    return (nr_stari, alfabet, stare_init, simbol_stiva, stari_finale, tranzitii)

def procesare_cuvant(dpda, cuvant):
    (nr_stari, alfabet, stare_init, simbol_stiva, stari_finale, tranzitii) = dpda

    stiva = [simbol_stiva]
    stare_curenta = stare_init

    i = 0

    while i < len(cuvant):
        litera = cuvant[i]
        print(stare_curenta,litera,stiva)
        if litera not in alfabet:
            return False
        if litera not in tranzitii.get(stare_curenta, {}):
            # verif lambda
            if 'l' in tranzitii.get(stare_curenta, {}):
                tranzitie_aplicata = False
                for (este_deja_pe_stiva, vreau_sa_pun_pe_stiva, stare_urm) in tranzitii[stare_curenta]['l']:
                    if stiva and stiva[-1] == este_deja_pe_stiva:
                        stiva.pop()
                        if vreau_sa_pun_pe_stiva != 'l':
                            for simbol in reversed(vreau_sa_pun_pe_stiva):
                                stiva.append(simbol)
                        stare_curenta = stare_urm
                        tranzitie_aplicata = True
                        break
                if tranzitie_aplicata:
                    continue
            return False
        else:
            tranzitie_aplicata = False
            for (este_deja_pe_stiva, vreau_sa_pun_pe_stiva, stare_urm) in tranzitii[stare_curenta][litera]:
                if stiva and stiva[-1] == este_deja_pe_stiva:
                    stiva.pop()
                    if vreau_sa_pun_pe_stiva != 'l':
                        for simbol in reversed(vreau_sa_pun_pe_stiva):
                            stiva.append(simbol)
                    stare_curenta = stare_urm
                    tranzitie_aplicata = True
                    break
            if not tranzitie_aplicata:
                # fortare lambda
                if 'l' in tranzitii.get(stare_curenta, {}):
                    for (este_deja_pe_stiva, vreau_sa_pun_pe_stiva, stare_urm) in tranzitii[stare_curenta]['l']:
                        if stiva and stiva[-1] == este_deja_pe_stiva:
                            stiva.pop()
                            if vreau_sa_pun_pe_stiva != 'l':
                                for simbol in reversed(vreau_sa_pun_pe_stiva):
                                    stiva.append(simbol)
                            stare_curenta = stare_urm
                            tranzitie_aplicata = True
                            break
                if tranzitie_aplicata:
                    continue
                return False
        i += 1

    # Verificare tranzitii lambda la final
    while 'l' in tranzitii.get(stare_curenta, {}):
        tranzitie_aplicata = False
        for (este_deja_pe_stiva, vreau_sa_pun_pe_stiva, stare_urm) in tranzitii[stare_curenta]['l']:
            if stiva and stiva[-1] == este_deja_pe_stiva:
                stiva.pop()
                if vreau_sa_pun_pe_stiva != 'l':
                    for simbol in reversed(vreau_sa_pun_pe_stiva):
                        stiva.append(simbol)
                stare_curenta = stare_urm
                tranzitie_aplicata = True
                break
        if not tranzitie_aplicata:
            break

    # Verificare condiții de acceptare
    if (stare_curenta in stari_finale and not stiva) or (stare_curenta in stari_finale) or (not stiva):
        return True

    return False

# Citirea DPDA din fișier
dpda = citire_dpda("input.txt")

# Citirea cuvântului de verificat
with open("input.txt", "r") as f:
    lines = f.readlines()
    cuvant = lines[-1].strip()

# Verificarea acceptării cuvântului
acceptat = procesare_cuvant(dpda, cuvant)
print("acceptat" if acceptat else "neacceptat")
