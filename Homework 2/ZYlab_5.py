# Luke Gilin 1216992
# Zybooks 9.10 CIS 2348 LAB: Word frequencies (lists)

import csv
#  Get file name from user
filename = input()
#  Open file in read only mode
with open(filename, 'r') as csvfile:
    frequency_count = csv.reader(csvfile, delimiter=',')

    for row in frequency_count:
        word_list = row

    frequency = {}

    for word in word_list:
        #  Checks if word is already in dictionary, if it is, it adds 1 to the count
        if word in frequency:
            frequency[word] = frequency[word] + 1
        #  If word isn't in the dictionary it adds it, with a value of one
        else:
            frequency[word] = 1

    #  Prints dictionary key and values
    for i, j in frequency.items():
        print('{word} {num}'.format(word=i, num=j))


