class DFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        """
        Args:
            states: set of state names
            alphabet: set of valid input characters
            transitions: dict with key (state, char) -> value next_state
            start_state: starting state
            accept_states: set of accepting states
        """
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states
    
    def is_accepted(self, s):
        """
        Check if string s is accepted by the DFA
        
        Args:
            s: input string to check
            
        Returns:
            True if string is accepted, False otherwise
        """
        current_state = self.start_state
        
        for char in s:
            if char not in self.alphabet:
                return False
            
            # Get next state from transition function
            if (current_state, char) not in self.transitions:
                return False
            
            current_state = self.transitions[(current_state, char)]
        
        return current_state in self.accept_states


def example1():
    print("Example 1: DFA accepting strings ending with '01'")
    print("-" * 50)
    
    dfa = DFA(
        states={'q0', 'q1', 'q2'},
        alphabet={'0', '1'},
        transitions={
            ('q0', '0'): 'q1',
            ('q0', '1'): 'q0',
            ('q1', '0'): 'q1',
            ('q1', '1'): 'q2',
            ('q2', '0'): 'q1',
            ('q2', '1'): 'q0',
        },
        start_state='q0',
        accept_states={'q2'}
    )
    
    test_strings = ['01', '001', '101', '0', '1', '11', '010', '0101']
    
    for s in test_strings:
        result = dfa.is_accepted(s)
        print(f"  '{s}': {'ACCEPTED' if result else 'REJECTED'}")
    print()


def example2():
    print("Example 2: DFA accepting even number of 1's")
    print("-" * 50)
    
    dfa = DFA(
        states={'even', 'odd'},
        alphabet={'0', '1'},
        transitions={
            ('even', '0'): 'even',
            ('even', '1'): 'odd',
            ('odd', '0'): 'odd',
            ('odd', '1'): 'even',
        },
        start_state='even',
        accept_states={'even'}
    )
    
    test_strings = ['', '0', '1', '11', '101', '1001', '111', '1111']
    
    for s in test_strings:
        result = dfa.is_accepted(s)
        print(f"  '{s}': {'ACCEPTED' if result else 'REJECTED'}")
    print()


def example3():
    print("Example 3: DFA accepting strings starting with '1'")
    print("-" * 50)
    
    dfa = DFA(
        states={'q0', 'q1'},
        alphabet={'0', '1'},
        transitions={
            ('q0', '0'): 'q0',
            ('q0', '1'): 'q1',
            ('q1', '0'): 'q1',
            ('q1', '1'): 'q1',
        },
        start_state='q0',
        accept_states={'q1'}
    )
    
    test_strings = ['', '0', '1', '10', '11', '100', '101', '011']
    
    for s in test_strings:
        result = dfa.is_accepted(s)
        print(f"  '{s}': {'ACCEPTED' if result else 'REJECTED'}")
    print()


if __name__ == "__main__":
    example1()
    example2()
    example3()