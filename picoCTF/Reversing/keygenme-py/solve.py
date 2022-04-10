#!/usr/local/python3

import hashlib

# the username_trial presented in the keygenme.py
username = b"PRITCHARD"

# 
hash_index = [4, 5, 3, 6, 2, 7, 1, 8]
final_str = ''
for index in hash_index:
    final_str+=(str(hashlib.sha256(username).hexdigest()[index]))
print(f"flag is: picoCTF{{1n_7h3_|<3y_of_{final_str}}}")
