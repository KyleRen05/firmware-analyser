import sys
import math
import os
import string

# PYTHON TERMINAL ARGUMENTS
if len(sys.argv) < 2:
    print("[ERROR] Please provide a firmware file.")
    print("[USAGE] python3 main.py <path_to_file>")
    sys.exit(1)

target_file = sys.argv[1]
file_size = os.path.getsize(target_file)
chunk_size = 4096

# READING BIN FILE - CONVERTING TO HEXADECIMAL
def read_file(target_file, file_size):
    try:
        with open(target_file, "rb") as file:
            first_bytes = file.read(chunk_size)
            return first_bytes
    except FileNotFoundError:
        print(f"[ERROR] Could not find file at {target_file}")
        return 0


# BINARY FREQUENCY COUNT
def shannons_formula(f_bytes):
    ''' FREQUENCY COUNT '''
    hex_array = [0] * 256
    current_chunk_size = len(f_bytes)

    # counting repeats
    for b in f_bytes:
        hex_array[b] += 1

    # printing all bytes + counter   
    print("Do you want to see all bytes?: Y/N")
    input1 = input().upper()
    if input1 == "Y":
        for x in range(256):
            if hex_array[x] > 0:
                print(f"{x:02X} : {hex_array[x]}")
    
    

    ''' PROBABILITY CHECK '''
    accum = 0
    for c in range(256):
        if hex_array[c] > 0:
            p = hex_array[c]/current_chunk_size 
            value = (p * math.log2(p))
            accum += value

    ''' SCORE CALCULATION '''
    score = accum * -1
    return score





if __name__ == "__main__":
    file_data = read_file(target_file=target_file, file_size=file_size)
    score  = shannons_formula(file_data)
    print(f"SCORE: {score:.1f}")