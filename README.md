# Assignments

## ASSIGNMENT 1
### Simulating an NFA and Word Acceptance

In this assignment, I simulate the functioning of a **Nondeterministic Finite Automaton (NFA)** and explore how to verify whether specific words are accepted by it.

Key aspects include:

- **Defining the NFA**: Establishing the set of states, the alphabet, transition functions, start state, and accepting states.
- **Simulating Word Acceptance**: Using algorithms to simulate how an NFA processes input words, considering the non-deterministic nature where multiple paths are possible.
- **Handling Epsilon Transitions**: Ensuring that the NFA correctly processes transitions that do not consume any input symbol.
- **Verifying Results**: Determining if an input word reaches an accepting state, confirming whether it is accepted by the automaton.

---

## ASSIGNMENT 2
### Converting an NFA to a DFA

This assignment focuses on the process of converting an NFA into a **Deterministic Finite Automaton (DFA)**.

Main topics covered:

- **Subset Construction Algorithm**: Applying this algorithm to systematically convert the NFA's non-deterministic states into deterministic sets of states.
- **Handling Epsilon Closures**: Accounting for epsilon transitions to ensure all possible state transitions are considered in the DFA.
- **Minimization of the DFA**: Optionally minimizing the resulting DFA by eliminating redundant states for improved efficiency.
- **Verification**: Comparing the behavior of the original NFA and the constructed DFA to ensure language equivalence.

---

## ASSIGNMENT 3
### Simulating a DPDA and Verifying Word Acceptance

In the final assignment, I focus on simulating a **Deterministic Pushdown Automaton (DPDA)** and checking how it accepts words.

Key areas include:

- **Defining the DPDA**: Setting up states, input and stack alphabets, transition functions, initial state, initial stack symbol, and accepting states.
- **Stack Operations**: Implementing push and pop operations on the stack as per transition rules.
- **Determinism in DPDA**: Ensuring that for each combination of current state, input symbol, and top of the stack, there is at most one possible transition.
- **Acceptance Conditions**: Verifying word acceptance either through final states or by emptying the stack.
- **Handling Edge Cases**: Addressing scenarios where the stack is empty or transitions are undefined.

---

This series of assignments not only enhances understanding of automata theory but also provides hands-on experience in simulating and analyzing different types of automata. These foundational concepts are crucial for fields such as formal language processing, compiler construction, and theoretical computer science.

___


# Teme

## TEMA 1
### Simularea unui NFA și acceptarea cuvintelor în acesta

În această temă, simulez functionarea unui **Nondeterministic Finite Automaton (NFA)** și cum pot verifica dacă anumite cuvinte sunt acceptate de acesta.

## TEMA 2
### Transformarea unui NFA în DFA

Această temă se va concentra pe procesul de conversie a unui NFA într-un **Deterministic Finite Automaton (DFA)**.

## TEMA 3
### Simularea unui DPDA (Deterministic Pushdown Automaton) și verificarea acceptării cuvintelor de către acesta

În ultima temă, ma concentrez pe simularea unui **Deterministic Pushdown Automaton (DPDA)**. Verific modul în care un DPDA poate accepta cuvinte.
