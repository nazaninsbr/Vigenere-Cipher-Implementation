PLAIN_TEXT_FILE = './plain_text.txt'
KEY = 'HUMAN'

def read_file(path):
	content = []
	with open(path, 'r') as f:
		for line in f:
			content.append(line)
	return content

def get_length(plain_text):
	l = 0
	for line in plain_text:
		for c in line:
			if not (c=='\n' or c==' '):
				l += 1
	return l

def create_key_of_the_same_length(l):
	key = ''
	i = 0
	while len(key)<l:
		key = key + KEY[i%len(KEY)]
		i += 1
	return key

def encrypt(plain_text):
	length_of_plain_text = get_length(plain_text)
	key = create_key_of_the_same_length(length_of_plain_text)
	char_index = 0
	encrypted = ''
	for line in plain_text:
		for c in line:
			if not (c=='\n' or c==' '):
				encrypted += chr((ord(key[char_index])+ord(c)))
				char_index += 1
			else:
				encrypted += c
	return encrypted

def decrypt(encrypted):
	length_of_encrypted_text = get_length(encrypted)
	key = create_key_of_the_same_length(length_of_encrypted_text)
	char_index = 0
	dencrypted = ''
	for line in encrypted:
		for c in line:
			if not (c=='\n' or c==' '):
				dencrypted += chr(abs((ord(key[char_index])-ord(c))))
				char_index += 1
			else:
				dencrypted += c
	return dencrypted

def main():
	plain_text = read_file(PLAIN_TEXT_FILE)
	encrypted = encrypt(plain_text)
	print('Encrypted: ', encrypted)
	decrypted = decrypt(encrypted)
	print('Decrypted: ', decrypted)

if __name__ == '__main__':
	main()