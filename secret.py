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
