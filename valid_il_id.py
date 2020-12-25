"""Checks whether or not a given il-id is valid"""
def valid(inp = '123456789'):
    output = [None] * len(inp)
    output[0::2] = [int(i) for i in inp[0::2]]
    sum_digits = lambda x: int(str(x)[0]) + int(str(x)[1]) #get digits from a 2 digit number

    for i in range(1, len(inp), 2):
        handler = int(inp[i]) * 2
        output[i] = sum_digits(handler) if handler > 9 else handler

    return sum(output) % 10 == 0
    #return output

if __name__ == '__main__':
    print(valid(input('enter an id: ')))