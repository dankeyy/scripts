from itertools import accumulate

nah = ['נ', 'נח', 'נחמ', 'נחמן', 'מאומן']
spaces = lambda x, y: f'{x} {y}'

for i in accumulate(nah, spaces):
    print(i)