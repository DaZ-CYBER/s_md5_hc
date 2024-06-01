This tool cracks Salted MD5 hashes that have the below format.
hash = $salt|$username|$password

usage: md5.py [-h] [-s SALT] [-u USERNAME] [-w WORDLIST]

Salted MD5 Hash Decrypter

options:
  -h, --help            show this help message and exit
  -s SALT, --salt SALT  Salt utilized for hashing
  -u USERNAME, --username USERNAME
                        Username
  -w WORDLIST, --wordlist WORDLIST
                        Path to Wordlist

Make sure to change the value for algorithm_hash within the POC to adjust the salt value that you have.

Example Command:

kali> python3 md5.py -u daz -s 18s89fa891jrajfja09820 -w /usr/share/wordlists/rockyou.txt
