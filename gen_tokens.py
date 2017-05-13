import os
import random
import hashlib


def main():
    with open('tokens.txt', 'w') as f:
        token_set = set()
        for i in range(100):
            token = hashlib.sha1(os.urandom(24)).hexdigest()[:5]
            token_set.add(token)
        for token in token_set:
            f.write(token + '\n')

if __name__ == '__main__':
    main()
