import sys

# Pseudocode:
# 1. Loop through each line from stdin.
# 2. Strip the whitespace.
# 3. If blank, skip (continue).
# 4. If ID is "ADMIN" (case-insensitive), print alert.
# 5. Otherwise, print success message.

for line in sys.stdin:
    clean_line = line.strip()

#1. If the line is empty. skip it
    if clean_line == "":
        pass
#2. Checks if it maches our threat target (ignores case sensitivity)
    elif clean_line.upper() == "ADMIN":
        print("ALERT: Unauthorized Admin Access Attempt!")
#3. For everything else
    else:
        #Failed the variable name inside the f-string here:
        print(f"User {clean_line} analysed") 