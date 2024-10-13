import base64

def encode_text():
    text_to_encode = input("|> Enter text to encode: ")

    encoded_text = base64.b64encode(text_to_encode.encode('utf-8'))
    print(f"Output: {encoded_text.decode('utf-8')}")
    
    user_option = input("|> Save output to a text file? (y/n): ")
    if (user_option == "y"):
        with open("./encoded-output-base64.txt", "wb") as file:
            file.write(encoded_text)
    elif (user_option == "n"):
        pass

def decode_text():
    encoded_text = input("|> Enter text to decode: ")
    
    decoded_text = base64.b64decode(encoded_text).decode('utf-8')
    print(f"Output: {decoded_text}")

    user_option = input("|> Save output to a text file? (y/n): ")
    if (user_option == "y"):
        with open("./decoded-output-base64.txt", "w") as file:
            file.write(decoded_text)
    elif (user_option == "n"):
        pass

def main():
    print(":: WELCOME TO BASE64 TEXT ENCODER & DECODER APP ::")
    print("\n1 - Encode text\n2 - Decode text\n")
    user_option = input("|> Select: ")

    if (user_option == "1"):
        encode_text()
    elif (user_option == "2"):
        decode_text()
    else:
        print("Invalid option!\n Please select one of the given options")

if __name__ == "__main__":
    main()