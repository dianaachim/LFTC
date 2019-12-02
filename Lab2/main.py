from Grammar import *
from FiniteAutomata import *

def printMenu():
    print("0. Exit")
    print("1. Input grammar file")
    print("2. Input grammar from console")
    print("3. Display non-terminals")
    print("4. Display terminals")
    print("5. Display productions for non-terminal")
    print("6. Display productions")
    print("7. Is regular")
    print("8. Input FA file")
    print("9. Input FA from console")
    print("10. Display states")
    print("11. Display alphabet")
    print("12. Display transitions")
    print("13. Display transitions for state")
    print("14. Display final states")
    print("15. Get FA from RG")
    print("16. Get grammar from FA")



def main():
    command = ""
    grammar = None
    fa = None
    printMenu()
    while command != "0":
        command = input(">> ")
        if command == "1":
            filename = input("filename: ")
            grammar = read_grammar_from_file(filename)
            print(grammar)
        if command == "2":
            grammar = read_grammar_from_console_input()
            print(grammar)
        if command == "3":
            print(grammar.get_non_terminals())
        if command == "4":
            print(grammar.get_terminals())
        if command == "5":
            non_terminal = input("terminal: ")
            try:
                print(grammar.get_productions_for_non_terminal(non_terminal))
            except Exception as e:
                print(e)
        if command == "6":
            print(grammar.get_productions_for_display())
        if command == "7":
            print(grammar.is_regular())
        if command == "8":
            filename = input("filename: ")
            fa = read_fa_from_file(filename)
            print(fa)
        if command == "9":
            fa = read_fa_from_console()
            print(fa)
        if command == "10":
            print(fa.get_states())
        if command == "11":
            print(fa.get_alphabet())
        if command == "12":
            print(fa.get_transitions())
        if command == "13":
            state = input("state: ")
            print(fa.get_transitions_for_state(state))
        if command == "14":
            print(fa.get_final_states())
        if command == "15":
            if grammar.is_regular():
                fa = get_fa_from_regular_grammar(grammar)
                print(fa)
            else:
                print("Grammar is not regular!")
        if command == "16":
            g = get_grammar_from_finite_automata(fa)
            print(g)


main()