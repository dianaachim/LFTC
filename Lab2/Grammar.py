def parse_line_from_file(line):
    return [value.strip() for value in line.strip().split('=')[1].strip()[1:-1].strip().split(',')]


def parse_productions(productions):
    result = []
    for prod in productions:
        left_hand_side, right_hand_side = prod.split('->')
        left_hand_side = left_hand_side.strip()
        right_hand_side = [value.strip() for value in right_hand_side.split('|')]

        for value in right_hand_side:
            result.append((left_hand_side, value))

    return result


def read_grammar_from_file(file_name):
    with open(file_name) as file:
        N = parse_line_from_file(file.readline())
        E = parse_line_from_file(file.readline())
        S = file.readline().split('=')[1].strip()
        P = parse_productions(parse_line_from_file(''.join([line for line in file])))
        return Grammar(N, E, P, S)


def parse_line_from_console(line):
    result = []
    for value in line.strip().split(','):
        result.append(value)
    return result


def read_grammar_from_console_input():
    input_non_terminals = input('N = ')
    N = parse_line_from_console(input_non_terminals)
    input_terminals = input('E = ')
    E = parse_line_from_console(input_terminals)
    S = input('S = ')
    input_productions = input('P = ')
    P = parse_productions(parse_line_from_console(input_productions))
    return Grammar(N, E, P, S)


def get_grammar_from_finite_automata(finite_automata):
    N = finite_automata.get_states()
    E = finite_automata.get_alphabet()
    S = finite_automata.get_initial_state()
    P = []

    if finite_automata.get_initial_state() in finite_automata.get_final_states():
        P.append((finite_automata.get_initial_state(), 'E'))

    for transition in finite_automata.get_transition_function():
        left_hand_side, state_2 = transition
        state_1, route = left_hand_side

        P.append((state_1, route + state_2))

        if state_2 in finite_automata.get_final_states():
            P.append((state_1, route))

    return Grammar(N, E, P, S)


class Grammar:
    def __init__(self, N, E, P, S):
        self._N = N  # set of non terminal symbols
        self._E = E  # set of terminal symbols
        self._P = P  # set of productions
        self._S = S  # starting symbol

    def is_non_terminal(self, value):
        return value in self._N

    def is_terminal(self, value):
        return value in self._E

    def is_regular(self):
        # a grammar is regular if all the productions have one of the following forms:
        # 1) A -> a
        # 2) A -> aB
        # 3) A -> E, E being the empty string

        used_in_right_hand_side = dict()
        not_allowed_in_right_hand_side = list()

        for production in self._P:
            left_hand_side, right_hand_side = production
            has_terminal = False
            has_non_terminal = False
            if len(right_hand_side) > 2:
                return False
            for char in right_hand_side:
                if self.is_non_terminal(char):
                    used_in_right_hand_side[char] = True
                    has_non_terminal = True
                elif self.is_terminal(char):
                    if has_non_terminal:
                        return False
                    has_terminal = True
                if char == 'E':
                    not_allowed_in_right_hand_side.append(left_hand_side)

            if has_non_terminal and not has_terminal:
                return False

        for char in not_allowed_in_right_hand_side:
            if char in used_in_right_hand_side:
                return False

        return True

    def get_starting_symbol(self):
        return self._S

    def get_non_terminals(self):
        return self._N

    def get_terminals(self):
        return self._E

    def get_productions(self):
        return self._P

    def get_productions_for_display(self):
        productions_string = "{ "
        for prod in self._P:
            productions_string += prod[0] + '->' + prod[1] + '\n'
        productions_string += " }"
        return productions_string

    def get_productions_for_non_terminal(self, non_terminal):
        if not self.is_non_terminal(non_terminal):
            raise Exception("Value given is not a non-terminal!")

        productions = [prod for prod in self._P if prod[0] == non_terminal]
        print(', '.join([' -> '.join(prod) for prod in productions]))

    def __str__(self):
        productions_string = "{ "
        for prod in self._P:
            productions_string += prod[0] + '->' + prod[1] + '\n'
        productions_string += " }"
        return 'N = { ' + ', '.join(self._N) + ' }\n' \
             + 'E = { ' + ', '.join(self._E) + ' }\n' \
             + 'P = ' + productions_string + '\n' \
             + 'S = ' + str(self._S) + '\n'