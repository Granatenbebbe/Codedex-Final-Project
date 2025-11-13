# Calculator (Codedex Final Project)

**Description**

A simple GUI calculator built with Tkinter. Supports basic arithmetic operations: addition, subtraction, multiplication and division. The interface is button-driven and intended for desktop use.

**Requirements**

- Python 3.7 or newer
- Tkinter (usually included with standard Python on Windows)

**Run**

From PowerShell run:

```powershell
python .\calculator.py
```



**Behavior & Notes**

- The display is a read-only `Entry` widget that shows the current expression and result.
- Expressions are evaluated with Python's `eval()` in a try/except block. Invalid input will show `Error` in the display.
- Some versions include basic protections (e.g. preventing consecutive operators); behavior may vary between the two UI files.

**Security**

This project uses `eval()` to evaluate arithmetic expressions. `eval()` can execute arbitrary Python code — do not paste or type untrusted input into this calculator.

**Suggested Improvements**

- Replace `eval()` with a safe math expression parser (e.g. `asteval`, `simpleeval`, or a custom parser).
- Add keyboard input support and better validation.
- Reduce repetition by generating buttons from a data structure.
- Improve error messages (e.g. show `Division by 0` for division by zero).

