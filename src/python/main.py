import sys

# PYTHON TERMINAL ARGUMENTS
if len(sys.argv) < 2:
    print("[ERROR] Please provide a firmware file.")
    print("[USAGE] python3 main.py <path_to_file>")
    sys.exit(1)

target_file = sys.argv[1]

# READING BIN FILE - CONVERTING TO HEXADECIMAL
try:
    with open(target_file, "rb") as file:
        first_bytes = file.read(16)
        print(first_bytes.hex(" ").upper())
except FileNotFoundError:
    print(f"[ERROR] Could not find file at {target_file}")