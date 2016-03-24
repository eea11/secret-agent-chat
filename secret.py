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

def get_plain_text():
    plain_text = input('Please type your message ')
    return plain_text.lower()

def load_file(filename):
    with open(filename, "r") as f:
        contents = f.read()
    return contents

def save_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data)

def encrypt(plaintext, sheet):
	ciphertext = ''
	for position, character in enumerate(plaintext):
		if character not in ALPHABET:
            ciphertext += character
		else:
            encrypted = (ALPHABET.index(character) + int(sheet[position])) % 26
            ciphertext += ALPHABET[encrypted]
	return ciphertext

def decrypt(ciphertext, sheet):
    plaintext = ''
    for position, character in enumerate(ciphertext):
        if character not in ALPHABET:
            plaintext += character
        else:
            decrypted = (ALPHABET.index(character) - int(sheet[position])) % 26
            plaintext += ALPHABET[decrypted]
    return plaintext

def menu():
	choices = ['1', '2', '3', '4']
    choice = '0'
    while True:
        while choice not in choices:
			print('What would you like to do?')
            print('1. Generate one-time pads')
            print('2. Encrypt a message')
            print('3. Decrypt a message')
            print('4. Quit the program')
            choice = input('Please type 1, 2, 3 or 4 and press Enter ')
