import string

def process_file(filename):
    temp = dict()
    file = open(filename)
    for line in file:
        process_line(line, temp)
    return temp

def process_line(line, temp):
    for word in line:
        word = word.lower()
        if word in string.digits:
            temp['Numbers'] = temp.get('Numbers', 0) + 1
        elif word in string.ascii_lowercase:
            temp[word] = temp.get(word, 0) + 1
        elif word in string.whitespace:
            temp['White space'] = temp.get('White sapce', 0) + 1
        elif word in string.punctuation:
            temp['Symbols'] = temp.get('Symbols', 0) + 1

def calProb(filename):
    frequencies = process_file(filename)
    total = sum(frequencies.values())
    for letter, freq in frequencies.items():
        frequencies[letter] = freq/total
    return frequencies