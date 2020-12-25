#!/usr/bin/python3
import string, random

take_from = string.ascii_letters + string.digits + string.punctuation

print(''.join([random.choice(take_from) for _ in range(30)]))