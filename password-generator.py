#!/usr/bin/python3

import string, random

pool = string.ascii_letters + string.digits + string.punctuation

print(*random.choices(pool, k=40), sep='')
