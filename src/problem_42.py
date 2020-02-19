def getWords(file_name):
    with open(file_name, 'r') as f:
        words = f.readline().split(',')
    
    for i in range(len(words)):
        words[i] = words[i].strip('"')
    
    return words


def calculateASCII(name):
    sum = 0

    for letter in name:
        sum += ord(letter) - 64

    return sum


def binary_search(collection, item):
    first = 0
    last = len(collection) - 1
    found = False

    while first <= last and not found:
        mid = (first + last)//2

        if collection[mid] == item:
            found = True
        else:
            if item < collection[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found


def main():
    triangle_words = 0
    triangle_numbers = sorted(set([i*(i + 1)//2 for i in range(30 * 30)]))

    for word in getWords('problem_42_words.txt'):
        if binary_search(triangle_numbers, calculateASCII(word)):
            triangle_words += 1


    print(triangle_words)

if __name__ == "__main__":
    main()