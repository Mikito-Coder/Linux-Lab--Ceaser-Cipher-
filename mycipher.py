import sys

def caesar_cipher(shift):
    for line in sys.stdin:
        raw_text = line.strip().upper()
        encrypted_text = ""
        group_counter = 0

        for char in raw_text:
            # only allow chars and makes them uppercase
            if char.isalpha():
                # Shift characters
                shifted_position = (ord(char) - ord('A') + shift) % 26 + ord('A')
                encrypted_text += chr(shifted_position)
                group_counter += 1

                # Add a space every five characters to format the output
                if group_counter == 5:
                    encrypted_text += " "
                    group_counter = 0

            # Ignore non-alphabets
            else:
                continue

        return encrypted_text.strip()

# Retrieve the shift value from command line arguments
shift = int(sys.argv[1])
encrypted_message = caesar_cipher(shift)

# Display the encrypted text in blocks of ten lines, each line containing 60 characters
position = 0
while position < len(encrypted_message):
    print(encrypted_message[position:position + 60])
    position += 60
