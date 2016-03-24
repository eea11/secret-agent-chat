from random import randint
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def generate_otp(sheets, length):
	for sheet in range(sheets, length):
		with open("otp" + str(sheet) + ".txt","w") as f:
			for i in range(length):
				f.write(str(randint(0,26))+"\n")

def load_sheet(filename):
    with open(filename, "r") as f:
		contents = f.read().splitlines()
	return contents

def decrypt(ciphertext, sheet):
    plaintext = ''
    for position, character in enumerate(ciphertext):
        if character not in ALPHABET:
            plaintext += character
        else:
            decrypted = (ALPHABET.index(character) - int(sheet[position])) % 26
            plaintext += ALPHABET[decrypted]
    return plaintext
