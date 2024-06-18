import operator

def main():
    with open ('books/frankenstein.txt') as f:
        contents = f.read()
        print(f'Report of {str(f)[25:-28]}:\n\n')
        wordcount = countwords(contents)
        print(f'{wordcount} words were found in the document.\n')
        charcount = countchars(contents)
        sorted_charcount = dict(sorted(charcount.items(), key=operator.itemgetter(1), reverse=True))
        for char, num in sorted_charcount.items():
            if char.isalpha():
                print(f'The letter {char} was found {num} times in this book.')
        print('End of report.')
        return

def countwords(contents):
    words = contents.split()
    return len(words)

def countchars(contents):
    chardict = {}
    for char in contents:
        char = char.lower()
        if char in chardict:
            chardict[char] += 1
        else:
            chardict[char] = 1
    return chardict


main()
