#  Luke Gilin
#  1216992

if __name__ == '__main__':

    text = input().split()
    #  count number of times "value" appears in "text" then print value + string
    for value in text:
        x = text.count(value)
        print(value, x)
