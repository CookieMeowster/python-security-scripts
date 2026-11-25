import sys
import argparse 

# This is the "what's this thing" text when someone runs --help
parser = argparse.ArgumentParser(description="Log parser")
#  --input [file] it reads from that file. No flag = reads from stdin.
parser.add_argument("--input", help="Path to a log file")
# On/off switch. Type it = True, skip it = False. No value needed.
parser.add_argument("--verbose", action="store_true")
# Reads what you typed and stores it in "args" so the code below can use it.
args = parser.parse_args()

# The only user I trust. Anyone else gets flagged.
authorized_users = {"HEIDI"}

# Pseudocode when i did it from stdin:
# 1. Loop through each line from stdin.
# 2. Strip the whitespace.
# 3. If blank, skip (continue).
# 4. If ID is "ADMIN" (case-insensitive), print alert.
# 5. If the ID is in authorized_users, print authorized. 
# 6. Otherwise, print an unauthorized alert.

# If I typed --input, reads from that file. Otherwise, reads from stdin like before.
if args.input:
    source = open(args.input, "r")
else:
    source = sys.stdin

# Trackers for the --verbose summary at the bottom.
count = 0
flagged = 0

# The "in" here means "for each item in." I also switched "for line in sys.stdin:"" to "for line in source:"
for line in source:
    count += 1  # one more line off the belt. count+=1 is shorthand for count = count + 1.
    clean_line = line.strip()  # peel the wrapper off
    # line comes off the belt with an invisible \n attached (the wrapper)
    # ex: line = "ADMIN\n" (raw, from the belt)
    # .strip peels off that wrapper
    # clean_line is the name I'm giving the stripped version so I can use it below.
    # ex: clean_line = "ADMIN" (stripped, ready to check)

# The code below makes sure that if someone hits enter with an empty line,
# it does not do a single thing.   
    if clean_line == "":
        continue   

    # I learned that casefold() checks  case-insensitive text matching and handles some 
    # Unicode characters more thoroughly than .upper().  
    # But I'll stick with .upper for this code.
    user_key = clean_line.upper()

    # Checks the user
    if user_key == "ADMIN":
        flagged += 1 # ticked up the threat counter
        print("ALERT: ADMIN login attempt detected")
    elif user_key in authorized_users:
        print(f"User {clean_line} authorized")
    else:
        flagged += 1
        print(f"ALERT: Unauthorized user attempt: {clean_line}")   

# Only prints if you typed --verbose. Gives you the summary line.
if args.verbose:
    print(f"Done. Read {count} lines, flagged {flagged} attempts.")

# Shut the file so it doesn't stay open in the background.
source.close()