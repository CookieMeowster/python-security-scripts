## Mission

An automated system is sending a stream of user IDs into your script.
However, some IDs are blank (space errors), and some might be a malicious threat actor.

Your mission is to write a script that reads lines from `sys.stdin`:

1. Ignore any completely blank lines.
2. If an ID matches the word `"ADMIN"`, trigger an alert by printing `"ALERT: Unauthorized Admin Access Attempt Detected!"`
3. For any other IDs, print `"User [ID] analyzed successfully."`

## Key Concepts

| Term | What it does |
|------|-------------|
| `sys.argv` | List of words typed in the terminal alongside the script name. |
| `sys.stdin` | Pours data into your script while it's running. |
| `print("Hello")` | Outputs text to the terminal. |
| `print(f"Hello {name}")` | Outputs the *value* of the variable `name` to the terminal. `f` stands for format (string substitution). |

## Conditionals

- **`if`** — Start of a decision tree. Evaluates whether a condition is true or false. If true, the indented code under it runs. If false, it's skipped and execution moves down.
- **`elif`** (else if) — When `if` fails, `elif` checks for specific conditions before giving up. Can stack as many as needed.
- **`else`** — Safety net at the very bottom. Catches everything that didn't match above.
- **`pass`** — Do nothing. Placeholder for an empty block.

## Rules

1. Every conditional must end with a colon (`:`).
2. Indentation matters! This defines what belongs to the block.