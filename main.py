MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}


def encode_text(message):
    return ' '.join(MORSE_CODE_DICT[char.upper()] for char in message if char.upper() in MORSE_CODE_DICT)


def decode_text(message):
    return ''.join(next((key for key, value in MORSE_CODE_DICT.items() if value == morse_char), '') for morse_char in
                   message.split())


text = input("Enter a message: ")

encoded_message = encode_text(text)
print(f"Encoded message: {encoded_message}")

decoded_message = decode_text(encoded_message)
print(f"Decoded message: {decoded_message}")
