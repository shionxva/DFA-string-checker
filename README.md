# DFA String Checker - Web Interface

A modern, user-friendly web interface for checking if strings are accepted by a Deterministic Finite Automaton (DFA).

## Features

✨ **Easy to Use**
- Clean, intuitive interface with step-by-step execution trace
- Try predefined DFA examples or create custom ones
- Real-time validation with helpful error messages

📚 **Predefined Examples**
- Strings ending with "01"
- Even number of 1's
- Strings starting with "1"

⚙️ **Custom DFA Support**
- Define your own states, alphabet, and transitions
- Interactive transition builder
- Full control over DFA configuration

📊 **Detailed Execution Trace**
- See each step of the DFA execution
- Understand how states transition on each input character
- Identify exactly where/why a string is rejected

## Installation

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Flask Application

```bash
python dfa_web_app.py
```

The application will start at `http://localhost:5000`

### 3. Open in Browser

Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage

### Using Predefined Examples

1. Click on the **📚 Examples** tab
2. Select an example DFA from the cards
3. Enter a test string
4. Click **Check String** to see the result

### Creating a Custom DFA

1. Click on the **✏️ Custom DFA** tab
2. Configure your DFA:
   - **States**: Enter comma-separated state names (e.g., `q0, q1, q2`)
   - **Alphabet**: Enter comma-separated input characters (e.g., `0, 1`)
   - **Transitions**: For each (state, character) pair, specify the target state
   - **Start State**: Select the initial state
   - **Accept States**: Enter comma-separated accepting states
3. Enter your test string
4. Click **Check String**

## Project Files

- `dfa_checker.py` - Core DFA class (original command-line version)
- `dfa_web_app.py` - Flask web server and API
- `templates/index.html` - Web interface (HTML, CSS, JavaScript)
- `requirements.txt` - Python package dependencies

## DFA Definition

A DFA consists of:
- **States**: Set of state names
- **Alphabet**: Set of valid input characters
- **Transitions**: Function mapping (state, character) → next_state
- **Start State**: Initial state for processing
- **Accept States**: States where input strings are "accepted"

## API Endpoint

The web app provides a REST API for checking strings:

**POST /api/check**

Request body:
```json
{
    "states": ["q0", "q1", "q2"],
    "alphabet": ["0", "1"],
    "transitions": {
        "q0,0": "q1",
        "q0,1": "q0",
        "q1,0": "q1",
        "q1,1": "q2",
        "q2,0": "q1",
        "q2,1": "q0"
    },
    "start_state": "q0",
    "accept_states": ["q2"],
    "input_string": "01"
}
```

Response:
```json
{
    "accepted": true,
    "final_state": "q2",
    "trace": [
        {
            "step": 0,
            "state": "q0",
            "input": "",
            "message": "Start"
        },
        {
            "step": 1,
            "state": "q1",
            "input": "0",
            "message": "Read '0' -> move to q1"
        },
        {
            "step": 2,
            "state": "q2",
            "input": "1",
            "message": "Read '1' -> move to q2"
        }
    ]
}
```

## Troubleshooting

**Port 5000 already in use?**
- Change the port in the last line of `dfa_web_app.py`:
  ```python
  app.run(debug=True, port=8000)  # Use port 8000 instead
  ```

**Module not found error?**
- Make sure Flask is installed:
  ```bash
  pip install flask
  ```

**Can't find templates?**
- Ensure `templates/index.html` exists in the same directory as `dfa_web_app.py`

## Examples

### Example 1: Strings Ending with "01"
- States: q0, q1, q2
- Alphabet: 0, 1
- Transitions: See the interface
- Accept: q2
- Test: "01" ✅, "001" ✅, "010" ❌

### Example 2: Even Number of 1's
- States: even, odd
- Alphabet: 0, 1
- Transitions: Toggle between even/odd on seeing '1'
- Accept: even
- Test: "" ✅, "11" ✅, "1" ❌

### Example 3: Strings Starting with "1"
- States: q0, q1
- Alphabet: 0, 1
- Transitions: Once first char is '1', stay in q1
- Accept: q1
- Test: "1" ✅, "100" ✅, "0" ❌

---

Made with ❤️ for theory of computation students!
