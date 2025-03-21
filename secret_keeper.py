from cryptography.fernet import Fernet
import argparse
import time
from colorama import init, Fore, Back, Style

# initialize colorama
init()

# cli arguments parsing
parser = argparse.ArgumentParser(description="Secret_Keeper is a basic message encrypt & decrypt program")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-e', '--encrypt', help='encrypt message', action="store_true")
group.add_argument('-d', '--decrypt', help='Decrypt message', action="store_true")
parser.add_argument('-gk', '--genkey', help="Generate key", action="store_true")
parser.add_argument('-s', '--save', help="Save generated key in a file")

args = parser.parse_args()

# key generator engine
def generate_key():
	generated_key = Fernet.generate_key()
	print(f' {Fore.BLUE}[+]{Style.RESET_ALL} Cipher Key: {Fore.GREEN}{generated_key.decode()}{Style.RESET_ALL}')

	# save key to file
	if args.save:
		filename = args.save + '.txt'
		with open(filename, 'wb') as file:
			file.write(b'Cipher Key: ' + generated_key)

	return generated_key


def encrypt(cipher_key):
	cipher_suite = Fernet(cipher_key)

	msg = input(f"{Fore.BLUE} [+]{Style.RESET_ALL} PlainText: ").encode()

	# encrypting
	for interval in range(0, 101):
		print(f"\r Encrypting Message:{Fore.LIGHTCYAN_EX} {interval}% {Style.RESET_ALL}", end="")
		time.sleep(0.05)

	print()
	encrypted_msg = cipher_suite.encrypt(msg)
	print(f'	{Fore.BLUE}[+]{Style.RESET_ALL} Encrypted message:\n		{Fore.GREEN}{encrypted_msg.decode()}{Style.RESET_ALL}')


def decrypt(cipher_key):
	cipher_suite = Fernet(cipher_key)

	msg = input(f" {Fore.BLUE}[+]{Style.RESET_ALL} Cipher-text: ").encode()

	# decrypting
	for interval in range(0, 101):
		print(f"\r Decrypting Message:{Fore.LIGHTCYAN_EX} {interval}% {Style.RESET_ALL}", end="")
		time.sleep(0.05)
	print()
	decrypted_msg = cipher_suite.decrypt(msg)

	print(f'	{Fore.BLUE}[+]{Style.RESET_ALL} Decrypted message: {Fore.GREEN}{decrypted_msg.decode()}{Style.RESET_ALL}')


def main():
	# banner
	print(Fore.BLACK + Back.WHITE + f"***************(Secret Keeper.)***************" + Style.RESET_ALL)
	print(Fore.BLACK + Back.WHITE + f"   By Sys_br3ach3r                            " + Style.RESET_ALL)

	if args.genkey:
		key = generate_key()

		if args.encrypt:
			encrypt(key)
	else:
		key = input(f' {Fore.BLUE}[+]{Style.RESET_ALL} Cipher Key: ')
		if args.encrypt:
			encrypt(key)

		if args.decrypt:
			decrypt(key)

	print(f"\n{Fore.BLACK + Back.WHITE}     Message encrypted Successfully.          " + Style.RESET_ALL)

if __name__ == '__main__':
	try:
		main()

	except KeyboardInterrupt:
		abort_countdown = [5, 4, 3, 2, 1]
		for count in abort_countdown:
			print(f"\r ({Fore.RED}Ctrl + c{Style.RESET_ALL}) Aborting in {count}", end="")
			time.sleep(0.5)
		quit()

	except Exception as e:
		print(f" {Fore.RED}Error:{Style.RESET_ALL} Incorrect CipherKey/CipherText. {Style.BRIGHT}{e}")
		quit()
