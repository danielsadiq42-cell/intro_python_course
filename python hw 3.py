def count_lines_words(filename):
    file = open(filename, "r")

    lines = file.readlines()

    number_of_lines = len(lines)
    number_of_words = 0

    for line in lines:
        words = line.split()
        number_of_words += len(words)

    file.close()

    print("Number of lines:", number_of_lines)
    print("Number of words:", number_of_words)

count_lines_words("text hw3.txt")