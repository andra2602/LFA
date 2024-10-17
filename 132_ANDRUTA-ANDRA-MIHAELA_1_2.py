def delta(q, a, d):
    if q in d:
        if a in d[q]:
            return d[q][a]
    return []
def d_tilda(q, w, d): # aici q nu mai e doar o stare,e o multime de stari
    if len(w) == 0:
        return q # <q>
    stari_noi = set()
    for st in q:
        # sts = <st>
        # for st in sts;
        tranzitie = delta(st, w[0], d)
        if tranzitie:
            stari_noi.update(tranzitie) # <tranzitie>
    if not stari_noi:
        return set()
    return d_tilda(stari_noi, w[1:], d)


with open("citire.txt", 'r') as f:
    nr_stari = int(f.readline().strip())
    L_stari = [int(x) for x in f.readline().strip().split()]

    card_alfabet = int(f.readline().strip())
    Alfabet = f.readline().strip().split()

    q0 = int(f.readline().strip())

    nr_stari_finale = int(f.readline().strip())
    qf = {int(x) for x in f.readline().strip().split()}

    nr_tranzitii = int(f.readline().strip())
    d = {}
    for _ in range(nr_tranzitii):
        s1, lit, s2 = f.readline().strip().split()
        st1 = int(s1)
        st2 = int(s2)
        if st1 not in d:
            d[st1] = {}
        if lit not in d[st1]:
            d[st1][lit] = [st2]
        else:
            d[st1][lit].append(st2)

    nr_cuv = int(f.readline().strip())
    L_cuv = [f.readline().strip() for _ in range(nr_cuv)]

# Afiseaza datele citite
# print("Numarul de stari:", nr_stari)
# print("Lista de stari:", L_stari)
# print("Cardinalul alfabetului:", card_alfabet)
# print("Alfabetul:", Alfabet)
# print("Starea initiala:", q0)
# print("Numarul starilor finale este:", nr_stari_finale)
# print("Starile finale:", qf)
# print("Nr. tranzitii:", nr_tranzitii)
# print("Tranzitiile:", d)
# print("Numar cuvinte de verificat:", nr_cuv)
# print("Lista de cuvinte:", L_cuv)

with open("afisare.txt", 'w') as g:
    for cuvant in L_cuv:
        rezultat = d_tilda({q0}, cuvant, d) # <q0>
        if rezultat.intersection(qf):
            g.write("DA\n")
        else:
            g.write("NU\n")


