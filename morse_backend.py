"""
===========================================================
MORSE LOVER - ADVANCED MORSE CODE BACKEND
===========================================================

Author : ChatGPT
Purpose:
    - Convert normal text to Morse code
    - Convert Morse code back to readable text
    - Support:
        * Letters
        * Numbers
        * Punctuation
        * Paragraphs
        * Special symbols
    - Clean APIs for integration with Flask/FastAPI/etc.

Features:
    ✔ Encode any text to Morse
    ✔ Decode Morse to text
    ✔ Handle multiline paragraphs
    ✔ Handles unsupported characters safely
    ✔ Detailed utility functions
    ✔ Beginner-friendly structure

===========================================================
"""

from typing import Dict


class MorseCodeTranslator:
    """
    Main Morse Code Translator Class
    """

    def __init__(self):

        # =====================================================
        # TEXT -> MORSE DICTIONARY
        # =====================================================

        self.TEXT_TO_MORSE: Dict[str, str] = {

            # Letters
            'A': '.-',
            'B': '-...',
            'C': '-.-.',
            'D': '-..',
            'E': '.',
            'F': '..-.',
            'G': '--.',
            'H': '....',
            'I': '..',
            'J': '.---',
            'K': '-.-',
            'L': '.-..',
            'M': '--',
            'N': '-.',
            'O': '---',
            'P': '.--.',
            'Q': '--.-',
            'R': '.-.',
            'S': '...',
            'T': '-',
            'U': '..-',
            'V': '...-',
            'W': '.--',
            'X': '-..-',
            'Y': '-.--',
            'Z': '--..',

            # Numbers
            '0': '-----',
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.',

            # Symbols
            '.': '.-.-.-',
            ',': '--..--',
            '?': '..--..',
            "'": '.----.',
            '!': '-.-.--',
            '/': '-..-.',
            '(': '-.--.',
            ')': '-.--.-',
            '&': '.-...',
            ':': '---...',
            ';': '-.-.-.',
            '=': '-...-',
            '+': '.-.-.',
            '-': '-....-',
            '_': '..--.-',
            '"': '.-..-.',
            '$': '...-..-',
            '@': '.--.-.',

            # Space
            ' ': '/'
        }

        # =====================================================
        # MORSE -> TEXT DICTIONARY
        # =====================================================

        self.MORSE_TO_TEXT: Dict[str, str] = {
            value: key for key, value in self.TEXT_TO_MORSE.items()
        }

    # =========================================================
    # ENCODE FUNCTION
    # =========================================================

    def text_to_morse(self, text: str) -> str:
        
        """
        Convert normal text into Morse code

        Parameters:
            text (str): Normal text input

        Returns:
            str: Morse code output
        """

        encoded_output = []

        # Convert everything to uppercase
        text = text.upper()

        for char in text:

            # If character exists in dictionary
            if char in self.TEXT_TO_MORSE:
                encoded_output.append(self.TEXT_TO_MORSE[char])

            else:
                # Unsupported character handling
                encoded_output.append('[UNKNOWN]')

        return ' '.join(encoded_output)

    # =========================================================
    # DECODE FUNCTION
    # =========================================================

    def morse_to_text(self, morse_code: str) -> str:
        """
        Convert Morse code into normal text

        Parameters:
            morse_code (str): Morse code input

        Returns:
            str: Decoded readable text
        """

        decoded_output = []

        # Split morse sequence
        morse_words = morse_code.split(' / ')

        for word in morse_words:

            letters = word.split()

            decoded_word = ''

            for letter in letters:

                if letter in self.MORSE_TO_TEXT:
                    decoded_word += self.MORSE_TO_TEXT[letter]
                else:
                    decoded_word += '?'

            decoded_output.append(decoded_word)

        return ' '.join(decoded_output)

    # =========================================================
    # PRETTY PRINT FUNCTIONS
    # =========================================================

    def print_conversion_summary(self, original: str):
        """
        Display conversion summary
        """

        morse = self.text_to_morse(original)

        print("\n==============================")
        print(" ORIGINAL TEXT")
        print("==============================")
        print(original)

        print("\n==============================")
        print(" MORSE CODE")
        print("==============================")
        print(morse)

        print("\n==============================")
        print(" DECODED AGAIN")
        print("==============================")
        print(self.morse_to_text(morse))

    # =========================================================
    # FILE ENCODER
    # =========================================================

    def encode_file(self, input_file: str, output_file: str):
        """
        Encode text file into Morse code
        """

        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        morse = self.text_to_morse(content)

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(morse)

        print(f"\n✅ File encoded successfully -> {output_file}")

    # =========================================================
    # FILE DECODER
    # =========================================================

    def decode_file(self, input_file: str, output_file: str):
        """
        Decode Morse file into readable text
        """

        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        decoded = self.morse_to_text(content)

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(decoded)

        print(f"\n✅ File decoded successfully -> {output_file}")


# =============================================================
# MAIN DRIVER
# =============================================================

if __name__ == "__main__":

    translator = MorseCodeTranslator()

    print("""
========================================================
                MORSE LOVER ENGINE
========================================================
1. Text -> Morse
2. Morse -> Text
3. Demo Paragraph
========================================================
""")

    choice = input("Enter your choice: ")

    # ---------------------------------------------------------
    # TEXT TO MORSE
    # ---------------------------------------------------------

    if choice == '1':

        user_text = input("\nEnter your text:\n")

        result = translator.text_to_morse(user_text)

        print("\n==============================")
        print(" MORSE OUTPUT")
        print("==============================")
        print(result)

    # ---------------------------------------------------------
    # MORSE TO TEXT
    # ---------------------------------------------------------

    elif choice == '2':

        user_morse = input("\nEnter Morse code:\n")

        result = translator.morse_to_text(user_morse)

        print("\n==============================")
        print(" TEXT OUTPUT")
        print("==============================")
        print(result)

    # ---------------------------------------------------------
    # DEMO
    # ---------------------------------------------------------

    elif choice == '3':

        demo_text = """
        Interstellar inspired Morse communication system.
        Morse code is one of the greatest inventions in communication history.
        """

        translator.print_conversion_summary(demo_text)

    else:
        print("\n❌ Invalid choice")