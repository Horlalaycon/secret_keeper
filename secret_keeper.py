from cryptography.fernet import Fernet
import argparse

parser = argparse.ArgumentParser(description="Secret_Keeper is a basic message encrypt & decrypt program")
group = parser.add_mutually_exclusive_group(required=True)

group.add_argument('-e', '--encrypt', help='encrypt message', action="store_true")
group.add_argument('-d', '--decrypt', help='Decrypt message', action="store_true")

parser.add_argument('-gk', '--genkey', help="Generate key", action="store_true")
parser.add_argument('-s', '--save', help="Save key")

args = parser.parse_args()

# key generator engine
def generate_key():
	generated_key = Fernet.generate_key()
	print(f'Cipher Key: {generated_key.decode()}')
	print("-" * 40)

	# save key to file
	if args.save:
		filename = args.save + '.txt'
		with open(filename, 'wb') as file:
			file.write(b'Cipher Key: ' + generated_key)

	return generated_key


def encrypt(cipher_key):
	cipher_suite = Fernet(cipher_key)

	msg = input(" PlainText: ").encode()

	print("-" * 40)

	encrypted_msg = cipher_suite.encrypt(msg)

	print(f'Encrypted message: {encrypted_msg.decode()}')


def decrypt(cipher_key):
	cipher_suite = Fernet(cipher_key)

	msg = input("CipherText: ").encode()

	print("-" * 40)

	decrypted_msg = cipher_suite.decrypt(msg)

	print(f'Decrypted message: {decrypted_msg.decode()}')


def main():
	if args.genkey:
		key = generate_key()

		if args.encrypt:
			encrypt(key)
	else:
		key = key = input('Cipher Key: ')

		print("-" * 40)
		if args.encrypt:
			encrypt(key)

		if args.decrypt:
			decrypt(key)


if __name__ == '__main__':
	try:
		print()
		print("=" * 40)
		print('  **********(Secret Keeper)**********')
		print("-" * 40)
		print("   By: sys_br3ach3r")
		print("=" * 40)
		main()
		print("=" * 40)

	except KeyboardInterrupt:
		print(f"""
========================================
  program Aborting... (Ctrl+c)
========================================""")
		quit()

	except Exception as e:
		print(f"""
Error: Incorrect CipherKey/CipherText.
{e}
========================================""")
		quit()
