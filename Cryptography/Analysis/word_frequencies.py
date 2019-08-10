from sys import argv


def frequencies(text, separator=' '):
    d = dict()
    strip = ['.', ',', '!']
    
    for char in strip:
        text = text.replace(char, '')

    text = text.replace('\n', ' ')

    for word in text.split(' '):
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1
    d = sorted(d.items(), key=lambda kv: kv[1], reverse=True)

    for k, v in d:
        print('%5s %s' % (v, k))

        
def main():
    if len(argv) != 2:
        print('Usage: %s <file>')
        exit(1)

    text = open(argv[1]).read()
    frequencies(text)


if __name__ == '__main__':
    main()

