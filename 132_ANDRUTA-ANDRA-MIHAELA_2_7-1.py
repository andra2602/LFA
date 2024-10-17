from queue import Queue

# Citirea NFA-ului din fișier
with open("citire.txt", 'r') as f:
    nr_stari = int(f.readline().strip())
    L_stari = [int(x) for x in f.readline().strip().split()]

    card_alfabet = int(f.readline().strip())
    Alfabet = f.readline().strip().split()

    q0 = int(f.readline().strip())
    q0 = L_stari.index(q0) + 1

    nr_stari_finale = int(f.readline().strip())
    qf = [int(x) for x in f.readline().strip().split()]
    for i in range(len(qf)):
        qf[i] = L_stari.index(qf[i]) + 1

    nr_tranzitii = int(f.readline().strip())
    nfa = {}
    for _ in range(nr_tranzitii):
        s1, lit, s2 = f.readline().strip().split()
        st1 = L_stari.index(int(s1)) + 1
        st2 = L_stari.index(int(s2)) + 1
        if st1 not in nfa:
            nfa[st1] = {}
        if lit not in nfa[st1]:
            nfa[st1][lit] = [st2]
        else:
            nfa[st1][lit].append(st2)
    for i in range(len(L_stari)):
        L_stari[i] = i+1

# Dictionare pt a procesa corespondenta intre starile nfa si dfa
d1 = {}
d2 = {}
qf_dfa = []

maxim_st = max(L_stari) + 1 #il folosim pt a genera noile stari
set_q0 = tuple(sorted({q0}))
d1[set_q0] = q0
d2[q0] = set_q0
# initializam coada ,vom procesa starea initiala si dupa parcurgem starile cu ajutorul ei
coada_stari = Queue()
coada_stari.put(q0)

# Procesarea pentru DFA
dfa = {}
dfa[q0] = {}

while not coada_stari.empty():
    stare_crt = coada_stari.get()
    stari_curente = d2[stare_crt]
    dfa[stare_crt] = {}
    for lit in Alfabet:
        L_nou = set()
        for state in stari_curente:
            if state in nfa and lit in nfa[state]:
                L_nou.update(nfa[state][lit])
        if L_nou:
            L_nou = tuple(sorted(L_nou))
            if L_nou not in d1:
                stare_next = maxim_st
                maxim_st += 1
                d2[stare_next] = L_nou
                d1[L_nou] = stare_next
                coada_stari.put(stare_next)
            dfa[stare_crt][lit] = d1[L_nou]

# determinam starile finale pt dfa
qf_dfa = []
for stare_dfa, L_stari in d2.items():
    if any(stare_nfa in qf for stare_nfa in L_stari):
        qf_dfa.append(stare_dfa)

L_stari_dfa = sorted(dfa.keys())
nr_stari_dfa = len(L_stari_dfa)
q0_dfa_output = q0
qf_dfa_output = sorted(qf_dfa)

tranzitii_dfa = []
for stare in L_stari_dfa:
    for lit in dfa[stare]:
        tranzitii_dfa.append((stare, lit, dfa[stare][lit]))

# Afisarea dfa-ului in fisiser
with open("dfa.txt", 'w') as f:
    f.write(f"{nr_stari_dfa}\n")
    f.write(" ".join(map(str, L_stari_dfa)) + "\n")
    f.write(f"{card_alfabet}\n")
    f.write(" ".join(Alfabet) + "\n")
    f.write(f"{q0_dfa_output}\n")
    f.write(f"{len(qf_dfa_output)}\n")
    f.write(" ".join(map(str, qf_dfa_output)) + "\n")
    f.write(f"{len(tranzitii_dfa)}\n")
    for tranz in tranzitii_dfa:
        f.write(f"{tranz[0]} {tranz[1]} {tranz[2]}\n")