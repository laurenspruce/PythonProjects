# Dictionary representing the morse code chart
MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
}

# Updated encrypt function to handle user input characters
def encrypt(message):
    cipher = ""
    for letter in message:
        if letter.upper() in MORSE_CODE_DICT:
            cipher += MORSE_CODE_DICT[letter.upper()] + " "
        elif letter == " ":
            cipher += " "
        else:
            print(f"Ignoring unsupported character: {letter}")
    return cipher

# Updated decrypt function to handle multiple spaces between words
def decrypt(message):
    message += " "
    decipher = ""
    citext = ""
    for letter in message:
        if letter != " ":
            citext += letter
        else:
            if citext:
                decipher += MORSE_CODE_DICT.get(citext, "")
                citext = ""
            else:
                # Add a space for multiple consecutive spaces
                decipher += " "
    return decipher

# Updated main function to take user input
def main():
    user_input = input("Enter a word to translate to Morse code: ")
    result = encrypt(user_input)
    print(f"Morse Code for '{user_input}': {result}")

    user_input_morse = input("Enter Morse code to translate to English: ")
    result = decrypt(user_input_morse)
    print(f"Decrypted message: {result}")

# Executes the main function
if __name__ == "__main__":
    main()
