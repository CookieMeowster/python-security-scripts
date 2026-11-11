import sys

authorized_users = {"HEIDI"}
# Pseudocode:
# 1. Loop through each line from stdin.
# 2. Strip the whitespace.
# 3. If blank, skip (continue).
# 4. If ID is "ADMIN" (case-insensitive), print alert.
# 5. If the ID is in authorized_users, print authorized. 
# 6. Otherwise, print an unauthorized alert.

for line in sys.stdin:
    clean_line = line.strip()

    if clean_line == "":
        continue

    # I learned that casefold() checks  case-insensitive text matching and handles some 
    # Unicode characters more thoroughly than .upper().  
    # But I'll stick with .upper for this code.
    user_key = clean_line.upper()

    # Checks the user
    if user_key == "ADMIN":
        print("ALERT: ADMIN login attempt detected")
    elif user_key in authorized_users:
        print(f"User {clean_line} authorized")
    else:
        print(f"ALERT: Unauthorized user attempt: {clean_line}")
