def get_fa_from_regular_grammar(grammar):
    Q = grammar.get_non_terminals() + ['K']
    E = grammar.get_terminals()
    q0 = grammar.get_starting_symbol()
    F = ['K']
    S = []

    for production in grammar.get_productions():
        state2 = 'K'
        state1, right_hand_size = production
        if state1 == q0 and right_hand_size[0] == 'E':
            F.append(q0)
            continue
        route = right_hand_size[0]
        if len(right_hand_size) == 2:
            state2 = right_hand_size[1]
        S.append(((state1, route), state2))

    return FiniteAutomata(Q, E, S, q0, F)


def parse_line_from_file(line):
    return [value.strip() for value in line.strip().split('=')[1].strip()[1:-1].strip().split(',')]


def parse_line_from_console(line):
    result = []
    for value in line.strip().split(','):
        result.append(value)
    return result


def parse_transitions(parts):
    result = []
    transitions = []
    index = 0

    while index < len(parts):
        transitions.append(parts[index] + ',' + parts[index + 1])
        index = index + 2

    for transition in transitions:
        left_hand_side, right_hand_side = transition.split('->')
        state2 = right_hand_side.strip()
        state1, route = [value.strip() for value in left_hand_side.strip()[1:-1].split(',')]
        result.append(((state1, route), state2))

    return result


def read_fa_from_file(file_name):
    with open(file_name) as file:
        Q = parse_line_from_file(file.readline())
        E = parse_line_from_file(file.readline())
        q0 = file.readline().split('=')[1].strip()
        F = parse_line_from_file(file.readline())
        S = parse_transitions(parse_line_from_file(''.join([line for line in file])))
        return FiniteAutomata(Q, E, S, q0, F)


def read_fa_from_console():
    input_states = input('Q = ')
    Q = parse_line_from_console(input_states)
    input_alphabet = input('E = ')
    E = parse_line_from_console(input_alphabet)
    q0 = input('q0 = ')
    input_final_states = input('F = ')
    F = parse_line_from_console(input_final_states)
    input_transitions = input('S = ')
    S = parse_transitions(parse_line_from_console(input_transitions))
    return FiniteAutomata(Q, E, S, q0, F)


class FiniteAutomata:
    def __init__(self, Q, E, S, q0, F):
        self._Q = Q  # set of states
        self._E = E  # alphabet
        self._S = S  # transition function
        self._q0 = q0  # initial state
        self._F = F  # final states

    def get_states(self):
        return self._Q

    def get_alphabet(self):
        return self._E

    def get_transition_function(self):
        return self._S

    def get_initial_state(self):
        return self._q0

    def get_final_states(self):
        return self._F

    def is_state(self, state):
        return state in self._Q

    def get_transitions_for_state(self, state):
        if not self.is_state(state):
            raise Exception("Input value is not a state!")

        transitions = [trans for trans in self._S if trans[0][0] == state]
        print('{ ' + ' '.join([' -> '.join([str(part) for part in trans]) for trans in transitions]) + ' }')

    def __str__(self):
        return 'Q = { ' + ', '.join(self._Q) + ' } \n' \
             + 'E = { ' + ', '.join(self._E) + ' } \n' \
             + 'F = { ' + ', '.join(self._F) + ' } \n' \
             + 'S = { ' + ', '.join([' -> '.join([str(part) for part in trans]) for trans in self._S]) + ' } \n' \
             + 'q0 = ' + str(self._q0) + '\n'