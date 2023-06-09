import html
import urllib.parse
import base64
from colorama import Fore, Style

def encode_text(text, encoding_option):
    if encoding_option == 1:
        return html.escape(text)
    elif encoding_option == 2:
        return urllib.parse.quote(text)
    elif encoding_option == 3:
        encoded_bytes = base64.b64encode(text.encode('utf-8'))
        return encoded_bytes.decode('utf-8')

def decode_text(text, decoding_option):
    if decoding_option == 1:
        return html.unescape(text)
    elif decoding_option == 2:
        return urllib.parse.unquote(text)
    elif decoding_option == 3:
        decoded_bytes = base64.b64decode(text.encode('utf-8'))
        return decoded_bytes.decode('utf-8')

def print_banner():
    banner = """
===========================================================================================

8888888b.                                          888
888  "Y88b                                         888
888    888                                         888
888    888  .d88b.  88888b.   .d8888b .d88b.   .d88888  .d88b.  888d888
888    888 d8P  Y8b 888 "88b d88P"   d88""88b d88" 888 d8P  Y8b 888P"
888    888 88888888 888  888 888     888  888 888  888 88888888 888
888  .d88P Y8b.     888  888 Y88b.   Y88..88P Y88b 888 Y8b.     888
8888888P"   "Y8888  888  888  "Y8888P "Y88P"   "Y88888  "Y8888  888
                                                By:otium44
===========================================================================================
"""
    print(Fore.GREEN + banner + Style.RESET_ALL)

def main():
    print_banner()
    print(Fore.BLUE + "Select an option:")
    print("========================================")
    print("1. Encoding")
    print("2. Decoding" + Style.RESET_ALL)
    option = int(input("Enter your choice (1 or 2): "))
    print("========================================")

    if option == 1:
        print(Fore.BLUE + "Select an encoding option:" + Style.RESET_ALL)
        print("========================================")
        print("1. HTML Encoding")
        print("2. URL Encoding")
        print("3. Base64 Encoding")
        encoding_option = int(input("Enter your choice (1, 2, or 3): "))
        text = input("Enter the text to encode: ")
        print("========================================")
        encoded_text = encode_text(text, encoding_option)
        print("Encoded text:" + Fore.GREEN + encoded_text)
    elif option == 2:
        print(Fore.BLUE + "Select a decoding option:" + Style.RESET_ALL)
        print("========================================")
        print("1. HTML Decoding")
        print("2. URL Decoding")
        print("3. Base64 Decoding" + Style.RESET_ALL)
        decoding_option = int(input("Enter your choice (1, 2, or 3): "))
        text = input("Enter the text to decode: ")
        print("========================================")
        decoded_text = decode_text(text, decoding_option)
        print("Decoded text:" + Fore.GREEN + decoded_text)
    else:
        print(Fore.RED + "Invalid option!")

    print(Style.RESET_ALL)

if __name__ == '__main__':
    main()
