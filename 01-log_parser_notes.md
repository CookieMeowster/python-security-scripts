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
| `print(f"Hello {name}")` | Outputs the value of the variable `name`. `f` stands for format. |
| `.strip()` | Removes white spaces from beginning and end of a text. Needed because sys.stdin adds a trailing newline. The user types "ADMIN", but the computer sees "ADMIN\n". |
| `.upper()` | This forces conversion in a string to uppercase. Used here for case-insensitive matching, so "admin", "Admin", and "ADMIN" all trigger the same check. |  
| `argparse` | Lets you pass arguments in the terminal like --input file.log |
| `re.search()` | Finds a pattern in a string (like an IP address in a log line). |
| `csv.writer` | Writes rows to a .csv file. |

## Conditionals

- **`if`** - Start of a decision tree. Evaluates whether a condition is true or false. If true, the indented code under it runs. If false, it's skipped and execution moves down.
- **`elif`** (else if) - When `if` fails, `elif` checks for specific conditions before giving up. Can stack as many as needed.
- **`else`** - Safety net at the very bottom. Catches everything that didn't match above.
- **`pass`** - Do nothing. Placeholder for an empty block.

## Rules

1. Every conditional must end with a colon (`:`).
2. Indentation matters! This defines what belongs to the block.

ex: if network_load > 90:
    print("Alert")

## Pseudocode

Writing out your program's logic in plain English before you write the actual code. Makes sure the logic is sound before you build.

1. Loop through each line from stdin. Think of stdin as a conveyor belt that keeps handing you one line at a time. The loop says: grab a line, run my code on it, grab the next one. Repeat until the belt runs out.

2. Strip the whitespace. The belt doesn't hand you a clean "ADMIN", it hands you "ADMIN\n". That \n is just the wrapper from when the line got boxed up and sent. Strip peels it off so you're holding the actual ID, not some invisible packaging.

3. IF the line is blank after stripping, skip it. This is the "blank space errors" part of the mission. The box was empty. Nothing to check, so just toss it and grab the next one off the belt.

4. ELSE IF the ID is "ADMIN", print the alert. We use .upper() so it doesn't matter if they type "admin" or "Admin" or "ADMIN", it all gets caught. This is similar to the kernel bouncer doing its job but in a different situation.

5. ELSE print the success message.Everything that isn't an empty box and isn't ADMIN just gets cleared. "You're fine, moving on." Next line off the belt.

## Test Output

```bash
$ echo -e "heidi\n\nADMIN\nrandom_guy" | python log_parser.py
User heidi authorized
ALERT: ADMIN login attempt detected
ALERT: Unauthorized user attempt: random_guy
```
<<<<<<< HEAD

## argparse



## Regex



## CSV Output

  
=======
>>>>>>> 9cb7cfb495f588b22d9271992f447aa3622e3542
