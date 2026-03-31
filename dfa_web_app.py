from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

class DFA:
    """DFA class"""
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states
    
    def is_accepted(self, s):
        current_state = self.start_state
        
        for char in s:
            if char not in self.alphabet:
                return False, f"Invalid character: '{char}'"
            
            if (current_state, char) not in self.transitions:
                return False, f"No transition from {current_state} on '{char}'"
            
            current_state = self.transitions[(current_state, char)]
        
        is_accepted = current_state in self.accept_states
        return is_accepted, current_state
    
    def trace_execution(self, s):
        current_state = self.start_state
        trace = [{'step': 0, 'state': current_state, 'input': '', 'message': 'Start'}]
        
        for i, char in enumerate(s):
            if char not in self.alphabet:
                trace.append({
                    'step': i + 1,
                    'state': current_state,
                    'input': char,
                    'message': f"Error: Invalid character '{char}'"
                })
                return trace, False
            
            if (current_state, char) not in self.transitions:
                trace.append({
                    'step': i + 1,
                    'state': current_state,
                    'input': char,
                    'message': f"Error: No transition from {current_state} on '{char}'"
                })
                return trace, False
            
            current_state = self.transitions[(current_state, char)]
            trace.append({
                'step': i + 1,
                'state': current_state,
                'input': char,
                'message': f"Read '{char}' -> move to {current_state}"
            })
        
        is_accepted = current_state in self.accept_states
        return trace, is_accepted


EXAMPLES = {
    'ending_01': {
        'name': 'Strings ending with "01"',
        'states': ['q0', 'q1', 'q2'],
        'alphabet': ['0', '1'],
        'transitions': {
            'q0,0': 'q1',
            'q0,1': 'q0',
            'q1,0': 'q1',
            'q1,1': 'q2',
            'q2,0': 'q1',
            'q2,1': 'q0'
        },
        'start_state': 'q0',
        'accept_states': ['q2']
    },
    'even_ones': {
        'name': 'Even number of 1\'s',
        'states': ['even', 'odd'],
        'alphabet': ['0', '1'],
        'transitions': {
            'even,0': 'even',
            'even,1': 'odd',
            'odd,0': 'odd',
            'odd,1': 'even'
        },
        'start_state': 'even',
        'accept_states': ['even']
    },
    'starts_one': {
        'name': 'Strings starting with "1"',
        'states': ['q0', 'q1'],
        'alphabet': ['0', '1'],
        'transitions': {
            'q0,0': 'q0',
            'q0,1': 'q1',
            'q1,0': 'q1',
            'q1,1': 'q1'
        },
        'start_state': 'q0',
        'accept_states': ['q1']
    }
}


@app.route('/')
def index():
    return render_template('index.html', examples=EXAMPLES)


@app.route('/api/check', methods=['POST'])
def check_string():
    try:
        data = request.json
        states = set(data.get('states', []))
        alphabet = set(data.get('alphabet', []))
        start_state = data.get('start_state', '')
        accept_states = set(data.get('accept_states', []))
        input_string = data.get('input_string', '')
        
        # Parse transitions from the format "state,char" -> "next_state"
        transitions = {}
        for key, value in data.get('transitions', {}).items():
            transitions[(key.split(',')[0], key.split(',')[1])] = value
        
        # Validate DFA configuration
        if not states or not start_state or not accept_states:
            return jsonify({'error': 'Incomplete DFA configuration'}), 400
        
        dfa = DFA(states, alphabet, transitions, start_state, accept_states)
        
        trace, is_accepted = dfa.trace_execution(input_string)
        
        return jsonify({
            'accepted': is_accepted,
            'trace': trace,
            'final_state': trace[-1]['state'] if trace else None
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True, port=5000)
