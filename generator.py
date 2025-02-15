from mnemonic import Mnemonic
import sys
import random
import string
import os  # For Directory Management

# This Function Generates A Random Seed Phrase
def generate_mnemonic(words_count=12):
    if words_count == 12:
        strength = 128  # 128 Bits For 12 Words
    elif words_count == 24:
        strength = 256  # 256 Bits For 24 Words
    else:
        raise ValueError("Only 12 Or 24 Words Are Supported")

    # Create A Mnemonic Object With The English Language
    mnemo = Mnemonic("english")
    
    # Generate Mnemonic (Seed Phrase) Based On Strength (128 Or 256 Bits)
    mnemonic_phrase = mnemo.generate(strength=strength)

    return mnemonic_phrase

# Request The User To Choose The Number Of Words (12 Or 24)
while True:
    try:
        words_count = int(input("Please Enter The Number Of Words For The Seed Phrase (12 Or 24): "))
        if words_count not in [12, 24]:
            print("Please Choose Either 12 Or 24.")
        else:
            break
    except ValueError:
        print("Invalid Input. Please Enter A Valid Number (12 Or 24).")

# Request The User To Input The Number Of Mnemonic Phrases They Want To Generate
while True:
    try:
        num_phrases = int(input(f"Please Enter The Number Of Mnemonic Phrases To Generate: "))
        if num_phrases <= 0:
            print("Please Enter A Positive Number.")
        else:
            break
    except ValueError:
        print("Invalid Input. Please Enter A Valid Number.")

# Create The Combo Folder If It Does Not Exist
combo_dir = "combo"
if not os.path.exists(combo_dir):
    os.makedirs(combo_dir)

# Determine The Desired Folder Based On The Number Of Words (12 Or 24)
output_dir = os.path.join(combo_dir, str(words_count))  # Folder Combo/12 Or Combo/24

# Create The Desired Folder If It Does Not Exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate A Random File Name With A Prefix Based On The Number Of Words
random_suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=8))  # Random Part
filename = f"{words_count}_{random_suffix}_mnemonic_phrases.txt"  # Final File Name

# Determine The Full File Path
file_path = os.path.join(output_dir, filename)

# Create Or Open The File To Save The Mnemonic Phrases
with open(file_path, "w") as file:
    for i in range(num_phrases):
        # Generate The Mnemonic Based On The Chosen Number Of Words
        mnemonic_phrase = generate_mnemonic(words_count)  
        # Save The Mnemonic To The File
        file.write(mnemonic_phrase + "\n")
        
        # Manually Display A Progress Bar
        progress = (i + 1) / num_phrases * 100  # Progress Percentage
        bar = '=' * int(progress / 2)  # Create The Progress Bar
        sys.stdout.write(f"\r[{bar:<50}] {i + 1}/{num_phrases} ({progress:.2f}%)")
        sys.stdout.flush()

print(f"\n{num_phrases} Mnemonic Phrases Have Been Written To '{file_path}'")
