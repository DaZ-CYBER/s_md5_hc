import os
import sys
import argparse
import base64
from hashlib import *

def decrypt():
	config = arguments(); hasUserName = False; hasSalt = False; hasWordlist = False;
	print(config)
	for i in config:
		if(str(i) == 'username'):
			username = config[i]
			hasUserName = True
		if(str(i) == 'salt'):
			salt = config[i]
			hasSalt = True
		if(str(i) == 'wordlist'):
			wordlist = config[i]
			hasWordlist = True
	
	if(hasUserName != True) or (hasSalt != True) or (hasWordlist != True):
		print("Argument Error")
		sys.exit()
	
	algorithm_hash = "a0de4d7f81676c3ea9eabcadfd2536f6"
	
	try:
		with open(wordlist, 'r', encoding='latin-1') as f:
			for line in f:
				line = line.strip()
				data = md5((salt+'|'+username+'|'+line).encode('utf-8')).hexdigest()
				if(str(data) == str(algorithm_hash)):
					print(f"Testing {line} against {algorithm_hash}; Match found: {line}")
					return
				else:
					print(f"Testing {line} against {algorithm_hash}")
					
		print(f"No matches for respective hash")
	except FileNotFoundError:
		print(f"File not found: {wordlist}")
	except Exception as e:
		print(f"Abnormal error has occurred: {e}")
	
	
		  

def arguments():
	# Initializing argument parser / parser title
    	parser = argparse.ArgumentParser(description="Salted MD5 Hash Decrypter", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    	# Adding arguments to script
    	parser.add_argument('-s', '--salt', type=str, help="Salt utilized for hashing", default=argparse.SUPPRESS)
    	parser.add_argument('-u', '--username', type=str, help="Username", default=argparse.SUPPRESS)
    	parser.add_argument('-w', '--wordlist', type=str, help="Path to Wordlist", default=argparse.SUPPRESS)
    	# Condensing args for configuration to be called in any other function
    	args = parser.parse_args()
    	config = vars(args)
    	return(config)
    	
def main():
	print(f"User: {os.getenv('USER')}")
	print(f"Cracking Hash for: Triss")
	print("Initializing...")
	decrypt()

main()
