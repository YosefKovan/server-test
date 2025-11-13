from fastapi import HTTPException


def encrypt_caesar(data):

    encrypted_text = ""

    for letter in data.text:

        if letter.isalpha() or letter == " ":
            if letter.islower():
                r = ((ord(letter) + data.offset) - ord('a')) % 26 + ord('a')
            elif letter.isupper():
                r = ((ord(letter) + data.offset) - ord('A')) % 26 + ord('A')
            else:
                r = ord(" ")

            encrypted_text += chr(r)

    return {"encrypted_text" : encrypted_text}


def decrypt_caesar(data):

    decrypted_text = ""

    for letter in data.text:

        if letter.isalpha() or letter == " ":
            if letter.islower():
                r = ((ord(letter) - data.offset) - ord('a') + 26) % 26 + ord('a')
            elif letter.isupper():
                r = ((ord(letter) - data.offset) - ord('A') + 26) % 26 + ord('A')
            else:
                r = ord(" ")

            decrypted_text += chr(r)

    return {"decrypted_text": decrypted_text}


def decrypt_fence_cipher(data):

    even = list(data.text[0 : len(data.text) - len(data.text) // 2])
    odd = list(data.text[len(data.text) - len(data.text) // 2 : ])

    decrypted = ""

    while even and odd:
        decrypted += even.pop(0)
        decrypted += odd.pop(0)

    if even:
        decrypted += even.pop(0)
    if odd:
        decrypted += odd.pop(0)

    return {"decrypted" : decrypted}


def encrypt_fence_cipher(text):
    text = text.replace(" ", "")
    even_letters = text[ : : 2]
    odd_letters = [letter for i, letter in enumerate(text) if i % 2 != 0]
    result = even_letters + ''.join(odd_letters)
    return { "encrypted_text" : result}


def handle_caesar(data):

    if data.mode == "encrypt":
        return encrypt_caesar(data)
    elif data.mode == "decrypt":
        return decrypt_caesar(data)

    raise  HTTPException(status_code=404, detail="mode is not corrct!")