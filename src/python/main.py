import sys
import os

# PYTHON TERMINAL ARGUMENTS
def read_bin():
    if len(sys.argv) < 2:
        print("[ERROR] Please provide a firmware file.")
        print("[USAGE] python3 main.py <path_to_file>")
        sys.exit(1)

    target_file = sys.argv[1]
    file_size = os.path.getsize(target_file)

    # READING BIN FILE - CONVERTING TO HEXADECIMAL
    try:
        with open(target_file, "rb") as file:
            first_bytes = file.read(file_size)
            print(first_bytes.hex(" ").upper())
    except FileNotFoundError:
        print(f"[ERROR] Could not find file at {target_file}")


# BINARY FREQUENCY COUNT
def binary_freq(t_file, f_size):
    pass



if __name__ == "__main__":
    read_bin()