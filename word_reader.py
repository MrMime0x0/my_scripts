def read_file(file_name):
    file = open(file_name, 'r')
    words = []
    for line in file:
        words.append(line.strip())
    file.close()
    return words
print(read_file('words.txt')) #you must have a text file with words in it
