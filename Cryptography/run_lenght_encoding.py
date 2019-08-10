from sys import argv

# Run lenght encoding decoder

def rle(string):
    index = 0
    encoding = ''

    while index < len(string):
        occurrences = 1
        while index + 1 < len(string) and string[index] == string[index + 1]:
            index += 1
            occurrences += 1
        encoding += str(occurrences)
        index += 1
    print(encoding)
    for i in range(int(len(encoding) / 2)):
        print(encoding[i*2:i*2+2])


def main():
    if len(argv) != 2:
        print('Usage %s <string>' % argv[0])
        exit(0)

    rle(argv[1])


if __name__ == '__main__':
    main()
