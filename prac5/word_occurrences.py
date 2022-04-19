def main():
    counted_words = {}
    text = input("enter your text: ")
    words = text.split()
    for word in words:
        frequence = counted_words.get(word, 0)
        counted_words[word] = frequence + 1

    words = list(counted_words.keys())
    words.sort()

    for word in words:
        word_with = word + ":"
        print("{:15}{}".format(word_with, counted_words[word]))


main()