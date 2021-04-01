#  Luke Gilin 1216992

if __name__ == '__main__':

    #  List to store input
    inputlist = input().split()
    #  List to store positive integers
    poslist = []

    inputlist = [int(i) for i in inputlist]

    #  add non-negitive values to poslist
    for number in inputlist:
        if number >= 0:
            poslist.append(number)
    poslist.sort()
    #  print positive values
    for value in poslist:
        print(value, end=' ')



